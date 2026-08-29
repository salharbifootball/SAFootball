# app.py
# =========================================
# Scout Dashboard (FULL - Arabic + RTL FIXED)
# - Arabic everywhere (UI + charts + PDF)
# - Robust RTL shaping for Matplotlib titles/labels
# - Fix mixed Arabic + numbers direction issues
# - Cube Radar (5 axes) + Circular Radar (5 axes)
# - Fix duplicated else bug in radar block
# - Fix PDF overlapping by re-layout
# - ✅ FIX: Stop "reversing" Arabic in Streamlit by separating RTL for Streamlit vs Matplotlib
# =========================================

import os, io, json, textwrap, re
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Optional (your extra libs)
import cv2
import seaborn as sns
from ultralytics import YOLO

from dotenv import load_dotenv
from openai import OpenAI

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PIL import Image, ImageDraw, ImageFont

from matplotlib.patches import FancyArrowPatch
from matplotlib.lines import Line2D
from matplotlib import rcParams

import arabic_reshaper
from bidi.algorithm import get_display
import html as _html
import matplotlib as mpl
import matplotlib.font_manager as font_manager
# -------------------------
# STREAMLIT RTL CSS (more targeted)
# -------------------------
# Ensure page config is set before any other Streamlit calls
st.set_page_config(page_title="لوحة الكشاف", layout="wide")

# -------------------------
# STREAMLIT RTL CSS (more targeted)
# -------------------------
st.markdown(
    """
    <style>
    html, body, [class*="css"]  { direction: rtl; text-align: right; }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------
# Logo (display if available) - safe, non-fatal
# -------------------------
LOGO_FILENAME = "WhatsApp Image 2026-06-30 at 1.01.16 AM.jpeg"
try:
    LOGO_PATH = os.path.join(os.path.dirname(__file__), LOGO_FILENAME)
except Exception:
    LOGO_PATH = os.path.join(os.getcwd(), LOGO_FILENAME)

_logo_img = None
try:
    if os.path.isfile(LOGO_PATH):
        _logo_img = Image.open(LOGO_PATH)
    else:
        alt = os.path.join(os.getcwd(), LOGO_FILENAME)
        if os.path.isfile(alt):
            _logo_img = Image.open(alt)
except Exception:
    _logo_img = None

if _logo_img is not None:
    try:
        # Place logo in a right column and show it larger (fixed width),
        # with a responsive fallback in case fixed width fails.
        cols = st.columns([6, 1])
        with cols[1]:
            try:
                st.image(_logo_img, width=320)
            except Exception:
                st.image(_logo_img, use_container_width=True)
    except Exception:
        try:
            st.image(_logo_img, width=200)
        except Exception:
            pass

# -------------------------
# OPTIONAL RTL shaping libs
# -------------------------
try:
    import arabic_reshaper
    from bidi.algorithm import get_display
    RTL_OK = True
except Exception:
    RTL_OK = False

# -------------------------
# STREAMLIT CONFIG
# -------------------------
load_dotenv(override=True)

# -------------------------
# THEME COLORS
# -------------------------
DARK_BG = "#1e5631"   # الخلفية
TEXT = "#ffffff"      # لون النص
MUTED = "#6b7280"
PURPLE = "#7c3aed"    # مهم
BLUE = "#0ea5e9"
GREEN = "#22c55e"
RED = "#ef4444"
GOLD = "#f59e0b"
LINE = "#22304a"

# -------------------------
# Matplotlib font
# -------------------------
rcParams["axes.unicode_minus"] = False

# Optional explicit Arabic font path (set via environment variable AR_FONT_PATH)
AR_FONT_PATH = os.getenv("AR_FONT_PATH", "").strip()
# If AR_FONT_PATH not provided, try to auto-detect a preferred Arabic-capable font file
if not AR_FONT_PATH:
    try:
        for pref in PREFERRED_AR_FONTS:
            for f in font_manager.fontManager.ttflist:
                if pref.lower() in (f.name or "").lower():
                    try:
                        AR_FONT_PATH = font_manager.findfont(f.name, fallback_to_default=True)
                        raise StopIteration
                    except Exception:
                        continue
    except StopIteration:
        pass

# -------------------------
# CONSTANTS
# -------------------------
st.session_state.setdefault("last_report_ar", "")
st.session_state.setdefault("pdf2_bytes", None)

PITCH_W, PITCH_H = 120.0, 80.0
ATTACK_DIR = "L2R"
MODEL = "gpt-4o-mini"


# ============================================================
# RTL HELPERS
# ============================================================
RLM = "\u200f"  # Right-to-Left Mark
LRM = "\u200e"  # Left-to-Right Mark


def _shape_ar(s: str) -> str:
    """Arabic reshaping for Matplotlib only."""
    if s is None:
        return ""
    s = str(s)

    if RTL_OK:
        try:
            return arabic_reshaper.reshape(s)
        except Exception:
            return s

    return s


def _wrap_ltr_tokens(s: str) -> str:
    """
    Wrap numbers and English words with LRM.
    Useful for mixed Arabic/English text in Matplotlib.
    """
    if s is None:
        return ""

    s = str(s)

    s = re.sub(
        r"([0-9]+(?:\.[0-9]+)?%?)",
        lambda m: f"{LRM}{m.group(1)}{LRM}",
        s
    )

    s = re.sub(
        r"([A-Za-z_]+)",
        lambda m: f"{LRM}{m.group(1)}{LRM}",
        s
    )

    return s


def ar_st(text: str) -> str:
    """
    Streamlit / HTML text.
    Do not use arabic_reshaper or bidi here.
    The browser handles Arabic RTL correctly.
    """
    if text is None:
        return ""

    return str(text)


def safe_rtl_html(text: str) -> str:
    """Escape and wrap text for safe RTL rendering in Streamlit HTML.

    Converts newlines to <br> and wraps in a RTL div with right alignment.
    """
    if text is None:
        return ""
    s = str(text)
    s = _html.escape(s)
    # Wrap contiguous Latin/number runs (names, codes, digits, punctuation)
    # so they render LTR inside an RTL paragraph. We allow common separators
    # (space, dash, dot, underscore, slash, parentheses, comma, colon, percent).
    try:
        pattern = r'([A-Za-z0-9](?:[A-Za-z0-9\-\._ \/\(\),:%&]+[A-Za-z0-9%])?)'
        s = re.sub(pattern,
                   r'<span dir="ltr" style="unicode-bidi:embed;">\1</span>',
                   s)
    except Exception:
        pass
    s = s.replace("\n", "<br>\n")
    return f'<div dir="rtl" style="direction: rtl; text-align: right; unicode-bidi:isolate-override;">{s}</div>'


def ar_mpl(text: str) -> str:
    """
    Matplotlib text only.
    Uses arabic_reshaper + bidi to fix reversed Arabic text.
    """
    if text is None:
        return ""

    # For Matplotlib we only apply Arabic shaping and bidi display.
    # Do NOT wrap LTR tokens with LRM here — that can introduce
    # visible control marks in some fonts/renderers and can cause
    # incorrect visual ordering inside image renderers. LTR wrapping
    # is handled when rendering HTML (safe_rtl_html) instead.
    s = str(text)
    shaped = _shape_ar(s)
    if RTL_OK:
        try:
            return get_display(shaped)
        except Exception:
            return shaped
    return shaped


def ar_mpl_plain(text: str) -> str:
    """
    Like ar_mpl but without wrapping LTR tokens with LRM. Use for legend/title
    where inserting control marks can produce visible boxes in some fonts.
    """
    if text is None:
        return ""
    shaped = _shape_ar(str(text))
    if RTL_OK:
        try:
            return get_display(shaped)
        except Exception:
            return shaped
    return shaped


def ar_text(text: str) -> str:
    """Utility for Matplotlib: reshape Arabic and apply bidi display.

    Use this for titles, ticklabels and legend entries rendered into images.
    """
    try:
        s = _wrap_ltr_tokens(str(text))
        return get_display(arabic_reshaper.reshape(s))
    except Exception:
        return str(text)


def rtl_plot_text(text: str) -> str:
    """
    Compatibility with old function calls.
    """
    return ar_mpl(text)


# -------------------------
# Matplotlib Arabic font helpers
# -------------------------
PREFERRED_AR_FONTS = [
    "Arabic Typesetting",
    "Tahoma",
    "Arial",
    "Times New Roman"
]


def find_arabic_font_name():
    try:
        names = [f.name for f in font_manager.fontManager.ttflist]

        for pref in PREFERRED_AR_FONTS:
            for n in names:
                if pref.lower() in n.lower():
                    return n

    except Exception:
        return None

    return None

def add_attack_direction_below(fig, direction="R2L"):
    y_arrow = 0.099
    x_left  = 0.40
    x_right = 0.60

    if direction == "R2L":
        x1, x2 = x_right, x_left
    else:
        x1, x2 = x_left, x_right

    arr = FancyArrowPatch(
        (x1, y_arrow), (x2, y_arrow),
        transform=fig.transFigure,
        arrowstyle="<|-",
        mutation_scale=18,
        linewidth=2.2,
        color=TEXT,
        alpha=0.95
    )
    fig.patches.append(arr)


def mpl_arabic_rc_context():
    """
    Return a Matplotlib rc_context with Arabic-capable font if available.
    """
    # Build an ordered list of available preferred fonts (preserve preference)
    try:
        names = [f.name for f in font_manager.fontManager.ttflist]
        available = []
        for pref in PREFERRED_AR_FONTS:
            for n in names:
                if pref.lower() in n.lower() and n not in available:
                    available.append(n)
    except Exception:
        available = []

    if available:
        # Prefer the first exact available font as primary family (stronger enforcement)
        try:
            print(f"[Ai agent] Matplotlib Arabic font candidates: {available}")
        except Exception:
            pass
        primary = available[0]
        # If an explicit AR_FONT_PATH is available, try to use it instead of family name
        try:
            if AR_FONT_PATH and os.path.isfile(AR_FONT_PATH):
                fp = font_manager.FontProperties(fname=AR_FONT_PATH)
                fam = fp.get_name()
                return mpl.rc_context({
                    "font.family": fam,
                    "font.sans-serif": available,
                    "axes.unicode_minus": False
                })
        except Exception:
            pass
        return mpl.rc_context({
            "font.family": primary,
            "font.sans-serif": available,
            "axes.unicode_minus": False
        })

    return mpl.rc_context({
        "axes.unicode_minus": False
    })


def get_mpl_ar_fontprop():
    """
    Return a Matplotlib FontProperties using the first available preferred Arabic font.
    Falls back to None if no suitable font is found.
    """
    try:
        # If AR_FONT_PATH is explicitly provided and valid, prefer it
        try:
            if AR_FONT_PATH and os.path.isfile(AR_FONT_PATH):
                return font_manager.FontProperties(fname=AR_FONT_PATH)
        except Exception:
            pass

        names = [f.name for f in font_manager.fontManager.ttflist]
        for pref in PREFERRED_AR_FONTS:
            for n in names:
                if pref.lower() in n.lower():
                    try:
                        fpath = font_manager.findfont(n, fallback_to_default=True)
                        return font_manager.FontProperties(fname=fpath)
                    except Exception:
                        # last-resort: return by family name
                        return font_manager.FontProperties(family=n)
    except Exception:
        return None
    return None


def arabic_fontprop():
    """Compatibility wrapper used by plotting code. Returns a FontProperties or None."""
    try:
        return get_mpl_ar_fontprop()
    except Exception:
        return None


# -------------------------
# PROMPTS
# -------------------------
SCOUT_PROMPT_AR = """
أنت كشاف كرة قدم محترف + محلل بيانات.
تعتمد فقط على المدخلات المرسلة (JSON) والتي تأتي من ملف أحداث (Event Log) لهذه المباراة.
لا تخترع أرقام أو معلومات غير موجودة.

اكتب تقريرًا عربيًا احترافيًا فقط.
إن كانت معلومة غير متاحة قل: غير متاح من البيانات الحالية.

مهم جداً:
- يجب ذكر "المراوغات" دائماً حتى لو كانت قليلة.
- يجب مقارنة المراوغات بمتوسط المباراة (match_average_0_10) إن توفر.
- لا تذكر اسم اللاعب داخل وصف الحدث؛ اشرح الحدث نفسه فقط.

الهيكل:
1) تعريف اللاعب
2) ملخص عام (4–6 سطور)
3) نقاط القوة (≤5)
4) نقاط التطوير (≤5)
5) الملاءمة التكتيكية
6) المراوغات مقارنة بمتوسط المباراة (سطرين واضحين)
7) ملاحظات/مخاطر
8) التوصية النهائية (✅ تعاقد / 🟨 متابعة / ❌ استبعاد) مع سببين رقميين من supporting_numbers.
"""

CHAT_PROMPT_AR = """
أنت مساعد محلل بيانات كرة قدم.
أجب بالعربية فقط.
استخدم JSON المعطى ولا تخترع أرقام.

قواعد مهمة جداً:
1) لا تكتب اسم اللاعب داخل "وصف الحدث" أو سرد الحدث نفسه. اشرح الحدث فقط.
2) لكن عند طلب "أفضل 10 لاعبين" يجب أن تذكر أسماء اللاعبين بوضوح مع أرقامهم/تقييماتهم.
3) عند الحديث عن اللاعب/المقاييس: يجب ذكر المراوغات دائماً ومقارنتها بمتوسط المباراة إن توفر.
"""


# -------------------------
# Small helpers
# -------------------------
def extract_section_lines(md: str, header: str):
    if not md:
        return []
    pattern = rf"(?im)^\s*##\s*{re.escape(header)}\s*$"
    m = re.search(pattern, md)
    if not m:
        return []
    start = m.end()
    tail = md[start:]
    stop = re.search(r"(?im)^\s*##\s+", tail)
    if stop:
        tail = tail[:stop.start()]

    lines = []
    for ln in tail.splitlines():
        t = ln.strip()
        if not t:
            continue
        t = re.sub(r"^\s*[-•*]\s+", "", t)
        t = re.sub(r"^\s*\d+[\)\.]\s+", "", t)
        if t:
            lines.append(t)
    return lines

def render_rtl_numbered_list(items, title_ar: str):
    if not items:
        return
    html_items = "\n".join([f"<li>{ar_st(it)}</li>" for it in items])
    st.markdown(f"### {ar_st(title_ar)}", unsafe_allow_html=True)
    st.markdown(
        f"""
        <ol dir="rtl" style="text-align:right; padding-right: 22px; line-height: 1.9;">
          {html_items}
        </ol>
        """,
        unsafe_allow_html=True
    )

def caption_mixed_ar(parts: list) -> str:
    html = '<div style="direction: rtl; text-align: right; font-size: 0.95rem;">'
    html += 'القيم (0-10): '
    segs = []
    for k, v in parts:
        segs.append(f'{ar_st(k)} <span dir="ltr" style="unicode-bidi:embed;">{v:.2f}</span>')
    html += " | ".join(segs)
    html += "</div>"
    return html

def safe_div(a, b):
    try:
        a = float(a); b = float(b)
        return a / b if b else 0.0
    except:
        return 0.0

def contains(s: pd.Series, pattern: str) -> pd.Series:
    return s.astype(str).str.contains(pattern, case=False, na=False)

def coerce_float(s: pd.Series):
    return pd.to_numeric(s, errors="coerce")

@st.cache_data
def load_data_from_upload(uploaded_file) -> pd.DataFrame:
    # Guard against None / missing uploads so the app doesn't crash when
    # called outside of a proper upload flow (or when user hasn't uploaded).
    if uploaded_file is None:
        try:
            st.warning("No file uploaded.")
        except Exception:
            pass
        return pd.DataFrame()

    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        try:
            st.error(f"Failed to read uploaded file: {e}")
        except Exception:
            pass
        return pd.DataFrame()

    return normalize_df(df)

def normalize_df(df: pd.DataFrame) -> pd.DataFrame:
    if df is None or df.empty:
        return pd.DataFrame()

    rename_map = {
        "playerName": "player_name",
        "PlayerName": "player_name",
        "player": "player_name",
        "teamName": "team_name",
        "TeamName": "team_name",
        "team": "team_name",
        "matchId": "match_id",
        "MatchId": "match_id",
        "match": "match_id",
        "startX": "start_x",
        "startY": "start_y",
        "endX": "end_x",
        "endY": "end_y",
        "x": "start_x",
        "y": "start_y",
        "to_x": "end_x",
        "to_y": "end_y",
        "endX.1": "end_x",
        "endY.1": "end_y",
    }
    for c in list(df.columns):
        if c in rename_map:
            df = df.rename(columns={c: rename_map[c]})

    needed = ["match_id","team_name","player_name","attribute","sub_attribute","action","description","timestamp","period"]
    for c in needed:
        if c not in df.columns:
            df[c] = np.nan

    for c in ["player_name","team_name","attribute","sub_attribute","action","description"]:
        df[c] = df[c].astype(str).fillna("")
        # Normalize names: remove RTL/LTR mark characters and collapse whitespace
        try:
            df[c] = df[c].str.replace('\u200f', '', regex=False).str.replace('\u200e', '', regex=False)
        except Exception:
            # older pandas may ignore regex kwarg; fall back
            df[c] = df[c].str.replace('\u200f', '').str.replace('\u200e', '')
        df[c] = df[c].str.replace(r"\s+", " ", regex=True).str.strip()

    return df


# -------------------------
# COORDS
# -------------------------
def detect_coord_cols(df: pd.DataFrame):
    cols = set(df.columns)
    candidates = [
        ("start_x","start_y","end_x","end_y"),
        ("x","y","endX","endY"),
        ("x","y","end_x","end_y"),
        ("x","y","to_x","to_y"),
    ]
    for sx,sy,ex,ey in candidates:
        if sx in cols and sy in cols and ex in cols and ey in cols:
            return sx,sy,ex,ey
    return None

def clip_pitch(x, y):
    x2 = np.clip(x, 0, PITCH_W)
    y2 = np.clip(y, 0, PITCH_H)
    return x2, y2

def infer_scale_max(series_x: pd.Series, series_y: pd.Series):
    x = coerce_float(series_x)
    y = coerce_float(series_y)
    try:
        x_max = np.nanmax(x.values)
        y_max = np.nanmax(y.values)
    except Exception:
        x_max = np.nan
        y_max = np.nan

    if (not np.isnan(x_max) and x_max > 101) or (not np.isnan(y_max) and y_max > 101):
        return PITCH_W, PITCH_H, "pitch_units"

    if (not np.isnan(x_max) and x_max <= 1.5) and (not np.isnan(y_max) and y_max <= 1.5):
        return 1.0, 1.0, "0_1"

    return 100.0, 100.0, "0_100"

def to_pitch_coords(df: pd.DataFrame, x_col: str, y_col: str):
    x = coerce_float(df[x_col])
    y = coerce_float(df[y_col])
    x_max, y_max, mode = infer_scale_max(df[x_col], df[y_col])

    if mode == "pitch_units":
        x2, y2 = clip_pitch(x.values, y.values)
        return x2, y2

    x2 = (x.astype(float) / float(x_max)) * PITCH_W
    y2 = (y.astype(float) / float(y_max)) * PITCH_H
    x2, y2 = clip_pitch(x2.values, y2.values)
    return x2, y2


# -------------------------
# PASS
# -------------------------
def is_pass_row(row) -> bool:
    if str(row.get("attribute","")).strip() not in ["Passing", "X_Passing"]:
        return False
    act = str(row.get("action","")).strip()
    if act.startswith("Received"):
        return False
    return act in ["Simple Pass", "Key Pass", "Assist", "Unsuccessful"]

def pass_label_type(row) -> str:
    act = str(row.get("action","")).strip()
    if act in ["Key Pass", "Assist"]:
        return "key"
    if act == "Unsuccessful":
        return "unsuccess"
    return "success"

def filter_player_passes(df_in: pd.DataFrame) -> pd.DataFrame:
    p = df_in[df_in["attribute"].isin(["Passing","X_Passing"])].copy()
    p = p[~contains(p["action"], r"^Received")].copy()
    p = p[p["action"].isin(["Simple Pass","Key Pass","Assist","Unsuccessful"])].copy()
    return p

def is_success_pass_action(a: str) -> bool:
    a = str(a)
    return ("Unsuccessful" not in a) and (a in ["Simple Pass","Key Pass","Assist"])


# -------------------------
# DRIBBLING (StepOut-style)
# -------------------------
def filter_stepout_dribbles(df_in: pd.DataFrame) -> pd.DataFrame:
    x = df_in[df_in["attribute"].isin(["Dribbling","X_Dribbling"])].copy()
    x["sub_attribute"] = x["sub_attribute"].astype(str)
    x["action"] = x["action"].astype(str)

    allow_sub = x["sub_attribute"].isin(["Dribbling", "Difficult Receives"])
    allow_act = x["action"].isin(["Successful", "Unsuccessful"])

    dr = x[allow_sub & allow_act].copy()

    bad = contains(dr["sub_attribute"], "Encounter") | contains(dr["action"], "Resisted")
    dr = dr[~bad].copy()
    return dr

def dribble_is_success(row) -> bool:
    return str(row.get("action","")).strip() == "Successful"


# -------------------------
# DUELS
# -------------------------
def filter_player_duels(df_in: pd.DataFrame) -> pd.DataFrame:
    x = df_in.copy()
    is_duel_attr = x["attribute"].str.contains("Duel", case=False, na=False) | x["attribute"].str.contains("Physical", case=False, na=False)
    is_duel_sub  = x["sub_attribute"].str.contains("Duel", case=False, na=False) | x["sub_attribute"].str.contains("Aerial", case=False, na=False)
    is_duel_act  = x["action"].str.contains("Duel", case=False, na=False) | x["action"].str.contains("Aerial", case=False, na=False)
    return x[is_duel_attr | is_duel_sub | is_duel_act].copy()

def duel_is_won(row: pd.Series) -> bool:
    a = str(row.get("action",""))
    s = str(row.get("sub_attribute",""))
    d = str(row.get("description",""))
    txt = " ".join([a, s, d]).lower()
    if any(k in txt for k in ["lost", "unsuccess", "fail"]):
        return False
    if any(k in txt for k in ["won", "success", "win"]):
        return True
    return False


# -------------------------
# PITCH DRAW
def draw_pitch(ax, bg="#070d18", line="#0b0c0c", alpha=0.90):
    ax.set_facecolor(bg)
    ax.plot([0, PITCH_W, PITCH_W, 0, 0], [0, 0, PITCH_H, PITCH_H, 0], color=line, lw=2, alpha=alpha)
    ax.plot([PITCH_W/2, PITCH_W/2], [0, PITCH_H], color=line, lw=2, alpha=alpha)
    cc = plt.Circle((PITCH_W/2, PITCH_H/2), 10, edgecolor=line, facecolor="none", lw=2, alpha=alpha)
    ax.add_patch(cc)
    ax.scatter([PITCH_W/2], [PITCH_H/2], color=line, s=10, alpha=alpha)

    ax.plot([0, 18, 18, 0], [18, 18, PITCH_H-18, PITCH_H-18], color=line, lw=2, alpha=alpha)
    ax.plot([0, 6, 6, 0], [30, 30, PITCH_H-30, PITCH_H-30], color=line, lw=2, alpha=alpha)
    ax.scatter([12], [PITCH_H/2], color=line, s=10, alpha=alpha)

    ax.plot([PITCH_W, PITCH_W-18, PITCH_W-18, PITCH_W], [18, 18, PITCH_H-18, PITCH_H-18], color=line, lw=2, alpha=alpha)
    ax.plot([PITCH_W, PITCH_W-6, PITCH_W-6, PITCH_W], [30, 30, PITCH_H-30, PITCH_H-30], color=line, lw=2, alpha=alpha)
    ax.scatter([PITCH_W-12], [PITCH_H/2], color=line, s=10, alpha=alpha)

    ax.set_xlim(0, PITCH_W)
    ax.set_ylim(0, PITCH_H)
    ax.set_aspect("equal")
    ax.axis("off")

def plot_pass_map(df_match: pd.DataFrame, player: str, title: str, direction="L2R"):
    d = df_match[df_match["player_name"].astype(str) == str(player)].copy()
    d = d[d.apply(is_pass_row, axis=1)].copy()

    cc = detect_coord_cols(df_match)
    if cc is None:
        with mpl_arabic_rc_context():
            fig = plt.figure(figsize=(10.5, 6), dpi=150)
            fig.patch.set_facecolor(DARK_BG)
            ax = fig.add_axes([0.04, 0.10, 0.92, 0.82])
            draw_pitch(ax)
            fp = arabic_fontprop()
            fp_kwargs = {"fontproperties": fp} if fp else {}
            ax.text(0.5, 0.5, rtl_plot_text("لا توجد أعمدة إحداثيات للتمريرات في الملف."),
                transform=ax.transAxes, ha="center", va="center", fontsize=14, color=TEXT, **fp_kwargs)
            return fig, {"total": 0, "acc": 0, "key": 0, "unsucc": 0}

    sx_c, sy_c, ex_c, ey_c = cc
    sx, sy = to_pitch_coords(d, sx_c, sy_c)
    ex, ey = to_pitch_coords(d, ex_c, ey_c)

    d["sx"], d["sy"], d["ex"], d["ey"] = sx, sy, ex, ey
    d["ptype"] = d.apply(pass_label_type, axis=1)

    total = len(d)
    succ = int((d["ptype"] == "success").sum())
    unsucc = int((d["ptype"] == "unsuccess").sum())
    keyp = int((d["ptype"] == "key").sum())
    acc = (succ / total * 100) if total else 0.0

    with mpl_arabic_rc_context():
        fig = plt.figure(figsize=(10.5, 6), dpi=150)
        fig.patch.set_facecolor(DARK_BG)
        ax = fig.add_axes([0.04, 0.12, 0.92, 0.78])
        draw_pitch(ax)
        fp = arabic_fontprop()
        fp_kwargs = {"fontproperties": fp} if fp else {}

    for _, r in d.iterrows():
        x1, y1, x2, y2 = float(r["sx"]), float(r["sy"]), float(r["ex"]), float(r["ey"])
        ptype = r["ptype"]
        if ptype == "success":
            color, ls, lw, a = PURPLE, "-", 2.2, 0.90
        elif ptype == "unsuccess":
            color, ls, lw, a = RED, "--", 2.2, 0.90
        else:
            color, ls, lw, a = GOLD, "-", 3.0, 0.95

        arrp = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=12,
                               linewidth=lw, linestyle=ls, color=color, alpha=a)
        ax.add_patch(arrp)

    handles = [
        Line2D([0],[0], color=PURPLE, lw=3, label=ar_mpl_plain("تمريرة ناجحة")),
        Line2D([0],[0], color=RED, lw=3, linestyle="--", label=ar_mpl_plain("تمريرة غير ناجحة")),
        Line2D([0],[0], color=GOLD, lw=3, label=ar_mpl_plain("تمريرة مفتاحية / أسيست")),
    ]
    leg = ax.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, -0.10),
                    ncol=3, frameon=False, fontsize=11)
    for t in leg.get_texts():
        t.set_color(TEXT)

    fig.text(0.5, 0.95,
             rtl_plot_text(title), ha="center", va="center",
             fontsize=16, color=TEXT,
             bbox=dict(facecolor=LINE, boxstyle="round,pad=0.6", alpha=0.95))

    fig.text(0.5, 0.055,
             rtl_plot_text(f"إجمالي التمريرات: {total}  |  الدقة: {acc:.1f}%  |  مفتاحية/أسيست: {keyp}  |  غير ناجحة: {unsucc}"),
             ha="center", va="center", fontsize=12, color=TEXT)

    # apply font properties to legend and figure texts if available
    try:
        if fp is not None:
            # set legend prop
            leg.set_prop(fp)
            # update figure text objects
            for t in fig.texts:
                try:
                    t.set_fontproperties(fp)
                except Exception:
                    pass
    except Exception:
        pass

    add_attack_direction_below(fig, direction=direction)
    return fig, {"total": total, "acc": acc, "key": keyp, "unsucc": unsucc}
# -------------------------
# METRICS
# -------------------------
def player_breakdown(x: pd.DataFrame) -> dict:
    p = filter_player_passes(x)
    p["is_success"] = p["action"].apply(is_success_pass_action)
    total_pass = int(p.shape[0])
    pass_success = int(p["is_success"].sum())
    pass_acc = safe_div(pass_success, total_pass)
    key_passes = int(p[p["action"].isin(["Key Pass","Assist"])].shape[0])
    long_pass  = int(p[contains(p["sub_attribute"], "Long Pass")].shape[0])

    dr = filter_stepout_dribbles(x)
    drib_t = int(dr.shape[0])
    drib_s = int(dr.apply(dribble_is_success, axis=1).sum()) if drib_t else 0
    drib_rate = safe_div(drib_s, drib_t)

    shots = x[x["attribute"].eq("Shooting")].copy()
    goals = int(contains(shots["action"], "Goal").sum())
    shots_t = int(shots.shape[0])
    finishing = safe_div(goals, shots_t)

    pressure     = x[contains(x["sub_attribute"], "Pressure")     | contains(x["action"], "Pressure")]
    interception = x[contains(x["sub_attribute"], "Interception") | contains(x["action"], "Interception")]
    clearance    = x[contains(x["sub_attribute"], "Clearance")    | contains(x["action"], "Clearance")]

    duels = filter_player_duels(x)
    duels_total = int(duels.shape[0])
    duels_won = int(duels.apply(duel_is_won, axis=1).sum()) if duels_total else 0
    duel_win_rate = safe_div(duels_won, duels_total)

    return {
        "passes_total": total_pass,
        "passes_success": pass_success,
        "pass_accuracy": float(pass_acc),
        "key_passes": key_passes,
        "long_passes": long_pass,

        "dribbles_total": drib_t,
        "dribbles_success": drib_s,
        "dribble_success_rate": float(drib_rate),

        "shots": shots_t,
        "goals": goals,
        "finishing_rate": float(finishing),

        "pressure": int(pressure.shape[0]),
        "interceptions": int(interception.shape[0]),
        "clearances": int(clearance.shape[0]),

        "duels_total": duels_total,
        "duels_won": duels_won,
        "duel_win_rate": float(duel_win_rate),

        "involvement": int(x.shape[0]),
    }

def compute_match_table(df_match: pd.DataFrame) -> pd.DataFrame:
    g = df_match.groupby(["player_name","team_name"], dropna=False)
    rows = []
    for (player, team), x in g:
        b = player_breakdown(x)
        rows.append({
            "player_name": player,
            "team_name": team,
            "breakdown": b,

            "Passing_raw": float(b["pass_accuracy"]),
            "Dribbling_raw": float(b["dribble_success_rate"]),
            "Shooting_raw": float(b["finishing_rate"]),
            "Physical_raw": float(b["duel_win_rate"]),
            "Defending_raw": float(b["pressure"] + b["interceptions"] + b["clearances"]),

            "passes_total": int(b["passes_total"]),
            "passes_success": int(b["passes_success"]),
            "dribbles_total": int(b["dribbles_total"]),
            "dribbles_success": int(b["dribbles_success"]),
            "duels_total": int(b["duels_total"]),
            "duels_won": int(b["duels_won"]),
            "def_actions_raw": int(b["pressure"] + b["interceptions"] + b["clearances"]),
            "shots": int(b["shots"]),
            "goals": int(b["goals"]),
        })
    out = pd.DataFrame(rows)
    if out.empty:
        return out

    for k in ["Passing","Dribbling","Shooting","Physical","Defending"]:
        raw = out[f"{k}_raw"]
        pct = raw.rank(pct=True, method="average").fillna(0)
        out[k] = (pct * 10).clip(0, 10)

    return out


# -------------------------
# DONUT
# -------------------------
def donut_chart(success, total, label, color):
    success = 0 if pd.isna(success) else int(success)
    total   = 0 if pd.isna(total) else int(total)
    success = max(0, min(success, total))

    if total == 0:
        values = [1, 0]
        pct = 0
        center_text = "0/0"
    else:
        values = [success, total-success]
        pct = int((success/total)*100)
        center_text = f"{success}/{total}"

    with mpl_arabic_rc_context():
        fig, ax = plt.subplots(figsize=(2.4, 2.4))
        fig.patch.set_facecolor(DARK_BG)
        ax.set_facecolor(DARK_BG)

        fp = arabic_fontprop()
        fp_kwargs = {"fontproperties": fp} if fp else {}

        ax.pie(values, startangle=90, colors=[color, "#1f2a44"], wedgeprops=dict(width=0.28))
        ax.text(0, 0.05, center_text, ha="center", va="center", fontsize=14, fontweight="bold", color=TEXT, **fp_kwargs)
        ax.text(0, -0.28, f"{pct}%", ha="center", va="center", fontsize=11, color=color, **fp_kwargs)
        # Title will be rendered by Streamlit (browser) using `ar_st()`
        # to avoid Matplotlib shaping issues on some systems.
        ax.axis("equal"); ax.axis("off")
        fig.tight_layout()
        return fig


# -------------------------
# RADAR (Circular)
# -------------------------
def plot_radar_5_ar(player_vals: dict, avg_vals: dict, title: str):
    labels_en = ["Passing","Dribbling","Shooting","Physical","Defending"]
    labels_ar = [ar_text("التمرير"), ar_text("المراوغة"), ar_text("التسديد"), ar_text("البدني"), ar_text("الدفاع")]

    v_player = [float(player_vals.get(k, 0.0)) for k in labels_en]
    v_avg    = [float(avg_vals.get(k, 0.0)) for k in labels_en]

    v_player += v_player[:1]
    v_avg    += v_avg[:1]
    angles = np.linspace(0, 2*np.pi, len(labels_en), endpoint=False).tolist()
    angles += angles[:1]

    with mpl_arabic_rc_context():
        fig, ax = plt.subplots(figsize=(6.4, 6.4), subplot_kw=dict(polar=True))
        fig.patch.set_facecolor(DARK_BG)
        ax.set_facecolor(DARK_BG)

        fp = arabic_fontprop()
        fp_kwargs = {"fontproperties": fp} if fp else {}

        ax.plot(angles, v_avg, linewidth=1.8, color="#94a3b8", alpha=0.95)
        ax.fill(angles, v_avg, color="#94a3b8", alpha=0.12)

        ax.plot(angles, v_player, linewidth=2.8, color=PURPLE)
        ax.fill(angles, v_player, color=PURPLE, alpha=0.25)

        ax.set_ylim(0, 10)
        ax.grid(True, alpha=0.22)

        ax.set_thetagrids(np.degrees(angles[:-1]), [""]*len(labels_en))
        label_r = 10.9
        for ang, lab in zip(angles[:-1], labels_ar):
            ax.text(ang, label_r, lab, color=TEXT, fontsize=13, ha="center", va="center", **fp_kwargs)

        ax.set_rticks([2,4,6,8,10])
        ax.tick_params(colors=MUTED)
        fig.text(0.5, 0.95,
                 ar_text(title), ha="center", va="center",
                 fontsize=16, color=TEXT,
                 bbox=dict(facecolor=LINE, boxstyle="round,pad=0.6", alpha=0.95), **fp_kwargs)

        leg = ax.legend(
            handles=[
                Line2D([0],[0], color=PURPLE, lw=3, label=ar_mpl_plain("اللاعب")),
                Line2D([0],[0], color="#94a3b8", lw=2, label=ar_mpl_plain("متوسط المباراة")),
            ],
            loc="lower center",
            bbox_to_anchor=(0.5, -0.14),
            ncol=2,
            frameon=False,
            prop=fp
        )
        # Shape legend text for Arabic and apply font properties
        try:
            for t in leg.get_texts():
                txt = t.get_text()
                t.set_text(ar_text(txt))
                t.set_color(TEXT)
                if fp is not None:
                    try:
                        t.set_fontproperties(fp)
                    except Exception:
                        pass
        except Exception:
            pass

        # Ensure all figure and axis text use the Arabic-capable FontProperties when available
        try:
            if fp is not None:
                # apply to legend and figure texts
                try:
                    leg.set_prop(fp)
                except Exception:
                    pass
                for t in fig.texts:
                    try:
                        t.set_fontproperties(fp)
                    except Exception:
                        pass
                for t in leg.get_texts():
                    try:
                        t.set_fontproperties(fp)
                    except Exception:
                        pass
                # apply to tick labels (if any)
                try:
                    for lbl in list(ax.get_xticklabels()) + list(ax.get_yticklabels()):
                        try:
                            lbl.set_fontproperties(fp)
                        except Exception:
                            pass
                except Exception:
                    pass
        except Exception:
            pass

        fig.tight_layout()
        return fig


# -------------------------
# RADAR (Cube style - 5 axes)
# -------------------------
def plot_cube_radar_5_ar(player_vals: dict, avg_vals: dict, title: str):
    labels_en = ["Passing","Dribbling","Shooting","Physical","Defending"]
    labels_ar = ["التمرير", "المراوغة", "التسديد", "البدني", "الدفاع"]

    vals_p = np.array([float(player_vals.get(k, 0.0)) for k in labels_en], dtype=float) / 10.0
    vals_a = np.array([float(avg_vals.get(k, 0.0)) for k in labels_en], dtype=float) / 10.0

    ang = np.deg2rad([90, 18, -54, -126, 162])
    dirs = np.c_[np.cos(ang), np.sin(ang)]

    def poly_points(vals):
        pts = dirs * vals[:, None]
        return np.vstack([pts, pts[0]])

    P = poly_points(vals_p)
    A = poly_points(vals_a)

    with mpl_arabic_rc_context():
        fig, ax = plt.subplots(figsize=(6.8, 6.8), dpi=160)
        fig.patch.set_facecolor(DARK_BG)
        ax.set_facecolor(DARK_BG)
        ax.set_aspect("equal")
        ax.axis("off")

        fp = arabic_fontprop()
        fp_kwargs = {"fontproperties": fp} if fp else {}

        for lvl in [0.2, 0.4, 0.6, 0.8, 1.0]:
            G = poly_points(np.ones(5) * lvl)
            ax.plot(G[:, 0], G[:, 1], color=TEXT, lw=1.3, ls="--", alpha=0.22)

        for i in range(5):
            ax.plot([0, dirs[i, 0]], [0, dirs[i, 1]], color=TEXT, lw=1.6, alpha=0.25)

        ax.plot(A[:, 0], A[:, 1], color="#94a3b8", lw=2.2, alpha=0.95)
        ax.fill(A[:, 0], A[:, 1], color="#94a3b8", alpha=0.12)

        ax.plot(P[:, 0], P[:, 1], color=PURPLE, lw=3.0, alpha=0.98)
        ax.fill(P[:, 0], P[:, 1], color=PURPLE, alpha=0.25)

        for i, lab in enumerate(labels_ar):
            x, y = dirs[i] * 1.18
            ax.text(x, y, ar_text(lab), ha="center", va="center",
                fontsize=13, color=TEXT, fontweight="bold", **fp_kwargs)

        ax.text(0, 1.52, ar_text(title), ha="center", va="center",
            fontsize=16, fontweight="bold", color=TEXT, **fp_kwargs)

        ax.plot([], [], color=PURPLE, lw=3, label=ar_mpl_plain("اللاعب"))
        ax.plot([], [], color="#94a3b8", lw=2.2, label=ar_mpl_plain("متوسط المباراة"))
        leg = ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.08), ncol=2, frameon=False, prop=fp)
        for t in leg.get_texts():
            t.set_color(TEXT)

        ax.set_xlim(-1.55, 1.55)
        ax.set_ylim(-1.45, 1.65)

        # Ensure the Arabic-capable font is applied everywhere (legend, texts, labels)
        try:
            if fp is not None:
                try:
                    leg.set_prop(fp)
                except Exception:
                    pass
                for t in fig.texts:
                    try:
                        t.set_fontproperties(fp)
                    except Exception:
                        pass
                for t in leg.get_texts():
                    try:
                        t.set_fontproperties(fp)
                    except Exception:
                        pass
                try:
                    for lbl in list(ax.get_xticklabels()) + list(ax.get_yticklabels()):
                        try:
                            lbl.set_fontproperties(fp)
                        except Exception:
                            pass
                except Exception:
                    pass
        except Exception:
            pass

        fig.tight_layout()
        return fig


def fig_to_png_bytes(obj, dpi=150):
    """Return PNG bytes for a Matplotlib Figure, PIL Image, raw bytes, BytesIO, or numpy image array.
    Falls back to an empty bytes object on failure.
    """
    buf = io.BytesIO()
    try:
        # raw bytes
        if isinstance(obj, (bytes, bytearray)):
            return bytes(obj)

        # BytesIO
        if isinstance(obj, io.BytesIO):
            return obj.getvalue()

        # PIL Image
        try:
            from PIL import Image
            if isinstance(obj, Image.Image):
                obj.save(buf, format='PNG')
                return buf.getvalue()
        except Exception:
            pass

        # Matplotlib Figure
        try:
            import matplotlib
            if isinstance(obj, matplotlib.figure.Figure) or hasattr(obj, 'savefig'):
                try:
                    obj.savefig(buf, format='png', dpi=dpi, bbox_inches='tight')
                except Exception:
                    try:
                        obj.canvas.draw()
                    except Exception:
                        pass
                    obj.savefig(buf, format='png', dpi=dpi)
                buf.seek(0)
                return buf.getvalue()
        except Exception:
            pass

        # numpy array (image)
        try:
            import numpy as _np
            if isinstance(obj, _np.ndarray):
                from PIL import Image as _PILImage
                im = _PILImage.fromarray(obj)
                im.save(buf, format='PNG')
                return buf.getvalue()
        except Exception:
            pass
    except Exception:
        pass
    return b''


# -------------------------
# OPENAI
# -------------------------
def openai_client():
    api_key = (os.getenv("OPENAI_API_KEY") or "").strip()
    if not api_key:
        return None, "OPENAI_API_KEY missing"
    try:
        return OpenAI(api_key=api_key), ""
    except Exception as e:
        return None, str(e)

def generate_ai_report_ar(payload: dict) -> str:
    client, err = openai_client()
    if client is None:
        return f"❌ خطأ: {err}"
    try:
        resp = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SCOUT_PROMPT_AR},
                {"role": "user", "content": json.dumps(payload, ensure_ascii=False, indent=2)},
            ],
            temperature=0.25
        )
        return resp.choices[0].message.content
    except Exception as e:
        return f"❌ خطأ في الذكاء الاصطناعي: {e}"

def chat_over_data_ar(question: str, context: dict) -> str:
    client, err = openai_client()
    if client is None:
        return "حالياً الذكاء الاصطناعي غير متاح (مفتاح OpenAI غير موجود)."
    try:
        resp = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": CHAT_PROMPT_AR},
                {"role": "user", "content": f"بيانات:\n{json.dumps(context, ensure_ascii=False)}\n\nالسؤال:\n{question}"}
            ],
            temperature=0.2
        )
        return resp.choices[0].message.content
    except Exception as e:
        return f"حدث خطأ في الذكاء الاصطناعي: {e}"


# -------------------------
# PDF (one-page) - FIX OVERLAP
# -------------------------
def render_one_page_a4(donuts, radar_fig, passmap_fig, report_text_ar: str, header_ar: str):
    fig = plt.figure(figsize=(8.27, 11.69), dpi=220)
    fig.patch.set_facecolor(DARK_BG)
    ax = fig.add_axes([0,0,1,1])
    ax.set_facecolor(DARK_BG)
    ax.axis("off")

    # Use Arabic-capable FontProperties when available for the header
    fp_h = arabic_fontprop()
    fp_kwargs_h = {"fontproperties": fp_h} if fp_h is not None else {}
    ax.text(0.95, 0.982, ar_text(header_ar), ha="right", va="top",
            fontsize=16, color=TEXT, fontweight="bold", **fp_kwargs_h)

    y_top = 0.84
    x0 = 0.06
    w = 0.17
    h = 0.12
    gap = 0.02
    for i, (_, dfig) in enumerate(donuts[:5]):
        img = plt.imread(io.BytesIO(fig_to_png_bytes(dfig, dpi=220)))
        ax_im = fig.add_axes([x0 + i*(w+gap), y_top, w, h])
        ax_im.imshow(img)
        ax_im.axis("off")

    radar_img = plt.imread(io.BytesIO(fig_to_png_bytes(radar_fig, dpi=220)))
    ax_r = fig.add_axes([0.06, 0.53, 0.42, 0.28])
    ax_r.imshow(radar_img)
    ax_r.axis("off")

    pass_img = plt.imread(io.BytesIO(fig_to_png_bytes(passmap_fig, dpi=220)))
    ax_p = fig.add_axes([0.52, 0.545, 0.42, 0.255])
    ax_p.imshow(pass_img)
    ax_p.axis("off")

    # Render the AI report block using PIL to ensure correct Arabic shaping
    # Prepare wrapped lines (header + body)
    lines = []
    header_line = "التقرير الكشفي (ذكاء اصطناعي)"
    lines.append((header_line, True))  # (text, is_header)

    for raw in (report_text_ar or "").splitlines():
        raw = raw.strip()
        if not raw:
            lines.append(("", False))
            continue
        for ln in textwrap.wrap(raw, width=82):
            lines.append((ln, False))

    max_lines = 34
    if len(lines) > max_lines:
        lines = lines[:max_lines-1] + [("...", False)]

    # Create an RGBA overlay image matching figure pixel size
    fw_px = int(fig.get_figwidth() * fig.dpi)
    fh_px = int(fig.get_figheight() * fig.dpi)
    overlay = Image.new("RGBA", (fw_px, fh_px), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # find a font path (prefer explicit AR_FONT_PATH)
    font_path = None
    try:
        if AR_FONT_PATH and os.path.isfile(AR_FONT_PATH):
            font_path = AR_FONT_PATH
        else:
            # prefer fonts that explicitly mention Arabic or known Arabic-friendly families
            keywords = ["arab", "noto", "amiri", "scheherazade", "tahoma", "naskh", "kufi", "arabic", "naskh"]
            for f in font_manager.fontManager.ttflist:
                name = (f.name or "").lower()
                for kw in keywords:
                    if kw in name:
                        try:
                            font_path = font_manager.findfont(f.name, fallback_to_default=True)
                            raise StopIteration
                        except Exception:
                            continue
            # fallback: try preferred list names
            names = [f.name for f in font_manager.fontManager.ttflist]
            for pref in PREFERRED_AR_FONTS:
                for n in names:
                    if pref.lower() in n.lower():
                        font_path = font_manager.findfont(n, fallback_to_default=True)
                        raise StopIteration
    except StopIteration:
        pass
    except Exception:
        font_path = None

    def hex_to_rgba(h):
        h = h.lstrip('#')
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4)) + (255,)

    text_color = hex_to_rgba(TEXT)

    # font sizing (points -> px)
    header_pt = 14
    body_pt = 11.2
    header_px = max(12, int(header_pt * fig.dpi / 72))
    body_px = max(10, int(body_pt * fig.dpi / 72))

    try:
        if font_path:
            header_font = ImageFont.truetype(font_path, header_px)
            body_font = ImageFont.truetype(font_path, body_px)
        else:
            header_font = ImageFont.load_default()
            body_font = ImageFont.load_default()
    except Exception:
        header_font = ImageFont.load_default()
        body_font = ImageFont.load_default()

    # starting pixel position (convert axes coords to pixels)
    x_frac = 0.95
    y_frac = 0.50
    x_px = int(fw_px * x_frac)
    y_px = int((1.0 - y_frac) * fh_px)  # PIL origin is top-left

    line_spacing = int(body_px * 1.25)

    for text, is_header in lines:
        if is_header:
            fp = header_font
        else:
            fp = body_font

        shaped = ar_mpl(text)
        # measure text size using draw.textbbox (more reliable for complex scripts)
        try:
            bbox = draw.textbbox((0, 0), shaped, font=fp)
            w = bbox[2] - bbox[0]
            h = bbox[3] - bbox[1]
        except Exception:
            try:
                w, h = fp.getsize(shaped)
            except Exception:
                # fallback conservative estimate
                w = int(len(shaped) * (body_px * 0.6))
                h = body_px

        draw.text((x_px - w, y_px), shaped, font=fp, fill=text_color)
        y_px += line_spacing

    # overlay onto figure
    ax_overlay = fig.add_axes([0, 0, 1, 1], zorder=11)
    ax_overlay.imshow(overlay)
    ax_overlay.axis('off')

    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight", facecolor=DARK_BG)
    plt.close(fig)
    buf.seek(0)
    return buf

def export_pdf_one_page(donuts, radar_fig, passmap_fig, report_text_ar: str, header_ar: str):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    W, H = A4
    page_img_buf = render_one_page_a4(donuts, radar_fig, passmap_fig, report_text_ar, header_ar)
    img = ImageReader(page_img_buf)
    c.drawImage(img, 0, 0, width=W, height=H, mask="auto")
    c.save()
    buf.seek(0)
    return buf


# -------------------------
# LEADERBOARD
# -------------------------
def build_event_leaderboard(df_match: pd.DataFrame, cat: str, attr: str, act: str) -> pd.DataFrame:
    x = df_match.copy()
    if cat != "الكل":
        x = x[x["attribute"] == cat].copy()
    if attr != "الكل":
        x = x[x["sub_attribute"] == attr].copy()
    if act != "الكل":
        x = x[x["action"] == act].copy()

    if x.empty:
        return pd.DataFrame(columns=["الترتيب","اللاعب","الفريق","النتيجة"])

    g = x.groupby(["player_name","team_name"]).size().reset_index(name="score")
    g = g.sort_values("score", ascending=False).reset_index(drop=True)
    g["rank"] = np.arange(1, len(g)+1)
    out = g.rename(columns={"rank":"الترتيب","player_name":"اللاعب","team_name":"الفريق","score":"النتيجة"})
    return out[["الترتيب","اللاعب","الفريق","النتيجة"]].head(20)

def bar_top10_horizontal(df_top: pd.DataFrame, title: str, value_col: str, label_col: str):
    fig, ax = plt.subplots(figsize=(10, 5), dpi=160)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    y = np.arange(len(df_top))
    ax.barh(y, df_top[value_col].values)
    ax.set_yticks(y)
    fp = arabic_fontprop()
    labels = [ar_text(x) for x in df_top[label_col].values]
    if fp is not None:
        ax.set_yticklabels(labels, fontproperties=fp, fontsize=10)
    else:
        ax.set_yticklabels(labels, fontsize=10)
    ax.invert_yaxis()
    fp = arabic_fontprop()
    if fp is not None:
        fig.text(0.5, 0.95,
                 ar_text(title), ha="center", va="center",
                 fontsize=16, color=TEXT,
                 bbox=dict(facecolor=LINE, boxstyle="round,pad=0.6", alpha=0.95), fontproperties=fp)
    else:
        fig.text(0.5, 0.95,
                 ar_text(title), ha="center", va="center",
                 fontsize=16, color=TEXT,
                 bbox=dict(facecolor=LINE, boxstyle="round,pad=0.6", alpha=0.95))
    ax.grid(axis="x", alpha=0.25)
    plt.tight_layout()
    return fig

def make_label(row):
    return f"{row['player_name']} — {row['team_name']}"

def top10_raw(metrics_df: pd.DataFrame, metric: str):
    m = metrics_df.copy()
    if metric == "تمريرات_إجمالي":
        col = "passes_total"; title = "أفضل 10 — التمرير (إجمالي التمريرات)"
    elif metric == "تمريرات_ناجحة":
        col = "passes_success"; title = "أفضل 10 — التمرير (التمريرات الناجحة)"
    elif metric == "مراوغات_إجمالي":
        col = "dribbles_total"; title = "أفضل 10 — المراوغة (إجمالي المحاولات)"
    elif metric == "مراوغات_ناجحة":
        col = "dribbles_success"; title = "أفضل 10 — المراوغة (الناجحة)"
    elif metric == "صراعات_إجمالي":
        col = "duels_total"; title = "أفضل 10 — البدني (إجمالي الصراعات)"
    elif metric == "صراعات_مكسوبة":
        col = "duels_won"; title = "أفضل 10 — البدني (الصراعات المكسبوة)"
    elif metric == "دفاع_RAW":
        col = "def_actions_raw"; title = "أفضل 10 — الدفاع (ضغط + اعتراض + إبعاد)"
    elif metric == "تسديدات":
        col = "shots"; title = "أفضل 10 — التسديد (عدد التسديدات)"
    else:
        col = "goals"; title = "أفضل 10 — الأهداف"

    m["label"] = m.apply(make_label, axis=1)
    m = m.sort_values(col, ascending=False).head(10).copy()
    m = m[["player_name","team_name","label",col]].reset_index(drop=True)
    m["rank"] = np.arange(1, len(m)+1)
    return m, col, title


# =========================
# UI
# =========================
st.title("⚽ لوحة الكشاف — تقرير لاعب + لوحات ترتيب + ذكاء اصطناعي + PDF")

st.sidebar.subheader("📂 رفع البيانات")
up = st.sidebar.file_uploader("ارفع ملف CSV", type=["csv"])
if not up:
    st.info("ارفع ملف CSV من الشريط الجانبي.")
    st.stop()

df = load_data_from_upload(up)

mode = st.sidebar.radio("اختر القسم", ["تقرير لاعب", "لوحات الترتيب"], index=0)

match_ids = sorted(pd.to_numeric(df["match_id"], errors="coerce").dropna().unique().tolist())
if not match_ids:
    st.error("لا يوجد match_id صالح داخل الملف.")
    st.stop()

match_id = st.sidebar.selectbox("اختر رقم المباراة (match_id)", match_ids)
df_match = df[pd.to_numeric(df["match_id"], errors="coerce") == match_id].copy()

# Diagnostic: Render a Matplotlib Arabic/English sample image on demand
if st.sidebar.button("تشخيص خطوط العربية في الرسم (عرض عينة)"):
    try:
        img = diagnostic_mpl_ar_demo()
        st.sidebar.image(img, caption="اختبار خطوط Matplotlib (عربي/إنجليزي)")
    except Exception as e:
        st.sidebar.error(f"خطأ أثناء إنشاء الصورة: {e}")

metrics_df = compute_match_table(df_match)
if metrics_df.empty:
    st.warning("لا توجد بيانات لاعبين في هذه المباراة.")
    st.stop()

match_table = compute_match_table(df_match)

# =========================
# LEADERBOARDS PAGE
# =========================
if mode == "لوحات الترتيب":
    st.subheader("🏆 لوحات الترتيب — (مشابهة لأسلوب StepOut)")

    tab1, tab2 = st.tabs(["أفضل 10 (RAW)", "لوحة أحداث (تصنيف/سمة/إجراء)"])

    with tab1:
        st.caption("هذه أعمدة خام (RAW) كما هي من أحداث المباراة.")

        metric_key = st.selectbox(
            "اختر مقياس RAW",
            ["تمريرات_إجمالي","تمريرات_ناجحة","مراوغات_إجمالي","مراوغات_ناجحة",
             "صراعات_إجمالي","صراعات_مكسوبة","دفاع_RAW","تسديدات","أهداف"],
            index=0
        )

        top, value_col, title = top10_raw(metrics_df, metric_key)

        st.dataframe(
            top[["rank","player_name","team_name",value_col]].rename(columns={
                "rank":"الترتيب","player_name":"اللاعب","team_name":"الفريق",value_col:"القيمة"
            }),
            use_container_width=True
        )

        fig = bar_top10_horizontal(top, title=title, value_col=value_col, label_col="label")
        st.pyplot(fig)

        st.markdown("### 🧠 تحليل أداء أفضل لاعبين حسب المقياس المختار")

        top2 = top.head(2).copy()
        payload_compare = {
            "metric": metric_key,
            "players": [
                {"player_name": row["player_name"], "team_name": row["team_name"], "value": row[value_col]}
                for _, row in top2.iterrows()
            ]
        }

        if st.button("تحليل أفضل لاعبين (AI)"):
            with st.spinner("جاري تحليل الأداء..."):
                ai_comment = generate_ai_report_ar(payload_compare)
                st.markdown("### 🔍 نتيجة التحليل")
                st.markdown(safe_rtl_html(ai_comment), unsafe_allow_html=True)

        st.markdown("### ⚔️ مقارنة لاعب ضد لاعب — رادار مكعب (5 محاور)")

        # Build disambiguated labels (player — team) to avoid duplicate names
        match_table["label"] = match_table.apply(make_label, axis=1)
        all_labels = match_table["label"].drop_duplicates().tolist()
        p1_label = st.selectbox("اختر اللاعب الأول", all_labels, key="cmp1")
        p2_label = st.selectbox("اختر اللاعب الثاني", all_labels, key="cmp2")

        radar_metrics_en = ["Passing","Dribbling","Shooting","Physical","Defending"]
        radar_metrics_ar = ["التمرير","المراوغة","التسديد","البدني","الدفاع"]

        p1_row = match_table[match_table["label"] == p1_label].iloc[0]
        p2_row = match_table[match_table["label"] == p2_label].iloc[0]

        p1_vals = np.array([p1_row[m] for m in radar_metrics_en]) / 10
        p2_vals = np.array([p2_row[m] for m in radar_metrics_en]) / 10

        angles_deg = [90, 18, -54, -126, 162]
        angles = np.deg2rad(angles_deg)

        def poly_points(vals):
            pts = np.c_[np.cos(angles), np.sin(angles)] * vals[:, None]
            return np.vstack([pts, pts[0]])

        P1 = poly_points(p1_vals)
        P2 = poly_points(p2_vals)

        fig_radar, ax = plt.subplots(figsize=(7, 7), dpi=150)
        fig_radar.patch.set_facecolor("#f7f8fa")
        ax.set_facecolor("#f7f8fa")
        ax.set_aspect("equal")
        ax.axis("off")

        # Arabic font for Matplotlib texts in this figure
        fp = arabic_fontprop()

        for lvl in [0.2, 0.4, 0.6, 0.8, 1.0]:
            G = poly_points(np.ones(5) * lvl)
            ax.plot(G[:, 0], G[:, 1], color="#999", lw=1, ls="--", alpha=0.25)

        dirs = np.c_[np.cos(angles), np.sin(angles)]
        for i in range(5):
            ax.plot([0, dirs[i, 0]], [0, dirs[i, 1]], color="#777", lw=1.3, alpha=0.4)

        ax.plot(P1[:, 0], P1[:, 1], color="#7c3aed", lw=3)
        ax.fill(P1[:, 0], P1[:, 1], color="#7c3aed", alpha=0.25)

        ax.plot(P2[:, 0], P2[:, 1], color="#0ea5e9", lw=3)
        ax.fill(P2[:, 0], P2[:, 1], color="#0ea5e9", alpha=0.25)

        for i, label in enumerate(radar_metrics_ar):
            x, y = dirs[i] * 1.25
            if fp is not None:
                ax.text(x, y, ar_text(label), ha="center", va="center", fontsize=13, color="#111", fontproperties=fp)
            else:
                ax.text(x, y, ar_text(label), ha="center", va="center", fontsize=13, color="#111")

        # ensure p1/p2 strings exist (we store rows earlier)
        try:
            p1 = p1_row["player_name"]
            p2 = p2_row["player_name"]
        except Exception:
            p1 = str(p1_row.get("player_name", "اللاعب 1"))
            p2 = str(p2_row.get("player_name", "اللاعب 2"))

        # Arabic-capable FontProperties for legend/title
        fp = arabic_fontprop()

        if fp is not None:
            ax.set_title(ar_text("مقارنة أداء اللاعبين — رادار مكعب"), fontsize=16, pad=20, color="#111", fontproperties=fp)
        else:
            ax.set_title("مقارنة أداء اللاعبين — رادار مكعب", fontsize=16, pad=20, color="#111")

        leg = ax.legend(
            handles=[
                plt.Line2D([0], [0], color="#7c3aed", lw=3, label=ar_mpl_plain(p1)),
                plt.Line2D([0], [0], color="#0ea5e9", lw=3, label=ar_mpl_plain(p2)),
            ],
            loc="lower center",
            bbox_to_anchor=(0.5, -0.12),
            ncol=2,
            frameon=False,
            prop=fp if fp is not None else None
        )

        # enforce legend text color and fontproperties
        try:
            for t in leg.get_texts():
                t.set_color("#111")
                if fp is not None:
                    try:
                        t.set_fontproperties(fp)
                    except Exception:
                        pass
        except Exception:
            pass

        st.pyplot(fig_radar)

        st.markdown("### 🧠 تحليل الذكاء الاصطناعي للرادار")

        payload_radar = {
            "player_1": {"name": p1, "scores": dict(zip(radar_metrics_en, (p1_vals * 10).tolist()))},
            "player_2": {"name": p2, "scores": dict(zip(radar_metrics_en, (p2_vals * 10).tolist()))}
        }

        if st.button("تحليل المقارنة (AI)"):
            with st.spinner("جاري تحليل المقارنة بالرادار..."):
                ai_radar_comment = generate_ai_report_ar(payload_radar)
            st.markdown(safe_rtl_html(ai_radar_comment), unsafe_allow_html=True)

    with tab2:
        st.caption("اختر (التصنيف/السمة/الإجراء) من نفس ملف الأحداث، والنتيجة = عدد تكرار الحدث لكل لاعب.")

        cats = ["الكل"] + sorted(df_match["attribute"].astype(str).unique().tolist())
        cat = st.selectbox("التصنيف (attribute)", cats, index=0)

        tmp = df_match.copy()
        if cat != "الكل":
            tmp = tmp[tmp["attribute"] == cat].copy()

        attrs = ["الكل"] + sorted(tmp["sub_attribute"].astype(str).unique().tolist())
        attr = st.selectbox("السمة (sub_attribute)", attrs, index=0)

        tmp2 = tmp.copy()
        if attr != "الكل":
            tmp2 = tmp2[tmp2["sub_attribute"] == attr].copy()

        acts = ["الكل"] + sorted(tmp2["action"].astype(str).unique().tolist())
        act = st.selectbox("الإجراء (action)", acts, index=0)

        lb = build_event_leaderboard(df_match, cat, attr, act)
        st.dataframe(lb, use_container_width=True)

        if not lb.empty:
            lb10 = lb.head(10).copy()
            lb10["label"] = lb10["اللاعب"].astype(str) + " — " + lb10["الفريق"].astype(str)
            fig2 = bar_top10_horizontal(
                lb10,
                title=f"أفضل 10 — {cat} / {attr} / {act}",
                value_col="النتيجة",
                label_col="label"
            )
            st.pyplot(fig2)

    st.stop()


# =========================
# PLAYER REPORT PAGE
# =========================
with st.expander("📌 فحص سريع للبيانات (أكثر القيم تكراراً)"):
    c1, c2, c3 = st.columns(3)
    with c1:
        st.write("أكثر 10 (attribute)")
        st.dataframe(df_match["attribute"].value_counts().head(10))
    with c2:
        st.write("أكثر 20 (sub_attribute)")
        st.dataframe(df_match["sub_attribute"].value_counts().head(20))
    with c3:
        st.write("أكثر 20 (action)")
        st.dataframe(df_match["action"].value_counts().head(20))

st.subheader("📊 جدول اللاعبين (هذه المباراة)")
st.dataframe(
    metrics_df.sort_values(["team_name","passes_total"], ascending=[True, False]).drop(columns=["breakdown"]),
    use_container_width=True
)

# Use disambiguated label (player — team) to avoid duplicate-name ambiguity
metrics_df["label"] = metrics_df.apply(make_label, axis=1)
player_label = st.selectbox("اختر اللاعب", metrics_df["label"].drop_duplicates().tolist())
row = metrics_df[metrics_df["label"] == player_label].iloc[0]
player_name = row["player_name"]
team_name = row["team_name"]
breakdown = row["breakdown"]
# Allow redaction of player name for privacy or reports
hide_name = st.checkbox("إخفاء اسم اللاعب في التقرير والرسومات", value=True)
player_display_name = "اللاعب" if hide_name else player_name

avg_vals = {
    "Passing": float(metrics_df["Passing"].mean()),
    "Dribbling": float(metrics_df["Dribbling"].mean()),
    "Shooting": float(metrics_df["Shooting"].mean()),
    "Physical": float(metrics_df["Physical"].mean()),
    "Defending": float(metrics_df["Defending"].mean()),
}
player_vals = {
    "Passing": float(row["Passing"]),
    "Dribbling": float(row["Dribbling"]),
    "Shooting": float(row["Shooting"]),
    "Physical": float(row["Physical"]),
    "Defending": float(row["Defending"]),
}

payload = {
    "player": {"name": player_display_name, "team": team_name},
    "match_context": {"match_id": str(match_id)},
    "radar_0_10": player_vals,
    "match_average_0_10": avg_vals,
    "supporting_numbers": {
        "passes_total": int(breakdown["passes_total"]),
        "passes_success": int(breakdown["passes_success"]),
        "pass_accuracy": float(breakdown["pass_accuracy"]),
        "key_passes": int(breakdown["key_passes"]),
        "long_passes": int(breakdown["long_passes"]),
        "dribbles_total": int(breakdown["dribbles_total"]),
        "dribbles_success": int(breakdown["dribbles_success"]),
        "dribble_success_rate": float(breakdown["dribble_success_rate"]),
        "shots": int(breakdown["shots"]),
        "goals": int(breakdown["goals"]),
        "pressure": int(breakdown["pressure"]),
        "interceptions": int(breakdown["interceptions"]),
        "clearances": int(breakdown["clearances"]),
        "duels_total": int(breakdown["duels_total"]),
        "duels_won": int(breakdown["duels_won"]),
        "duel_win_rate": float(breakdown["duel_win_rate"]),
    },
    "constraints": {
        "attack_direction_fixed": "visual only (no coordinate flip)",
        "must_mention_dribbles": True,
        "dribble_vs_match_average": True
    }
}

# -------------------------
# 1) Donuts
# -------------------------
st.subheader("1) مؤشرات مختصرة (Donuts)")

pass_s = int(breakdown["passes_success"])
pass_t = int(breakdown["passes_total"])
drib_s = int(breakdown["dribbles_success"])
drib_t = int(breakdown["dribbles_total"])
shot_s = int(breakdown["goals"])
shot_t = int(breakdown["shots"])
phys_s = int(breakdown["duels_won"])
phys_t = int(breakdown["duels_total"])
def_s = int(breakdown["interceptions"]) + int(breakdown["clearances"])
def_t = max(1, int(breakdown["pressure"]) + def_s)

d1,d2,d3,d4,d5 = st.columns(5)
with d1:
    fig_pass = donut_chart(pass_s, pass_t, "التمرير", PURPLE)
    st.markdown(ar_st("التمرير"))
    st.pyplot(fig_pass)
with d2:
    fig_drib = donut_chart(drib_s, drib_t, "المراوغة", BLUE)
    st.markdown(ar_st("المراوغة"))
    st.pyplot(fig_drib)
with d3:
    fig_shot = donut_chart(shot_s, shot_t, "التسديد", GREEN)
    st.markdown(ar_st("التسديد"))
    st.pyplot(fig_shot)
with d4:
    fig_phys = donut_chart(phys_s, phys_t, "البدني (الصراعات)", GOLD)
    st.markdown(ar_st("البدني (الصراعات)"))
    st.pyplot(fig_phys)
with d5:
    fig_def = donut_chart(def_s, def_t, "الدفاع", "#fb7185")
    st.markdown(ar_st("الدفاع"))
    st.pyplot(fig_def)

st.caption(ar_st("ملاحظة: المراوغات محسوبة بأسلوب أقرب لـ StepOut (Dribbling + Difficult Receives فقط)."))

# -------------------------
# 2) Radar
# -------------------------
st.subheader("2) الرادار")

radar_mode = st.radio(
    "اختر نوع الرادار",
    ["الرادار المكعّب (5 محاور)", "الرادار الدائري (5 محاور)"],
    horizontal=True
)

if radar_mode.startswith("الرادار المكعّب"):
    radar_fig = plot_cube_radar_5_ar(
        player_vals=player_vals,
        avg_vals=avg_vals,
        title=f"الرادار المكعّب — {player_display_name} ({team_name})"
    )
    st.pyplot(radar_fig)

    st.markdown(
        caption_mixed_ar([
            ("التمرير", player_vals["Passing"]),
            ("المراوغة", player_vals["Dribbling"]),
            ("التسديد", player_vals["Shooting"]),
            ("البدني", player_vals["Physical"]),
            ("الدفاع", player_vals["Defending"]),
        ]),
        unsafe_allow_html=True
    )
else:
    radar_fig = plot_radar_5_ar(
        player_vals=player_vals,
        avg_vals=avg_vals,
        title=f"{player_display_name} — {team_name}"
    )
    st.pyplot(radar_fig)

    st.markdown(
        f'<div style="direction: rtl; text-align:right;">'
        f'المراوغة (0-10): '
        f'<span dir="ltr" style="unicode-bidi:embed;">{player_vals["Dribbling"]:.2f}</span>'
        f' مقابل '
        f'<span dir="ltr" style="unicode-bidi:embed;">{avg_vals["Dribbling"]:.2f}</span>'
        f' متوسط المباراة'
        f'</div>',
        unsafe_allow_html=True
    )

# -------------------------
# 3) Pass Map
# -------------------------
st.subheader("3) خريطة التمريرات")
direction = "L2R" if ATTACK_DIR == "L2R" else "R2L"

passmap_fig, pass_stats = plot_pass_map(
    df_match=df_match,
    player=player_name,
    title=f"خريطة تمريرات — {player_display_name}",
    direction=direction
)
st.pyplot(passmap_fig)

# -------------------------
# 4) AI Report
# -------------------------
st.subheader("4) التقرير الآلي (ذكاء اصطناعي)")

cA, cB = st.columns(2)
with cA:
    if st.button("🚀 توليد التقرير العربي", use_container_width=True):
        with st.spinner("جارٍ توليد التقرير..."):
            st.session_state["last_report_ar"] = generate_ai_report_ar(payload)
with cB:
    if st.button("🧹 مسح التقرير", use_container_width=True):
        st.session_state["last_report_ar"] = ""

if st.session_state["last_report_ar"]:
    st.markdown(safe_rtl_html(st.session_state["last_report_ar"]), unsafe_allow_html=True)
else:
    st.info("اضغط زر (توليد التقرير العربي).")

# -------------------------
# 5) Chat over data
# -------------------------
st.subheader("5) محادثة عربية على بيانات المباراة")

if "chat_msgs" not in st.session_state:
    st.session_state["chat_msgs"] = []

def build_data_context():
    top10 = metrics_df.sort_values("passes_total", ascending=False).head(10)[
        ["player_name","team_name","passes_total","passes_success","dribbles_total","dribbles_success","duels_total","duels_won","def_actions_raw","shots","goals"]
    ]
    sample_events = df_match[["attribute","sub_attribute","action","description"]].head(40).fillna("").to_dict("records")
    return {
        "match_id": str(match_id),
        "top10_raw": top10.to_dict(orient="records"),
        "selected_player_payload": payload,
        "event_samples": sample_events,
        "note": "في أفضل 10: اذكر الأسماء. في وصف الحدث: لا تذكر اسم اللاعب."
    }

for m in st.session_state["chat_msgs"]:
    with st.chat_message(m["role"]):
        if m.get("role") == "assistant":
            st.markdown(safe_rtl_html(m["content"]), unsafe_allow_html=True)
        else:
            st.markdown(m["content"])

user_q = st.chat_input("اكتب سؤالك بالعربي…")
if user_q:
    st.session_state["chat_msgs"].append({"role":"user","content":user_q})
    with st.chat_message("user"):
        st.markdown(user_q)

    ctx = build_data_context()
    ans = chat_over_data_ar(user_q, ctx)
    with st.chat_message("assistant"):
        st.markdown(safe_rtl_html(ans), unsafe_allow_html=True)
    st.session_state["chat_msgs"].append({"role":"assistant","content":ans})

# -------------------------
# 6) PDF one-page
# -------------------------
st.subheader("6) تصدير PDF (صفحة واحدة)")
st.caption("إذا كان التقرير طويل سيتم اختصاره تلقائياً ليناسب الصفحة الواحدة، مع إصلاح المسافات ومنع التداخل.")

if st.button("📄 توليد PDF عربي", use_container_width=True, disabled=(st.session_state["last_report_ar"].strip() == "")):
    with st.spinner("جارٍ تجهيز ملف PDF..."):
        donuts = [
            ("التمرير", fig_pass),
            ("المراوغة", fig_drib),
            ("التسديد", fig_shot),
            ("البدني", fig_phys),
            ("الدفاع", fig_def),
        ]

        header = f"تقرير المباراة الكشفي — {player_name} | {team_name} | مباراة رقم {match_id}"

        pdf_buf = export_pdf_one_page(
            donuts=donuts,
            radar_fig=radar_fig,
            passmap_fig=passmap_fig,
            report_text_ar=st.session_state["last_report_ar"].strip(),
            header_ar=header
        )

    st.success("✅ تم إنشاء PDF بنجاح")
    st.download_button(
        "⬇️ تحميل PDF",
        data=pdf_buf,
        file_name=f"تقرير_كشفي_{player_name.replace(' ', '_')}_مباراة_{match_id}.pdf",
        mime="application/pdf",
        use_container_width=True
    )

if st.session_state["last_report_ar"].strip() == "":
    st.info("لازم تولّد التقرير أولاً ثم تصدّر PDF.")
