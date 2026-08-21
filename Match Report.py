
# دالة مصفوفة التمريرات
import arabic_reshaper
from bidi.algorithm import get_display
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
from mplsoccer import Pitch
from matplotlib.colors import to_rgba
from matplotlib.lines import Line2D
from PIL import Image
import urllib
from scipy.ndimage import gaussian_filter
from scipy.spatial import ConvexHull
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
from matplotlib.colors import to_rgba
import colorsys
from mplsoccer import Pitch
import io

from PIL import Image
import base64
from io import BytesIO
import streamlit as st
import os
import matplotlib.patheffects as path_effects

from PIL import Image
import matplotlib.image as mpimg

import streamlit as st
import os
from PIL import Image

from highlight_text import fig_text  # ⬅️ هذا هو المطلوب



import streamlit_authenticator as stauth

import streamlit as st

# رابط الصورة من GitHub (نسخة RAW)
# رابط الصورة من GitHub (نسخة RAW)

import base64
import streamlit as st

# مسار الصورة المحلي
import base64
import streamlit as st

# مسار الصورة المحلي
import base64
import streamlit as st

# مسار الصورة المحلي
#local_image_path = r"C:\Users\aalturaidi\Downloads\WhatsApp Image 2025-08-11 at 10.23.35 PM.jpeg"

# تحويل الصورة المحلية إلى Base64
#with open(local_image_path, "rb") as img_file:
#    encoded_image = base64.b64encode(img_file.read()).decode()

# عرض الصورة + النص في الوسط بحجم أكبر


# تحميل كلمات المرور المشفرة

green = '#69f900'
red = '#ff4b44'
blue = '#00a0de'
violet = '#a369ff'
bg_color= "#f5f5f5"
line_color= '#000000'
col1 = '#ff4b44'
col2 = '#00a0de'

# ألوان أساسية
bg_color = '#f5f5f5'
line_color = '#000000'

green = '#00FF00'        # تمريرة حاسمة
violet = '#8A2BE2'       # تمريرة مفتاحية

# تأثيرات النصوص
path_eff = [path_effects.Stroke(linewidth=3, foreground=bg_color), path_effects.Normal()]

# خريطة الألوان المخصصة لكل فريق
from matplotlib.colors import LinearSegmentedColormap


# تأثيرات النصوص
path_eff = [path_effects.Stroke(linewidth=3, foreground=bg_color), path_effects.Normal()]

# خريطة الألوان للفريقين
#pearl_earring_cmaph = LinearSegmentedColormap.from_list("Pearl Earring H", [bg_color, color_team1], N=20)
#pearl_earring_cmapa = LinearSegmentedColormap.from_list("Pearl Earring A", [bg_color, color_team2], N=20)

# رابط الصورة من GitHub (نسخة RAW)
image_url = "images/fg.jpg"

# عرض الصورة في الوسط
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="{image_url}" width="250">
    </div>
    """,
    unsafe_allow_html=True
)

import streamlit as st

# إعداد الصفحة


st.markdown("""
<div dir="rtl" style='background-color:#1a2a3a; padding:15px; border-radius:10px; font-size:16px; color:#f5f5f5; text-align: right;'>

 <strong>تحليل مرئي شامل للمباراة بين الفريقين:</strong>
<ul>
<li> <strong>خريطة الإحصائيات العامة:</strong> توضح المؤشرات الرئيسية مثل الاستحواذ، التمريرات، التدخلات، الضغط، والمواجهات الهوائية.</li>
<li> <strong>خريطة التسديدات:</strong> تعكس مواقع التسديدات الناجحة والخاطئة والفرص الكبيرة، موزعة حسب الفريق.</li>
<li> <strong>خريطة المرمى:</strong> تحليل مرئي لفرص التسجيل وجودة التسديدات في مواجهة المرمى.</li>
<li> <strong>تحليل الزخم:</strong> يوضح فترات السيطرة الهجومية والتهديد من كل فريق طوال زمن المباراة.</li>
</ul>
</div>
""", unsafe_allow_html=True)


# ✅ الجزء الثاني - مؤشرات إضافية RTL
# ✅ الجزء الثاني - مؤشرات إضافية RTL
st.markdown("""
<div dir="rtl" style="text-align: right;">

<h3> مؤشر PPDA (عدد التمريرات المسموح بها قبل التدخل الدفاعي)</h3>
<p>
هو مقياس يُستخدم لتحديد مدى قوة الضغط الذي يمارسه الفريق.  
كلما قل الرقم، كان الضغط أعلى وأسرع على الخصم.
</p>

<hr>

<h3> التمريرات لكل استحواذ</h3>
<p>
هو متوسط عدد التمريرات التي يُجريها الفريق خلال كل مرة يملك فيها الكرة.  
رقم مرتفع يعني لعب هادئ وتحكم بالرتم، ورقم منخفض يدل على اللعب المباشر.
</p>

<hr>

<h3> سلاسل تمرير +10</h3>
<p>
هو عدد المرات التي نفذ فيها الفريق سلسلة تمريرات متواصلة مكونة من 10 تمريرات أو أكثر.  
هذا يعكس قدرة الفريق على الحفاظ على الكرة وبناء اللعب بشكل منظم.
</p>

<hr>

<h3> ميل الملعب</h3>
<p>
هو مقياس يوضح نسبة اللعب في الثلث الهجومي للفريق مقارنة بثلثه الدفاعي.  
يُحسب من خلال نسبة التمريرات في الثلث الهجومي للفريق إلى مجموع التمريرات في الثلثين الهجوميين للفريقين.  
كلما ارتفعت النسبة دل ذلك على سيطرة أكبر في مناطق الخصم.
</p>

<!-- المعادلة بالإنجليزية -->
<p style="background-color:#222; color:#0f0; padding:10px; border-radius:8px; direction:ltr; text-align:center; font-size:15px;">
Field Tilt (%) = (Attacking Third Passes of Team) / (Attacking Third Passes of Both Teams) × 100
</p>

<!-- المعادلة بالعربية -->
<p style="background-color:#222; color:#0ff; padding:10px; border-radius:8px; text-align:center; font-size:15px;">
ميل الملعب (%) = (تمريرات الفريق في الثلث الهجومي) ÷ (مجموع تمريرات الفريقين في الثلثين الهجوميين) × 100
</p>

</div>
""", unsafe_allow_html=True)




# (اختياري) تنسيق RTL عام
st.markdown("""
    <style>
    .rtl {direction: rtl; text-align: right;}
    h1, h2, h3, h4, h5, h6, p, li {direction: rtl; text-align: right;}
    </style>
""", unsafe_allow_html=True)

# =========================

# تحميل البيانات (استخدمه في صفحات التحليل فقط)
# =========================
@st.cache_data(show_spinner=False)
def load_data_csv(path_or_url: str) -> pd.DataFrame:
    df = pd.read_csv(path_or_url)
    df.columns = df.columns.str.strip()
    return df

# =========================
# صفحة: عن المنصّة
# =========================
def about_page():
    st.markdown("""
        <style>
        .hero {
            background: linear-gradient(90deg, #f5f9ff 0%, #ffffff 100%);
            border: 1px solid #e6eefc; border-radius: 14px;
            padding: 24px 22px; margin-bottom: 16px;
        }
        .card {
            background: #ffffff; border: 1px solid #eef2f7; border-radius: 12px;
            padding: 18px 16px; margin-bottom: 12px;
            box-shadow: 0 1px 0 rgba(16,24,40,0.04);
        }
        .tag {
            display:inline-block; padding: 4px 10px; border-radius: 999px;
            background:#eef6ff; color:#1b64d8; font-size: 0.85rem; margin-left: 6px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="hero rtl"><h2>عن المنصّة</h2>'
        '<div class="tag">⚽ تحليل مباريات</div>'
        '<div class="tag">📊 إحصائيات متقدمة</div>'
        '<div class="tag">🧠 قرارات أفضل</div>'
        '</div>', unsafe_allow_html=True
    )

    st.markdown('<div class="rtl"><h3>أهمية تحليل البيانات في كرة القدم</h3></div>', unsafe_allow_html=True)
    st.markdown("""
<div class="card rtl">
في كرة القدم الحديثة، لم تعد القرارات تعتمد على الانطباعات أو المشاهدة فقط، بل أصبحت <b>البيانات</b> عنصرًا أساسيًا في فهم الواقع وصناعة الفارق داخل الملعب. يقوم <b>محلل البيانات</b> بـ:
<ul>
<li><b>جمع البيانات:</b> من المباريات والتدريبات (التمريرات، التسديدات، التحركات، الضغط).</li>
<li><b>تنظيم وتنظيف البيانات:</b> لضمان الدقة وتحويلها إلى مؤشرات قابلة للقياس.</li>
<li><b>تحليل الأداء بالمؤشرات المتقدمة:</b> 
    <ul>
        <li><b>PPDA:</b> قياس شدة الضغط الدفاعي.</li>
        <li><b>Field Tilt:</b> قياس نسبة السيطرة الهجومية.</li>
        <li><b>xT:</b> قياس التهديد المتوقع من التمريرات والحملات.</li>
        <li><b>شبكات التمرير:</b> فهم الترابط وأنماط بناء اللعب.</li>
    </ul>
</li>
<li><b>إخراج تقارير بصرية:</b> تسهّل على الجهاز الفني تحويل الأرقام إلى خطط عملية.</li>
</ul>
</div>
""", unsafe_allow_html=True)

    st.markdown('<div class="rtl"><h3>كيف يستفيد الجميع من المشروع؟</h3></div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
<div class="card rtl">
<h4>👨‍🏫 المدربون والجهاز الفني</h4>
<ul>
<li>تحليل أداء الفريق واللاعبين بالأرقام والرسوم.</li>
<li>تحديد نقاط القوة والضعف لصناعة خطط تكتيكية أدق.</li>
<li>دراسة الخصوم قبل المباريات.</li>
</ul>
</div>
<div class="card rtl">
<h4>🧑‍💻 المحللون الرياضيون</h4>
<ul>
<li>بيانات ورسوم تدعم التحليل التلفزيوني أو الصحفي.</li>
<li>تقارير احترافية مدعمة بالأرقام لتفسير مجريات اللعب.</li>
</ul>
</div>
<div class="card rtl">
<h4>🏢 إدارات الأندية</h4>
<ul>
<li>دعم قرارات التعاقد أو الاستغناء عن اللاعبين.</li>
<li>متابعة مؤشرات الأداء لفرق الفئات السنية.</li>
<li>قياس أثر التغييرات الفنية والإدارية.</li>
</ul>
</div>
""", unsafe_allow_html=True)
    with c2:
        st.markdown("""
<div class="card rtl">
<h4>⚽ اللاعبون</h4>
<ul>
<li>فهم التأثير داخل الملعب بمؤشرات دقيقة.</li>
<li>تحديد جوانب التطوير (دقة التمرير، الحركة بدون كرة...).</li>
<li>مقارنة الأداء عبر المباريات والمواسم.</li>
</ul>
</div>
<div class="card rtl">
<h4>💛 المشجعون</h4>
<ul>
<li>رؤية المباريات من منظور إحصائي، وليس بالعين فقط.</li>
<li>فهم كيف ولماذا فاز الفريق أو خسر.</li>
<li>متابعة تطور الأداء طوال الموسم.</li>
</ul>
</div>
""", unsafe_allow_html=True)

    st.markdown('<div class="rtl"><h3>ماذا تقدّم المنصّة عمليًا؟</h3></div>', unsafe_allow_html=True)
    st.markdown("""
<div class="card rtl">
<ul>
<li><b>لوحات تفاعلية:</b> إحصائيات عامة، خرائط تسديد، شبكة تمريرات، تحليلات xT والزخم.</li>
<li><b>تخصيص الألوان والعناصر:</b> لاستخدام هوية النادي في العروض.</li>
<li><b>تصدير النتائج:</b> صور/تقارير لاجتماعات الجهاز الفني أو مواد إعلامية.</li>
</ul>
<p><b>النتيجة:</b> التحليل الذكي للبيانات = قرارات أدق + أداء أقوى + نتائج أفضل.</p>
</div>
""", unsafe_allow_html=True)

    with st.expander("🔎 مثال سريع لما يمكن تحليله داخل المنصّة"):
        st.markdown("""
- مقارنة <b>Field Tilt</b> بين الشوطين لمعرفة أين كان الثقل الهجومي.
- اكتشاف <b>روابط التمرير</b> الأقوى بين اللاعبين وأثر التبديلات.
- تحديد مناطق خلق الفرص عبر <b>xT</b> لمعالجة الاختناقات الهجومية.
- ربط المؤشرات بالأحداث (هدف، بطاقة، تبديل) لفهم السياق التكتيكي.
""", unsafe_allow_html=True)


# ✅ دالة تعريب النصوص
def ar(text):
    if text is None:
        return ""
    return str(text)

# ✅ دالة إعادة تعيين التأكيد عند تغيير الاختيارات
def reset_confirmed():
    st.session_state['confirmed'] = False


# ============================ #
#      تحميل وتنظيف البيانات   #
# ============================ #

# ✅ تحميل الملف مباشرة من GitHub مع كاش

# ✅ تحميل الملف مباشرة من GitHub مع كاش
import streamlit as st
import pandas as pd

# ============================ #
#       تحميل البيانات         #
# ============================ #
# ============================ #
#       تحميل البيانات         #
# ============================ #
import streamlit as st
import pandas as pd

import streamlit as st
import pandas as pd
import io

# ========================= #
# دالة تحميل البيانات
# ========================= #
# =========================
# 📦 الاستيرادات الأساسية
# =========================
import streamlit as st
import pandas as pd
import io

# =========================
# ⚙️ دالة تحميل CSV (مع كاش)
# =========================
@st.cache_data(show_spinner=False)
def load_csv(source, is_bytes=False) -> pd.DataFrame:
    """تحميل بيانات CSV من ملف أو من رابط"""
    if is_bytes:
        df = pd.read_csv(io.BytesIO(source), low_memory=False, encoding="utf-8-sig")
    else:
        df = pd.read_csv(source, low_memory=False, encoding="utf-8-sig")
    df.columns = df.columns.str.strip()
    return df


# =========================
# 📂 تحميل بيانات المباراة
# =========================
st.markdown("## 📂 تحميل بيانات المباراة")

uploaded = st.file_uploader("⬆️ ارفع ملف CSV للمباراة", type=["csv"])
if uploaded is None:
    st.warning("⚠️ يرجى رفع ملف CSV يحتوي على مباراة واحدة.")
    st.stop()

# ✅ قراءة الملف فعليًا الآن
try:
    df = load_csv(uploaded.getvalue(), is_bytes=True)
    st.success(f"✅ تم تحميل الملف بنجاح — عدد الصفوف: {len(df):,}")
except Exception as e:
    st.error(f"❌ خطأ أثناء تحميل الملف: {e}")
    st.stop()


# =========================
# 🔍 التأكد من عمود "Big Chance"
# =========================
possible_names = ['type_value_Big Chance', 'Big Chance', 'big_chance', 'type_BigChance']
for col in df.columns:
    if any(name.lower() in col.lower() for name in possible_names):
        df.rename(columns={col: 'type_value_Big Chance'}, inplace=True)
        break
else:
    df['type_value_Big Chance'] = 0


# =========================
# 🏟️ التحقق من الأعمدة الأساسية
# =========================
required_columns = ['type', 'name', 'teamName', 'oppositionTeamName']
missing = [c for c in required_columns if c not in df.columns]
if missing:
    st.error(f"⚠️ الملف يفتقد الأعمدة الضرورية: {missing}")
    st.stop()


# =========================
# ⚽ تعريف أسماء الفرق
# =========================
try:
    hteam = df['teamName'].unique()[0]
    ateam = df['teamName'].unique()[1]
except Exception:
    hteam, ateam = "Home Team", "Away Team"

st.info(f"📊 التحليل بين: **{hteam} 🆚 {ateam}**")

# ============================ #
# 🟡 تعريف أسماء الفريقين
# ============================ #
try:
    hteam = df['teamName'].unique()[0]   # الفريق المستضيف
    ateam = df['teamName'].unique()[1]   # الفريق الضيف
except Exception as e:
    st.warning(f"⚠️ لم يتم التعرف على أسماء الفرق تلقائياً: {e}")
    hteam = "Home Team"
    ateam = "Away Team"

st.info(f"🎯 الفريق المستضيف: **{hteam}** | الفريق الضيف: **{ateam}**")

# ============================ #
# التحقق من الأعمدة
# ============================ #
required_columns = ['type', 'name', 'playerId', 'teamName', 'oppositionTeamName']
missing = [c for c in required_columns if c not in df.columns]
if missing:
    st.error(f"⚠️ الملف يفتقد الأعمدة الضرورية: {missing}")
    st.stop()


# ===========================
# 🟢 معالجة عمود pass_receiver إذا لم يكن موجودًا
# ===========================
# ===========================
# 🟢 إنشاء DataFrames لاستقبال التمريرات (Home & Away)
# ===========================

# إذا لم يكن هناك عمود pass_receiver نولده يدويًا
if 'pass_receiver' not in df.columns:
    df = df.sort_values(['teamName', 'minute', 'x', 'y'], ascending=True)
    df['pass_receiver'] = df['name'].shift(-1)
    df.loc[df['teamName'] != df['teamName'].shift(-1), 'pass_receiver'] = None

# ✅ الفريق المستضيف
if 'pass_receiver' in df.columns:
    home_receiver_df = (
        df[(df['teamName'] == hteam) & (df['type'] == 'Pass')]
        .groupby('pass_receiver')
        .size()
        .reset_index(name='pass_count')
        .sort_values('pass_count', ascending=False)
        .rename(columns={'pass_receiver': 'name'})
    )
else:
    home_receiver_df = pd.DataFrame({'name': [], 'pass_count': []})

# ✅ الفريق الضيف
if 'pass_receiver' in df.columns:
    away_receiver_df = (
        df[(df['teamName'] == ateam) & (df['type'] == 'Pass')]
        .groupby('pass_receiver')
        .size()
        .reset_index(name='pass_count')
        .sort_values('pass_count', ascending=False)
        .rename(columns={'pass_receiver': 'name'})
    )
else:
    away_receiver_df = pd.DataFrame({'name': [], 'pass_count': []})

# ✅ تعبئة اسم اللاعب في حمل الكرة إذا مفقود
df.loc[
    (df['type'] == 'Carry') & (df['name'].isna()) & (df['playerId'] == df['playerId'].shift(-1)),
    'name'
] = df['name'].shift(-1)

# ✅ اختصار الأسماء
def get_short_name(full_name):
    if pd.isna(full_name):
        return full_name
    parts = str(full_name).split()
    if len(parts) == 1:
        return full_name
    elif len(parts) == 2:
        return parts[0][0] + ". " + parts[1]
    else:
        return parts[0][0] + ". " + parts[1][0] + ". " + " ".join(parts[2:])

df['shortName'] = df['name'].apply(get_short_name)

# ✅ عمود الأهداف العكسية
df['type_value_Own goal'] = pd.to_numeric(
    df.get('type_value_Own goal', pd.Series([0]*len(df))), errors='coerce'
).fillna(0)

# ✅ إنشاء عمود team_vs
if 'team_vs' not in df.columns:
    if {'teamName', 'oppositionTeamName'}.issubset(df.columns):
        df['team_vs'] = df.apply(
            lambda row: " vs ".join(sorted([str(row['teamName']), str(row['oppositionTeamName'])])),
            axis=1
        )
    else:
        st.error("⚠️ الملف لا يحتوي على أعمدة الفريقين.")
        st.stop()


# ============================ #
# اختيارات الواجهة             #
# ============================ #
# ============================ #
# تحديد الشوط المطلوب بشكل دقيق #
# ============================ #
if "minute" not in df.columns:
    st.warning("⚠️ لا يوجد عمود 'minute' لتحديد الشوط، سيتم استخدام المباراة كاملة.")
    df_selected = df.copy()
else:
    half_option = st.radio(
        "⏱️ اختر الفترة:",
        ["الشوط الأول", "الشوط الثاني", "المباراة كاملة"],
        horizontal=True
    )

    if half_option == "الشوط الأول":
        df_selected = df[(df["minute"] >= 0) & (df["minute"] < 45)]
    elif half_option == "الشوط الثاني":
        df_selected = df[(df["minute"] >= 45) & (df["minute"] <= 90)]
    else:
        df_selected = df.copy()


df = df_selected.copy()

# ✅ اختيار المباراة
matches = sorted(df['team_vs'].dropna().unique().tolist())
if not matches:
    st.error("⚠️ لا توجد مباريات في هذه الجولة.")
    st.stop()

selected_match = st.selectbox("⚽ اختر المباراة", matches)
match_df = df[df['team_vs'] == selected_match]


# ============================ #
#          معالجة المباراة     #
# ============================ #
if selected_match:
    df = df[df['team_vs'] == selected_match].copy()
    df_match = df.copy()
    st.session_state['df_match'] = df_match

    t1, t2 = selected_match.split(" vs ")

    if 'h_a' in df.columns:
        ha = df[['teamName', 'h_a']].dropna()
        # تطبيع القيم المحتملة
        ha['h_a_norm'] = ha['h_a'].astype(str).str.lower().map({'h': 'h', 'a': 'a', 'home': 'h', 'away': 'a'})
        home_name = ha.loc[ha['h_a_norm'] == 'h', 'teamName']
        away_name = ha.loc[ha['h_a_norm'] == 'a', 'teamName']
        if not home_name.empty and not away_name.empty:
            hteamName, ateamName = home_name.iloc[0], away_name.iloc[0]
        else:
            hteamName, ateamName = t1, t2
    else:
        hteamName, ateamName = t1, t2

    st.session_state['hteam'] = hteamName
    st.session_state['ateam'] = ateamName

    homedf = df[df['teamName'] == hteamName].copy()
    awaydf = df[df['teamName'] == ateamName].copy()

    score_df = df[df['type'] == 'Goal'][['type', 'minute', 'type_value_Own goal', 'name', 'teamName']].fillna(0)
    h_goal = score_df[(score_df['teamName'] == hteamName) & (score_df['type_value_Own goal'] == 0)]
    h_og   = score_df[(score_df['teamName'] == hteamName) & (score_df['type_value_Own goal'] != 0)]
    a_goal = score_df[(score_df['teamName'] == ateamName) & (score_df['type_value_Own goal'] == 0)]
    a_og   = score_df[(score_df['teamName'] == ateamName) & (score_df['type_value_Own goal'] != 0)]
    hgoal_count = len(h_goal) + len(a_og)
    agoal_count = len(a_goal) + len(h_og)

    st.markdown(f"###  النتيجة: {ar(hteamName)} {hgoal_count} - {agoal_count} {ar(ateamName)}")

    # 👥 أسماء اللاعبين (قد تحتاجها لاحقًا)
    hpnames = homedf['name'].dropna().unique()
    apnames = awaydf['name'].dropna().unique()
    home_unique_players = homedf['name'].dropna().unique()
    away_unique_players = awaydf['name'].dropna().unique()

   

    



    team_for_sonar = hteamName  # أو ateamName إذا أردت الفريق الضيف

    # استخراج التمريرات للفريق المختار
    passes = df_match[(df_match['teamName'] == team_for_sonar) & (df_match['type'] == 'Pass')].copy()

    if passes.empty:
        st.warning(" لا توجد تمريرات لهذا الفريق في المباراة.")
        st.stop()

    # التأكد من توفّر إحداثيات النهاية
    if 'end_x' not in passes.columns and 'endX' in passes.columns:
        passes['end_x'] = passes['endX']
    if 'end_y' not in passes.columns and 'endY' in passes.columns:
        passes['end_y'] = passes['endY']

    needed_xy = ['x', 'y', 'end_x', 'end_y']
    missing_xy = [c for c in needed_xy if c not in passes.columns]
    if missing_xy:
        st.error(f" أعمدة الإحداثيات غير مكتملة (مفقود: {missing_xy}).")
        st.stop()

    # حساب الطول والزاوية
    passes['length'] = np.sqrt((passes['end_x'] - passes['x'])**2 + (passes['end_y'] - passes['y'])**2)
    passes['angle']  = np.arctan2(passes['end_y'] - passes['y'], passes['end_x'] - passes['x'])

    passes['angle_bin'] = pd.cut(
        passes['angle'],
        bins=np.linspace(-np.pi, np.pi, 21),
        labels=False,
        include_lowest=True
    )

    sonar_df = passes.groupby(["name", "angle_bin"], as_index=False).agg({"length": "mean"})
    pass_amt = passes.groupby(['name', 'angle_bin']).size().to_frame(name='amount').reset_index()
    sonar_df = pd.merge(sonar_df, pass_amt, on=['name', 'angle_bin'])

    average_location = passes.groupby('name', as_index=False).agg({'x': 'mean', 'y': 'mean'})
    sonar_df = sonar_df.merge(average_location, on="name", how="left")


else:
    st.warning(" الرجاء تحديد مباراة لتحليلها.")

# =========================
# ========================================
# 🔹 تحديد أكثر لاعب استقبل تمريرات (Home Team)
# ========================================
if 'pass_receiver' in df.columns:
    home_receiver_df = (
        df[(df['teamName'] == hteam) & (df['type'] == 'Pass')]
        .groupby('pass_receiver')
        .size()
        .reset_index(name='pass_count')
        .sort_values('pass_count', ascending=False)
        .rename(columns={'pass_receiver': 'name'})
    )
elif 'name' in df.columns:
    home_receiver_df = (
        df[(df['teamName'] == hteam) & (df['type'] == 'Pass')]
        .groupby('name')
        .size()
        .reset_index(name='pass_count')
        .sort_values('pass_count', ascending=False)
    )
else:
    home_receiver_df = pd.DataFrame({'name': [], 'pass_count': []})

# Stats
        
#Possession%

 # Stats
        
        #Possession%
hpossdf = df[(df['teamName']==hteamName) & (df['type']=='Pass')]
apossdf = df[(df['teamName']==ateamName) & (df['type']=='Pass')]
hposs = round((len(hpossdf)/(len(hpossdf)+len(apossdf)))*100,2)
aposs = round((len(apossdf)/(len(hpossdf)+len(apossdf)))*100,2)
        
        #Field Tilt%
# --- Field Tilt (الثلث الهجومي) ---
# تأكد أن الأعمدة رقمية
for c in ["x", "endX", "isTouch"]:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce")

# قناع "لمسة" في حال عمود isTouch غير موجود
if "isTouch" in df.columns:
    touch_mask = df["isTouch"] == 1
else:
    touch_mask = df["type"].isin(["Pass", "Carry", "Dribble", "BallRecovery", "Shot", "Cross", "TakeOn"])

# استخدم endX إن وُجد وإلا x
X = "endX" if "endX" in df.columns else "x"

# المضيف: إلى اليمين ⇒ X >= 70
hftdf = df[(df["teamName"] == hteamName) & touch_mask & (df[X] >= 70)]

# الضيف: إلى اليسار ⇒ X <= 35
aftdf = df[(df["teamName"] == ateamName) & touch_mask & (df[X] <= 35)]

hft_n = len(hftdf)
aft_n = len(aftdf)
den = hft_n + aft_n

if den == 0:
    hft = aft = 0.0
else:
    hft = round(hft_n / den * 100, 2)
    aft = round(aft_n / den * 100, 2)
   
        #Total Passes
htotalPass = len(df[(df['teamName']==hteamName) & (df['type']=='Pass')])
atotalPass = len(df[(df['teamName']==ateamName) & (df['type']=='Pass')])
        
        #Accurate Pass
hAccPass = len(df[(df['teamName']==hteamName) & (df['type']=='Pass') & (df['outcomeType']=='Successful')])
aAccPass = len(df[(df['teamName']==ateamName) & (df['type']=='Pass') & (df['outcomeType']=='Successful')])
        
        #LongBall
hLongB = len(df[(df['teamName']==hteamName) & (df['type']=='Pass') & (df['type_value_Long ball']==1) & (df['type_value_Corner taken']!=6) & (df['type_value_Cross']!=1)])
aLongB = len(df[(df['teamName']==ateamName) & (df['type']=='Pass') & (df['type_value_Long ball']==1) & (df['type_value_Corner taken']!=6) & (df['type_value_Cross']!=1)])
        #Accurate LongBall
hAccLongB = len(df[(df['teamName']==hteamName) & (df['type']=='Pass') & (df['type_value_Long ball']==1) & (df['outcomeType']=='Successful') & (df['type_value_Corner taken']!=6) & (df['type_value_Cross']!=1)])
aAccLongB = len(df[(df['teamName']==ateamName) & (df['type']=='Pass') & (df['type_value_Long ball']==1) & (df['outcomeType']=='Successful') & (df['type_value_Corner taken']!=6) & (df['type_value_Cross']!=1)])
        
        # Defensive Stats
htkl = len(df[(df['teamName']==hteamName) & (df['type']=='Tackle')])
atkl = len(df[(df['teamName']==ateamName) & (df['type']=='Tackle')])
        
        #Tackles Won
htklw = len(df[(df['teamName']==hteamName) & (df['type']=='Tackle') & (df['outcomeType']=='Successful')])
atklw = len(df[(df['teamName']==ateamName) & (df['type']=='Tackle') & (df['outcomeType']=='Successful')])
        
        #Interceptions
hintc= len(df[(df['teamName']==hteamName) & (df['type']=='Interception')])
aintc= len(df[(df['teamName']==ateamName) & (df['type']=='Interception')])
        
        #Clearances
hclr= len(df[(df['teamName']==hteamName) & (df['type']=='Clearance')])
aclr= len(df[(df['teamName']==ateamName) & (df['type']=='Clearance')])
        
        #Aerials
harl= len(df[(df['teamName']==hteamName) & (df['type']=='Aerial')])
aarl= len(df[(df['teamName']==ateamName) & (df['type']=='Aerial')])
        
        #Aerials Wins
harlw= len(df[(df['teamName']==hteamName) & (df['type']=='Aerial') & (df['outcomeType']=='Successful')])
aarlw= len(df[(df['teamName']==ateamName) & (df['type']=='Aerial') & (df['outcomeType']=='Successful')])
        
        # PPDA
home_def_acts = df[(df['teamName']==hteamName) & (df['type'].str.contains('Interception|Foul|Challenge|BlockedPass|Tackle')) & (df['x']>35)]
away_def_acts = df[(df['teamName']==ateamName) & (df['type'].str.contains('Interception|Foul|Challenge|BlockedPass|Tackle')) & (df['x']>35)]
home_pass = df[(df['teamName']==hteamName) & (df['type']=='Pass') & (df['outcomeType']=='Successful') & (df['x']<70)]
away_pass = df[(df['teamName']==ateamName) & (df['type']=='Pass') & (df['outcomeType']=='Successful') & (df['x']<70)]
home_ppda = round((len(away_pass)/len(home_def_acts)), 2)
away_ppda = round((len(home_pass)/len(away_def_acts)), 2)
        
        # Average Passes per Sequence
pass_df_home = df[(df['type'] == 'Pass') & (df['teamName']==hteamName)]
pass_counts_home = pass_df_home.groupby('possession_id').size()
PPS_home = pass_counts_home.mean().round()
pass_df_away = df[(df['type'] == 'Pass') & (df['teamName']==ateamName)]
pass_counts_away = pass_df_away.groupby('possession_id').size()
PPS_away = pass_counts_away.mean().round()
        
        # Number of Sequence with 10+ Passes
possessions_with_10_or_more_passes = pass_counts_home[pass_counts_home >= 10]
pass_seq_10_more_home = possessions_with_10_or_more_passes.count()
possessions_with_10_or_more_passes = pass_counts_away[pass_counts_away >= 10]
pass_seq_10_more_away = possessions_with_10_or_more_passes.count()
        
path_eff1 = [path_effects.Stroke(linewidth=1.5, foreground=line_color), path_effects.Normal()]
path_eff = [path_effects.Stroke(linewidth=3, foreground=bg_color), path_effects.Normal()]
# =========================
# أدوات مساعدة عامة
# =========================
def ar(text: str) -> str:
    """تعريب النص (اتجاه عربي صحيح)."""
    return str(text)

def compute_field_tilt(
    df, home_team, away_team,
    team_col="teamName",
    prefer_end=True,                      # استخدم endX إن وُجد
    use_types=("Pass","Carry","Dribble","BallRecovery","Shot","Cross","TakeOn"),
    face_each_other=True                  # الضيف يهاجم لليسار
):
    import numpy as np
    import pandas as pd

    # تحويل الإحداثيات لأرقام
    for c in ["x", "endX"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    # اختر العمود (endX أولًا إن توافر)
    X = "endX" if (prefer_end and "endX" in df.columns) else "x"

    # تصفية الأحداث التي تُحسب
    if "type" in df.columns and use_types:
        if isinstance(use_types, (list, tuple, set)):
            mask = df["type"].astype(str).isin(use_types)
        else:
            mask = df["type"].astype(str).str.contains(str(use_types), case=False, na=False)
        d = df.loc[mask, [team_col, X]].dropna().copy()
    else:
        d = df[[team_col, X]].dropna().copy()

    if d.empty:
        return {"home_count": 0, "away_count": 0, "home_ft": 0.0, "away_ft": 0.0, "x_col": X}

    # حدود الثلثين من النطاق الفعلي
    max_x = float(d[X].max())
    left_third  = max_x / 3.0
    right_third = 2.0 * max_x / 3.0

    d_home = d[d[team_col] == home_team]
    d_away = d[d[team_col] == away_team]

    # المستضيف: الثلث الهجومي يمين
    home_count = int((d_home[X] >= right_third).sum())

    # الضيف: يسار إذا متقابلين، وإلا يمين
    if face_each_other:
        away_count = int((d_away[X] <= left_third).sum())
    else:
        away_count = int((d_away[X] >= right_third).sum())

    total = home_count + away_count
    home_ft = round(home_count / total * 100.0, 2) if total else 0.0
    away_ft = round(100.0 - home_ft, 2) if total else 0.0

    return {"home_count": home_count, "away_count": away_count,
            "home_ft": home_ft, "away_ft": away_ft, "x_col": X}


# ===== Field Tilt helpers =====
from mplsoccer import Pitch
from matplotlib.patches import Rectangle

def compute_field_tilt(
    df, home_team, away_team,
    team_col="teamName",
    prefer_end=True,   # استخدم endX إن وُجد
    use_types=("Pass","Carry","Dribble","BallRecovery","Shot","Cross","TakeOn"),
    face_each_other=True
):
    import numpy as np
    import pandas as pd

    # تحويل إحداثيات لأرقام
    for c in ["x", "endX"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    # اختر العمود X
    X = "endX" if (prefer_end and "endX" in df.columns) else "x"

    # أحداث تُحسب كـ لمسات/تمريرات
    if "type" in df.columns and use_types:
        if isinstance(use_types, (list, tuple, set)):
            mask = df["type"].astype(str).isin(use_types)
        else:
            mask = df["type"].astype(str).str.contains(str(use_types), case=False, na=False)
        d = df.loc[mask, [team_col, X]].dropna().copy()
    else:
        d = df[[team_col, X]].dropna().copy()

    if d.empty:
        return dict(home_count=0, away_count=0, home_ft=0.0, away_ft=0.0, x_col=X)

    # حدود الأثلاث من نطاق البيانات نفسه
    max_x = float(d[X].max())
    left_third  = max_x / 3.0
    right_third = 2.0 * max_x / 3.0

    d_home = d[d[team_col] == home_team]
    d_away = d[d[team_col] == away_team]

    # المضيف دائمًا يهاجم يمينًا
    home_count = int((d_home[X] >= right_third).sum())

    # الضيف يسار إذا متقابلين
    away_count = int((d_away[X] <= left_third).sum()) if face_each_other else int((d_away[X] >= right_third).sum())

    total = home_count + away_count
    if total == 0:
        home_ft = away_ft = 0.0
    else:
        home_ft = round(home_count / total * 100.0, 2)
        away_ft = round(100.0 - home_ft, 2)

    return dict(home_count=home_count, away_count=away_count,
                home_ft=home_ft, away_ft=away_ft, x_col=X)


def draw_field_tilt_both_teams(
    df, home_team, away_team,
    team_col="teamName",
    pitch_type="statsbomb",
    home_color="#1565C0", away_color="#C62828",
    face_each_other=True,                 # تقابل: الضيف يهاجم لليسار
    use_types=None,                       # إن تُركت None تُستخدم افتراضات compute_field_tilt
    show_arrows=True,
    prefer_end=True
):
    # تعريب آمن
    def ar(t): return str(t)

    # حساب الميل الموحّد
    stats = compute_field_tilt(
        df, home_team, away_team,
        team_col=team_col,
        prefer_end=prefer_end,
        use_types=use_types if use_types is not None else ("Pass","Carry","Dribble","BallRecovery","Shot","Cross","TakeOn"),
        face_each_other=face_each_other
    )
    home_ft = stats["home_ft"]
    # عرض كنِسَب صحيحة مع ضمان المجموع 100
    home_disp = int(round(home_ft))
    away_disp = 100 - home_disp

    # الرسم
    pitch = Pitch(pitch_type=pitch_type, line_color="black")
    fig, ax = pitch.draw(figsize=(10, 6))
    L = pitch.dim.pitch_length
    W = pitch.dim.pitch_width

    # تظليل الثلث الهجومي لكل فريق
    ax.add_patch(Rectangle((L*(2/3), 0), L/3, W, color=home_color, alpha=0.18, lw=0))  # المضيف يمينًا
    away_third_x = 0 if face_each_other else L*(2/3)
    ax.add_patch(Rectangle((away_third_x, 0), L/3, W, color=away_color, alpha=0.18, lw=0))

    # النِّسب
    ax.text(L*5/6, W/2, f"{home_disp}%", ha="center", va="center",
            fontsize=26, weight="bold", color=home_color)
    ax.text((L*1/6 if face_each_other else L*5/6), W/2, f"{away_disp}%", ha="center", va="center",
            fontsize=26, weight="bold", color=away_color)

    # أسهم اتجاه اللعب
    if show_arrows:
        # المضيف يمينًا
        ax.annotate("", xy=(L*0.88, W*0.90), xytext=(L*0.62, W*0.90),
                    arrowprops=dict(arrowstyle='-|>', lw=2.2, color=home_color))
        ax.text(L*0.75, W*0.95, ar("اتجاه لعب") + f" {home_team}",
                ha="center", va="bottom", fontsize=11, color=home_color)

        # الضيف
        if face_each_other:
            xy, xytext, label_x = (L*0.12, W*0.10), (L*0.38, W*0.10), (L*0.25)
        else:
            xy, xytext, label_x = (L*0.88, W*0.10), (L*0.62, W*0.10), (L*0.75)

        ax.annotate("", xy=xy, xytext=xytext,
                    arrowprops=dict(arrowstyle='-|>', lw=2.2, color=away_color))
        ax.text(label_x, W*0.05, ar("اتجاه لعب") + f" {away_team}",
                ha="center", va="top", fontsize=11, color=away_color)

    ax.set_title(f"{ar('ميل الملعب – تمريرات/لمسات الثلث الهجومي')}\n{home_team} ضد {away_team}", fontsize=14)
    fig.tight_layout()

    stats.update({
        "home_color": home_color,
        "away_color": away_color,
        "home_ft_display": home_disp,
        "away_ft_display": away_disp
    })
    return fig, stats

# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
def plotting_match_stats(
    ax,
    df,
    hteamName: str,
    ateamName: str,
    col1: str = "#43A1D5",   # لون المضيف
    col2: str = "#FF4C4C",   # لون الضيف
    bg_color: str = "#0C0D0E",
    line_color: str = "white",
):
    """
    يرسم لوحة «إحصائيات المباراة» (10 بنود) مع تعريب كامل.
    البنود: الاستحواذ – ميل الملعب – التمريرات(الناجحة) – الكرات الطويلة(الناجحة) – الافتكاكات
            التشتيت – الثنائيات الهوائية – PPDA – تمريرات/استحواذ – سلاسل 10+ تمريرة
    """
    # ====== واردات محلية ======
    import re
    import numpy as np
    import pandas as pd
    import matplotlib.patheffects as path_effects
    from mplsoccer import Pitch

    # ====== دوال مساعدة ======
    def ar(text: str) -> str:
        return str(text)

    def safe_len(frame):
        try:
            return int(len(frame))
        except Exception:
            return 0

    def _col(df_, name, fallback=None):
        """إرجاع عمود إذا وُجد وإلا سلسلة/قيمة بديلة بنفس الطول"""
        if name in df_.columns:
            return df_[name]
        if fallback is not None:
            return fallback
        return pd.Series([np.nan] * len(df_))

    def to_num_cols(df_, cols):
        for c in cols:
            if c in df_.columns:
                df_[c] = pd.to_numeric(df_[c], errors="coerce")

    # اجعل الأعمدة الرقمية فعلًا أرقامًا
    to_num_cols(df, ["x", "y", "endX", "endY", "isTouch"])

    # ====== تقسيم بيانات الفريقين ======
    hdf = df[df["teamName"] == hteamName].copy()
    adf = df[df["teamName"] == ateamName].copy()

    # ====== الاستحواذ (تقريبًا: نسبة عدد التمريرات) ======
    hpossdf = hdf[hdf["type"] == "Pass"]
    apossdf = adf[adf["type"] == "Pass"]
    total_poss = safe_len(hpossdf) + safe_len(apossdf)
    hposs = round((safe_len(hpossdf) / total_poss) * 100, 2) if total_poss > 0 else 0.0
    aposs = round((safe_len(apossdf) / total_poss) * 100, 2) if total_poss > 0 else 0.0

    # ====== Field Tilt (ميل الملعب) الموحَّد ======
    ft_stats = compute_field_tilt(
        df, hteamName, ateamName,
        team_col="teamName",
        prefer_end=True,      # استخدم endX إن وُجد
        face_each_other=True  # نفس اتجاه التقابل المستخدم في الرسم
    )
    hft, aft = ft_stats["home_ft"], ft_stats["away_ft"]

    # ====== تمريرات إجمالي/ناجح ======
    htotalPass = safe_len(hpossdf)
    atotalPass = safe_len(apossdf)
    hpass_acc = safe_len(hpossdf[hpossdf["outcomeType"] == "Successful"])
    apass_acc = safe_len(apossdf[apossdf["outcomeType"] == "Successful"])

    # ====== الكرات الطويلة ======
    long_col = "type_value_Long ball"
    hLongB_df = hdf[(hdf["type"] == "Pass") & (_col(hdf, long_col, 0) == 1)]
    aLongB_df = adf[(adf["type"] == "Pass") & (_col(adf, long_col, 0) == 1)]
    hLongB = safe_len(hLongB_df)
    aLongB = safe_len(aLongB_df)
    hlong_acc = safe_len(hLongB_df[hLongB_df["outcomeType"] == "Successful"])
    along_acc = safe_len(aLongB_df[aLongB_df["outcomeType"] == "Successful"])

    # ====== الدفاع ======
    def cnt(df_, t):  # عدّ نوع الحدث بأمان
        return safe_len(df_[df_["type"] == t])

    htkl, atkl = cnt(hdf, "Tackle"), cnt(adf, "Tackle")
    hclr, aclr = cnt(hdf, "Clearance"), cnt(adf, "Clearance")
    harl, aarl = cnt(hdf, "Aerial"), cnt(adf, "Aerial")

    # ====== PPDA ======
    def_actions_pattern = re.compile(r"Interception|Foul|Challenge|BlockedPass|Tackle", flags=re.I)
    home_def_acts = hdf[
        _col(hdf.astype({"type": str}), "type").str.contains(def_actions_pattern, na=False)
        & (_col(hdf, "x", pd.Series([0] * len(hdf))) > 35)
    ]
    away_def_acts = adf[
        _col(adf.astype({"type": str}), "type").str.contains(def_actions_pattern, na=False)
        & (_col(adf, "x", pd.Series([0] * len(adf))) > 35)
    ]
    home_pass = hdf[(hdf["type"] == "Pass") & (_col(hdf, "x", pd.Series([0] * len(hdf))) < 70)]
    away_pass = adf[(adf["type"] == "Pass") & (_col(adf, "x", pd.Series([0] * len(adf))) < 70)]
    home_def_n = safe_len(home_def_acts)
    away_def_n = safe_len(away_def_acts)
    home_ppda = round(safe_len(away_pass) / home_def_n, 2) if home_def_n > 0 else np.nan
    away_ppda = round(safe_len(home_pass) / away_def_n, 2) if away_def_n > 0 else np.nan

    # ====== تمريرات/استحواذ (PPS) و 10+ تمريرة ======
    def passes_per_sequence(team_df):
        if "possession_id" not in team_df.columns:
            return 0.0, 0
        g = team_df[team_df["type"] == "Pass"].groupby("possession_id").size()
        mean = float(g.mean()) if not g.empty else 0.0
        seq10 = int((g >= 10).sum()) if not g.empty else 0
        return mean, seq10

    PPS_home, pass_seq_10_more_home = passes_per_sequence(hdf)
    PPS_away, pass_seq_10_more_away = passes_per_sequence(adf)

    # ====== البدء في الرسم ======
    pe_border = [path_effects.Stroke(linewidth=3, foreground=bg_color), path_effects.Normal()]
    pitch = Pitch(pitch_type="uefa", corner_arcs=True, pitch_color=bg_color, line_color=bg_color, linewidth=2)
    pitch.draw(ax=ax)
    ax.set_xlim(-0.5, 105.5)
    ax.set_ylim(-5, 68.5)

    # الهيدر
    ax.fill([0, 0, 105, 105], [62, 68, 68, 62], "#F5A000")
    ax.text(52.5, 64.5, ar("إحصائيات المباراة"), ha="center", va="center",
            color=line_color, fontsize=28, fontweight="bold", path_effects=pe_border)

    # ----- بيانات التطبيع للشريطين (10 بنود فقط) -----
    stats_y = [58 - i * 6 for i in range(10)]

    stats_home = [
        hposs,
        hft,                  # Field Tilt (من الحساب الموحَّد)
        htotalPass,
        hLongB,
        htkl,
        hclr,
        harl,
        (0.0 if np.isnan(home_ppda) else home_ppda),
        PPS_home,
        pass_seq_10_more_home
    ]
    stats_away = [
        aposs,
        aft,                  # Field Tilt (Away)
        atotalPass,
        aLongB,
        atkl,
        aclr,
        aarl,
        (0.0 if np.isnan(away_ppda) else away_ppda),
        PPS_away,
        pass_seq_10_more_away,
    ]

    # تطبيع إلى ±50 حول المركز 52.5
    stats_home_norm, stats_away_norm = [], []
    for hv, av in zip(stats_home, stats_away):
        tot = (hv + av)
        if tot == 0:
            stats_home_norm.append(0.0)
            stats_away_norm.append(0.0)
        else:
            stats_home_norm.append(-hv / tot * 50.0)
            stats_away_norm.append( av / tot * 50.0)

    ax.barh(stats_y, stats_home_norm, height=4, color=col1, left=52.5)
    ax.barh(stats_y, stats_away_norm, height=4, color=col2, left=52.5)

    # ----- العناوين -----
    stat_labels = [
        "الاستحواذ",
        "ميل الملعب (Field Tilt)",
        "التمريرات (الناجحة)",
        "الكرات الطويلة (الناجحة)",
        "الافتكاكات",
        "التشتيت",
        "الثنائيات الهوائية",
        "مؤشر PPDA",
        "تمريرات/استحواذ",
        "سلاسل 10+ تمريرة",
    ]

    # الأرقام الخام يمين/يسار
    stats_home_raw = [
        f"{int(round(hposs))}%",
        f"{int(round(hft))}%",                 # Field Tilt Home
        f"{htotalPass} ({hpass_acc})",
        f"{hLongB} ({hlong_acc})",
        int(htkl),
        int(hclr),
        int(harl),
        ("-" if np.isnan(home_ppda) else f"{home_ppda:.2f}"),
        (f"{PPS_home:.2f}" if PPS_home == PPS_home else "0.00"),
        int(pass_seq_10_more_home),
    ]
    stats_away_raw = [
        f"{int(round(aposs))}%",
        f"{int(round(aft))}%",                 # Field Tilt Away
        f"{atotalPass} ({apass_acc})",
        f"{aLongB} ({along_acc})",
        int(atkl),
        int(aclr),
        int(aarl),
        ("-" if np.isnan(away_ppda) else f"{away_ppda:.2f}"),
        (f"{PPS_away:.2f}" if PPS_away == PPS_away else "0.00"),
        int(pass_seq_10_more_away),
    ]

    # تسميات البنود في المنتصف
    for y, label in zip(stats_y, stat_labels):
        ax.text(52.5, y, ar(label), color="black", fontsize=15, weight="bold",
                ha="center", va="center")

    # القيم على الجانبين
    for i, y in enumerate(stats_y):
        ax.text(0,   y, f"{stats_home_raw[i]}", color=line_color, fontsize=20,
                ha="right", va="center", fontweight="bold")
        ax.text(105, y, f"{stats_away_raw[i]}", color=line_color, fontsize=20,
                ha="left",  va="center", fontweight="bold")

    # خط سفلي تمييزي بسيط
    ax.axhline(-1.5, color=bg_color, linewidth=0)
    return




    # تنفيذ خريطة التسديد والتحليل
def draw_shotmap_both_teams(df, hteamName, ateamName, col1, col2, bg_color, line_color, ax=None):
    """
    ترسم خريطة تسديدات الفريقين + شريط إحصائي وسطي.
    - يعتمد تحديد المُسدد على teamName (أدق من possession_team لأحداث التسديد).
    - يقلب إحداثيات تسديدات المستضيف ليهاجم من اليمين لتوحيد الاتجاه البصري.
    """
    import matplotlib.pyplot as plt
    from mplsoccer import Pitch
    import numpy as np

    def ar(text):
        return str(text)

    # ============ الشكل/المحور ============
    if ax is None:
        fig, ax = plt.subplots(figsize=(12, 6.8))  # حجم مناسب لستريملت
    else:
        fig = ax.get_figure()

    # ============ لون النص حسب الخلفية ============
    def _hex_to_rgb(h):
        h = h.lstrip('#')
        return tuple(int(h[i:i+2], 16)/255 for i in (0, 2, 4)) if len(h) == 6 else (0.1, 0.1, 0.1)
    def _luminance(rgb):
        r, g, b = rgb
        return 0.2126*r + 0.7152*g + 0.0722*b
    bg_rgb = _hex_to_rgb(bg_color) if isinstance(bg_color, str) else bg_color
    auto_text_color = "#FFFFFF" if _luminance(bg_rgb) < 0.5 else "#000000"
    txt = line_color if isinstance(line_color, str) and line_color.strip() else auto_text_color

    # ============ تجهيز البيانات ============
    shot_types = ['Goal', 'MissedShots', 'SavedShot', 'ShotOnPost']
    Shotsdf = df[df['type'].isin(shot_types)].copy().reset_index(drop=True)

    # استخدم teamName لتحديد المُسدد (أدق في التسديدات)
    hShotsdf = Shotsdf[Shotsdf['teamName'] == hteamName].copy()
    aShotsdf = Shotsdf[Shotsdf['teamName'] == ateamName].copy()

    # أهداف عكسية (إن وُجد العمود isOwnGoal)
    hogdf = hShotsdf[hShotsdf.get('isOwnGoal', False) == True] if 'isOwnGoal' in hShotsdf.columns else hShotsdf.iloc[0:0]
    aogdf = aShotsdf[aShotsdf.get('isOwnGoal', False) == True] if 'isOwnGoal' in aShotsdf.columns else aShotsdf.iloc[0:0]

    # عدادات أساسية
    hgoal_count = int((hShotsdf['type'] == 'Goal').sum())
    agoal_count = int((aShotsdf['type'] == 'Goal').sum())
    hSavedf = hShotsdf[hShotsdf['type'] == 'SavedShot']
    aSavedf = aShotsdf[aShotsdf['type'] == 'SavedShot']

    # ============ رسم الملعب ============
    pitch = Pitch(pitch_type='uefa', corner_arcs=True,
                  pitch_color=bg_color, line_color=line_color, linewidth=2)
    pitch.draw(ax=ax)
    ax.set_ylim(-0.5, 68.5)
    ax.set_xlim(-0.5, 105.5)

    # ============ دالة رسم النقاط ============
    def plot_events(dff, x_flip=False, color='#000000', size=220,
                    marker='o', edge='none', fill=True, z=3):
        if dff.empty:
            return
        x = 105 - dff['x'] if x_flip else dff['x']
        y = 68 - dff['y'] if x_flip else dff['y']

        # ماركر كرة القدم (يتطلب edge ووجه)
        if marker == 'football':
            face = color if fill and str(color).lower() not in ['none', 'null'] else 'white'
            pitch.scatter(x, y, ax=ax, s=size, marker='football',
                          c=face, edgecolors=edge, linewidths=1.6, zorder=z)
            return

        face = (color if fill and str(color).lower() not in ['none', 'null'] else 'none')
        pitch.scatter(x, y, ax=ax, s=size, edgecolors=edge, c=face,
                      marker=marker, zorder=z)

    # ============ رسم نقاط التسديد ============
    # المستضيف (نقلب الاتجاه ليهاجم يمين الشاشة)
    plot_events(hShotsdf[hShotsdf['type'] == 'Goal'], True,
                color='white', size=360, marker='football', edge='green', fill=True, z=6)
    plot_events(hShotsdf[hShotsdf['type'] == 'MissedShots'], True,
                color=col1, size=200, marker='o', edge=col1, fill=True)
    plot_events(hShotsdf[hShotsdf['type'] == 'ShotOnPost'], True,
                color=col1, size=230, marker='o', edge=col1, fill=True)
    plot_events(hShotsdf[hShotsdf['type'] == 'SavedShot'], True,
                color='none', size=200, marker='o', edge=col1, fill=False)
    plot_events(hogdf, True,
                color='white', size=400, marker='football', edge='orange', fill=True, z=7)

    # الضيف
    plot_events(aShotsdf[aShotsdf['type'] == 'Goal'], False,
                color='white', size=360, marker='football', edge='lime', fill=True, z=6)
    plot_events(aShotsdf[aShotsdf['type'] == 'MissedShots'], False,
                color=col2, size=200, marker='o', edge=col2, fill=True)
    plot_events(aShotsdf[aShotsdf['type'] == 'ShotOnPost'], False,
                color=col2, size=230, marker='o', edge=col2, fill=True)
    plot_events(aShotsdf[aShotsdf['type'] == 'SavedShot'], False,
                color='none', size=200, marker='o', edge=col2, fill=False)
    plot_events(aogdf, False,
                color='white', size=400, marker='football', edge='orange', fill=True, z=7)

    # ============ الإحصاءات الوسطى ============
    def norm(val, tot):
        return (val / tot * 20) if tot > 0 else 10

    hTotalShots = int(len(hShotsdf))
    aTotalShots = int(len(aShotsdf))

    # على المرمى = أهداف + تصديات
    hShotsOnT = int(len(hSavedf) + hgoal_count)
    aShotsOnT = int(len(aSavedf) + agoal_count)

    # ليست على المرمى = مهدرة + على القائم
    hOffT = int(len(hShotsdf[hShotsdf['type'].isin(['MissedShots', 'ShotOnPost'])]))
    aOffT = int(len(aShotsdf[aShotsdf['type'].isin(['MissedShots', 'ShotOnPost'])]))

    # متوسط المسافة (إلى مركز المرمى 105,34)
    g = (105, 34)
    home_avg = float(np.sqrt((hShotsdf['x']-g[0])**2 + (hShotsdf['y']-g[1])**2).mean()) if not hShotsdf.empty else 0.0
    away_avg = float(np.sqrt((aShotsdf['x']-g[0])**2 + (aShotsdf['y']-g[1])**2).mean()) if not aShotsdf.empty else 0.0

    # فرص كبيرة (إن وُجد العمود بنفس الترميز)
    big_key = 'type_value_Big Chance'
    hBigC = int((hShotsdf[big_key] == 214).sum()) if big_key in hShotsdf.columns else 0
    aBigC = int((aShotsdf[big_key] == 214).sum()) if big_key in aShotsdf.columns else 0
    hBigCmiss = int(((hShotsdf.get(big_key, 0) == 214) & (hShotsdf['type'] != 'Goal')).sum())
    aBigCmiss = int(((aShotsdf.get(big_key, 0) == 214) & (aShotsdf['type'] != 'Goal')).sum())

    # إعداد صفوف الإحصائيات
    stats_y = [52, 46, 40, 34, 28, 22, 16]   # 7 صفوف
    stats_lbls = [
        ar("الأهداف"),
        ar("التسديدات"),
        ar("على المرمى"),
        ar("ليست على المرمى"),
        ar("فرص كبيرة"),
        ar("فرص كبيرة ضائعة"),
        ar("متوسط المسافة"),
    ]

    home_vals = [hgoal_count, hTotalShots, hShotsOnT, hOffT, hBigC, hBigCmiss, round(home_avg, 2)]
    away_vals = [agoal_count, aTotalShots, aShotsOnT, aOffT, aBigC, aBigCmiss, round(away_avg, 2)]

    home_norm = [norm(v, home_vals[i] + away_vals[i]) for i, v in enumerate(home_vals)]
    away_norm = [norm(v, home_vals[i] + away_vals[i]) for i, v in enumerate(away_vals)]

    start_x = 42.5
    ax.barh(stats_y, home_norm, height=5, color=col1, left=start_x)
    ax.barh(stats_y, away_norm, height=5, color=col2, left=[start_x + x for x in home_norm])

    for i, y in enumerate(stats_y):
        ax.text(52.5, y, stats_lbls[i], color=txt, fontsize=13,
                ha='center', va='center', fontweight='bold')
        ax.text(41.5, y, f"{home_vals[i]}", color=txt, fontsize=13,
                ha='right', va='center', fontweight='bold')
        ax.text(63.5, y, f"{away_vals[i]}", color=txt, fontsize=13,
                ha='left', va='center', fontweight='bold')

    # أسهم الاتجاه وأسماء الفرق
    ax.text(0, 70, f"{hteamName}\n<---", color=col1, size=15, ha='left', fontweight='bold')
    ax.text(105, 70, f"{ateamName}\n--->", color=col2, size=15, ha='right', fontweight='bold')

    # تنظيف حدود/محاور
    for spine in ['top', 'right', 'bottom', 'left']:
        ax.spines[spine].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])

    plt.tight_layout()
    return fig



# Goal Post Viz

# ShotMap
        

def plot_goalPost(ax, Shotsdf, hteamName, ateamName, col1, col2, bg_color, line_color):
            hShotsdf = Shotsdf[Shotsdf['teamName']==hteamName]
            aShotsdf = Shotsdf[Shotsdf['teamName']==ateamName]
            # converting the datapoints according to the pitch dimension, because the goalposts are being plotted inside the pitch using pitch's dimension
            hShotsdf['goalMouthZ_custom'] = hShotsdf['value_Goal mouth z coordinate']*0.75
            aShotsdf['goalMouthZ_custom'] = (aShotsdf['value_Goal mouth z coordinate']*0.75) + 38
        
            # hShotsdf['goalMouthY_custom'] = ((44 - hShotsdf['value_Goal mouth y coordinate'])*12.295) + 7.5
            # aShotsdf['goalMouthY_custom'] = ((44 - aShotsdf['value_Goal mouth y coordinate'])*12.295) + 7.5
        
            hShotsdf['goalMouthY_custom'] = ((55.5 - hShotsdf['value_Goal mouth y coordinate'])*8.5) + 7.5
            aShotsdf['goalMouthY_custom'] = ((55.5 - aShotsdf['value_Goal mouth y coordinate'])*8.5) + 7.5
        
            # plotting an invisible pitch using the pitch color and line color same color, because the goalposts are being plotted inside the pitch using pitch's dimension
            pitch = Pitch(pitch_type='uefa', corner_arcs=True, pitch_color=bg_color, line_color=bg_color, linewidth=2)
            pitch.draw(ax=ax)
            ax.set_ylim(-0.5,68.5)
            ax.set_xlim(-0.5,105.5)
            # ax.set_ylim(-200,200)
            # ax.set_xlim(-200,150)
        
            # away goalpost bars
            ax.plot([7.5, 7.5], [0, 30], color=line_color, linewidth=5)
            ax.plot([7.5, 97.5], [30, 30], color=line_color, linewidth=5)
            ax.plot([97.5, 97.5], [30, 0], color=line_color, linewidth=5)
            ax.plot([0, 105], [0, 0], color=line_color, linewidth=3)
            # plotting the away net
            y_values = np.arange(0, 6) * 6
            for y in y_values:
                ax.plot([7.5, 97.5], [y, y], color=line_color, linewidth=2, alpha=0.2)
            x_values = (np.arange(0, 11) * 9) + 7.5
            for x in x_values:
                ax.plot([x, x], [0, 30], color=line_color, linewidth=2, alpha=0.2)
            # home goalpost bars
            ax.plot([7.5, 7.5], [38, 68], color=line_color, linewidth=5)
            ax.plot([7.5, 97.5], [68, 68], color=line_color, linewidth=5)
            ax.plot([97.5, 97.5], [68, 38], color=line_color, linewidth=5)
            ax.plot([0, 105], [38, 38], color=line_color, linewidth=3)
            # plotting the home net
            y_values = (np.arange(0, 6) * 6) + 38
            for y in y_values:
                ax.plot([7.5, 97.5], [y, y], color=line_color, linewidth=2, alpha=0.2)
            x_values = (np.arange(0, 11) * 9) + 7.5
            for x in x_values:
                ax.plot([x, x], [38, 68], color=line_color, linewidth=2, alpha=0.2)
        
            # filtering different types of shots without BigChance
            hSavedf = hShotsdf[(hShotsdf['type']=='SavedShot') & (hShotsdf['type_value_Blocked']!=82) & (hShotsdf['type_value_Big Chance']!=214)]
            hGoaldf = hShotsdf[(hShotsdf['type']=='Goal') & (hShotsdf['type_value_Own goal']!=28) & (hShotsdf['type_value_Big Chance']!=214)]
            hPostdf = hShotsdf[(hShotsdf['type']=='ShotOnPost') & (hShotsdf['type_value_Big Chance']!=214)]
            aSavedf = aShotsdf[(aShotsdf['type']=='SavedShot') & (aShotsdf['type_value_Blocked']!=82) & (aShotsdf['type_value_Big Chance']!=214)]
            aGoaldf = aShotsdf[(aShotsdf['type']=='Goal') & (aShotsdf['type_value_Own goal']!=28) & (aShotsdf['type_value_Big Chance']!=214)]
            aPostdf = aShotsdf[(aShotsdf['type']=='ShotOnPost') & (aShotsdf['type_value_Big Chance']!=214)]
            # filtering different types of shots with BigChance
            hSavedf_bc = hShotsdf[(hShotsdf['type']=='SavedShot') & (hShotsdf['type_value_Blocked']!=82) & (hShotsdf['type_value_Big Chance']==214)]
            hGoaldf_bc = hShotsdf[(hShotsdf['type']=='Goal') & (hShotsdf['type_value_Own goal']!=28) & (hShotsdf['type_value_Big Chance']==214)]
            hPostdf_bc = hShotsdf[(hShotsdf['type']=='ShotOnPost') & (hShotsdf['type_value_Big Chance']==214)]
            aSavedf_bc = aShotsdf[(aShotsdf['type']=='SavedShot') & (aShotsdf['type_value_Blocked']!=82) & (aShotsdf['type_value_Big Chance']==214)]
            aGoaldf_bc = aShotsdf[(aShotsdf['type']=='Goal') & (aShotsdf['type_value_Own goal']!=28) & (aShotsdf['type_value_Big Chance']==214)]
            aPostdf_bc = aShotsdf[(aShotsdf['type']=='ShotOnPost') & (aShotsdf['type_value_Big Chance']==214)]
        
            # scattering those shots without BigChance
            sc1 = pitch.scatter(hSavedf.goalMouthY_custom, hSavedf.goalMouthZ_custom, marker='o', c=bg_color, zorder=3, edgecolor=col2, hatch='/////', s=350, ax=ax)
            sc2 = pitch.scatter(hGoaldf.goalMouthY_custom, hGoaldf.goalMouthZ_custom, marker='football', c=bg_color, zorder=3, edgecolors='green', s=350, ax=ax)
            sc3 = pitch.scatter(hPostdf.goalMouthY_custom, hPostdf.goalMouthZ_custom, marker='o', c=bg_color, zorder=3, edgecolors='orange', hatch='/////', s=350, ax=ax)
            sc4 = pitch.scatter(aSavedf.goalMouthY_custom, aSavedf.goalMouthZ_custom, marker='o', c=bg_color, zorder=3, edgecolor=col1, hatch='/////', s=350, ax=ax)
            sc5 = pitch.scatter(aGoaldf.goalMouthY_custom, aGoaldf.goalMouthZ_custom, marker='football', c=bg_color, zorder=3, edgecolors='green', s=350, ax=ax)
            sc6 = pitch.scatter(aPostdf.goalMouthY_custom, aPostdf.goalMouthZ_custom, marker='o', c=bg_color, zorder=3, edgecolors='orange', hatch='/////', s=350, ax=ax)
            # scattering those shots with BigChance
            sc1_bc = pitch.scatter(hSavedf_bc.goalMouthY_custom, hSavedf_bc.goalMouthZ_custom, marker='o', c=bg_color, zorder=3, edgecolor=col2, hatch='/////', s=1000, ax=ax)
            sc2_bc = pitch.scatter(hGoaldf_bc.goalMouthY_custom, hGoaldf_bc.goalMouthZ_custom, marker='football', c=bg_color, zorder=3, edgecolors='green', s=1000, ax=ax)
            sc3_bc = pitch.scatter(hPostdf_bc.goalMouthY_custom, hPostdf_bc.goalMouthZ_custom, marker='o', c=bg_color, zorder=3, edgecolors='orange', hatch='/////', s=1000, ax=ax)
            sc4_bc = pitch.scatter(aSavedf_bc.goalMouthY_custom, aSavedf_bc.goalMouthZ_custom, marker='o', c=bg_color, zorder=3, edgecolor=col1, hatch='/////', s=1000, ax=ax)
            sc5_bc = pitch.scatter(aGoaldf_bc.goalMouthY_custom, aGoaldf_bc.goalMouthZ_custom, marker='football', c=bg_color, zorder=3, edgecolors='green', s=1000, ax=ax)
            sc6_bc = pitch.scatter(aPostdf_bc.goalMouthY_custom, aPostdf_bc.goalMouthZ_custom, marker='o', c=bg_color, zorder=3, edgecolors='orange', hatch='/////', s=1000, ax=ax)
        
            # Headlines and other texts
            ax.text(52.5, 70, f"{hteamName} GK saves", color=col1, fontsize=30, ha='center', fontweight='bold')
            ax.text(52.5, -2, f"{ateamName} GK saves", color=col2, fontsize=30, ha='center', va='top', fontweight='bold')
        
            ax.text(100, 68, f"Saves = {len(aSavedf)+len(aSavedf_bc)}",
                            color=col1, fontsize=16, va='top', ha='left')
            ax.text(100, 2, f"Saves = {len(hSavedf)+len(hSavedf_bc)}",
                            color=col2, fontsize=16, va='bottom', ha='left')
        
            return

##################################

def generate_and_plot_momentum(df, hteamName, ateamName, col1, col2, bg_color, line_color):
    u_df = df.copy()
    u_df = u_df[(u_df['type_value_Corner taken'] != 6)]
    u_df = u_df[['x', 'minute', 'period', 'type', 'teamName']]
    u_df = u_df[~u_df['type'].isin([
        'Start', 'OffsidePass', 'OffsideProvoked', 'Card', 'CornerAwarded', 'End',
        'OffsideGiven', 'SubstitutionOff', 'SubstitutionOn', 'FormationChange', 'FormationSet'
    ])].reset_index(drop=True)

    u_df.loc[u_df['teamName'] == ateamName, 'x'] = 105 - u_df.loc[u_df['teamName'] == ateamName, 'x']

    Momentumdf = u_df.groupby('minute')['x'].mean().reset_index()
    Momentumdf.columns = ['minute', 'average_x']
    Momentumdf['average_x'] -= 52.5

    u_df_1 = u_df[u_df['period'] == 'FirstHalf']
    u_df_2 = u_df[u_df['period'] == 'SecondHalf']

    Momentumdf1 = u_df_1.groupby('minute')['x'].mean().reset_index()
    Momentumdf1.columns = ['minute', 'average_x']
    Momentumdf1['average_x'] -= 52.5

    Momentumdf2 = u_df_2.groupby('minute')['x'].mean().reset_index()
    Momentumdf2.columns = ['minute', 'average_x']
    Momentumdf2['average_x'] -= 52.5

    def plot_Momentum(ax):
        colors1 = [col1 if x > 0 else col2 for x in Momentumdf1['average_x']]
        colors2 = [col1 if x > 0 else col2 for x in Momentumdf2['average_x']]

        homedf = df[df['teamName'] == hteamName]
        awaydf = df[df['teamName'] == ateamName]
        hxT = homedf['xT'].sum().round(2)
        axT = awaydf['xT'].sum().round(2)

        hgoal_list = homedf[(homedf['type'] == 'Goal') & (homedf['type_value_Own goal'] != 28)]['minute'].tolist()
        agoal_list = awaydf[(awaydf['type'] == 'Goal') & (awaydf['type_value_Own goal'] != 28)]['minute'].tolist()
        hog_list = homedf[(homedf['type'] == 'Goal') & (homedf['type_value_Own goal'] == 28)]['minute'].tolist()
        aog_list = awaydf[(awaydf['type'] == 'Goal') & (awaydf['type_value_Own goal'] == 28)]['minute'].tolist()

        highest_x = Momentumdf['average_x'].max()
        lowest_x = Momentumdf['average_x'].min()
        highest_minute = Momentumdf['minute'].max()
        hscatter_y = [highest_x] * len(hgoal_list)
        ascatter_y = [lowest_x] * len(agoal_list)
        hogscatter_y = [highest_x] * len(aog_list)
        aogscatter_y = [lowest_x] * len(hog_list)
        extra_time = Momentumdf1['minute'].max() - 45

        ax.text((45 / 2), lowest_x, 'First Half', color='gray', fontsize=20, alpha=0.25, va='center', ha='center')
        ax.text((45 + (45 / 2)), lowest_x, 'Second Half', color='gray', fontsize=20, alpha=0.25, va='center', ha='center')

        ax.scatter(hgoal_list, hscatter_y, s=250, c='None', edgecolor='green', hatch='////', marker='o')
        ax.scatter(agoal_list, ascatter_y, s=250, c='None', edgecolor='green', hatch='////', marker='o')
        ax.scatter(hog_list, aogscatter_y, s=250, c='None', edgecolor='orange', hatch='////', marker='o')
        ax.scatter(aog_list, hogscatter_y, s=250, c='None', edgecolor='orange', hatch='////', marker='o')

        ax.bar(Momentumdf1['minute'], Momentumdf1['average_x'], width=1, color=colors1)
        ax.bar(Momentumdf2['minute'] + extra_time, Momentumdf2['average_x'], width=1, color=colors2)

        ax.set_xticks(range(0, len(Momentumdf['minute']), 5))
        ax.axvline(45, color='gray', linewidth=2, linestyle='dotted')
        ax.set_facecolor(bg_color)
        for spine in ['top', 'right', 'left', 'bottom']:
            ax.spines[spine].set_visible(False)
        ax.tick_params(axis='both', which='both', length=0)
        ax.tick_params(axis='x', colors=line_color)
        ax.tick_params(axis='y', colors=bg_color)
        ax.set_xlabel('Minute', color=line_color, fontsize=20)
        ax.axhline(y=0, color=line_color, alpha=1, linewidth=2)
        ax.text(highest_minute + 1, highest_x, f"{hteamName}\nxT: {hxT}", color=col1, fontsize=20, va='bottom', ha='left')
        ax.text(highest_minute + 1, lowest_x, f"{ateamName}\nxT: {axT}", color=col2, fontsize=20, va='top', ha='left')
        ax.set_title('Match Momentum', color=line_color, fontsize=30, fontweight='bold')

    return plot_Momentum
 




from sklearn.cluster import KMeans

def ar(text):
    return str(text)

def draw_kmeans_pass_clusters_single_team(df, teamName):
    # التحقق من الأعمدة المطلوبة
    required_cols = ['x', 'y', 'endX', 'endY', 'teamName', 'type', 'value_Corner taken']
    if not all(col in df.columns for col in required_cols):
        raise ValueError(f"البيانات يجب أن تحتوي الأعمدة التالية: {required_cols}")

    # تصفية تمريرات الفريق واستبعاد الركنيات
    team_df = df[(df['teamName'] == teamName) & 
                 (df['type'] == 'Pass') & 
                 (df['value_Corner taken'].isnull())].copy()

    if team_df.empty:
        raise ValueError("لا توجد تمريرات صالحة لهذا الفريق.")

    # توحيد اتجاه اللعب (عكس التمريرات القادمة من جهة اليمين)
    mask = team_df['x'] > 100
    team_df.loc[mask, ['x', 'endX']] = 105 - team_df.loc[mask, ['x', 'endX']].values
    team_df.loc[mask, ['y', 'endY']] = 68 - team_df.loc[mask, ['y', 'endY']].values
    team_df = team_df[~(((team_df['x'] < 5) | (team_df['x'] > 100)) & ((team_df['y'] < 5) | (team_df['y'] > 63)))]
    # تطبيق KMeans
    X = team_df[['x', 'y', 'endX', 'endY']].values
    kmeans = KMeans(n_clusters=6, random_state=0)
    team_df['cluster'] = kmeans.fit_predict(X)

    # إعداد الرسم
    cluster_colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown']
    pitch = Pitch(pitch_type='uefa', line_color='black', pitch_color='white')
    fig, ax = pitch.draw(figsize=(12, 7))

    for i in range(6):
        cluster_data = team_df[team_df['cluster'] == i]
        label = ar(f'تجمع {i+1}')
        pitch.arrows(cluster_data['x'], cluster_data['y'],
                     cluster_data['endX'], cluster_data['endY'],
                     ax=ax, color=cluster_colors[i], width=1.5, headwidth=4,
                     alpha=0.6, label=label)

    title = f"تحليل التمريرات باستخدام KMeans لفريق: {teamName}"
    plt.title(ar(title), fontsize=16, color='black', pad=20)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08), fancybox=True, shadow=False, ncol=3, fontsize=9)
    plt.tight_layout()

    return fig



def ar(text):
    return str(text)

import matplotlib.pyplot as plt
import seaborn as sns
from mplsoccer import Pitch

# ========= خريطة بداية التمريرات (فريق واحد) =========
import matplotlib.pyplot as plt
import seaborn as sns
from mplsoccer import Pitch

# =========================
# خريطة فريق واحد
# =========================
import matplotlib.pyplot as plt
import seaborn as sns
from mplsoccer import Pitch

# خريطة فريق واحد
def draw_pass_start_density_map(
    df, team_name, color="#1565C0", pitch_type="statsbomb",
    face_each_other=True   # لا يؤثّر هنا لكن للإتساق مع الواجهة
):
    d = df[(df['teamName'] == team_name) & (df['type'] == 'Pass')][['x','y']].dropna().copy()

    pitch = Pitch(pitch_type=pitch_type, line_color='black')
    fig, ax = pitch.draw(figsize=(8, 6))

    L = pitch.dim.pitch_length
    W = pitch.dim.pitch_width
    ax.set_xlim(0, L); ax.set_ylim(0, W)

    if not d.empty:
        sns.kdeplot(x=d['x'], y=d['y'], fill=True, alpha=0.55, levels=12, thresh=0.02,
                    ax=ax, color=color, clip=((0, L), (0, W)), bw_adjust=1.0)
        sns.kdeplot(x=d['x'], y=d['y'], fill=False, levels=12, linewidths=0.6,
                    ax=ax, color=color, clip=((0, L), (0, W)), bw_adjust=1.0)

    ax.set_title(f"خريطة بداية التمريرات - {team_name}", fontsize=14)
    return fig

# خريطتان للفريقين
def draw_pass_start_density_both_teams(
    df, home_team, away_team,
    home_color="#1565C0", away_color="#C62828",
    pitch_type="statsbomb", face_each_other=True
):
    d_home = df[(df['teamName'] == home_team) & (df['type'] == 'Pass')][['x','y']].dropna().copy()
    d_away = df[(df['teamName'] == away_team) & (df['type'] == 'Pass')][['x','y']].dropna().copy()

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    pitch = Pitch(pitch_type=pitch_type, line_color='black')
    L = pitch.dim.pitch_length
    W = pitch.dim.pitch_width

    # قلب اتجاه الضيف عند الرغبة
    if face_each_other and not d_away.empty:
        d_away['x'] = L - d_away['x']

    for ax, data, color, title in [
        (axes[0], d_home, home_color, f"بدايات التمرير - {home_team}"),
        (axes[1], d_away, away_color, f"بدايات التمرير - {away_team}")
    ]:
        pitch.draw(ax=ax)
        ax.set_xlim(0, L); ax.set_ylim(0, W)
        if not data.empty:
            sns.kdeplot(x=data['x'], y=data['y'], fill=True, alpha=0.55, levels=12, thresh=0.02,
                        ax=ax, color=color, clip=((0, L), (0, W)), bw_adjust=1.0)
            sns.kdeplot(x=data['x'], y=data['y'], fill=False, levels=12, linewidths=0.6,
                        ax=ax, color=color, clip=((0, L), (0, W)), bw_adjust=1.0)
        else:
            ax.text(0.5, 0.5, "لا توجد بيانات تمرير", ha="center", va="center", transform=ax.transAxes)

        ax.set_title(title, fontsize=12)

    fig.tight_layout()
    return fig




from mplsoccer import VerticalPitch
def draw_pass_flow_map(
    df,
    team_name,
    hteamName,
    team_color="#ff0000",
    bg_color="#ffffff",
    line_color="#808080",
    grid=(5, 5),              # (nx, ny)
    min_passes=3,             # لا يرسم سهم إلا إذا >=
    curved=True,              # سهم منحني
    curvature=0.25,           # مقدار الانحناء
    arrow_scale=18,           # حجم رأس السهم
    alpha_min=0.10,
    alpha_max=0.90,
    lw_max=8,
    title_ar=None,            # نص عنوان عربي جاهز إن رغبت
):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from mplsoccer import Pitch
    from matplotlib.colors import to_rgba
    from matplotlib.patches import FancyArrowPatch

    nx, ny = grid
    pitch_length, pitch_width = 105.0, 68.0

    # 1) فلترة تمريرات ناجحة للفريق
    pass_df = df[
        (df["teamName"] == team_name) &
        (df["type"] == "Pass") &
        (df["outcomeType"] == "Successful")
    ].copy()

    # دعم أسماء أعمدة بديلة
    if "endX" not in pass_df.columns and "end_x" in pass_df.columns:
        pass_df["endX"] = pass_df["end_x"]
    if "endY" not in pass_df.columns and "end_y" in pass_df.columns:
        pass_df["endY"] = pass_df["end_y"]

    # ضمان وجود الأعمدة
    for c in ["x", "y", "endX", "endY"]:
        if c not in pass_df.columns:
            pass_df[c] = np.nan
    pass_df = pass_df.dropna(subset=["x", "y", "endX", "endY"]).copy()

    # 2) تحويل الإحداثيات إلى Zones (5x5)
    #    zone_x: 0..nx-1, zone_y: 0..ny-1
    x_bins = np.linspace(0, pitch_length, nx + 1)
    y_bins = np.linspace(0, pitch_width,  ny + 1)

    pass_df["from_x"] = np.clip(np.digitize(pass_df["x"],    x_bins) - 1, 0, nx-1)
    pass_df["from_y"] = np.clip(np.digitize(pass_df["y"],    y_bins) - 1, 0, ny-1)
    pass_df["to_x"]   = np.clip(np.digitize(pass_df["endX"], x_bins) - 1, 0, nx-1)
    pass_df["to_y"]   = np.clip(np.digitize(pass_df["endY"], y_bins) - 1, 0, ny-1)

    # 3) تجميع التدفقات Zone->Zone
    flows = (
        pass_df.groupby(["from_x", "from_y", "to_x", "to_y"])
        .size()
        .reset_index(name="count")
        .sort_values("count", ascending=False)
        .reset_index(drop=True)
    )

    # تصفية الأسهم الصغيرة
    flows_plot = flows[flows["count"] >= int(min_passes)].copy()

    # 4) مراكز المناطق (Centers)
    #    center_x = (bin_left + bin_right)/2
    x_centers = (x_bins[:-1] + x_bins[1:]) / 2.0
    y_centers = (y_bins[:-1] + y_bins[1:]) / 2.0

    flows_plot["sx"] = flows_plot["from_x"].map(lambda i: x_centers[int(i)])
    flows_plot["sy"] = flows_plot["from_y"].map(lambda j: y_centers[int(j)])
    flows_plot["ex"] = flows_plot["to_x"].map(lambda i: x_centers[int(i)])
    flows_plot["ey"] = flows_plot["to_y"].map(lambda j: y_centers[int(j)])

    # 5) إعداد الشكل + رسم الملعب + خطوط التقسيم 5x5
    fig, ax = plt.subplots(figsize=(10, 6), dpi=200)
    pitch = Pitch(pitch_type="uefa", pitch_color=bg_color, line_color=line_color, linewidth=2)
    pitch.draw(ax=ax)
    ax.set_xlim(0, pitch_length)
    ax.set_ylim(0, pitch_width)

    # 6) قلب اتجاه الضيف (عادة invert_xaxis فقط)
    is_home = team_name.strip().lower() == str(hteamName).strip().lower()
    if not is_home:
        ax.invert_xaxis()

    # 7) رسم Grid 5x5 بنفس لون الخطوط
    for xb in x_bins[1:-1]:
        ax.axvline(xb, color=line_color, lw=1.5, alpha=0.6, zorder=1)
    for yb in y_bins[1:-1]:
        ax.axhline(yb, color=line_color, lw=1.5, alpha=0.6, zorder=1)

    # 8) رسم الأسهم (منحنية أو مستقيمة) مع سماكة/شفافية بحسب العدد
    if len(flows_plot):
        max_cnt = flows_plot["count"].max()
        base_rgba = np.array(to_rgba(team_color))

        def _width(c):
            return (c / max_cnt) * lw_max

        def _alpha(c):
            return (c / max_cnt) * (alpha_max - alpha_min) + alpha_min

        for _, r in flows_plot.iterrows():
            lw = _width(r["count"])
            a  = _alpha(r["count"])
            rgba = base_rgba.copy()
            rgba[3] = a

            # إذا من نفس المنطقة إلى نفس المنطقة تجاهل
            if (r["sx"] == r["ex"]) and (r["sy"] == r["ey"]):
                continue

            if curved:
                rad = curvature
                # لو اتجاه معاكس (يمين/يسار) خفف الانحناء
                # (اختياري) يمكنك تعديل الراد حسب الحاجة
                con = f"arc3,rad={rad}"
                patch = FancyArrowPatch(
                    (r["sx"], r["sy"]),
                    (r["ex"], r["ey"]),
                    connectionstyle=con,
                    arrowstyle="-|>",
                    mutation_scale=arrow_scale,
                    lw=lw,
                    color=rgba,
                    zorder=3,
                )
            else:
                patch = FancyArrowPatch(
                    (r["sx"], r["sy"]),
                    (r["ex"], r["ey"]),
                    arrowstyle="-|>",
                    mutation_scale=arrow_scale,
                    lw=lw,
                    color=rgba,
                    zorder=3,
                )

            ax.add_patch(patch)

    # 9) العنوان
    if title_ar is None:
        title_ar = f"{team_name} - Pass Flow Map ({nx}x{ny})"
    ax.set_title(title_ar, fontsize=18, fontweight="bold", color=team_color)

    # 10) إخراج جدول التدفقات بشكل مقروء
    # Zone label: (x,y) ويمكنك تحويلها لأسماء مثل Zone 1..25
    flows_out = flows.copy()
    flows_out["from_zone"] = flows_out.apply(lambda r: f"({int(r['from_x'])},{int(r['from_y'])})", axis=1)
    flows_out["to_zone"]   = flows_out.apply(lambda r: f"({int(r['to_x'])},{int(r['to_y'])})", axis=1)
    flows_out = flows_out[["from_zone", "to_zone", "count"]]

    return fig, flows_out

def draw_xt_heatmaps_top_players(df_match, team_name, base_color='#0099ff', title_fontsize=16):
    
    def ar(text):
        return str(text)

    # تدرج لوني من الأبيض إلى اللون المختار
    cmap = LinearSegmentedColormap.from_list("custom_xt", ['white', base_color], N=100)

    # تصفية أحداث الفريق (بما فيها xT السالب)
    team_df = df_match[(df_match['teamName'] == team_name) & 
                       (df_match['xT'].notna())]

    # أفضل 6 لاعبين حسب مجموع xT الحقيقي (السالب والموجب)
    top_players_xt = team_df.groupby('shortName')['xT'].sum().sort_values(ascending=False).head(6)
    top_players = top_players_xt.index.tolist()

    # إعداد الملعب
    pitch = VerticalPitch(pitch_type='uefa', line_zorder=2)
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(18, 10))
    axes = axes.flatten()

    for ax, player in zip(axes, top_players):
        player_data = team_df[team_df['shortName'] == player]
        total_xt = player_data['xT'].sum()  # ✅ لحساب xT الكامل حتى مع السالب

        # ✅ إزالة السالب مؤقتًا عند الرسم
        kde_data = player_data[player_data['xT'] > 0]

        # تجاهل اللاعب إذا لا يوجد بيانات موجبة
        if len(kde_data) < 3:
            ax.set_title(f"{player} – لا توجد بيانات كافية", fontsize=12)
            ax.axis('off')
            continue

        pitch.draw(ax=ax)

        pitch.kdeplot(
            x=kde_data['x'],
            y=kde_data['y'],
            ax=ax,
            cmap=cmap,
            shade=True,
            fill=True,
            bw_adjust=0.8,
            weights=kde_data['xT'],
            levels=50,
            thresh=0.01
        )

        ax.set_title(f"{player} – xT: {total_xt:.2f}", fontsize=13, weight='bold', color='black')

    # العنوان الرئيسي
    title = f'xT Heatmap – أفضل لاعبي {team_name}'
    fig.suptitle(ar(title), fontsize=title_fontsize, y=1.03)
    plt.tight_layout()
    plt.subplots_adjust(top=0.90)
    return fig





from matplotlib.patches import Rectangle



def ar(text):
    return str(text)

def draw_xt_pass_and_carry_map(df, player_name, team_name, base_color='#0099ff', max_carry_length=50, reverse=False):

    # تصفية بيانات اللاعب
    player_df = df[(df['shortName'] == player_name) & 
                   (df['teamName'] == team_name) & 
                   (df['xT'].notna())]

    pitch = Pitch(pitch_type='uefa', pitch_color="#fafcfb", line_color="#0E0101", line_zorder=2)
    fig, ax = pitch.draw(figsize=(10, 7))
    
    
    passes = player_df[player_df['type'] == 'Pass']
    carries = player_df[player_df['type'] == 'Carry']

    # رسم التمريرات
    pitch.arrows(passes['x'], passes['y'], passes['endX'], passes['endY'],
                 ax=ax, color=base_color, width=2, headwidth=5, alpha=0.5, zorder=2, label='Pass')
    
    # رسم الحملات بشرط الطول
    for _, row in carries.iterrows():
        if (
            0 <= row['x'] <= 105 and 0 <= row['y'] <= 68 and
            0 <= row['endX'] <= 105 and 0 <= row['endY'] <= 68 and
            not np.isnan(row['x']) and not np.isnan(row['y']) and
            not np.isnan(row['endX']) and not np.isnan(row['endY'])
        ):
            dx = row['endX'] - row['x']
            dy = row['endY'] - row['y']
            distance = (dx**2 + dy**2) ** 0.5
            if distance > max_carry_length:
                continue

            ax.annotate('', xy=(row['endX'], row['endY']), xytext=(row['x'], row['y']),
                        arrowprops=dict(arrowstyle='->', color='green', lw=2, linestyle='--', alpha=0.9),
                        annotation_clip=False)


            





    # شبكة xT
    
    bins_x = np.linspace(0, 105, 9)  # كان 6 ← أصبح 9 تقسيمات أفقية
    bins_y = np.linspace(0, 68, 7)   # كان 5 ← أصبح 7 تقسيمات رأسية
    xt_grid = np.zeros((len(bins_x)-1, len(bins_y)-1))

    for i in range(len(bins_x)-1):
        for j in range(len(bins_y)-1):
            in_zone = player_df[
                (player_df['x'] >= bins_x[i]) & (player_df['x'] < bins_x[i+1]) &
                (player_df['y'] >= bins_y[j]) & (player_df['y'] < bins_y[j+1])
            ]
            xt_grid[i, j] = in_zone['xT'].sum()

    for i in range(len(bins_x)-1):
        for j in range(len(bins_y)-1):
            x0, x1 = bins_x[i], bins_x[i+1]
            y0, y1 = bins_y[j], bins_y[j+1]
            center_x = (x0 + x1) / 2
            center_y = (y0 + y1) / 2
            val = xt_grid[i, j]
            
            if 0 <= x0 < 105 and 0 <= y0 < 68 and x1 <= 105 and y1 <= 68:    
                if val > 0:
                    ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0,
                                           color='red', alpha=min(val, 0.4), zorder=1))
                ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0,
                                       fill=False, edgecolor='gray', linestyle='--', lw=0.5))
                if abs(val) > 0.001:
                    ax.text(center_x, center_y, f"{val:.2f}", color='black',
                            ha='center', va='center', fontsize=9)

    # عنوان
    ax.set_title(f"xT Map – {player_name}", fontsize=14)

    # ملخص التهديد
    
    
    total_xt = round(player_df['xT'].sum(), 2)
    xt_from_pass = round(passes['xT'].sum(), 2)
    xt_from_carry = round(carries['xT'].sum(), 2)

    
    
    
    
    
    text_line = f"💬 إجمالي التهديد xT: {total_xt:.2f} | من التمريرات: {xt_from_pass:.2f} | من الحملات: {xt_from_carry:.2f}"
    plt.gcf().text(0.5, 0.05, ar(text_line), fontsize=11, color='black', ha='center', va='bottom',
                   bbox=dict(facecolor='white', alpha=0.6, boxstyle='round'))

    # وسيلة إيضاح
    ax.plot([], [], color=base_color, lw=3, label='Passes')
    ax.plot([], [], color='green', lw=3, linestyle='--', label='Carries')
    ax.legend(loc='upper left')


    arrow_x_start = 0.4
    arrow_x_end = 0.6
    arrow_y = -0.04  # ⬅️ رفع السهم لأعلى
    text_y = -0.06  

# رسم السهم في منتصف المحور
    ax.annotate(
    '', xy=(arrow_x_end, arrow_y), xytext=(arrow_x_start, arrow_y),
    xycoords='axes fraction',
    arrowprops=dict(arrowstyle='-|>', linewidth=0.8, color='black', fc='gray', mutation_scale=15, zorder=4)
)

# النص تحت السهم
    bidi_text = str("اتجاه الهجوم")
    ax.annotate(bidi_text, xy=((arrow_x_start + arrow_x_end) / 2, text_y),
            xycoords='axes fraction', ha='center', fontsize=11,
            color='black', weight="bold")


    return fig



from matplotlib.colors import to_rgba

def draw_static_passing_network(df_match, team_name, opponent_name,
                                bg_color='white', line_color='gray',
                                highlight_color='red', node_edge_color='b'):
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    from matplotlib.colors import to_rgba
    from matplotlib.lines import Line2D
    from mplsoccer import Pitch
    import arabic_reshaper
    from bidi.algorithm import get_display

    # ===== 1) تنظيف وتحويل الأعمدة =====
    for c in ['name', 'teamName']:
        if c in df_match.columns:
            df_match[c] = df_match[c].astype(str).fillna("Unknown")

    if 'minute' in df_match.columns:
        df_match['minute'] = pd.to_numeric(df_match['minute'], errors='coerce').fillna(0).astype(int)
    else:
        df_match['minute'] = 0

    if 'period' in df_match.columns:
        df_match['period'] = pd.to_numeric(df_match['period'], errors='coerce').fillna(1).astype(int)
        df_match.loc[df_match['period'] == 2, 'minute'] += 45

    # ===== 2) تحديد المستقبل =====
    if 'pass_recipient' in df_match.columns:
        df_match['pass_receiver'] = df_match['pass_recipient'].astype(str).fillna("Unknown")
    else:
        df_match['pass_receiver'] = np.where(
            (df_match['type'] == 'Pass') &
            (df_match['outcomeType'] == 'Successful') &
            (df_match['teamName'] == df_match['teamName'].shift(-1)),
            df_match['name'].shift(-1),
            np.nan
        )
        df_match['pass_receiver'] = df_match['pass_receiver'].astype(str).fillna("Unknown")

    # ===== 3) إنشاء فترات 15 دقيقة =====
    df_match['interval'] = pd.cut(
        df_match['minute'],
        bins=[0, 15, 30, 45, 60, 75, 90],
        labels=["0-15'", "15-30'", "30-45'", "45-60'", "60-75'", "75-90'"],
        right=False
    )

    # ===== 4) تحديد البدلاء الحقيقيين =====
    team_events = df_match[df_match['teamName'] == team_name]
    first_appearance = (
        team_events.groupby('name')['minute']
        .min()
        .reset_index()
        .rename(columns={'minute': 'first_minute'})
    )
    first_appearance['is_sub'] = first_appearance['first_minute'] > 45
    df_match = df_match.merge(first_appearance, on='name', how='left')

    # ===== 5) إعداد الشكل العام =====
    fig, axes = plt.subplots(2, 3, figsize=(24, 15), facecolor=bg_color)
    axes = axes.flatten()
    interval_labels = ["0-15'", "15-30'", "30-45'", "45-60'", "60-75'", "75-90'"]
    interval_comments = []

    passes_team_all = df_match[
        (df_match['type'] == 'Pass') &
        (df_match['outcomeType'] == 'Successful') &
        (df_match['teamName'] == team_name)
    ]

    # ===== 6) رسم الشبكات لكل فترة =====
    for i, interval in enumerate(interval_labels):
        ax = axes[i]
        pass_df_full = passes_team_all[passes_team_all['interval'] == interval]

        if pass_df_full.empty:
            ax.axis('off')
            ax.set_title(interval, color=line_color)
            interval_comments.append(f"🕒 {interval}: لا توجد تمريرات في هذه الفترة.")
            continue

        pass_counts_df = pass_df_full.groupby(['name', 'pass_receiver']).size().reset_index(name='pass_count')

        # ===== تموضع اللاعبين (بدون تكرار) =====
        players_involved = pd.unique(pass_counts_df[['name', 'pass_receiver']].values.ravel('K'))
        player_positions = (
            df_match[(df_match['teamName'] == team_name) & (df_match['name'].isin(players_involved))]
            .groupby('name')[['x', 'y']].median()
            .rename(columns={'x': 'avg_x', 'y': 'avg_y'})
            .reset_index()
        )

        # ===== إزالة التكرارات نهائيًا =====
        player_positions = player_positions.drop_duplicates(subset=['name'], keep='first')

        total_passes = pass_counts_df.groupby('name')['pass_count'].sum().reset_index()
        avg_locs_df = pd.merge(player_positions, total_passes, on='name', how='left').fillna(0)
        avg_locs_df['marker_size'] = avg_locs_df['pass_count'].apply(lambda x: 100 + 500 * np.log1p(x))

        pitch = Pitch(pitch_type='uefa', pitch_color=bg_color, line_color='black')
        pitch.draw(ax=ax)

        # ===== دمج المرسل والمستقبل =====
        pass_counts_df = pd.merge(pass_counts_df, avg_locs_df, on='name', how='inner')
        pass_counts_df = pd.merge(pass_counts_df, avg_locs_df, left_on='pass_receiver', right_on='name',
                                  how='inner', suffixes=('', '_receiver'))
        pass_counts_df = pass_counts_df[pass_counts_df['pass_count'] >= 2]

        # ===== رسم الخطوط =====
        if not pass_counts_df.empty:
            pass_counts_df['width'] = pass_counts_df['pass_count'] / pass_counts_df['pass_count'].max() * 20
            top_pairs = pass_counts_df.sort_values(by='pass_count', ascending=False).head(5)
            top_pairs_list = list(zip(top_pairs['name'], top_pairs['pass_receiver']))
            colors = []
            for _, row in pass_counts_df.iterrows():
                color_rgba = np.array(to_rgba(highlight_color if (row['name'], row['pass_receiver']) in top_pairs_list else line_color))
                color_rgba[3] = 0.9 if (row['name'], row['pass_receiver']) in top_pairs_list else 0.4
                colors.append(color_rgba)

            pitch.lines(pass_counts_df['avg_x'], pass_counts_df['avg_y'],
                        pass_counts_df['avg_x_receiver'], pass_counts_df['avg_y_receiver'],
                        lw=pass_counts_df['width'], color=colors, zorder=2, ax=ax)

        # ===== رسم اللاعبين =====
        for _, row in avg_locs_df.iterrows():
            sub_status = first_appearance[first_appearance['name'] == row['name']]['is_sub'].values[0]
            marker_shape = 's' if sub_status else 'o'
            edge_color = 'gray' if sub_status else node_edge_color
            text_color = 'dimgray' if sub_status else 'black'
            size = row['marker_size'] * (0.8 if sub_status else 1.0)

            pitch.scatter(row['avg_x'], row['avg_y'], s=size, marker=marker_shape,
                          color=bg_color, edgecolor=edge_color, linewidth=2, zorder=3, ax=ax)
            short = ''.join([n[0] for n in row['name'].split()])
            pitch.annotate(short, xy=(row['avg_x'], row['avg_y']),
                           c=text_color, ha='center', va='center', size=10, ax=ax)

        ax.set_title(interval, fontsize=16, color='black', pad=10)

        if not pass_counts_df.empty:
            top_text = "\n".join([f"{r['name']} → {r['pass_receiver']}: {r['pass_count']}" for _, r in top_pairs.iterrows()])
            ax.text(75, -10, top_text, color='black', ha='right', va='center', fontsize=12)
            interval_comments.append(f"🕒 {interval}: أقوى علاقة تمريرية: {top_pairs.iloc[0]['name']} → {top_pairs.iloc[0]['pass_receiver']} ({top_pairs.iloc[0]['pass_count']})")

    # ===== 7) العنوان والوسيلة =====
    title_text = f"شبكة التمريرات: {team_name} ضد {opponent_name} حسب فترات كل 15 دقيقة"
    bidi_title = str(title_text)
    fig.suptitle(bidi_title, color='black', fontsize=22)

    line = Line2D([0.3, 0.4], [0.04, 0.04], color=highlight_color, linewidth=3, transform=fig.transFigure, figure=fig)
    fig.add_artist(line)
    fig.text(0.42, 0.04, str("أقوى علاقة تمريرية"), color='black', fontsize=20, ha='left', va='center')
    fig.text(0.88, 0.04, str("○ أساسي   ☐ بديل"), fontsize=18, color='black', ha='right')
    fig.text(0.97, 0.01, '@Turadi_7', color='gray', fontsize=22, ha='right', va='bottom', style='italic')

    # ===== 8) تحليل AI تلقائي =====
    subs = first_appearance[first_appearance['is_sub']].sort_values('first_minute')
    subs_text = "، ".join([f"{n} ({m}')" for n, m in zip(subs['name'], subs['first_minute'])]) or "لا يوجد بدلاء للفريق."
    ai_comment = "### 🧠 تحليل AI\n" + "\n".join(interval_comments) + f"\n\n**البدلاء:** {subs_text}"

    return fig, ai_comment







import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import arabic_reshaper
from bidi.algorithm import get_display

# ==============================================================
# 🎯 دالة رسم مصفوفة التمريرات بالعربية مع إظهار اسم الفريق المختار
# ==============================================================

def draw_pass_matrix_arabic(df_match, team1, color_low='#b5ffe1', color_high='#0099ff'):
    df_match['minute'] = df_match['minute'].astype(int)

    # تحديد اللاعب المستقبل للتمريرات
    df_match['pass_receiver'] = np.where(
        (df_match['type'] == 'Pass') & 
        (df_match['outcomeType'] == 'Successful') & 
        (df_match['teamName'] == df_match['teamName'].shift(-1)),
        df_match['name'].shift(-1),
        np.nan
    )
    df_match['pass_receiver'] = df_match['pass_receiver'].fillna('No')

    # تصفية التمريرات للفريق المختار فقط
    passes_team1 = df_match[
        (df_match['type'] == 'Pass') &
        (df_match['outcomeType'] == 'Successful') &
        (df_match['teamName'] == team1) &
        (df_match['pass_receiver'] != 'No')
    ]

    # بناء المصفوفة
    matrix = passes_team1.groupby(['name', 'pass_receiver']).size().unstack(fill_value=0)

    # تعريب أسماء اللاعبين
    matrix.index = matrix.index.map(lambda x: str(x))
    matrix.columns = matrix.columns.map(lambda x: str(x))

    # 🎨 الألوان
    custom_cmap = LinearSegmentedColormap.from_list("custom_map", [color_low, color_high])
    
    fig, ax = plt.subplots(figsize=(15, 13))
    sns.heatmap(
        matrix, annot=True, fmt="d", cmap=custom_cmap, cbar=True,
        linewidths=0.7, linecolor='gray', annot_kws={"fontsize": 10}, ax=ax
    )

    # 🟢 إضافة اسم الفريق المختار في العنوان
    team_display = str(team1)
    title_text = str(f"مصفوفة التمريرات: {team1}")
    xlabel = str("اللاعب المستقبل")
    ylabel = str("اللاعب المرسل")

    ax.set_title(title_text, fontsize=20, pad=20, color="#333333")
    ax.set_xlabel(xlabel, fontsize=16)
    ax.set_ylabel(ylabel, fontsize=16)
    ax.tick_params(axis='x', rotation=45)
    ax.tick_params(axis='y', rotation=0)

    # 🟡 عنوان علوي أنيق يشمل الفريق
    
    # ✅ تحليل AI بعد الرسم
    total_passes = matrix.values.sum()
    if total_passes > 0:
        top_pair = matrix.stack().idxmax()
        top_value = matrix.stack().max()
        comment = f"""
        ### 🤖 تحليل AI للفريق **{team1}**:

        - عدد التمريرات الكلي للفريق هو **{int(total_passes)}** تمريرة.
        - أكثر تمريرات بين لاعبين كانت من **{top_pair[0]}** إلى **{top_pair[1]}** بعدد **{int(top_value)}** تمريرة.
        """
    else:
        comment = f"❌ لا توجد تمريرات ناجحة للفريق **{team1}** في هذه الفترة."

    return fig, comment

def plot_congestion(df, hteamName, ateamName, col1, col2, bg_color, line_color, ax):
            from highlight_text import ax_text
            pcmap = LinearSegmentedColormap.from_list("Pearl Earring - 10 colors",  [col2, 'gray', col1], N=20)
            df1 = df[(df['teamName']==hteamName) & (~df['type'].str.contains('SubstitutionOff|SubstitutionOn|Challenge|Card')) &
                     (df['type_value_Corner taken']!=6) & (df['type_value_Free kick taken']!=5)]
            df2 = df[(df['teamName']==ateamName) & (~df['type'].str.contains('SubstitutionOff|SubstitutionOn|Challenge|Card')) & 
                     (df['type_value_Corner taken']!=6) & (df['type_value_Free kick taken']!=5)]
            df2['x'] = 105-df2['x']
            df2['y'] =  68-df2['y']
            pitch = Pitch(pitch_type='uefa', corner_arcs=True, pitch_color=bg_color, line_color=line_color, linewidth=2, line_zorder=6)
            pitch.draw(ax=ax)
            ax.set_ylim(-0.5,68.5)
            ax.set_xlim(-0.5,105.5)
        
            bin_statistic1 = pitch.bin_statistic(df1.x, df1.y, bins=(6,5), statistic='count', normalize=False)
            bin_statistic2 = pitch.bin_statistic(df2.x, df2.y, bins=(6,5), statistic='count', normalize=False)
        
            # Assuming 'cx' and 'cy' are as follows:
            cx = np.array([[ 8.75, 26.25, 43.75, 61.25, 78.75, 96.25],
                       [ 8.75, 26.25, 43.75, 61.25, 78.75, 96.25],
                       [ 8.75, 26.25, 43.75, 61.25, 78.75, 96.25],
                       [ 8.75, 26.25, 43.75, 61.25, 78.75, 96.25],
                       [ 8.75, 26.25, 43.75, 61.25, 78.75, 96.25]])
        
            cy = np.array([[61.2, 61.2, 61.2, 61.2, 61.2, 61.2],
                       [47.6, 47.6, 47.6, 47.6, 47.6, 47.6],
                       [34.0, 34.0, 34.0, 34.0, 34.0, 34.0],
                       [20.4, 20.4, 20.4, 20.4, 20.4, 20.4],
                       [ 6.8,  6.8,  6.8,  6.8,  6.8,  6.8]])
        
            # Flatten the arrays
            cx_flat = cx.flatten()
            cy_flat = cy.flatten()
        
            # Create a DataFrame
            df_cong = pd.DataFrame({'cx': cx_flat, 'cy': cy_flat})
        
            hd_values = []
        
        
            # Loop through the 2D arrays
            for i in range(bin_statistic1['statistic'].shape[0]):
                for j in range(bin_statistic1['statistic'].shape[1]):
                    stat1 = bin_statistic1['statistic'][i, j]
                    stat2 = bin_statistic2['statistic'][i, j]
                
                    if (stat1 / (stat1 + stat2)) > 0.55:
                        hd_values.append(1)
                    elif (stat1 / (stat1 + stat2)) < 0.45:
                        hd_values.append(0)
                    else:
                        hd_values.append(0.5)
        
            df_cong['hd']=hd_values
            bin_stat = pitch.bin_statistic(df_cong.cx, df_cong.cy, bins=(6,5), values=df_cong['hd'], statistic='sum', normalize=False)
            pitch.heatmap(bin_stat, ax=ax, cmap=pcmap, edgecolors='#000000', lw=0, zorder=3, alpha=0.85)
        
            ax_text(52.5, 71, s=f"<{hteamName}>  |  Contested  |  <{ateamName }>", highlight_textprops=[{'color':col1}, {'color':col2}],
                    color='gray', fontsize=18, ha='center', va='center', ax=ax)
            ax.set_title("Team's Dominating Zone", color=line_color, fontsize=30, fontweight='bold', y=1.075)
            ax.text(0,  -3, 'Attacking Direction--->', color=col1, fontsize=13, ha='left', va='center')
            ax.text(105,-3, '<---Attacking Direction', color=col2, fontsize=13, ha='right', va='center')
        
            ax.vlines(1*(105/6), ymin=0, ymax=68, color=bg_color, lw=2, ls='--', zorder=5)
            ax.vlines(2*(105/6), ymin=0, ymax=68, color=bg_color, lw=2, ls='--', zorder=5)
            ax.vlines(3*(105/6), ymin=0, ymax=68, color=bg_color, lw=2, ls='--', zorder=5)
            ax.vlines(4*(105/6), ymin=0, ymax=68, color=bg_color, lw=2, ls='--', zorder=5)
            ax.vlines(5*(105/6), ymin=0, ymax=68, color=bg_color, lw=2, ls='--', zorder=5)
        
            ax.hlines(1*(68/5), xmin=0, xmax=105, color=bg_color, lw=2, ls='--', zorder=5)
            ax.hlines(2*(68/5), xmin=0, xmax=105, color=bg_color, lw=2, ls='--', zorder=5)
            ax.hlines(3*(68/5), xmin=0, xmax=105, color=bg_color, lw=2, ls='--', zorder=5)
            ax.hlines(4*(68/5), xmin=0, xmax=105, color=bg_color, lw=2, ls='--', zorder=5)
            
            home_unique_players = homedf['name'].unique()
            away_unique_players = awaydf['name'].unique()
  
            
            return






            # 🔝 Top Ball Progressor - أكثر اللاعبين تقدمًا بالكرة في الفريق المستضيف
home_progressor_counts = {'name': [], 'Progressive Passes': [], 'Progressive Carries': []}

for name in home_unique_players:
    progressive_passes = len(df[
        (df['name'] == name) &
        (df['prog_pass'] >= 9.144) &
        (df['x'] >= 35) &
        (df['outcomeType'] == 'Successful') &
        (df['type_value_Corner taken'] != 6) &
        (df['type_value_Free kick taken'] != 5)
    ])

    progressive_carries = len(df[
        (df['name'] == name) &
        (df['prog_carry'] >= 9.144) &
        (df['endX'] >= 35)
    ])

    home_progressor_counts['name'].append(name)
    home_progressor_counts['Progressive Passes'].append(progressive_passes)
    home_progressor_counts['Progressive Carries'].append(progressive_carries)

# تحويل إلى DataFrame وترتيبه
home_progressor_df = pd.DataFrame(home_progressor_counts)
home_progressor_df['total'] = home_progressor_df['Progressive Passes'] + home_progressor_df['Progressive Carries']
home_progressor_df = home_progressor_df.sort_values(by='total', ascending=False).reset_index(drop=True)
home_progressor_df = home_progressor_df.head(5)
home_progressor_df['shortName'] = home_progressor_df['name'].apply(get_short_name)


 # Top Threate Creators
        # Initialize an empty dictionary to store home players different type of Carries counts
home_xT_counts = {'name': home_unique_players, 'xT from Pass': [], 'xT from Carry': []}
for name in home_unique_players:
            home_xT_counts['xT from Pass'].append((df[(df['name'] == name) & (df['type'] == 'Pass') & (df['xT']>=0) & (df['outcomeType']=='Successful') & (df['type_value_Corner taken']!=6) & (df['type_value_Free kick taken']!=5)])['xT'].sum().round(2))
            home_xT_counts['xT from Carry'].append((df[(df['name'] == name) & (df['type'] == 'Carry') & (df['xT']>=0)])['xT'].sum().round(2))
home_xT_df = pd.DataFrame(home_xT_counts)
home_xT_df['total'] = home_xT_df['xT from Pass']+home_xT_df['xT from Carry']
home_xT_df = home_xT_df.sort_values(by='total', ascending=False)
home_xT_df.reset_index(drop=True, inplace=True)
home_xT_df = home_xT_df.head(5)
home_xT_df['shortName'] = home_xT_df['name'].apply(get_short_name)
        
        # Initialize an empty dictionary to store home players different type of Carries counts
away_xT_counts = {'name': away_unique_players, 'xT from Pass': [], 'xT from Carry': []}
for name in away_unique_players:
            away_xT_counts['xT from Pass'].append((df[(df['name'] == name) & (df['type'] == 'Pass') & (df['xT']>=0) & (df['outcomeType']=='Successful') & (df['type_value_Corner taken']!=6) & (df['type_value_Free kick taken']!=5)])['xT'].sum().round(2))
            away_xT_counts['xT from Carry'].append((df[(df['name'] == name) & (df['type'] == 'Carry') & (df['xT']>=0)])['xT'].sum().round(2))
away_xT_df = pd.DataFrame(away_xT_counts)
away_xT_df['total'] = away_xT_df['xT from Pass']+away_xT_df['xT from Carry']
away_xT_df = away_xT_df.sort_values(by='total', ascending=False)
away_xT_df.reset_index(drop=True, inplace=True)
away_xT_df = away_xT_df.head(5)
away_xT_df['shortName'] = away_xT_df['name'].apply(get_short_name)
        
        
# Shot Sequence Involvement
df_no_carry = df[df['type']!='Carry']
        # Initialize an empty dictionary to store home players different type of shot sequence counts
home_shot_seq_counts = {'name': home_unique_players, 'Shots': [], 'Shot Assist': [], 'Buildup to shot': []}
        # Putting counts in those lists
for name in home_unique_players:
            home_shot_seq_counts['Shots'].append(len(df[(df['name'] == name) & ((df['type']=='MissedShots') | (df['type']=='SavedShot') | (df['type']=='ShotOnPost') | (df['type']=='Goal'))]))
            home_shot_seq_counts['Shot Assist'].append(len(df[(df['name'] == name) & (df['type'] == 'Pass') & (df['type_value_Assist']==210)]))
            home_shot_seq_counts['Buildup to shot'].append(len(df_no_carry[(df_no_carry['name'] == name) & (df_no_carry['type'] == 'Pass') & (df['type_value_Assist'].shift(-1)==210)]))
        # converting that list into a dataframe
home_sh_sq_df = pd.DataFrame(home_shot_seq_counts)
home_sh_sq_df['total'] = home_sh_sq_df['Shots']+home_sh_sq_df['Shot Assist']+home_sh_sq_df['Buildup to shot']
home_sh_sq_df = home_sh_sq_df.sort_values(by='total', ascending=False)
home_sh_sq_df.reset_index(drop=True, inplace=True)
home_sh_sq_df = home_sh_sq_df.head(5)
home_sh_sq_df['shortName'] = home_sh_sq_df['name'].apply(get_short_name)

# Initialize an empty dictionary to store away players different type of shot sequence counts
# تهيئة القاموس فارغًا
away_shot_seq_counts = {'name': [], 'Shots': [], 'Shot Assist': [], 'Buildup to shot': []}

# حلقة عبر اللاعبين
for name in away_unique_players:
    # عدد التسديدات
    shots = len(df_no_carry[(df_no_carry['name'] == name) & (df_no_carry['type'] == 'Shot')])
    # تمريرات حاسمة للتسديد
    shot_assist = len(df_no_carry[(df_no_carry['name'] == name) & (df_no_carry['type_value_Assist'] == 210)])
    # بناء الهجمة للتسديد (تمريرات قبل المساعدة)
    buildup = len(df_no_carry[
        (df_no_carry['name'] == name) & 
        (df_no_carry['type'] == 'Pass') & 
        (df_no_carry['type_value_Assist'].shift(-1) == 210)
    ])

    away_shot_seq_counts['name'].append(name)
    away_shot_seq_counts['Shots'].append(shots)
    away_shot_seq_counts['Shot Assist'].append(shot_assist)
    away_shot_seq_counts['Buildup to shot'].append(buildup)

# تحويل إلى DataFrame
away_sh_sq_df = pd.DataFrame(away_shot_seq_counts)
away_sh_sq_df['total'] = away_sh_sq_df['Shots'] + away_sh_sq_df['Shot Assist'] + away_sh_sq_df['Buildup to shot']
away_sh_sq_df['shortName'] = away_sh_sq_df['name'].apply(get_short_name)


 
# Top Defenders
# Initialize an empty dictionary to store home players different type of defensive actions counts
home_defensive_actions_counts = {'name': home_unique_players, 'Tackles': [], 'Interceptions': [], 'Clearance': []}
for name in home_unique_players:
            home_defensive_actions_counts['Tackles'].append(len(df[(df['name'] == name) & (df['type'] == 'Tackle') & (df['outcomeType']=='Successful')]))
            home_defensive_actions_counts['Interceptions'].append(len(df[(df['name'] == name) & (df['type'] == 'Interception')]))
            home_defensive_actions_counts['Clearance'].append(len(df[(df['name'] == name) & (df['type'] == 'Clearance')]))
home_defender_df = pd.DataFrame(home_defensive_actions_counts)
home_defender_df['total'] = home_defender_df['Tackles']+home_defender_df['Interceptions']+home_defender_df['Clearance']
home_defender_df = home_defender_df.sort_values(by='total', ascending=False)
home_defender_df.reset_index(drop=True, inplace=True)
home_defender_df = home_defender_df.head(5)
home_defender_df['shortName'] = home_defender_df['name'].apply(get_short_name)        

# Initialize an empty dictionary to store away players different type of defensive actions counts
away_defensive_actions_counts = {'name': away_unique_players, 'Tackles': [], 'Interceptions': [], 'Clearance': []}
for name in away_unique_players:
            away_defensive_actions_counts['Tackles'].append(len(df[(df['name'] == name) & (df['type'] == 'Tackle') & (df['outcomeType']=='Successful')]))
            away_defensive_actions_counts['Interceptions'].append(len(df[(df['name'] == name) & (df['type'] == 'Interception')]))
            away_defensive_actions_counts['Clearance'].append(len(df[(df['name'] == name) & (df['type'] == 'Clearance')]))
away_defender_df = pd.DataFrame(away_defensive_actions_counts)
away_defender_df['total'] = away_defender_df['Tackles']+away_defender_df['Interceptions']+away_defender_df['Clearance']
away_defender_df = away_defender_df.sort_values(by='total', ascending=False)
away_defender_df.reset_index(drop=True, inplace=True)
away_defender_df = away_defender_df.head(5)
away_defender_df['shortName'] = away_defender_df['name'].apply(get_short_name)
        
        # Get unique players
unique_players = df['name'].unique()
        
        
 # Initialize an empty dictionary to store away players different type of pass counts
away_progressor_counts = {'name': away_unique_players, 'Progressive Passes': [], 'Progressive Carries': []}
for name in away_unique_players:
            away_progressor_counts['Progressive Passes'].append(len(df[(df['name'] == name) & (df['prog_pass'] >= 9.144) & (df['x']>=35) & (df['outcomeType']=='Successful') & (df['type_value_Corner taken']!=6) & (df['type_value_Free kick taken']!=5)]))
            away_progressor_counts['Progressive Carries'].append(len(df[(df['name'] == name) & (df['prog_carry'] >= 9.144) & (df['endX']>=35)]))
            
away_progressor_df = pd.DataFrame(away_progressor_counts)
away_progressor_df['total'] = away_progressor_df['Progressive Passes']+away_progressor_df['Progressive Carries']
away_progressor_df = away_progressor_df.sort_values(by='total', ascending=False)
away_progressor_df.reset_index(drop=True, inplace=True)
away_progressor_df = away_progressor_df.head(5)
away_progressor_df['shortName'] = away_progressor_df['name'].apply(get_short_name)       
progressor_counts = {'name': unique_players, 'Progressive Passes': [], 'Progressive Carries': []}
for name in unique_players:
            progressor_counts['Progressive Passes'].append(len(df[(df['name'] == name) & (df['prog_pass'] >= 9.144) & (df['x']>=35) & (df['outcomeType']=='Successful') & (df['type_value_Corner taken']!=6) & (df['type_value_Free kick taken']!=5)]))
            progressor_counts['Progressive Carries'].append(len(df[(df['name'] == name) & (df['prog_carry'] >= 9.144) & (df['endX']>=35)]))
        
progressor_df = pd.DataFrame(progressor_counts)
progressor_df['total'] = progressor_df['Progressive Passes']+progressor_df['Progressive Carries']
progressor_df = progressor_df.sort_values(by='total', ascending=False)
progressor_df.reset_index(drop=True, inplace=True)
progressor_df = progressor_df.head(10)
progressor_df['shortName'] = progressor_df['name'].apply(get_short_name)
        
        
        
        
        # Top Threate Creators
        # Initialize an empty dictionary to store home players different type of Carries counts
xT_counts = {'name': unique_players, 'xT from Pass': [], 'xT from Carry': []}
for name in unique_players:
            xT_counts['xT from Pass'].append((df[(df['name'] == name) & (df['type'] == 'Pass') & (df['xT']>=0) & (df['outcomeType']=='Successful') & (df['type_value_Corner taken']!=6) & (df['type_value_Free kick taken']!=5)])['xT'].sum().round(2))
            xT_counts['xT from Carry'].append((df[(df['name'] == name) & (df['type'] == 'Carry') & (df['xT']>=0)])['xT'].sum().round(2))
xT_df = pd.DataFrame(xT_counts)
xT_df['total'] = xT_df['xT from Pass']+xT_df['xT from Carry']
xT_df = xT_df.sort_values(by='total', ascending=False)
xT_df.reset_index(drop=True, inplace=True)
xT_df = xT_df.head(10)
xT_df['shortName'] = xT_df['name'].apply(get_short_name)
        
        
        
        
        # Shot Sequence Involvement
df_no_carry = df[df['type']!='Carry']
        # Initialize an empty dictionary to store home players different type of shot sequence counts
shot_seq_counts = {'name': unique_players, 'Shots': [], 'Shot Assist': [], 'Buildup to shot': []}
        # Putting counts in those lists
for name in unique_players:
            shot_seq_counts['Shots'].append(len(df[(df['name'] == name) & ((df['type']=='MissedShots') | (df['type']=='SavedShot') | (df['type']=='ShotOnPost') | (df['type']=='Goal'))]))
            shot_seq_counts['Shot Assist'].append(len(df[(df['name'] == name) & (df['type'] == 'Pass') & (df['type_value_Assist']==210)]))
            shot_seq_counts['Buildup to shot'].append(len(df_no_carry[(df_no_carry['name'] == name) & (df_no_carry['type'] == 'Pass') & (df['type_value_Assist'].shift(-1)==210)]))
        # converting that list into a dataframe
sh_sq_df = pd.DataFrame(shot_seq_counts)
sh_sq_df['total'] = sh_sq_df['Shots']+sh_sq_df['Shot Assist']+sh_sq_df['Buildup to shot']
sh_sq_df = sh_sq_df.sort_values(by='total', ascending=False)
sh_sq_df.reset_index(drop=True, inplace=True)
sh_sq_df = sh_sq_df.head(10)
sh_sq_df['shortName'] = sh_sq_df['name'].apply(get_short_name)
        
        
        
        
        # Top Defenders
        # Initialize an empty dictionary to store home players different type of defensive actions counts
defensive_actions_counts = {'name': unique_players, 'Tackles': [], 'Interceptions': [], 'Clearance': []}
for name in unique_players:
            defensive_actions_counts['Tackles'].append(len(df[(df['name'] == name) & (df['type'] == 'Tackle') & (df['outcomeType']=='Successful')]))
            defensive_actions_counts['Interceptions'].append(len(df[(df['name'] == name) & (df['type'] == 'Interception')]))
            defensive_actions_counts['Clearance'].append(len(df[(df['name'] == name) & (df['type'] == 'Clearance')]))
defender_df = pd.DataFrame(defensive_actions_counts)
defender_df['total'] = defender_df['Tackles']+defender_df['Interceptions']+defender_df['Clearance']
defender_df = defender_df.sort_values(by='total', ascending=False)
defender_df.reset_index(drop=True, inplace=True)
defender_df = defender_df.head(10)
defender_df['shortName'] = defender_df['name'].apply(get_short_name)
        
        
        
        # Top Passer's PassMap
import matplotlib.patches as patches
from highlight_text import ax_text       
from mplsoccer import Pitch
import matplotlib.patches as patches
from highlight_text import ax_text
import pandas as pd

def home_player_passmap(ax):
    # 🎨 إعداد الملعب
    pitch = Pitch(pitch_type='uefa', corner_arcs=True,
                  pitch_color=bg_color, line_color=line_color, linewidth=2)
    pitch.draw(ax=ax)
    ax.set_xlim(-0.5, 105.5)
    ax.set_ylim(-0.5, 68.5)

    # 👤 تحديد اللاعب الأعلى تمريرًا
    home_player_name = home_progressor_df['name'].iloc[0]

    # 📊 تمريرات ناجحة
    acc_pass = df[
        (df['name'] == home_player_name) &
        (df['type'] == 'Pass') &
        (df['outcomeType'] == 'Successful')
    ]

    # 📈 تمريرات تقدمية
    pro_pass = acc_pass[
        (acc_pass.get('prog_pass', 0) >= 9.11) &
        (acc_pass.get('x', 0) >= 35) &
        (acc_pass.get('type_value_Corner taken', 0) != 6) &
        (acc_pass.get('type_value_Free kick taken', 0) != 5)
    ]

    # 🚀 حمولات تقدمية
    pro_carry = df[
        (df['name'] == home_player_name) &
        (df.get('prog_carry', 0) >= 9.11) &
        (df.get('endX', 0) >= 35)
    ]

    # 🎯 تمريرات مفتاحية
    key_pass = acc_pass[acc_pass.get('type_value_Assist', 0) == 210]

    # 🅰️ تمريرات أدت إلى أهداف (مساعدات)
    if 'assist' in acc_pass.columns:
        g_assist = acc_pass[acc_pass['assist'] == 1]
    else:
        g_assist = pd.DataFrame()

    # 🟢 تمريرات ناجحة عامة
    if not acc_pass.empty and all(col in acc_pass.columns for col in ['x', 'y', 'endX', 'endY']):
        pitch.lines(acc_pass['x'], acc_pass['y'], acc_pass['endX'], acc_pass['endY'],
                    color=line_color, lw=2, alpha=0.15, comet=True, zorder=2, ax=ax)

    # 🔵 تمريرات تقدمية
    if not pro_pass.empty and all(col in pro_pass.columns for col in ['x', 'y', 'endX', 'endY']):
        pitch.lines(pro_pass['x'], pro_pass['y'], pro_pass['endX'], pro_pass['endY'],
                    color=col1, lw=3, alpha=1, comet=True, zorder=3, ax=ax)

    # 🟣 تمريرات مفتاحية
    if not key_pass.empty and all(col in key_pass.columns for col in ['x', 'y', 'endX', 'endY']):
        pitch.lines(key_pass['x'], key_pass['y'], key_pass['endX'], key_pass['endY'],
                    color=violet, lw=4, alpha=1, comet=True, zorder=4, ax=ax)

    # 🟩 تمريرات أدت إلى أهداف (مع حماية كاملة)
    if not g_assist.empty and all(col in g_assist.columns for col in ['x', 'y', 'endX', 'endY']):
        pitch.lines(g_assist['x'], g_assist['y'], g_assist['endX'], g_assist['endY'],
                    color='green', lw=4, alpha=1, comet=True, zorder=5, ax=ax)
        ax.scatter(g_assist['endX'], g_assist['endY'], s=50, color=bg_color,
                   edgecolor='green', alpha=1, zorder=5)

    # ⚪ رسم نقاط النهاية
    if not acc_pass.empty and 'endX' in acc_pass.columns and 'endY' in acc_pass.columns:
        ax.scatter(acc_pass['endX'], acc_pass['endY'], s=30, color=bg_color,
                   edgecolor='gray', alpha=1, zorder=2)

    if not pro_pass.empty and 'endX' in pro_pass.columns and 'endY' in pro_pass.columns:
        ax.scatter(pro_pass['endX'], pro_pass['endY'], s=40, color=bg_color,
                   edgecolor=col1, alpha=1, zorder=3)

    if not key_pass.empty and 'endX' in key_pass.columns and 'endY' in key_pass.columns:
        ax.scatter(key_pass['endX'], key_pass['endY'], s=50, color=bg_color,
                   edgecolor=violet, alpha=1, zorder=4)

    # 🌀 الأسهم الخاصة بالحمل التقدمي
    if not pro_carry.empty and all(col in pro_carry.columns for col in ['x', 'y', 'endX', 'endY']):
        for _, row in pro_carry.iterrows():
            arrow = patches.FancyArrowPatch(
                (row['x'], row['y']),
                (row['endX'], row['endY']),
                arrowstyle='->', color=col1, zorder=4,
                mutation_scale=20, alpha=0.9, linewidth=2, linestyle='--'
            )
            ax.add_patch(arrow)

    # 🧠 عنوان وتحليل نصي
    home_name_show = home_progressor_df['shortName'].iloc[0]
    ax.set_title(f"{home_name_show} PassMap", color=col1,
                 fontsize=25, fontweight='bold', y=1.03)

    ax.text(0, -3,
            f'Prog. Pass: {len(pro_pass)} | Prog. Carry: {len(pro_carry)}',
            fontsize=15, color=col1, ha='left', va='center')

    ax_text(105, -3,
            s=f'Key Pass: {len(key_pass)} | <Assist: {len(g_assist)}>',
            fontsize=15, color=violet, ha='right', va='center',
            highlight_textprops=[{'color': 'green'}], ax=ax)

from mplsoccer import Pitch
import matplotlib.patches as patches
from highlight_text import ax_text
import pandas as pd

def away_player_passmap(ax):
    # 🎨 إعداد الملعب
    pitch = Pitch(pitch_type='uefa', corner_arcs=True,
                  pitch_color=bg_color, line_color=line_color, linewidth=2)
    pitch.draw(ax=ax)
    ax.set_xlim(-0.5, 105.5)
    ax.set_ylim(-0.5, 68.5)
    ax.invert_xaxis()
    ax.invert_yaxis()

    # 👤 تحديد اللاعب الأعلى تمريرًا
    away_player_name = away_progressor_df['name'].iloc[0]

    # 📊 تمريرات ناجحة
    acc_pass = df[
        (df['name'] == away_player_name) &
        (df['type'] == 'Pass') &
        (df['outcomeType'] == 'Successful')
    ]

    # 📈 تمريرات تقدمية
    pro_pass = acc_pass[
        (acc_pass.get('prog_pass', 0) >= 9.11) &
        (acc_pass.get('x', 0) >= 35) &
        (acc_pass.get('type_value_Corner taken', 0) != 6) &
        (acc_pass.get('type_value_Free kick taken', 0) != 5)
    ]

    # 🚀 حمولات تقدمية
    pro_carry = df[
        (df['name'] == away_player_name) &
        (df.get('prog_carry', 0) >= 9.11) &
        (df.get('endX', 0) >= 35)
    ]

    # 🎯 تمريرات مفتاحية
    key_pass = acc_pass[acc_pass.get('type_value_Assist', 0) == 210]

    # 🅰️ تمريرات أدت إلى أهداف (مساعدات)
    if 'assist' in acc_pass.columns:
        g_assist = acc_pass[acc_pass['assist'] == 1]
    else:
        g_assist = pd.DataFrame()

    # 🟢 تمريرات ناجحة عامة
    if not acc_pass.empty and all(col in acc_pass.columns for col in ['x', 'y', 'endX', 'endY']):
        pitch.lines(acc_pass['x'], acc_pass['y'], acc_pass['endX'], acc_pass['endY'],
                    color=line_color, lw=2, alpha=0.15, comet=True, zorder=2, ax=ax)

    # 🔵 تمريرات تقدمية
    if not pro_pass.empty and all(col in pro_pass.columns for col in ['x', 'y', 'endX', 'endY']):
        pitch.lines(pro_pass['x'], pro_pass['y'], pro_pass['endX'], pro_pass['endY'],
                    color=col2, lw=3, alpha=1, comet=True, zorder=3, ax=ax)

    # 🟣 تمريرات مفتاحية
    if not key_pass.empty and all(col in key_pass.columns for col in ['x', 'y', 'endX', 'endY']):
        pitch.lines(key_pass['x'], key_pass['y'], key_pass['endX'], key_pass['endY'],
                    color=violet, lw=4, alpha=1, comet=True, zorder=4, ax=ax)

    # 🟩 تمريرات أدت إلى أهداف (مع حماية كاملة)
    if not g_assist.empty and all(col in g_assist.columns for col in ['x', 'y', 'endX', 'endY']):
        pitch.lines(g_assist['x'], g_assist['y'], g_assist['endX'], g_assist['endY'],
                    color='green', lw=4, alpha=1, comet=True, zorder=5, ax=ax)
        ax.scatter(g_assist['endX'], g_assist['endY'], s=50, color=bg_color,
                   edgecolor='green', alpha=1, zorder=5)

    # ⚪ نقاط نهاية التمريرات
    if not acc_pass.empty and 'endX' in acc_pass.columns and 'endY' in acc_pass.columns:
        ax.scatter(acc_pass['endX'], acc_pass['endY'], s=30, color=bg_color,
                   edgecolor='gray', alpha=1, zorder=2)

    if not pro_pass.empty and 'endX' in pro_pass.columns and 'endY' in pro_pass.columns:
        ax.scatter(pro_pass['endX'], pro_pass['endY'], s=40, color=bg_color,
                   edgecolor=col2, alpha=1, zorder=3)

    if not key_pass.empty and 'endX' in key_pass.columns and 'endY' in key_pass.columns:
        ax.scatter(key_pass['endX'], key_pass['endY'], s=50, color=bg_color,
                   edgecolor=violet, alpha=1, zorder=4)

    # 🌀 الأسهم الخاصة بالحمل التقدمي
    if not pro_carry.empty and all(col in pro_carry.columns for col in ['x', 'y', 'endX', 'endY']):
        for _, row in pro_carry.iterrows():
            arrow = patches.FancyArrowPatch(
                (row['x'], row['y']),
                (row['endX'], row['endY']),
                arrowstyle='->', color=col2, zorder=4,
                mutation_scale=20, alpha=0.9, linewidth=2, linestyle='--'
            )
            ax.add_patch(arrow)

    # 🧠 العنوان والنصوص التوضيحية
    away_name_show = away_progressor_df['shortName'].iloc[0]
    ax.set_title(f"{away_name_show} PassMap", color=col2,
                 fontsize=25, fontweight='bold', y=1.03)

    ax.text(0, 71,
            f'Prog. Pass: {len(pro_pass)} | Prog. Carry: {len(pro_carry)}',
            fontsize=15, color=col2, ha='right', va='center')

    ax_text(105, 71,
            s=f'Key Pass: {len(key_pass)} | <Assist: {len(g_assist)}>',
            fontsize=15, color=violet, ha='left', va='center',
            highlight_textprops=[{'color': 'green'}], ax=ax)

            
        # Forward Pass Receiving
        
from mplsoccer import Pitch
import pandas as pd
from highlight_text import ax_text

def home_passes_recieved(ax):
    # ملعب
    pitch = Pitch(pitch_type='uefa', corner_arcs=True,
                  pitch_color=bg_color, line_color=line_color, linewidth=2)
    pitch.draw(ax=ax)
    ax.set_xlim(-0.5, 105.5)
    ax.set_ylim(-0.5, 68.5)

    # اسم اللاعب (المهاجم) + الاسم المختصر
    name = home_Forward
    name_show = get_short_name(name) if callable(get_short_name) else str(name)

    # أعمدة قد تكون مفقودة في بعض الملفات → نتهيأ لها
    if 'assist' not in df.columns:
        df['assist'] = 0
    if 'type_value_Assist' not in df.columns:
        df['type_value_Assist'] = 0

    # تأكيد الأعمدة المكانية
    needed_xy = {'x', 'y', 'endX', 'endY'}
    if not needed_xy.issubset(df.columns):
        ax.set_title(f"{name_show} Passes Received", color=col1, fontsize=25, fontweight='bold', y=1.03)
        ax.text(52.5, 34, "⚠️ الملف يفتقد أعمدة المواقع (x,y,endX,endY)", color='w',
                ha='center', va='center', fontsize=14)
        return

    # تمريرات ناجحة والمستقبل هو اللاعب الهدف (باستخدام shift)
    filtered_rows = df[
        (df['type'] == 'Pass') &
        (df['outcomeType'] == 'Successful') &
        (df['name'].shift(-1) == name)
    ]

    # تمريرات مفتاحية ومساعدات مستلمة
    keypass_recieved_df = filtered_rows[filtered_rows['type_value_Assist'] == 210] if not filtered_rows.empty else pd.DataFrame()
    assist_recieved_df  = filtered_rows[filtered_rows['assist'] == 1]               if not filtered_rows.empty else pd.DataFrame()

    pr  = len(filtered_rows)
    kpr = len(keypass_recieved_df)
    ar  = len(assist_recieved_df)

    # رسم الخطوط والنقاط (باستخدام الأقواس لضمان الأمان)
    if pr > 0:
        pitch.lines(filtered_rows['x'], filtered_rows['y'], filtered_rows['endX'], filtered_rows['endY'],
                    lw=3, comet=True, color=col1, alpha=0.5, ax=ax)
        pitch.scatter(filtered_rows['endX'], filtered_rows['endY'], s=30, edgecolor=col1,
                      linewidth=1, color=bg_color, zorder=2, ax=ax)

    if kpr > 0:
        pitch.lines(keypass_recieved_df['x'], keypass_recieved_df['y'],
                    keypass_recieved_df['endX'], keypass_recieved_df['endY'],
                    lw=4, comet=True, color=violet, alpha=0.75, ax=ax)
        pitch.scatter(keypass_recieved_df['endX'], keypass_recieved_df['endY'], s=40,
                      edgecolor=violet, linewidth=1.5, color=bg_color, zorder=2, ax=ax)

    if ar > 0:
        pitch.lines(assist_recieved_df['x'], assist_recieved_df['y'],
                    assist_recieved_df['endX'], assist_recieved_df['endY'],
                    lw=4, comet=True, color='green', alpha=0.75, ax=ax)
        pitch.scatter(assist_recieved_df['endX'], assist_recieved_df['endY'], s=50,
                      edgecolors='green', linewidths=1, marker='football', c=bg_color, zorder=2, ax=ax)

    # خطوط المتوسط
    if pr > 0 and 'endX' in filtered_rows.columns and 'endY' in filtered_rows.columns:
        avg_endX = float(filtered_rows['endX'].median())
        avg_endY = float(filtered_rows['endY'].median())
        ax.axvline(x=avg_endX, color='gray', linestyle='--', alpha=0.6, linewidth=2)
        ax.axhline(y=avg_endY, color='gray', linestyle='--', alpha=0.6, linewidth=2)

    # العنوان والإحصائيات
    ax.set_title(f"{name_show} Passes Received", color=col1, fontsize=25, fontweight='bold', y=1.03)
    highlight_text = [{'color': violet}, {'color': 'green'}]
    ax_text(52.5, -3,
            f'Passes Received: {pr + kpr} | <Keypasses Received: {kpr}> | <Assist Received: {ar}>',
            color=line_color, fontsize=15, ha='center', va='center',
            highlight_textprops=highlight_text, ax=ax)

    return



        
from mplsoccer import Pitch
import pandas as pd
from highlight_text import ax_text

def away_passes_recieved(ax):
    # ملعب
    pitch = Pitch(pitch_type='uefa', corner_arcs=True,
                  pitch_color=bg_color, line_color=line_color, linewidth=2)
    pitch.draw(ax=ax)
    ax.set_xlim(-0.5, 105.5)
    ax.set_ylim(-0.5, 68.5)
    ax.invert_xaxis()
    ax.invert_yaxis()

    # اسم اللاعب (المهاجم) + الاسم المختصر
    name = away_Forward
    name_show = get_short_name(name) if callable(get_short_name) else str(name)

    # أعمدة قد تكون مفقودة
    if 'assist' not in df.columns:
        df['assist'] = 0
    if 'type_value_Assist' not in df.columns:
        df['type_value_Assist'] = 0

    # تأكيد الأعمدة المكانية
    needed_xy = {'x', 'y', 'endX', 'endY'}
    if not needed_xy.issubset(df.columns):
        ax.set_title(f"{name_show} Passes Received", color=col2, fontsize=25, fontweight='bold', y=1.03)
        ax.text(52.5, 34, "⚠️ الملف يفتقد أعمدة المواقع (x,y,endX,endY)", color='w',
                ha='center', va='center', fontsize=14)
        return

    # تمريرات ناجحة والمستقبل هو اللاعب الهدف
    filtered_rows = df[
        (df['type'] == 'Pass') &
        (df['outcomeType'] == 'Successful') &
        (df['name'].shift(-1) == name)
    ]

    # تمريرات مفتاحية ومساعدات مستلمة
    keypass_recieved_df = filtered_rows[filtered_rows['type_value_Assist'] == 210] if not filtered_rows.empty else pd.DataFrame()
    assist_recieved_df  = filtered_rows[filtered_rows['assist'] == 1]               if not filtered_rows.empty else pd.DataFrame()

    pr  = len(filtered_rows)
    kpr = len(keypass_recieved_df)
    ar  = len(assist_recieved_df)

    # رسم
    if pr > 0:
        pitch.lines(filtered_rows['x'], filtered_rows['y'], filtered_rows['endX'], filtered_rows['endY'],
                    lw=3, comet=True, color=col2, alpha=0.5, ax=ax)
        pitch.scatter(filtered_rows['endX'], filtered_rows['endY'], s=30, edgecolor=col2,
                      linewidth=1, color=bg_color, zorder=2, ax=ax)

    if kpr > 0:
        pitch.lines(keypass_recieved_df['x'], keypass_recieved_df['y'],
                    keypass_recieved_df['endX'], keypass_recieved_df['endY'],
                    lw=4, comet=True, color=violet, alpha=0.75, ax=ax)
        pitch.scatter(keypass_recieved_df['endX'], keypass_recieved_df['endY'], s=40,
                      edgecolor=violet, linewidth=1.5, color=bg_color, zorder=2, ax=ax)

    if ar > 0:
        pitch.lines(assist_recieved_df['x'], assist_recieved_df['y'],
                    assist_recieved_df['endX'], assist_recieved_df['endY'],
                    lw=4, comet=True, color='green', alpha=0.75, ax=ax)
        pitch.scatter(assist_recieved_df['endX'], assist_recieved_df['endY'], s=50,
                      edgecolors='green', linewidths=1, marker='football', c=bg_color, zorder=2, ax=ax)

    # خطوط المتوسط
    if pr > 0 and 'endX' in filtered_rows.columns and 'endY' in filtered_rows.columns:
        avg_endX = float(filtered_rows['endX'].median())
        avg_endY = float(filtered_rows['endY'].median())
        ax.axvline(x=avg_endX, color='gray', linestyle='--', alpha=0.6, linewidth=2)
        ax.axhline(y=avg_endY, color='gray', linestyle='--', alpha=0.6, linewidth=2)

    # العنوان والإحصائيات
    ax.set_title(f"{name_show} Passes Received", color=col2, fontsize=25, fontweight='bold', y=1.03)
    highlight_text = [{'color': violet}, {'color': 'green'}]
    ax_text(52.5, 71,
            f'Passes Received: {pr + kpr} | <Keypasses Received: {kpr}> | <Assist Received: {ar}>',
            color=line_color, fontsize=15, ha='center', va='center',
            highlight_textprops=highlight_text, ax=ax)

    return


        
        
        # Top Defenders
        
def home_player_def_acts(ax):
            pitch = Pitch(pitch_type='uefa', corner_arcs=True, pitch_color=bg_color, line_color=line_color, line_zorder=2, linewidth=2)
            pitch.draw(ax=ax)
            ax.set_xlim(-0.5, 105.5)
            ax.set_ylim(-12,68.5)
        
            # taking the top home defender and plotting his defensive actions
            home_player_name = home_defender_df['name'].iloc[0]
            home_playerdf = df[(df['name']==home_player_name)]
        
            hp_tk = home_playerdf[home_playerdf['type']=='Tackle']
            hp_intc = home_playerdf[(home_playerdf['type']=='Interception') | (home_playerdf['type']=='BlockedPass')]
            hp_br = home_playerdf[home_playerdf['type']=='BallRecovery']
            hp_cl = home_playerdf[home_playerdf['type']=='Clearance']
            hp_fl = home_playerdf[(home_playerdf['type']=='Foul') & (home_playerdf['outcomeType']=='Unsuccessful')]
            hp_ar = home_playerdf[(home_playerdf['type']=='Aerial')]
        
            sc1 = pitch.scatter(hp_tk.x, hp_tk.y, s=250, c=col1, lw=2.5, edgecolor=col1, marker='+', hatch='/////', ax=ax)
            sc2 = pitch.scatter(hp_intc.x, hp_intc.y, s=250, c='None', lw=2.5, edgecolor=col1, marker='s', hatch='/////', ax=ax)
            sc3 = pitch.scatter(hp_br.x, hp_br.y, s=250, c='None', lw=2.5, edgecolor=col1, marker='o', hatch='/////', ax=ax)
            sc4 = pitch.scatter(hp_cl.x, hp_cl.y, s=250, c='None', lw=2.5, edgecolor=col1, marker='d', hatch='/////', ax=ax)
            sc5 = pitch.scatter(hp_fl.x, hp_fl.y, s=250, c=col1, lw=2.5, edgecolor=col1, marker='x', hatch='/////', ax=ax)
            sc6 = pitch.scatter(hp_ar.x, hp_ar.y, s=250, c='None', lw=2.5, edgecolor=col1, marker='^', hatch='/////', ax=ax)
        
            sc7 =  pitch.scatter(2, -4, s=150, c=col1, lw=2.5, edgecolor=col1, marker='+', hatch='/////', ax=ax)
            sc8 =  pitch.scatter(2, -10, s=150, c='None', lw=2.5, edgecolor=col1, marker='s', hatch='/////', ax=ax)
            sc9 =  pitch.scatter(41, -4, s=150, c='None', lw=2.5, edgecolor=col1, marker='o', hatch='/////', ax=ax)
            sc10 = pitch.scatter(41, -10, s=150, c='None', lw=2.5, edgecolor=col1, marker='d', hatch='/////', ax=ax)
            sc11 = pitch.scatter(103, -4, s=150, c=col1, lw=2.5, edgecolor=col1, marker='x', hatch='/////', ax=ax)
            sc12 = pitch.scatter(103, -10, s=150, c='None', lw=2.5, edgecolor=col1, marker='^', hatch='/////', ax=ax)
        
            ax.text(5, -3, f"Tackle: {len(hp_tk)}\n\nInterception: {len(hp_intc)}", color=col1, ha='left', va='top', fontsize=13)
            ax.text(43, -3, f"BallRecovery: {len(hp_br)}\n\nClearance: {len(hp_cl)}", color=col1, ha='left', va='top', fontsize=13)
            ax.text(100, -3, f"{len(hp_fl)} Fouls\n\n{len(hp_ar)} Aerials", color=col1, ha='right', va='top', fontsize=13)
        
            home_name_show = home_defender_df['shortName'].iloc[0]
            ax.set_title(f"{home_name_show} Defensive Actions", color=col1, fontsize=25, fontweight='bold')
        
def away_player_def_acts(ax):
            pitch = Pitch(pitch_type='uefa', corner_arcs=True, pitch_color=bg_color, line_color=line_color, line_zorder=2, linewidth=2)
            pitch.draw(ax=ax)
            ax.set_xlim(-0.5, 105.5)
            ax.set_ylim(-0.5,80)
            ax.invert_xaxis()
            ax.invert_yaxis()
        
            # taking the top home defender and plotting his defensive actions
            away_player_name = away_defender_df['name'].iloc[0]
            away_playerdf = df[(df['name']==away_player_name)]
        
            ap_tk = away_playerdf[away_playerdf['type']=='Tackle']
            ap_intc = away_playerdf[(away_playerdf['type']=='Interception') | (away_playerdf['type']=='BlockedPass')]
            ap_br = away_playerdf[away_playerdf['type']=='BallRecovery']
            ap_cl = away_playerdf[away_playerdf['type']=='Clearance']
            ap_fl = away_playerdf[(away_playerdf['type']=='Foul') & (away_playerdf['outcomeType']=='Unsuccessful')]
            ap_ar = away_playerdf[(away_playerdf['type']=='Aerial')]
        
            sc1 = pitch.scatter(ap_tk.x, ap_tk.y, s=250, c=col2, lw=2.5, edgecolor=col2, marker='+', hatch='/////', ax=ax)
            sc2 = pitch.scatter(ap_intc.x, ap_intc.y, s=250, c='None', lw=2.5, edgecolor=col2, marker='s', hatch='/////', ax=ax)
            sc3 = pitch.scatter(ap_br.x, ap_br.y, s=250, c='None', lw=2.5, edgecolor=col2, marker='o', hatch='/////', ax=ax)
            sc4 = pitch.scatter(ap_cl.x, ap_cl.y, s=250, c='None', lw=2.5, edgecolor=col2, marker='d', hatch='/////', ax=ax)
            sc5 = pitch.scatter(ap_fl.x, ap_fl.y, s=250, c=col2, lw=2.5, edgecolor=col2, marker='x', hatch='/////', ax=ax)
            sc6 = pitch.scatter(ap_ar.x, ap_ar.y, s=250, c='None', lw=2.5, edgecolor=col2, marker='^', hatch='/////', ax=ax)
        
            sc7 =  pitch.scatter(2, 72, s=150, c=col2, lw=2.5, edgecolor=col2, marker='+', hatch='/////', ax=ax)
            sc8 =  pitch.scatter(2, 78, s=150, c='None', lw=2.5, edgecolor=col2, marker='s', hatch='/////', ax=ax)
            sc9 =  pitch.scatter(41, 72, s=150, c='None', lw=2.5, edgecolor=col2, marker='o', hatch='/////', ax=ax)
            sc10 = pitch.scatter(41, 78, s=150, c='None', lw=2.5, edgecolor=col2, marker='d', hatch='/////', ax=ax)
            sc11 = pitch.scatter(103, 72, s=150, c=col2, lw=2.5, edgecolor=col2, marker='x', hatch='/////', ax=ax)
            sc12 = pitch.scatter(103, 78, s=150, c='None', lw=2.5, edgecolor=col2, marker='^', hatch='/////', ax=ax)
        
            ax.text(5, 71, f"Tackle: {len(ap_tk)}\n\nInterception: {len(ap_intc)}", color=col2, ha='right', va='top', fontsize=13)
            ax.text(43, 71, f"BallRecovery: {len(ap_br)}\n\nClearance: {len(ap_cl)}", color=col2, ha='right', va='top', fontsize=13)
            ax.text(100, 71, f"{len(ap_fl)} Fouls\n\n{len(ap_ar)} Aerials", color=col2, ha='left', va='top', fontsize=13)
        
            away_name_show = away_defender_df['shortName'].iloc[0]
            ax.set_title(f"{away_name_show} Defensive Actions", color=col2, fontsize=25, fontweight='bold')
            
            
        # GoalKeeper PassMap
        
def home_gk(ax):
            df_gk = df[(df['name']==homeGK) & (df['shortName'].notna())]
            gk_pass = df_gk[df_gk['type']=='Pass']
            op_pass = df_gk[(df_gk['type']=='Pass') & (df_gk['type_value_Goal Kick']!=124) & (df_gk['type_value_Free kick taken']!=5)]
            sp_pass = df_gk[(df_gk['type']=='Pass') & ((df_gk['type_value_Goal Kick']==124) | (df_gk['type_value_Free kick taken']==5))]
            pitch = Pitch(pitch_type='uefa', corner_arcs=True, pitch_color=bg_color, line_color=line_color, linewidth=2)
            pitch.draw(ax=ax)
            ax.set_xlim(-0.5, 105.5)
            ax.set_ylim(-0.5, 68.5)
            gk_name = df_gk['shortName'].unique()[0]
            op_succ = sp_succ = 0
            for index, row in op_pass.iterrows():
                if row['outcomeType']=='Successful':
                    pitch.lines(row['x'], row['y'], row['endX'], row['endY'], color=col1, lw=4, comet=True, alpha=0.5, zorder=2, ax=ax)
                    ax.scatter(row['endX'], row['endY'], s=40, color=col1, edgecolor=line_color, zorder=3)
                    op_succ += 1
                if row['outcomeType']=='Unsuccessful':
                    pitch.lines(row['x'], row['y'], row['endX'], row['endY'], color=col1, lw=4, comet=True, alpha=0.5, zorder=2, ax=ax)
                    ax.scatter(row['endX'], row['endY'], s=40, color=bg_color, edgecolor=col1, zorder=3)
            for index, row in sp_pass.iterrows():
                if row['outcomeType']=='Successful':
                    pitch.lines(row['x'], row['y'], row['endX'], row['endY'], color=violet, lw=4, comet=True, alpha=0.5, zorder=2, ax=ax)
                    ax.scatter(row['endX'], row['endY'], s=40, color=violet, edgecolor=line_color, zorder=3)
                    sp_succ += 1
                if row['outcomeType']=='Unsuccessful':
                    pitch.lines(row['x'], row['y'], row['endX'], row['endY'], color=violet, lw=4, comet=True, alpha=0.35, zorder=2, ax=ax)
                    ax.scatter(row['endX'], row['endY'], s=40, color=bg_color, edgecolor=violet, zorder=3)
        
            op_pass['length'] = np.sqrt((op_pass['x']-op_pass['endX'])**2 + (op_pass['y']-op_pass['endY'])**2)
            sp_pass['length'] = np.sqrt((sp_pass['x']-sp_pass['endX'])**2 + (sp_pass['y']-sp_pass['endY'])**2)
            avg_len_op = round(op_pass['length'].median(), 2)
            avg_len_sp = round(sp_pass['length'].median(), 2)
            
            ax.set_title(f'{gk_name} PassMap', color=col1, fontsize=25, fontweight='bold', y=1.07)
            ax.text(52.5, -3, f'Avg. OpenPlay Pass Length: {avg_len_op}m     |     Avg. SetPiece Pass Length: {avg_len_sp}m', color=line_color, fontsize=14, ha='center', va='center')
            ax_text(52.5, 70, s=f'<Open-play Pass (Acc.): {len(op_pass)} ({op_succ})>     |     <GoalKick/Freekick (Acc.): {len(sp_pass)} ({sp_succ})>', 
                    fontsize=15, highlight_textprops=[{'color':col1}, {'color':violet}], ha='center', va='center', ax=ax)
        
            return
        
def away_gk(ax):
            df_gk = df[(df['name']==awayGK) & (df['shortName'].notna())]
            gk_pass = df_gk[df_gk['type']=='Pass']
            op_pass = df_gk[(df_gk['type']=='Pass') & (df_gk['type_value_Goal Kick']!=124) & (df_gk['type_value_Free kick taken']!=5)]
            sp_pass = df_gk[(df_gk['type']=='Pass') & ((df_gk['type_value_Goal Kick']==124) | (df_gk['type_value_Free kick taken']==5))]
            pitch = Pitch(pitch_type='uefa', corner_arcs=True, pitch_color=bg_color, line_color=line_color, linewidth=2)
            pitch.draw(ax=ax)
            ax.set_xlim(-0.5, 105.5)
            ax.set_ylim(-0.5, 68.5)
            ax.invert_xaxis()
            ax.invert_yaxis()
            gk_name = df_gk['shortName'].unique()[0]
            op_succ = sp_succ = 0
            for index, row in op_pass.iterrows():
                if row['outcomeType']=='Successful':
                    pitch.lines(row['x'], row['y'], row['endX'], row['endY'], color=col2, lw=4, comet=True, alpha=0.5, zorder=2, ax=ax)
                    ax.scatter(row['endX'], row['endY'], s=40, color=col2, edgecolor=line_color, zorder=3)
                    op_succ += 1
                if row['outcomeType']=='Unsuccessful':
                    pitch.lines(row['x'], row['y'], row['endX'], row['endY'], color=col2, lw=4, comet=True, alpha=0.5, zorder=2, ax=ax)
                    ax.scatter(row['endX'], row['endY'], s=40, color=bg_color, edgecolor=col2, zorder=3)
            for index, row in sp_pass.iterrows():
                if row['outcomeType']=='Successful':
                    pitch.lines(row['x'], row['y'], row['endX'], row['endY'], color=violet, lw=4, comet=True, alpha=0.5, zorder=2, ax=ax)
                    ax.scatter(row['endX'], row['endY'], s=40, color=violet, edgecolor=line_color, zorder=3)
                    sp_succ += 1
                if row['outcomeType']=='Unsuccessful':
                    pitch.lines(row['x'], row['y'], row['endX'], row['endY'], color=violet, lw=4, comet=True, alpha=0.35, zorder=2, ax=ax)
                    ax.scatter(row['endX'], row['endY'], s=40, color=bg_color, edgecolor=violet, zorder=3)
        
            op_pass['length'] = np.sqrt((op_pass['x']-op_pass['endX'])**2 + (op_pass['y']-op_pass['endY'])**2)
            sp_pass['length'] = np.sqrt((sp_pass['x']-sp_pass['endX'])**2 + (sp_pass['y']-sp_pass['endY'])**2)
            avg_len_op = round(op_pass['length'].median(), 2)
            avg_len_sp = round(sp_pass['length'].median(), 2)
        
            ax.set_title(f'{gk_name} PassMap', color=col2, fontsize=25, fontweight='bold', y=1.07)
            ax.text(52.5, 71, f'Avg. OpenPlay Pass Length: {avg_len_op}m     |     Avg. SetPiece Pass Length: {avg_len_sp}m', color=line_color, fontsize=14, ha='center', va='center')
            ax_text(52.5, -2, s=f'<Open-play Pass (Acc.): {len(op_pass)} ({op_succ})>     |     <GoalKick/Freekick (Acc.): {len(sp_pass)} ({sp_succ})>', 
                    fontsize=15, highlight_textprops=[{'color':col2}, {'color':violet}], ha='center', va='center', ax=ax)
        
            return
        
        
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import MaxNLocator

def sh_sq_bar(ax):

    # نفس السابق لكن نستبعد الأسماء الفارغة بدل Unknown
    tmp = sh_sq_df.dropna(subset=['shortName']).nsmallest(10, 'total')

    top10_sh_sq = tmp['shortName'].astype(str).tolist()
    shsq_sh = tmp['Shots'].tolist()
    shsq_sa = tmp['Shot Assist'].tolist()
    shsq_bs = tmp['Buildup to shot'].tolist()

    left1 = [w + x for w, x in zip(shsq_sh, shsq_sa)]

    ax.barh(top10_sh_sq, shsq_sh, label='Shot', color=col1, left=0)
    ax.barh(top10_sh_sq, shsq_sa, label='Shot Assist', color=violet, left=shsq_sh)
    ax.barh(top10_sh_sq, shsq_bs, label='Buildup to Shot', color=col2, left=left1)

    # Add counts in the middle of the bars
    for i, player in enumerate(top10_sh_sq):
        for j, count in enumerate([shsq_sh[i], shsq_sa[i], shsq_bs[i]]):
            if count > 0:
                x_position = sum([shsq_sh[i], shsq_sa[i]][:j]) + count / 2
                ax.text(
                    x_position, i, str(count),
                    ha='center', va='center',
                    color=bg_color, fontsize=18, fontweight='bold'
                )

    # نفس السابق: اعتمد max_x من الجدول الأصلي
    max_x = sh_sq_df['total'].iloc[0]
    x_coord = [2 * i for i in range(1, int(max_x / 2))]
    for x in x_coord:
        ax.axvline(x=x, color='gray', linestyle='--', zorder=2, alpha=0.5)

    ax.set_facecolor(bg_color)
    ax.tick_params(axis='x', colors=line_color, labelsize=15)
    ax.tick_params(axis='y', colors=line_color, labelsize=15)

    for spine in ax.spines.values():
        spine.set_edgecolor(bg_color)

    ax.set_title("Shot Sequence Involvement", color=line_color, fontsize=25, fontweight='bold')
    ax.legend(fontsize=13)


        
def passer_bar(ax):
    top10_passers = (
        progressor_df.nsmallest(10, 'total')['shortName']
        .fillna("Unknown")
        .astype(str)
        .tolist()
    )

    passers_pp = progressor_df.nsmallest(10, 'total')['Progressive Passes'].tolist()
    passers_tp = progressor_df.nsmallest(10, 'total')['Progressive Carries'].tolist()

    left1 = [w + x for w, x in zip(passers_pp, passers_tp)]

    ax.barh(top10_passers, passers_pp, label='Prog. Pass', color=col1, left=0)
    ax.barh(top10_passers, passers_tp, label='Prog. Carries', color=col2, left=passers_pp)

    for i, player in enumerate(top10_passers):
        for j, count in enumerate([passers_pp[i], passers_tp[i]]):
            if count > 0:
                x_position = sum([passers_pp[i], passers_tp[i]][:j]) + count / 2
                ax.text(x_position, i, str(count), ha='center', va='center',
                        color=bg_color, fontsize=18, fontweight='bold')

    max_x = progressor_df['total'].iloc[0]
    x_coord = [2 * i for i in range(1, int(max_x / 2))]
    for x in x_coord:
        ax.axvline(x=x, color='gray', linestyle='--', zorder=2, alpha=0.5)

    ax.set_facecolor(bg_color)
    ax.tick_params(axis='x', colors=line_color, labelsize=15)
    ax.tick_params(axis='y', colors=line_color, labelsize=15)
    for spine in ax.spines.values():
        spine.set_edgecolor(bg_color)

    ax.set_title("Top10 Ball Progressors", color=line_color, fontsize=25, fontweight='bold')
    ax.legend(fontsize=13)

        
        
def defender_bar(ax):
    top10_defenders = (
        defender_df.nsmallest(10, 'total')['shortName']
        .fillna("Unknown")
        .astype(str)
        .tolist()
    )

    defender_tk = defender_df.nsmallest(10, 'total')['Tackles'].tolist()
    defender_in = defender_df.nsmallest(10, 'total')['Interceptions'].tolist()
    defender_ar = defender_df.nsmallest(10, 'total')['Clearance'].tolist()

    left1 = [w + x for w, x in zip(defender_tk, defender_in)]

    ax.barh(top10_defenders, defender_tk, label='Tackle', color=col1, left=0)
    ax.barh(top10_defenders, defender_in, label='Interception', color=violet, left=defender_tk)
    ax.barh(top10_defenders, defender_ar, label='Clearance', color=col2, left=left1)

    for i, player in enumerate(top10_defenders):
        for j, count in enumerate([defender_tk[i], defender_in[i], defender_ar[i]]):
            if count > 0:
                x_position = sum([defender_tk[i], defender_in[i]][:j]) + count / 2
                ax.text(x_position, i, str(count), ha='center', va='center',
                        color=bg_color, fontsize=18, fontweight='bold')

    max_x = defender_df['total'].iloc[0]
    x_coord = [2 * i for i in range(1, int(max_x / 2))]
    for x in x_coord:
        ax.axvline(x=x, color='gray', linestyle='--', zorder=2, alpha=0.5)

    ax.set_facecolor(bg_color)
    ax.tick_params(axis='x', colors=line_color, labelsize=15)
    ax.tick_params(axis='y', colors=line_color, labelsize=15)
    for spine in ax.spines.values():
        spine.set_edgecolor(bg_color)

    ax.set_title("Top10 Defenders", color=line_color, fontsize=25, fontweight='bold')
    ax.legend(fontsize=13)

        
        
def threat_creators(ax):
    top10_xT = (
        xT_df.nsmallest(10, 'total')['shortName']
        .fillna("Unknown")
        .astype(str)
        .tolist()
    )

    xT_pass = xT_df.nsmallest(10, 'total')['xT from Pass'].tolist()
    xT_carry = xT_df.nsmallest(10, 'total')['xT from Carry'].tolist()

    left1 = [w + x for w, x in zip(xT_pass, xT_carry)]

    ax.barh(top10_xT, xT_pass, label='xT from pass', color=col1, left=0)
    ax.barh(top10_xT, xT_carry, label='xT from carry', color=violet, left=xT_pass)

    for i, player in enumerate(top10_xT):
        for j, count in enumerate([xT_pass[i], xT_carry[i]]):
            if count > 0:
                x_position = sum([xT_pass[i], xT_carry[i]][:j]) + count / 2
                ax.text(x_position, i, str(count), ha='center', va='center',
                        color=line_color, fontsize=15, rotation=45)

    ax.set_facecolor(bg_color)
    ax.tick_params(axis='x', colors=line_color, labelsize=15)
    ax.tick_params(axis='y', colors=line_color, labelsize=15)
    for spine in ax.spines.values():
        spine.set_edgecolor(bg_color)

    ax.set_title("Top10 Threatening Players", color=line_color, fontsize=25, fontweight='bold')
    ax.legend(fontsize=13)

          
          


def offensive_actions(ax, pname):
    # Viz Dfs:
    playerdf = df[df['name'] == pname]
    passdf = playerdf[playerdf['type'] == 'Pass']
    succ_passdf = passdf[passdf['outcomeType'] == 'Successful']
    prg_pass = playerdf[
        (playerdf['prog_pass'] > 9.144)
        & (playerdf['outcomeType'] == 'Successful')
        & (playerdf['x'] > 35)
        & (playerdf['type_value_Corner taken'] != 6)
        & (playerdf['type_value_Free kick taken'] != 5)
    ]
    prg_carry = playerdf[
        (playerdf['prog_carry'] > 9.144) & (playerdf['endX'] > 35)
    ]
    cc = playerdf[playerdf['type_value_Assist'] == 210]

    # ✅ حماية ضد غياب عمود assist
    if 'assist' not in playerdf.columns:
        playerdf['assist'] = 0

    ga = playerdf[playerdf['assist'] == 1]
    goal = playerdf[(playerdf['type'] == 'Goal') & (playerdf['isOwnGoal'].isna())]
    owngoal = playerdf[(playerdf['type'] == 'Goal') & (playerdf['isOwnGoal'].notna())]
    ontr = playerdf[(playerdf['type'] == 'SavedShot')]
    oftr = playerdf[playerdf['type'].isin(['MissedShots', 'ShotOnPost'])]
    takeOns = playerdf[
        (playerdf['type'] == 'TakeOn') & (playerdf['outcomeType'] == 'Successful')
    ]
    takeOnu = playerdf[
        (playerdf['type'] == 'TakeOn') & (playerdf['outcomeType'] == 'Unsuccessful')
    ]

    # Pitch Plot
    pitch = VerticalPitch(
        pitch_type='uefa',
        corner_arcs=True,
        pitch_color=bg_color,
        line_color=line_color,
        line_zorder=2,
        linewidth=2,
        pad_bottom=27,
    )
    pitch.draw(ax=ax)

    # line, arrow, scatter Plots
    pitch.lines(
        succ_passdf.x, succ_passdf.y, succ_passdf.endX, succ_passdf.endY,
        color='gray', comet=True, lw=2, alpha=0.65, zorder=1, ax=ax
    )
    pitch.scatter(succ_passdf.endX, succ_passdf.endY, color=bg_color, ec='gray', s=20, zorder=2, ax=ax)
    pitch.lines(prg_pass.x, prg_pass.y, prg_pass.endX, prg_pass.endY, color=col2, comet=True, lw=3, zorder=2, ax=ax)
    pitch.scatter(prg_pass.endX, prg_pass.endY, color=bg_color, ec=col2, s=40, zorder=3, ax=ax)
    pitch.lines(cc.x, cc.y, cc.endX, cc.endY, color=violet, comet=True, lw=3.5, zorder=3, ax=ax)
    pitch.scatter(cc.endX, cc.endY, color=bg_color, ec=violet, s=50, lw=1.5, zorder=4, ax=ax)
    pitch.lines(ga.x, ga.y, ga.endX, ga.endY, color='green', comet=True, lw=4, zorder=4, ax=ax)
    pitch.scatter(ga.endX, ga.endY, color=bg_color, ec='green', s=60, lw=2, zorder=5, ax=ax)

    for _, row in prg_carry.iterrows():
        arrow = patches.FancyArrowPatch(
            (row['y'], row['x']), (row['endY'], row['endX']),
            arrowstyle='->', color=col2, zorder=2, mutation_scale=20,
            linewidth=2, linestyle='--'
        )
        ax.add_patch(arrow)

    pitch.scatter(goal.x, goal.y, c=bg_color, edgecolors='green', linewidths=1.2, s=300, marker='football', zorder=10, ax=ax)
    pitch.scatter(owngoal.x, owngoal.y, c=bg_color, edgecolors='orange', linewidths=1.2, s=300, marker='football', zorder=10, ax=ax)
    pitch.scatter(ontr.x, ontr.y, c=col1, edgecolors=line_color, linewidths=1.2, s=200, alpha=0.75, zorder=9, ax=ax)
    pitch.scatter(oftr.x, oftr.y, c=bg_color, edgecolors=col1, linewidths=1.2, s=200, alpha=0.75, zorder=8, ax=ax)
    pitch.scatter(takeOns.x, takeOns.y, c='orange', edgecolors=line_color, marker='h', s=200, alpha=0.75, zorder=7, ax=ax)
    pitch.scatter(takeOnu.x, takeOnu.y, c=bg_color, edgecolors='orange', marker='h', lw=1.2, hatch='//////', s=200, alpha=0.85, zorder=7, ax=ax)

    # النصوص الإحصائية
    if len(owngoal) > 0:
        ax_text(64, -4.5, f'Goals: {len(goal)} | <OwnGoal: {len(owngoal)}>',
                fontsize=12, highlight_textprops=[{'color':'orange'}], ax=ax)
    else:
        ax.text(64, -5.5, f'Goals: {len(goal)}', fontsize=12)
    ax.text(64, -10.5, f'Shots on Target: {len(ontr)}', fontsize=12)
    ax.text(64, -15.5, f'Shots off Target: {len(oftr)}', fontsize=12)
    ax.text(64, -20.5, f'TakeOn (Succ.): {len(takeOns)}', fontsize=12)
    ax.text(64, -25.5, f'TakeOn (Unsucc.): {len(takeOnu)}', fontsize=12)
    ax.text(21, -5.5, f'Successful Pass: {len(succ_passdf)}', fontsize=12)
    ax.text(21, -10.5, f'Porgressive Pass: {len(prg_pass)}', fontsize=12)
    ax.text(21, -15.5, f'Porgressive Carry: {len(prg_carry)}', fontsize=12)
    ax.text(21, -20.5, f'Key Passes: {len(cc)}', fontsize=12)
    ax.text(21, -25.5, f'Assists: {len(ga)}', fontsize=12)
    ax.text(34, 110, 'Offensive Actions', fontsize=20, fontweight='bold', ha='center', va='center')

    return

        

def pass_receiving_and_touchmap(ax, pname):
    # بيانات اللاعب
    playerdf = df[df['name'] == pname]

    # 🔹 استخراج رقم القميص الحقيقي من العمود
    if 'value_Jersey number.y' in playerdf.columns:
        jersey_series = playerdf['value_Jersey number.y'].dropna()
        if not jersey_series.empty:
            shirt_number = str(int(jersey_series.iloc[0]))
        else:
            shirt_number = ""
    else:
        shirt_number = ""

    # بيانات التمريرات واللمسات
    touch_df = playerdf[(playerdf['x'] > 0) & (playerdf['y'] > 0)]
    pass_rec = df[(df['type'] == 'Pass') & (df['outcomeType'] == 'Successful') & (df['name'].shift(-1) == pname)]
    actual_touch = playerdf[playerdf['isTouch'] == 1]

    fthd_tch = actual_touch[actual_touch['x'] >= 70]
    penbox_tch = actual_touch[(actual_touch['x'] >= 88.5) & (actual_touch['y'] >= 13.6) & (actual_touch['y'] <= 54.4)]

    fthd_rec = pass_rec[pass_rec['endX'] >= 70]
    penbox_rec = pass_rec[(pass_rec['endX'] >= 88.5) & (pass_rec['endY'] >= 13.6) & (pass_rec['endY'] <= 54.4)]

    # رسم الملعب
    pitch = VerticalPitch(pitch_type='uefa', corner_arcs=True, pitch_color=bg_color, line_color=line_color, linewidth=2, pad_bottom=27)
    pitch.draw(ax=ax)

    # اللمسات
    ax.scatter(touch_df.y, touch_df.x, marker='o', s=30, c='None', edgecolor=col2, lw=2)
    if len(touch_df) > 3:
        mean_point = np.mean(touch_df[['y', 'x']].values, axis=0)
        distances = np.linalg.norm(touch_df[['y', 'x']].values - mean_point[None, :], axis=1)
        q1, q3 = np.percentile(distances, [20, 80])
        iqr_mask = (distances >= q1) & (distances <= q3)
        points_within_iqr = touch_df[['y', 'x']].values[iqr_mask]
        if len(points_within_iqr) >= 3:
            hull = ConvexHull(points_within_iqr)
            for simplex in hull.simplices:
                ax.plot(points_within_iqr[simplex, 0], points_within_iqr[simplex, 1], color=col2, linestyle='--')
            ax.fill(points_within_iqr[hull.vertices, 0], points_within_iqr[hull.vertices, 1],
                    facecolor='none', edgecolor=col2, alpha=0.3, hatch='/////', zorder=1)

    # تمريرات مستلمة
    ax.scatter(pass_rec.endY, pass_rec.endX, marker='o', s=30, c='None', edgecolor=col1, lw=2)
    if len(pass_rec) > 0:
        avg_x = pass_rec['endX'].mean()
        avg_y = pass_rec['endY'].mean()
        ax.scatter(avg_y, avg_x, s=400, c=col1, edgecolor='white', lw=2, zorder=4)
        if shirt_number != "":
            ax.text(avg_y, avg_x, shirt_number, color='white', fontsize=13, fontweight='bold',
                    ha='center', va='center', zorder=5)

    # النصوص التوضيحية
    ax_text(34, 110, '<Touches> & <Pass Receiving> Points', fontsize=20, fontweight='bold',
            ha='center', va='center', highlight_textprops=[{'color': col2}, {'color': col1}])
    ax.text(34, -5, f'Total Touches: {len(actual_touch)} | at Final Third: {len(fthd_tch)} | at Penalty Box: {len(penbox_tch)}', color=col2, fontsize=13, ha='center', va='center')
    ax.text(34, -9, f'Total Pass Received: {len(pass_rec)} | at Final Third: {len(fthd_rec)} | at Penalty Box: {len(penbox_rec)}', color=col1, fontsize=13, ha='center', va='center')
    ax.text(34, -17, '*blue area = middle 75% touches area', color=col2, fontsize=13, fontstyle='italic', ha='center', va='center')
    ax.text(34, -21, '*red circle = avg receiving position (with shirt number)', color=col1, fontsize=13, fontstyle='italic', ha='center', va='center')

    return

        

def defensive_actions(ax, pname, df, team_color="#0099ff", bg_color="#ffffff", line_color="#000000"):

            # Viz Dfs:
            playerdf = df[df['name']==pname]
            tackles = playerdf[(playerdf['type']=='Tackle') & (playerdf['outcomeType']=='Successful')]
            tackleu = playerdf[(playerdf['type']=='Tackle') & (playerdf['outcomeType']=='Unsuccessful')]
            ballrec = playerdf[playerdf['type']=='BallRecovery']
            intercp = playerdf[playerdf['type']=='Interception']
            clearnc = playerdf[playerdf['type']=='Clearance']
            passbkl = playerdf[playerdf['type']=='BlockedPass']
            shotbkl = playerdf[playerdf['type']=='Save']
            chalnge = playerdf[playerdf['type']=='Challenge']
            aerialw = playerdf[(playerdf['type']=='Aerial') & (playerdf['outcomeType']=='Successful')]
            aerialu = playerdf[(playerdf['type']=='Aerial') & (playerdf['outcomeType']=='Unsuccessful')]

            # Pitch Plot
            pitch = VerticalPitch(pitch_type='uefa', corner_arcs=True, pitch_color=bg_color, line_color=line_color, linewidth=2, pad_bottom=27)
            pitch.draw(ax=ax)

            # Scatter Plots
            sns.scatterplot(x=tackles.y, y=tackles.x, marker='X', s=300, color=col2, edgecolor=line_color, linewidth=1.5, alpha=0.8, ax=ax)
            sns.scatterplot(x=tackleu.y, y=tackleu.x, marker='X', s=300, color=col1, edgecolor=line_color, linewidth=1.5, alpha=0.8, ax=ax)
            pitch.scatter(ballrec.x, ballrec.y, marker='o', lw=1.5, s=300, c=col2, edgecolors=line_color, ax=ax, alpha=0.8)
            pitch.scatter(intercp.x, intercp.y, marker='*', lw=1.25, s=600, c=col2, edgecolors=line_color, ax=ax, alpha=0.8)
            pitch.scatter(clearnc.x, clearnc.y, marker='h', lw=1.5, s=400, c=col2, edgecolors=line_color, ax=ax, alpha=0.8)
            pitch.scatter(passbkl.x, passbkl.y, marker='s', lw=1.5, s=300, c=col2, edgecolors=line_color, ax=ax, alpha=0.8)
            pitch.scatter(shotbkl.x, shotbkl.y, marker='s', lw=1.5, s=300, c=col1, edgecolors=line_color, ax=ax, alpha=0.8)
            pitch.scatter(chalnge.x, chalnge.y, marker='+', lw=5, s=300, c=col1, edgecolors=line_color, ax=ax, alpha=0.8)
            pitch.scatter(aerialw.x, aerialw.y, marker='^', lw=1.5, s=300, c=col2, edgecolors=line_color, ax=ax, alpha=0.8)
            pitch.scatter(aerialu.x, aerialu.y, marker='^', lw=1.5, s=300, c=col1, edgecolors=line_color, ax=ax, alpha=0.8)

            # Stats
            sns.scatterplot(x=[65], y=[-5], marker='X', s=300, color=col2, edgecolor=line_color, linewidth=1.5, alpha=0.8, ax=ax)
            sns.scatterplot(x=[65], y=[-10], marker='X', s=300, color=col1, edgecolor=line_color, linewidth=1.5, alpha=0.8, ax=ax)
            pitch.scatter(-15, 65, marker='o', lw=1.5, s=300, c=col2, edgecolors=line_color, ax=ax, alpha=0.8)
            pitch.scatter(-20, 65, marker='*', lw=1.25, s=600, c=col2, edgecolors=line_color, ax=ax, alpha=0.8)
            pitch.scatter(-25, 65, marker='h', lw=1.5, s=400, c=col2, edgecolors=line_color, ax=ax, alpha=0.8)
            
            pitch.scatter(-5, 26, marker='s', lw=1.5, s=300, c=col2, edgecolors=line_color, ax=ax, alpha=0.8)
            pitch.scatter(-10, 26, marker='s', lw=1.5, s=300, c=col1, edgecolors=line_color, ax=ax, alpha=0.8)
            pitch.scatter(-15, 26, marker='+', lw=5, s=300, c=col1, edgecolors=line_color, ax=ax, alpha=0.8)
            pitch.scatter(-20, 26, marker='^', lw=1.5, s=300, c=col2, edgecolors=line_color, ax=ax, alpha=0.8)
            pitch.scatter(-25, 26, marker='^', lw=1.5, s=300, c=col1, edgecolors=line_color, ax=ax, alpha=0.8)

            ax.text(60, -5.5, f'Tackle (Succ.): {len(tackles)}', fontsize=12)
            ax.text(60, -10.5, f'Tackle (Unsucc.): {len(tackleu)}', fontsize=12)
            ax.text(60, -15.5, f'Ball Recoveries: {len(ballrec)}', fontsize=12)
            ax.text(60, -20.5, f'Interceptions: {len(intercp)}', fontsize=12)
            ax.text(60, -25.5, f'Clearance: {len(clearnc)}', fontsize=12)

            ax.text(21, -5.5, f'Passes Blocked: {len(passbkl)}', fontsize=12)
            ax.text(21, -10.5, f'Shots Blocked: {len(shotbkl)}', fontsize=12)
            ax.text(21, -15.5, f'Dribble Past: {len(chalnge)}', fontsize=12)
            ax.text(21, -20.5, f'Aerials Won: {len(aerialw)}', fontsize=12)
            ax.text(21, -25.5, f'Aerials Lost: {len(aerialu)}', fontsize=12)

            ax.text(34, 110, 'Defensive Actions', fontsize=20, fontweight='bold', ha='center', va='center')
            return




def generate_player_dahsboard(pname, hteamName, hgoal_count, ateamName, agoal_count):
    global df, col1, col2, line_color, bg_color, violet, ax_text

    fig, axs = plt.subplots(1, 3, figsize=(27, 17), facecolor=bg_color)

    # ✅ تمرير كل المعاملات المطلوبة للدالة
    offensive_actions(axs[0], pname)
    defensive_actions(axs[1], pname, df, team_color=col1, bg_color=bg_color, line_color=line_color)
    pass_receiving_and_touchmap(axs[2], pname)

    fig.subplots_adjust(wspace=0.025)

    fig.text(0.5, 0.995, pname, fontsize=34, fontweight='bold', ha='center', va='center', color='black')
    fig.text(0.14, 0.97, f'in {hteamName} {hgoal_count} - {agoal_count} {ateamName}', fontsize=30, ha='left', va='center')

    st.pyplot(fig)




# ====== حساب المؤشر + التفسير التكتيكي ======
import numpy as np
import pandas as pd

def _to_numeric(df, cols):
    for c in cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')
    return df

def _pick_starting(team_df: pd.DataFrame, fallback_n=11):
    """يحاول أخذ isFirstEleven، وإلا يأخذ أول 11 اسم فريد."""
    if 'name' not in team_df.columns:
        return []
    names = team_df['name'].dropna()
    if 'isFirstEleven' in team_df.columns and team_df['isFirstEleven'].notna().any():
        start = team_df[team_df['isFirstEleven'] == True]['name'].dropna().unique().tolist()
        if len(start) < fallback_n:  # اكمل من بقية اللاعبين
            extra = [p for p in names.unique().tolist() if p not in start][:fallback_n - len(start)]
            start += extra
        return start[:fallback_n]
    return names.unique().tolist()[:fallback_n]

def _team_block_band(team_rows: pd.DataFrame, starters: list[str]) -> tuple[float, float, float]:
    """
    يحدد خطي الدفاع/الهجوم من ميديان x للاعبين الأساسيين (تقريبي)،
    ثم يعيد: defense_line, forward_line, median_line
    """
    d = team_rows.copy()
    _to_numeric(d, ['x', 'y'])
    if 'name' in d.columns and starters:
        d = d[d['name'].isin(starters)]
    pos = (d.dropna(subset=['x'])
             .groupby('name', as_index=False)['x']
             .median()
             .rename(columns={'x':'avg_x'}))
    if pos.empty:
        # افتراض وسط الملعب
        return 40.0, 60.0, 52.5
    defense_line = float(pos['avg_x'].quantile(0.25))
    forward_line = float(pos['avg_x'].quantile(0.75))
    median_line  = float(pos['avg_x'].median())
    return defense_line, forward_line, median_line

def _passes_inside_band(team_df: pd.DataFrame,
                        defense_line: float,
                        forward_line: float,
                        successful_only: bool = True) -> tuple[int, int, float]:
    """
    يحسب (عدد التمريرات داخل الكتلة / إجمالي التمريرات) ونسبتها.
    "داخل الكتلة" = مقطع التمريرة يقطع الشريط [min(def,forw), max(def,forw)]
    """
    d = team_df.copy()
    _to_numeric(d, ['x','y','endX','endY'])
    d = d[d['type'] == 'Pass']
    if successful_only and 'outcomeType' in d.columns:
        d = d[d['outcomeType'] == 'Successful']
    d = d.dropna(subset=['x','endX'])  # محور X كفاية لقرار القطع

    if d.empty:
        return 0, 0, 0.0

    xmin, xmax = sorted([defense_line, forward_line])
    crosses = (np.minimum(d['x'], d['endX']) <= xmax) & \
              (np.maximum(d['x'], d['endX']) >= xmin)

    cnt_in = int(crosses.sum())
    total = int(len(d))
    pct = round(100.0 * cnt_in / total, 2) if total > 0 else 0.0
    return cnt_in, total, pct

def explain_block_pct(pct: float, team_name: str) -> str:
    """
    يكتب تفسير تكتيكي بسيط حسب العتبات.
    يمكنك تعديل العتبات حسب دوريّتك.
    """
    if pct >= 55:
        tone = "عالية"
        style = "لعب عمودي وكسر لخطوط الخصم عبر العمق، مع توظيف لاعبي الوسط بين الخطوط."
        risk  = "يتطلب دقة بالتمرير وحلول دعم قريبة لتجنب فقدان الكرة في مناطق خطرة."
    elif pct >= 40:
        tone = "متوسطة"
        style = "مزيج متوازن بين اللعب عبر العمق واستغلال الأطراف حسب ظروف الهجمة."
        risk  = "التوازن جيد، ويمكن رفع الفاعلية بتحسين تموضع صانع اللعب بين الخطوط."
    else:
        tone = "منخفضة"
        style = "اعتماد أكبر على الأطراف أو تمريرات خارج الكتلة، مع توجيه اللعب للمناطق الآمنة."
        risk  = "مفيد لخفض المخاطرة، لكن قد يقلل فرص الاختراق المباشر وصناعة الفرص السريعة."

    return (f"نسبة التمريرات داخل الكتلة لدى {team_name}: {pct:.2f}% — وهي نسبة {tone}. "
            f"هذا يعكس {style} {risk}")

import pandas as pd

def _select_team_rows(df: pd.DataFrame, team_selector):
    # اسم كنص
    if isinstance(team_selector, str):
        mask = df['teamName'].astype(str).str.strip().str.lower() == team_selector.strip().lower()
        return df[mask].copy()

    # قناع منطقي بنفس طول df
    if isinstance(team_selector, pd.Series) and team_selector.dtype == bool and len(team_selector) == len(df):
        return df[team_selector].copy()

    # Series أو ndarray فيه اسم واحد: خذ أول قيمة
    if isinstance(team_selector, pd.Series) and team_selector.dtype != bool:
        vals = team_selector.dropna()
        if not vals.empty:
            return _select_team_rows(df, str(vals.iloc[0]))

    # رقم معرّف الفريق (لو عندك عمود teamId)
    if isinstance(team_selector, (int, float)) and 'teamId' in df.columns:
        return df[df['teamId'] == team_selector].copy()

    raise ValueError("team_name يجب أن يكون نصًا واحدًا، أو قناعًا منطقيًا مطابق الطول، أو Series يحتوي اسمًا واحدًا.")

def analyze_block_passing(df: pd.DataFrame, team_name, successful_only: bool = True) -> dict:
    team_rows = _select_team_rows(df, team_name)
    starters = _pick_starting(team_rows)
    def_line, fwd_line, med_line = _team_block_band(team_rows, starters)
    cnt_in, total, pct = _passes_inside_band(team_rows, def_line, fwd_line, successful_only)
    return {
        'team': team_rows['teamName'].dropna().iloc[0] if 'teamName' in team_rows.columns and not team_rows.empty else str(team_name),
        'cnt_in': cnt_in,
        'total': total,
        'pct': pct,
        'def_line': def_line,
        'fwd_line': fwd_line,
        'median_line': med_line,
        'explanation': explain_block_pct(pct, str(team_name))
    }

import pandas as pd

def get_team_names(df: pd.DataFrame, preferred_home=None, preferred_away=None):
    # 1) لو عندك أسماء جاهزة
    if preferred_home and preferred_away:
        return str(preferred_home), str(preferred_away)

    # 2) أعمدة شائعة للأسماء المباشرة
    for h_col, a_col in [('home_team','away_team'),
                         ('HomeTeam','AwayTeam'),
                         ('homeName','awayName'),
                         ('home','away')]:
        if h_col in df.columns and a_col in df.columns:
            h = str(df[h_col].dropna().iloc[0])
            a = str(df[a_col].dropna().iloc[0])
            return h, a

    # 3) بدلاً من isHomeTeam: لو فيه أعمدة «جانب/جهة» تدل على البيت/خارج
    for side_col in ['teamSide','side','home_away','isHome']:
        if side_col in df.columns and 'teamName' in df.columns:
            # نفترض أن القيم تكون مثل: 'home'/'away' أو 1/0
            side_series = df[side_col].astype(str).str.lower()
            if side_series.isin(['home','away','1','0','true','false']).any():
                # خذ أول اسمين مختلفين مع تفضيل home إن وجد
                home_mask = side_series.isin(['home','1','true'])
                away_mask = side_series.isin(['away','0','false'])
                if home_mask.any():
                    h = str(df.loc[home_mask, 'teamName'].dropna().iloc[0])
                else:
                    h = None
                if away_mask.any():
                    a = str(df.loc[away_mask, 'teamName'].dropna().iloc[0])
                else:
                    a = None
                if h and a:
                    return h, a

    # 4) الملاذ الأخير: أول اسمين فريدين من teamName
    name_col_candidates = ['teamName','team_name','team']
    for col in name_col_candidates:
        if col in df.columns:
            teams = pd.Index(df[col].dropna().unique().tolist())
            if len(teams) >= 2:
                return str(teams[0]), str(teams[1])

    raise KeyError("تعذّر تحديد اسمي الفريقين: وفّر hteamName/ateamName يدويًا أو أعمدة home/away مناسبة.")
home_name, away_name = get_team_names(df, preferred_home=hteamName if 'hteamName' in globals() else None,
                                         preferred_away=ateamName if 'ateamName' in globals() else None)

home_r = analyze_block_passing(df, home_name)   # كما هي دالتك
away_r = analyze_block_passing(df, away_name)











          
def ar(text):
    return str(text)

def pass_network(ax, team_name, col, hteamName, df, bg_color, line_color, ar):
    import pandas as pd
    import numpy as np
    from mplsoccer import Pitch
    from matplotlib.colors import to_rgba
    import matplotlib.patheffects as path_effects

    # --- أعمدة محتملة لأرقام القمصان
    jersey_candidates = ['jerseyNumber', 'value_Jersey number.x', 'value_Jersey number.y']
    jersey_cols = [c for c in jersey_candidates if c in df.columns]

    def _clean_num(s):
        if pd.isna(s): return np.nan
        s = str(s).strip()
        import re
        m = re.search(r'\d+', s)
        return int(m.group(0)) if m else np.nan

    # صفوف الفريق
    team_rows = df[df['teamName'] == team_name].copy()

    # تحديد الأساسيين
    if 'isFirstEleven' in team_rows.columns:
        starting_players = team_rows[team_rows['isFirstEleven'] == True]['name'].dropna().unique().tolist()
        if len(starting_players) < 11:
            extra = [p for p in team_rows['name'].dropna().unique().tolist()
                     if p not in starting_players][:11 - len(starting_players)]
            starting_players += extra
        starting_players = starting_players[:11]
    else:
        starting_players = team_rows['name'].dropna().unique().tolist()[:11]

    # خريطة أرقام القمصان
    jersey_map = {}
    if jersey_cols:
        sub = team_rows[['name'] + jersey_cols].dropna(subset=['name']).copy()
        for c in jersey_cols:
            sub[c] = sub[c].apply(_clean_num)
        for p, g in sub.groupby('name'):
            nums = []
            for c in jersey_cols:
                nums += g[c].dropna().astype(int).tolist()
            if nums:
                jersey_map[p] = pd.Series(nums).mode().iloc[0]

    def label_for(player_name):
        num = jersey_map.get(player_name, np.nan)
        return str(int(num)) if pd.notna(num) else ""

    # تمريرات ناجحة متتالية داخل نفس الفريق
    pass_df_full = df[(df['type'] == 'Pass') &
                      (df['outcomeType'] == 'Successful') &
                      (df['teamName'] == team_name)].copy()
    pass_df_full['pass_receiver'] = pass_df_full['name'].shift(-1)
    pass_df_full['next_team'] = pass_df_full['teamName'].shift(-1)
    pass_df_full.loc[pass_df_full['teamName'] != pass_df_full['next_team'], 'pass_receiver'] = np.nan

    pass_df = pass_df_full[pass_df_full['name'].isin(starting_players) &
                           pass_df_full['pass_receiver'].isin(starting_players)].copy()

    # ضمان الأعمدة
    for a, b in [('endX','end_x'), ('endY','end_y')]:
        if a not in pass_df.columns and b in pass_df.columns:
            pass_df[a] = pass_df[b]
    for c in ['x','y','endX','endY']:
        if c not in pass_df.columns:
            pass_df[c] = np.nan
    pass_df = pass_df.dropna(subset=['x','y','endX','endY'])

    # Verticality (اختياري)
    pass_df['pass_angle'] = np.degrees(np.arctan2(pass_df['endY'] - pass_df['y'],
                                                  pass_df['endX'] - pass_df['x']))
    pass_df['pass_angle_abs'] = pass_df['pass_angle'].abs()
    valid = pass_df[(pass_df['pass_angle_abs'] >= 0) & (pass_df['pass_angle_abs'] <= 90)]
    verticality = round((1 - valid['pass_angle_abs'].median() / 90) * 100, 2) if len(valid) else 0.0

    # عدّ الثنائيات
    pass_counts_df = (pass_df.groupby(['name','pass_receiver'])
                             .size().reset_index(name='pass_count')
                             .sort_values('pass_count', ascending=False)
                             .reset_index(drop=True))

    # تمركز اللاعبين (ميديان)
    team_pos = (team_rows[team_rows['name'].isin(starting_players)]
                .groupby('name').agg(avg_x=('x','median'), avg_y=('y','median')).reset_index())
    # سدّ النواقص
    for p in starting_players:
        if p not in team_pos['name'].values:
            team_pos = pd.concat([team_pos, pd.DataFrame({'name':[p],'avg_x':[52.5],'avg_y':[34]})],
                                 ignore_index=True)
    team_pos['label'] = team_pos['name'].apply(label_for)

    # ربط المواقع مع الثنائيات
    pass_counts_df = pass_counts_df.merge(team_pos, on='name', how='left')
    pass_counts_df = pass_counts_df.merge(team_pos, left_on='pass_receiver', right_on='name',
                                          suffixes=('', '_recv'), how='left')
    pass_counts_df.drop(columns=['name_recv'], inplace=True)
    pass_counts_df.rename(columns={'avg_x_recv':'rx', 'avg_y_recv':'ry'}, inplace=True)

    # حساب خطوط/منطقة الكتلة (تقريبي)
    def _lines_from_positions():
        defense_line = team_pos['avg_x'].quantile(0.25)
        forward_line = team_pos['avg_x'].quantile(0.75)
        median_line  = float(team_pos['avg_x'].median())
        return float(defense_line), float(forward_line), median_line

    defense_line, forward_line, median_line = _lines_from_positions()

    # --- الرسم
    pitch = Pitch(pitch_type='uefa', line_color=line_color, pitch_color=bg_color, linewidth=2)
    pitch.draw(ax=ax)
    ax.set_xlim(0, 105)
    ax.set_ylim(0, 68)

    # الفريق الضيف فقط: قلب محور X ليتقابل الفريقان. (لا نقلب الإحداثيات ولا محور Y)
    is_home = team_name.strip().lower() == hteamName.strip().lower()
    if not is_home:
        ax.invert_yaxis()
        ax.invert_xaxis()
    # خطوط التمرير
    MAX_LINE_WIDTH, MIN_A, MAX_A = 15, 0.05, 0.85
    max_cnt = pass_counts_df['pass_count'].max() if len(pass_counts_df) else 1
    pass_counts_df['width'] = pass_counts_df['pass_count'] / max_cnt * MAX_LINE_WIDTH
    color_rgba = np.array(to_rgba(col))
    colors = np.tile(color_rgba, (len(pass_counts_df), 1))
    if len(pass_counts_df):
        alphas = pass_counts_df['pass_count'] / max_cnt
        colors[:, 3] = (alphas * (MAX_A - MIN_A)) + MIN_A
        pitch.lines(pass_counts_df['avg_x'], pass_counts_df['avg_y'],
                    pass_counts_df['rx'], pass_counts_df['ry'],
                    lw=pass_counts_df['width'], color=colors, zorder=2, ax=ax)

    # عقد اللاعبين + الأرقام بحد أبيض
    for _, r in team_pos.iterrows():
        pitch.scatter(r['avg_x'], r['avg_y'], s=1000, marker='o',
                      color=bg_color, edgecolor=line_color, zorder=3, linewidth=2, ax=ax)
        t = pitch.annotate(r['label'], (r['avg_x'], r['avg_y']),
                           c='black', ha='center', va='center', size=10, ax=ax)
        t.set_path_effects([path_effects.Stroke(linewidth=2, foreground='white'),
                            path_effects.Normal()])

    # خطوط/تظليل الكتلة
    ax.axvline(defense_line, color='lightgray', linestyle=':', alpha=0.8, linewidth=2, zorder=1)
    ax.axvline(forward_line, color='lightgray', linestyle=':', alpha=0.8, linewidth=2, zorder=1)
    ax.axvline(median_line,  color='lightgray', linestyle='--', alpha=0.9, linewidth=2, zorder=1)
    xmin, xmax = sorted([defense_line, forward_line])
    ax.fill_betweenx([0, 68], xmin, xmax, color=col, alpha=0.12, zorder=0)

    # نسب أسفل الشكل (بالنسبة لإحداثيات المحور لضمان عدم القص)
    total = len(pass_df)
    if total > 0:
        crosses = (np.minimum(pass_df['x'], pass_df['endX']) <= xmax) & \
                  (np.maximum(pass_df['x'], pass_df['endX']) >= xmin)
        cnt_in = int(crosses.sum())
        block_pct = round(100.0 * cnt_in / total, 2)
    else:
        cnt_in, block_pct = 0, 0.0

    vert_lbl  = f"{ar('العمودي')}: {verticality:.2f}%"
    med_lbl   = f"{ar('متوسط المسافة الطولية')}: {median_line:.2f}m"
    block_lbl = ar(f"نسبة التمريرات داخل الكتلة: {block_pct:.2f}% ({cnt_in}/{total})")
    metrics_text = f"{vert_lbl}  |  {med_lbl}  |  {block_lbl}"

    ax.text(0.5, -0.06, metrics_text, transform=ax.transAxes,
            ha="center", va="top", fontsize=11, color=col,
            bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=line_color, lw=1, alpha=0.9),
            zorder=10, clip_on=False)

    # العنوان + سطر “متوسط التمركز الطولي”
    # العنوان فقط بدون نصوص مكررة في أسفل اليسار
    title_txt = ar(f"{team_name} - شبكة التمريرات")
    ax.set_title(title_txt, color=col, size=20, fontweight='bold')

# سطر متوسط التمركز في وسط أسفل الملعب
    # ضع السطر أسفل يسار الملعب (ثابت عند home/away)
    ax.text(0.03, 0.05, ar("— — —  متوسط التمركز"), transform=ax.transAxes,
            ha="left", va="center", fontsize=9, color="gray")
    ax.text(0.03, 0.02, ar("·····  خطي الدفاع/الهجوم (تقريبي)"), transform=ax.transAxes,
            ha="left", va="center", fontsize=9, color="gray")
    ax.text(0.03, -0.06, ar("█  منطقة الكتلة"), transform=ax.transAxes,
            ha="left", va="center", fontsize=9, color=col,
            bbox=dict(fc=col, alpha=0.15, ec="none"))

    # سطر متوسط التمركز (متمركز تحت/فوق الملعب حسب الحاجة)














    

def defensive_heatmap(ax, team_name, color, df, bg_color, line_color):


    # تحديد أحداث التدخلات الدفاعية
    defensive_actions_ids = df.index[((df['type'] == 'Aerial') & (df['type_value_Defensive'] == 285)) |
                                     (df['type'] == 'BallRecovery') |
                                     (df['type'] == 'BlockedPass') |
                                     (df['type'] == 'Challenge') |
                                     (df['type'] == 'Clearance') |
                                     (df['type'] == 'Error') |
                                     ((df['type'] == 'Foul') & (df['outcomeType'] == 'Unsuccessful')) |
                                     (df['type'] == 'Interception') |
                                     (df['type'] == 'Tackle')]

    # تصفية البيانات للفريق المحدد
    df_def = df.loc[defensive_actions_ids, ["x", "y", "teamName", "name", "type", "outcomeType"]]
    df_def = df_def[df_def['teamName'] == team_name].reset_index(drop=True)

    # حساب متوسط التمركز وعدد الأحداث لكل لاعب
    locs_df = df_def.groupby('name').agg({'x': ['median'], 'y': ['median', 'count']})
    locs_df.columns = ['x', 'y', 'count']
    locs_df = locs_df.reset_index()
    locs_df['short_name'] = locs_df['name'].apply(lambda x: ''.join([n[0] for n in x.split()]))

    # إعداد الملعب
    pitch = Pitch(pitch_type='uefa', pitch_color=bg_color, line_color=line_color,
                  linewidth=2, line_zorder=2, corner_arcs=True)
    pitch.draw(ax=ax)
    ax.set_facecolor(bg_color)
    ax.set_xlim(-0.5, 105.5)

    # إعداد الحجم
    MAX_MARKER_SIZE = 3500
    locs_df['marker_size'] = locs_df['count'] / locs_df['count'].max() * MAX_MARKER_SIZE

    # خريطة الكثافة KDE
    
    cmap = LinearSegmentedColormap.from_list("TeamCmap", [bg_color, color], N=500)

    pitch.kdeplot(df_def.x, df_def.y, ax=ax, fill=True, levels=5000, thresh=0.02, cut=4, cmap=cmap)

    # تحديد اللاعبين البدلاء
    subs = df[(df['type'] == 'SubstitutionOn') & (df['teamName'] == team_name)].name.to_list()

    # رسم تمركز اللاعبين
    for _, row in locs_df.iterrows():
        marker = 's' if row['name'] in subs else 'o'
        size = row['marker_size'] + (75 if marker == 's' else 100)
        pitch.scatter(row['x'], row['y'], s=size, marker=marker, color=bg_color,
                      edgecolor=line_color, linewidth=1, zorder=3, ax=ax)

    # عرض مواقع الأحداث الدفاعية
    pitch.scatter(df_def.x, df_def.y, s=10, marker='x', color='yellow', alpha=0.2, ax=ax)

    # كتابة الأسماء المختصرة
    for _, row in locs_df.iterrows():
        pitch.annotate(row["short_name"], xy=(row.x, row.y), c=line_color,
                       ha='center', va='center', size=10, ax=ax)

    # خط متوسط الارتفاع الدفاعي
    dah = round(locs_df['x'].mean(), 2)
    ax.vlines(x=dah, ymin=0, ymax=68, color='gray', linestyle='--', alpha=0.75, linewidth=2)

    # عرض النصوص حسب الفريق
    avg_txt = ar(f"متوسط ارتفاع التدخلات الدفاعية: {dah}م")
    title_txt = ar(f"خريطة التدخلات الدفاعية - {team_name}")

    if team_name.strip().lower() == hteam.strip().lower():
        ax.text(52.5, -5, avg_txt, fontsize=15, color=col1, ha='center')
    else:
        ax.invert_xaxis()
        ax.invert_yaxis()
        ax.text(52.5, 73, avg_txt, fontsize=15, color=col2, ha='center')

    ax.set_title(title_txt, color=line_color, size=20, fontweight='bold')


def draw_progressive_pass_map(ax, team_name, col, line_color):
    # تصفية التمريرات التقدمية
    dfpro = df_match[
        (df_match['teamName'] == team_name) &
        (df_match['prog_pass'] >= 9.11) &
        (df_match['type_value_Corner taken'] != 6) &
        (df_match['type_value_Free kick taken'] != 5) &
        (df_match['x'] >= 35) &
        (df_match['outcomeType'] == 'Successful')
    ]

    # رسم الملعب
    pitch = Pitch(pitch_type='uefa', pitch_color=bg_color, line_color=line_color, linewidth=2, corner_arcs=True)
    pitch.draw(ax=ax)
    ax.set_xlim(-0.5, 105.5)

    # عكس الاتجاه للفريق الضيف
    if team_name == ateam:
        ax.invert_xaxis()
        ax.invert_yaxis()

    # حساب التوزيع الأفقي
    pro_count = len(dfpro)
    left = len(dfpro[dfpro['y'] >= 45.33])
    mid = len(dfpro[(dfpro['y'] >= 22.67) & (dfpro['y'] < 45.33)])
    right = len(dfpro[dfpro['y'] < 22.67])

    # خطوط تقسيم الملعب
    ax.hlines([22.67, 45.33], xmin=0, xmax=105, colors=line_color, linestyle='--', alpha=0.3)

    # مربع النسب
    bbox = dict(boxstyle="round,pad=0.3", edgecolor="None", facecolor=bg_color, alpha=0.75)
    ax.text(8, 11.335, f'{right}\n({right * 100 // pro_count if pro_count else 0}%)', color=col, fontsize=18, ha='center', bbox=bbox)
    ax.text(8, 34, f'{mid}\n({mid * 100 // pro_count if pro_count else 0}%)', color=col, fontsize=18, ha='center', bbox=bbox)
    ax.text(8, 56.675, f'{left}\n({left * 100 // pro_count if pro_count else 0}%)', color=col, fontsize=18, ha='center', bbox=bbox)

    # رسم التمريرات
    pitch.lines(dfpro.x, dfpro.y, dfpro.endX, dfpro.endY, lw=3.5, comet=True, color=col, ax=ax, alpha=0.5)
    pitch.scatter(dfpro.endX, dfpro.endY, s=35, edgecolor=col, linewidth=1, color=bg_color, ax=ax)

    # العنوان
    ax.set_title(f"{team_name}\n{pro_count} Progressive Passes", fontsize=20, color=line_color)



def draw_progressive_carry_map(ax, team_name, col, line_color):
    
    dfpro = df[(df['teamName'] == team_name) & 
               (df['prog_carry'] >= 9.11) & 
               (df['endX'] >= 35)]

    pitch = Pitch(pitch_type='uefa', pitch_color=bg_color, line_color=line_color, linewidth=2, corner_arcs=True)
    pitch.draw(ax=ax)
    ax.set_xlim(-0.5, 105.5)

    if team_name == ateam:
        ax.invert_xaxis()
        ax.invert_yaxis()

    pro_count = len(dfpro)

    # حساب التوزيع الأفقي
    left_pro = len(dfpro[dfpro['y'] >= 45.33])
    mid_pro = len(dfpro[(dfpro['y'] >= 22.67) & (dfpro['y'] < 45.33)])
    right_pro = len(dfpro[dfpro['y'] < 22.67])

    left_percentage = round((left_pro / pro_count) * 100) if pro_count else 0
    mid_percentage = round((mid_pro / pro_count) * 100) if pro_count else 0
    right_percentage = round((right_pro / pro_count) * 100) if pro_count else 0

    ax.hlines([22.67, 45.33], xmin=0, xmax=105, colors=line_color, linestyle='dashed', alpha=0.35)

    bbox_props = dict(boxstyle="round,pad=0.3", edgecolor="None", facecolor=bg_color, alpha=0.75)
    ax.text(8, 11.335, f'{right_pro}\n({right_percentage}%)', color=col, fontsize=20, va='center', ha='center', bbox=bbox_props)
    ax.text(8, 34, f'{mid_pro}\n({mid_percentage}%)', color=col, fontsize=20, va='center', ha='center', bbox=bbox_props)
    ax.text(8, 56.675, f'{left_pro}\n({left_percentage}%)', color=col, fontsize=20, va='center', ha='center', bbox=bbox_props)

    # رسم الأسهم للتقدم بالكرة
    for _, row in dfpro.iterrows():
        arrow = patches.FancyArrowPatch((row['x'], row['y']), (row['endX'], row['endY']),
                                        arrowstyle='->', color=col, mutation_scale=20,
                                        alpha=0.8, linewidth=2.5, linestyle='--')
        ax.add_patch(arrow)

    count_text = f"{pro_count} Progressive Carries"
    ax.set_title(f"{team_name}\n{count_text}", color=line_color, fontsize=22, fontweight='bold')



from matplotlib import patheffects as path_effects
path_eff = [path_effects.withStroke(linewidth=3, foreground='white')]

from bidi.algorithm import get_display
import arabic_reshaper
def ar(txt): return str(txt)


def Final_third_entry(ax, df, team_name, color, bg_color, line_color, hteamName, ateamName, is_away=False):
    dfpass = df[(df['teamName'] == team_name) & (df['type'] == 'Pass') &
                (df['x'] < 70) & (df['endX'] >= 70) &
                (df['outcomeType'] == 'Successful') &
                (df['type_value_Free kick taken'] != 5)]

    dfcarry = df[(df['teamName'] == team_name) & (df['type'] == 'Carry') &
                 (df['x'] < 70) & (df['endX'] >= 70)]

    pitch = Pitch(pitch_type='uefa', pitch_color=bg_color, line_color=line_color, linewidth=2, corner_arcs=True)
    pitch.draw(ax=ax)
    ax.set_xlim(-0.5, 105.5)

    if is_away:
        ax.invert_xaxis()
        ax.invert_yaxis()

    total = len(dfpass) + len(dfcarry)
    right_entry = mid_entry = left_entry = 0
    if total > 0:
        right_entry = len(dfpass[dfpass['y'] < 22.67]) + len(dfcarry[dfcarry['y'] < 22.67])
        mid_entry = len(dfpass[(dfpass['y'] >= 22.67) & (dfpass['y'] < 45.33)]) + \
                    len(dfcarry[(dfcarry['y'] >= 22.67) & (dfcarry['y'] < 45.33)])
        left_entry = len(dfpass[dfpass['y'] >= 45.33]) + len(dfcarry[dfcarry['y'] >= 45.33])

    # النسب
    right_percentage = round((right_entry / total) * 100) if total > 0 else 0
    mid_percentage = round((mid_entry / total) * 100) if total > 0 else 0
    left_percentage = round((left_entry / total) * 100) if total > 0 else 0

    # خطوط التقسيم
    ax.hlines([22.67, 45.33], xmin=0, xmax=70, colors=line_color, linestyle='dashed', alpha=0.35)
    ax.vlines(70, ymin=-2, ymax=70, colors=line_color, linestyle='dashed', alpha=0.55)

    # عرض الأرقام
    bbox_props = dict(boxstyle="round,pad=0.3", edgecolor="None", facecolor=bg_color, alpha=0.75)
    ax.text(8, 11.335, f'{right_entry}\n({right_percentage}%)', color=color, fontsize=24, ha='center', va='center', bbox=bbox_props)
    ax.text(8, 34, f'{mid_entry}\n({mid_percentage}%)', color=color, fontsize=24, ha='center', va='center', bbox=bbox_props)
    ax.text(8, 56.675, f'{left_entry}\n({left_percentage}%)', color=color, fontsize=24, ha='center', va='center', bbox=bbox_props)

    # التمريرات
    pitch.lines(dfpass.x, dfpass.y, dfpass.endX, dfpass.endY, lw=3.5, comet=True, color=color, ax=ax, alpha=0.5)
    pitch.scatter(dfpass.endX, dfpass.endY, s=35, edgecolor=color, linewidth=1, color=bg_color, zorder=2, ax=ax)

    # الحمولات
    for _, row in dfcarry.iterrows():
        arrow = patches.FancyArrowPatch((row['x'], row['y']), (row['endX'], row['endY']),
                                        arrowstyle='->', color=color, zorder=4, mutation_scale=20,
                                        alpha=1, linewidth=2, linestyle='--')
       
        ax.add_patch(arrow)

    # العنوان
    team_title = hteamName if team_name == hteamName else ateamName
    ax.set_title(ar(f"{team_title}\nعدد الدخول إلى الثلث الهجومي: {total}"), color=line_color,
                 fontsize=20, fontweight='bold', path_effects=path_eff, pad=20)

    # سهم وتوضيح المنطقة
    if not is_away:
        ax.text(87, 67, ar('<-------------- الثلث الهجومي -------------->'), color=line_color, ha='center', fontsize=12)
        pitch.lines(53, -2, 73, -2, lw=3, comet=True, color=color, ax=ax, alpha=0.6)
        ax.scatter(73, -2, s=35, edgecolor=color, linewidth=1, color=bg_color, zorder=2)
        ax.add_patch(patches.FancyArrowPatch((83, -2), (103, -2), arrowstyle='->', color=color,
                                             zorder=4, mutation_scale=20, alpha=1, linewidth=2, linestyle='--'))
        ax.text(70, -5, ar(f'بالتمرير: {len(dfpass)}'), fontsize=13, color=col1, ha='center')
        ax.text(93, -5, ar(f'بالحمل: {len(dfcarry)}'), fontsize=13, color=col1, ha='center')
    else:
        ax.text(87, 4, ar('<-------------- الثلث الهجومي -------------->'), color=line_color, ha='center', fontsize=12)
        pitch.lines(53, 70, 73, 70, lw=3, comet=True, color=color, ax=ax, alpha=0.6)
        ax.scatter(73, 70, s=35, edgecolor=color, linewidth=1, color=bg_color, zorder=2)
        ax.add_patch(patches.FancyArrowPatch((83, 70), (103, 70), arrowstyle='->', color=color,
                                             zorder=4, mutation_scale=20, alpha=1, linewidth=2, linestyle='--'))
        ax.text(63, 73, ar(f'بالتمرير: {len(dfpass)}'), fontsize=13, color=col2, ha='center')
        ax.text(93, 73, ar(f'بالحمل: {len(dfcarry)}'), fontsize=13, color=col2, ha='center')



def box_entry(ax, df, team_name, hteamName, ateamName, col, bg_color, line_color, is_away=False):
    

    pitch = Pitch(pitch_type='uefa', line_color=line_color, pitch_color=bg_color, linewidth=2)
    pitch.draw(ax=ax)

    if is_away:
        ax.invert_xaxis()
        ax.invert_yaxis()

    # تصفية الدخول لمنطقة الجزاء
    bentry = df[((df['type'] == 'Pass') | (df['type'] == 'Carry')) &
                (df['outcomeType'] == 'Successful') & 
                (df['endX'] >= 88.5) & 
                ~((df['x'] >= 88.5) & (df['y'] >= 13.6) & (df['y'] <= 54.6)) &
                (df['endY'] >= 13.6) & (df['endY'] <= 54.4) &
                (df['teamName'] == team_name)]

    dfpass = bentry[bentry['type'] == 'Pass']
    dfcarry = bentry[bentry['type'] == 'Carry']
    total = len(bentry)

    # رسم التمريرات
    pitch.lines(dfpass.x, dfpass.y, dfpass.endX, dfpass.endY, lw=3.5, comet=True, color=col, ax=ax, alpha=0.5)
    pitch.scatter(dfpass.endX, dfpass.endY, s=35, edgecolor=col, linewidth=1, color=bg_color, zorder=2, ax=ax)

    # رسم الحمولات
    for _, row in dfcarry.iterrows():
        arrow = patches.FancyArrowPatch((row['x'], row['y']), (row['endX'], row['endY']),
                                        arrowstyle='->', color=col, zorder=4, mutation_scale=20,
                                        alpha=1, linewidth=2, linestyle='--')
        ax.add_patch(arrow)

    ax.set_title(ar(f"{team_name}\nعدد الدخول إلى منطقة الجزاء: {total}"),
                 color=col, fontsize=20, fontweight='normal', pad=20)

    if not is_away:
        ax.text(87, 67, ar('<-------------- منطقة الجزاء -------------->'), color=col, ha='center', fontsize=12)
        pitch.lines(53, -2, 73, -2, lw=3, comet=True, color=col, ax=ax, alpha=0.6)
        ax.scatter(73, -2, s=35, edgecolor=col, linewidth=1, color=bg_color, zorder=2)
        ax.add_patch(patches.FancyArrowPatch((83, -2), (103, -2), arrowstyle='->', color=col,
                                             zorder=4, mutation_scale=20, alpha=1, linewidth=2, linestyle='--'))
        ax.text(70, -5, ar(f'بالتمرير: {len(dfpass)}'), fontsize=14, color=col, ha='center')
        ax.text(93, -5, ar(f'بالحمل: {len(dfcarry)}'), fontsize=14, color=col, ha='center')
    else:
        ax.text(87, 4, ar('<-------------- منطقة الجزاء -------------->'), color=col, ha='center', fontsize=12)
        pitch.lines(53, 70, 73, 70, lw=3, comet=True, color=col, ax=ax, alpha=0.6)
        ax.scatter(73, 70, s=35, edgecolor=col, linewidth=1, color=bg_color, zorder=2)
        ax.add_patch(patches.FancyArrowPatch((83, 70), (103, 70), arrowstyle='->', color=col,
                                             zorder=4, mutation_scale=20, alpha=1, linewidth=2, linestyle='--'))
        ax.text(63, 73, ar(f'بالتمرير: {len(dfpass)}'), fontsize=14, color=col, ha='center')
        ax.text(93, 73, ar(f'بالحمل: {len(dfcarry)}'), fontsize=14, color=col, ha='center')


# دالة جديدة لعرض دخول الفريقين معًا
def box_entry_both(ax, df, hteam, ateam, col1, col2, bg_color, line_color):
    """
    دمج دخول منطقة الجزاء للفريقين في خريطة واحدة
    """
    box_entry(ax, df, hteam, hteam, ateam, col1, bg_color, line_color, is_away=False)
    box_entry(ax, df, ateam, hteam, ateam, col2, bg_color, line_color, is_away=True)
    ax.set_title(ar("دخول الفريقين إلى منطقة الجزاء"), fontsize=20, color=line_color, pad=20)






def Crosses(ax, df, hteamName, ateamName, col1, col2, bg_color, line_color):
    from mplsoccer import Pitch
    import matplotlib.patches as patches

    pitch = Pitch(pitch_type='uefa', corner_arcs=True, pitch_color=bg_color, line_color=line_color, linewidth=2)
    pitch.draw(ax=ax)
    ax.set_ylim(-0.5, 68.5)
    ax.set_xlim(-0.5, 105.5)

    # تصفية العرضيات
    home_cross = df[(df['teamName'] == hteamName) & 
                    (df['type'] == 'Pass') & 
                    (df['type_value_Cross'] == 2) & 
                    (df['type_value_Corner taken'] != 6) & 
                    (df['type_value_Free kick taken'] != 5)]

    away_cross = df[(df['teamName'] == ateamName) & 
                    (df['type'] == 'Pass') & 
                    (df['type_value_Cross'] == 2) & 
                    (df['type_value_Corner taken'] != 6) & 
                    (df['type_value_Free kick taken'] != 5)]

    # العدادات
    hsuc = hunsuc = asuc = aunsuc = 0

    # عرضيات الفريق المضيف (معكوس الاتجاه)
    for _, row in home_cross.iterrows():
        x, y = 105 - row['x'], 68 - row['y']
        endX, endY = 105 - row['endX'], 68 - row['endY']
        if row['outcomeType'] == 'Successful':
            color, alpha = col1, 1
            hsuc += 1
        else:
            color, alpha = line_color, 0.25
            hunsuc += 1
        arrow = patches.FancyArrowPatch((x, y), (endX, endY), arrowstyle='->',
                                        mutation_scale=12, color=color, linewidth=2, alpha=alpha)
        ax.add_patch(arrow)

    # عرضيات الفريق الضيف (باتجاه اللعب الطبيعي)
    for _, row in away_cross.iterrows():
        x, y = row['x'], row['y']
        endX, endY = row['endX'], row['endY']
        if row['outcomeType'] == 'Successful':
            color, alpha = col2, 1
            asuc += 1
        else:
            color, alpha = line_color, 0.25
            aunsuc += 1
        arrow = patches.FancyArrowPatch((x, y), (endX, endY), arrowstyle='->',
                                        mutation_scale=12, color=color, linewidth=2, alpha=alpha)
        ax.add_patch(arrow)

    # توزيع العرضيات حسب الجهة
        home_left = len(home_cross[home_cross['y'] >= 34])
        home_right = len(home_cross[home_cross['y'] < 34])
        away_left = len(away_cross[away_cross['y'] >= 34])
        away_right = len(away_cross[away_cross['y'] < 34])

#  كتابة النصوص التوضيحية بالعربية (مع الحفاظ على المحاذاة)
        ax.text(51, 2, ar(f"الجهة اليمنى: {home_right}"), color=col1, fontsize=15, va='bottom', ha='right')
        ax.text(51, 66, ar(f"الجهة اليسرى: {home_left}"), color=col1, fontsize=15, va='top', ha='right')
        ax.text(54, 66, ar(f"الجهة اليسرى: {away_left}"), color=col2, fontsize=15, va='top', ha='left')
        ax.text(54, 2, ar(f"الجهة اليمنى: {away_right}"), color=col2, fontsize=15, va='bottom', ha='left')

#  عدد العرضيات الناجحة وغير الناجحة
        ax.text(0, -2, ar(f"الناجحة: {hsuc}"), color=col1, fontsize=16, ha='left', va='top')
        ax.text(0, -5.5, ar(f"غير الناجحة: {hunsuc}"), color=line_color, fontsize=16, ha='left', va='top')
        ax.text(105, -2, ar(f"الناجحة: {asuc}"), color=col2, fontsize=16, ha='right', va='top')
        ax.text(105, -5.5, ar(f"غير الناجحة: {aunsuc}"), color=line_color, fontsize=16, ha='right', va='top')

#  العنوان الرئيسي بالرسم
        ax.text(0, 70, ar(f"{hteamName}\n<--- العرضيات"), color=col1, size=22, ha='left', fontweight='bold')
        ax.text(105, 70, ar(f"{ateamName}\nالعرضيات --->"), color=col2, size=22, ha='right', fontweight='bold')

    return hsuc, hunsuc, asuc, aunsuc




def HighTO(ax, df, hteam, ateam, col1, col2, bg_color, line_color):
    import numpy as np
    import matplotlib.pyplot as plt
    from mplsoccer import Pitch
    from matplotlib.lines import Line2D
    # دعم العربية (اختياري)
    try:
        import arabic_reshaper
        from bidi.algorithm import get_display
        def _ar(s):
            return str(str(s))
    except Exception:
        def _ar(s):  # fallback
            return str(s)

    # رسم الملعب بخلفية وخطوط مكيّفة
    pitch = Pitch(pitch_type='uefa', corner_arcs=True,
                  pitch_color=bg_color, line_color=line_color, linewidth=2)
    pitch.draw(ax=ax)
    ax.set_xlim(-0.5, 105.5)
    ax.set_ylim(-0.5, 68.5)
    ax.set_facecolor(bg_color)

    # نسخة بيانات + مسافة عن مرمى يمين الشاشة (105,34) لتحديد الضغط العالي (<=40م)
    df_ = df.copy().reset_index(drop=True)
    df_['Distance'] = np.hypot(df_['x'] - 105, df_['y'] - 34)

    # عدادات
    aht_count = ashot_count = agoal_count = 0
    hht_count = hshot_count = hgoal_count = 0

    # ---------- الفريق الضيف (يهاجم يسار->يمين في هذا الشكل) ----------
    for i in range(len(df_)):
        row = df_.iloc[i]
        if row['teamName'] == ateam and row['type'] in ['BallRecovery', 'Interception'] and row['Distance'] <= 40:
            pid = row['possession_id']
            j = i + 1
            # نبحث ضمن نفس الاستحواذ ونفس الفريق عما إذا انتهى بتسديدة أو هدف
            while j < len(df_) and df_.iloc[j]['possession_id'] == pid and df_.iloc[j]['teamName'] == ateam:
                t = df_.iloc[j]['type']
                if t == 'Goal':
                    ax.scatter(row['x'], row['y'], s=600, marker='*',
                               color='green', edgecolor='k', zorder=4)
                    agoal_count += 1
                    break
                elif 'Shot' in t:
                    ax.scatter(row['x'], row['y'], s=150,
                               color=col2, edgecolor=bg_color, zorder=3)
                    ashot_count += 1
                    break
                j += 1
            # علامة الاسترجاع (بدون تسديدة)
            ax.scatter(row['x'], row['y'], s=100, facecolor='none',
                       edgecolor=col2, linewidth=1.6, zorder=2)
            aht_count += 1

    # ---------- الفريق المستضيف (نقلب الاتجاه ليهاجم يمين الشاشة بصريًا) ----------
    for i in range(len(df_)):
        row = df_.iloc[i]
        if row['teamName'] == hteam and row['type'] in ['BallRecovery', 'Interception'] and row['Distance'] <= 40:
            pid = row['possession_id']
            j = i + 1
            while j < len(df_) and df_.iloc[j]['possession_id'] == pid and df_.iloc[j]['teamName'] == hteam:
                t = df_.iloc[j]['type']
                if t == 'Goal':
                    ax.scatter(105 - row['x'], 68 - row['y'], s=600, marker='*',
                               color='green', edgecolor='k', zorder=4)
                    hgoal_count += 1
                    break
                elif 'Shot' in t:
                    ax.scatter(105 - row['x'], 68 - row['y'], s=150,
                               color=col1, edgecolor=bg_color, zorder=3)
                    hshot_count += 1
                    break
                j += 1
            ax.scatter(105 - row['x'], 68 - row['y'], s=100, facecolor='none',
                       edgecolor=col1, linewidth=1.6, zorder=2)
            hht_count += 1

    # مناطق الضغط (نصف قطر 40م حول كل مرمى)
    ax.add_artist(plt.Circle((0, 34), 40, color=col1, fill=True, alpha=0.25, linestyle='dashed'))
    ax.add_artist(plt.Circle((105, 34), 40, color=col2, fill=True, alpha=0.25, linestyle='dashed'))

    # نصوص العناوين واتجاه الهجوم
    ax.text(0, 70, f"{_ar(hteam)}\nHigh Turnover: {hht_count}",
            color=col1, size=16, ha='left', fontweight='bold')
    ax.text(105, 70, f"{_ar(ateam)}\nHigh Turnover: {aht_count}",
            color=col2, size=16, ha='right', fontweight='bold')
    ax.text(0, -3, '<--- Attacking Direction', color=col1, fontsize=11, ha='left')
    ax.text(105, -3, 'Attacking Direction --->', color=col2, fontsize=11, ha='right')

    # وسيلة الإيضاح (رموز مطابقة للرسم)
    legend_elements = [
        # بدون تسديدة (حواف بلون الفريق)
        Line2D([0], [0], marker='o', linestyle='None',
               markerfacecolor='none', markeredgecolor=col1, markeredgewidth=1.8, markersize=8,
               label=_ar(f"{hteam} - بدون تسديدة")),
        Line2D([0], [0], marker='o', linestyle='None',
               markerfacecolor='none', markeredgecolor=col2, markeredgewidth=1.8, markersize=8,
               label=_ar(f"{ateam} - بدون تسديدة")),
        # مع تسديدة (مملوء بلون الفريق)
        Line2D([0], [0], marker='o', linestyle='None',
               markerfacecolor=col1, markeredgecolor=bg_color, markersize=8,
               label=_ar(f"{hteam} - مع تسديدة")),
        Line2D([0], [0], marker='o', linestyle='None',
               markerfacecolor=col2, markeredgecolor=bg_color, markersize=8,
               label=_ar(f"{ateam} - مع تسديدة")),
        # هدف (نجمة خضراء)
        Line2D([0], [0], marker='*', linestyle='None',
               color='none', markerfacecolor='green', markeredgecolor='k', markersize=10,
               label=_ar("انتهى بهدف")),
    ]
    ax.legend(handles=legend_elements,
              loc='lower center', bbox_to_anchor=(0.5, -0.15),
              ncol=3, frameon=True, fontsize=9, fancybox=True, framealpha=0.9)

    ax.set_aspect('equal', adjustable='box')




def zone14hs(ax, df, team_name, col, bg_color, line_color, hteam, ateam):
    from matplotlib import patheffects
    path_eff = [patheffects.Stroke(linewidth=3, foreground=bg_color), patheffects.Normal()]

    dfhp = df[(df['teamName'] == team_name) & (df['type'] == 'Pass') & 
              (df['outcomeType'] == 'Successful') & 
              (df['type_value_Corner taken'] != 6) & 
              (df['type_value_Free kick taken'] != 5)]

    pitch = Pitch(pitch_type='uefa', pitch_color=bg_color, line_color=line_color, linewidth=2, corner_arcs=True)
    pitch.draw(ax=ax)
    ax.set_xlim(-0.5, 105.5)
    ax.set_facecolor(bg_color)

    is_away = team_name == ateam
    if is_away:
        ax.invert_xaxis()
        ax.invert_yaxis()

    z14 = hs = lhs = rhs = 0

    for _, row in dfhp.iterrows():
        if 70 <= row['endX'] <= 88.54 and 22.66 <= row['endY'] <= 45.32:
            pitch.lines(row['x'], row['y'], row['endX'], row['endY'], color='orange', comet=True, lw=3, zorder=3, ax=ax, alpha=0.75)
            ax.scatter(row['endX'], row['endY'], s=35, linewidth=1, color=bg_color, edgecolor='orange', zorder=4)
            z14 += 1
        elif row['endX'] >= 70 and 11.33 <= row['endY'] <= 22.66:
            pitch.lines(row['x'], row['y'], row['endX'], row['endY'], color=col, comet=True, lw=3, zorder=3, ax=ax, alpha=0.75)
            ax.scatter(row['endX'], row['endY'], s=35, linewidth=1, color=bg_color, edgecolor=col, zorder=4)
            hs += 1; rhs += 1
        elif row['endX'] >= 70 and 45.32 <= row['endY'] <= 56.95:
            pitch.lines(row['x'], row['y'], row['endX'], row['endY'], color=col, comet=True, lw=3, zorder=3, ax=ax, alpha=0.75)
            ax.scatter(row['endX'], row['endY'], s=35, linewidth=1, color=bg_color, edgecolor=col, zorder=4)
            hs += 1; lhs += 1

    # المناطق
    ax.fill([70, 88.54, 88.54, 70], [22.66, 22.66, 45.32, 45.32], 'orange', alpha=0.2, label='Zone14')
    ax.fill([70, 105, 105, 70], [11.33, 11.33, 22.66, 22.66], col, alpha=0.2, label='HalfSpace')
    ax.fill([70, 105, 105, 70], [45.32, 45.32, 56.95, 56.95], col, alpha=0.2, label='HalfSpace')

    # العدادات
    ax.scatter(16.46, 13.85, color=col, s=15000, edgecolor=line_color, linewidth=2, alpha=1, marker='h')
    ax.scatter(16.46, 54.15, color='orange', s=15000, edgecolor=line_color, linewidth=2, alpha=1, marker='h')
    ax.text(16.46, 13.85-4, ar("المساحات النصفية"), fontsize=12, color=col, ha='center', path_effects=path_eff)
    ax.text(16.46, 54.15-4, ar("المنطقة 14zone"), fontsize=12, color=col1, ha='center', path_effects=path_eff)
    ax.text(16.46, 13.85+2, str(hs), fontsize=14, color=col2, ha='center', path_effects=path_eff)
    ax.text(16.46, 54.15+2, str(z14), fontsize=14, color=col2, ha='center', path_effects=path_eff)

    ax.set_title(ar(f"{team_name}\nالتمريرات إلى المنطقة 14zone والمساحات النصفية"), color=line_color, fontsize=22, fontweight='bold')


##############################################################

def draw_pass_flow_map(
    df,
    team_name,
    hteamName,
    team_color="#ff0000",
    bg_color="#ffffff",
    line_color="#808080",
    grid=(5, 5),              # (nx, ny)
    min_passes=3,             # لا يرسم سهم إلا إذا >=
    curved=True,              # سهم منحني
    curvature=0.25,           # مقدار الانحناء
    arrow_scale=18,           # حجم رأس السهم
    alpha_min=0.10,
    alpha_max=0.90,
    lw_max=8,
    title_ar=None,            # عنوان عربي جاهز (اختياري)
    show_explanation=True,    # ✅ إظهار الشرح تحت الخريطة
):
    """
    خريطة تدفّق التمريرات (Zone → Zone) لفريق واحد
    - تقسيم الملعب إلى شبكة (افتراضي 5×5)
    - عدّ التمريرات الناجحة من منطقة إلى منطقة
    - رسم أسهم اتجاهية بين مراكز المناطق
    - سهم "اتجاه اللعب" يظهر أسفل الخريطة
    - الضيف يتم عكس اتجاهه (محور X مقلوب) + سهم اتجاه اللعب يصبح بالعكس
    المخرجات:
        fig فقط (بدون جدول)
    """
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from mplsoccer import Pitch
    from matplotlib.colors import to_rgba
    from matplotlib.patches import FancyArrowPatch

    # ---------- Arabic shaping helper (prevents reversed Arabic) ----------
    def _ar(txt: str) -> str:
        try:
            import arabic_reshaper
            from bidi.algorithm import get_display
            return str(str(txt))
        except Exception:
            return str(txt)

    nx, ny = grid
    pitch_length, pitch_width = 105.0, 68.0

    # 1) Validate columns
    need_cols = ["teamName", "type", "outcomeType"]
    for c in need_cols:
        if c not in df.columns:
            raise ValueError(f"Missing column: {c}")

    # 2) Filter successful passes
    pass_df = df[
        (df["teamName"] == team_name) &
        (df["type"] == "Pass") &
        (df["outcomeType"] == "Successful")
    ].copy()

    # Support alternative end columns
    if "endX" not in pass_df.columns and "end_x" in pass_df.columns:
        pass_df["endX"] = pass_df["end_x"]
    if "endY" not in pass_df.columns and "end_y" in pass_df.columns:
        pass_df["endY"] = pass_df["end_y"]

    # Ensure coordinates exist
    for c in ["x", "y", "endX", "endY"]:
        if c not in pass_df.columns:
            pass_df[c] = np.nan

    pass_df = pass_df.dropna(subset=["x", "y", "endX", "endY"]).copy()

    # 3) Create figure & pitch early (so even empty data returns a proper figure)
    fig, ax = plt.subplots(figsize=(10, 6), dpi=200)
    pitch = Pitch(pitch_type="uefa", pitch_color=bg_color, line_color=line_color, linewidth=2)
    pitch.draw(ax=ax)
    ax.set_xlim(0, pitch_length)
    ax.set_ylim(0, pitch_width)

    # ✅ enlarge bottom margin to fit arrow + explanation
    fig.subplots_adjust(bottom=0.22)

    # 4) Home/Away (away is inverted to face each other)
    is_home = str(team_name).strip().lower() == str(hteamName).strip().lower()
    if not is_home:
        ax.invert_xaxis()

    # 5) Draw grid lines
    x_bins = np.linspace(0, pitch_length, nx + 1)
    y_bins = np.linspace(0, pitch_width,  ny + 1)

    for xb in x_bins[1:-1]:
        ax.axvline(xb, color=line_color, lw=1.5, alpha=0.6, zorder=1)
    for yb in y_bins[1:-1]:
        ax.axhline(yb, color=line_color, lw=1.5, alpha=0.6, zorder=1)

    # 6) If empty passes: just title + direction arrow + optional explanation
    if pass_df.empty:
        if title_ar is None:
            title_ar = f"{team_name} - {_ar('خريطة تدفّق التمريرات')} ({nx}×{ny})"
        ax.set_title(_ar(title_ar), fontsize=18, fontweight="bold", color=team_color)

        # ✅ Direction arrow under the pitch (axes fraction, NOT affected by invert_xaxis)
        y_under = -0.08
        if is_home:
            # to the right
            ax.annotate(
                "", xy=(0.70, y_under), xytext=(0.30, y_under),
                xycoords="axes fraction", textcoords="axes fraction",
                arrowprops=dict(arrowstyle="-|>", lw=2.8, color=team_color),
                zorder=20,
            )
            ax.text(0.50, y_under + 0.02, _ar("اتجاه اللعب →"),
                    transform=ax.transAxes, ha="center", va="bottom",
                    fontsize=12, color=team_color, weight="bold")
        else:
            # to the left
            ax.annotate(
                "", xy=(0.30, y_under), xytext=(0.70, y_under),
                xycoords="axes fraction", textcoords="axes fraction",
                arrowprops=dict(arrowstyle="-|>", lw=2.8, color=team_color),
                zorder=20,
            )
            ax.text(0.50, y_under + 0.02, _ar("← اتجاه اللعب"),
                    transform=ax.transAxes, ha="center", va="bottom",
                    fontsize=12, color=team_color, weight="bold")

        if show_explanation:
            exp = (
                "ماذا تمثّل هذه الخريطة؟\n"
                "• الأسهم تمثّل التمريرات الناجحة من منطقة إلى منطقة (Zone → Zone).\n"
                f"• لا يتم رسم أي سهم إلا إذا تكرّر المسار {int(min_passes)} مرات أو أكثر.\n"
                "• سُمك/وضوح السهم يزيد كلما زاد تكرار المسار.\n"
                "• سهم اتجاه اللعب يوضّح جهة هجوم الفريق."
            )
            fig.text(0.5, 0.04, _ar(exp), ha="center", va="bottom", fontsize=12)

        ax.axis("off")
        return fig

    # 7) Zone assignment
    pass_df["from_x"] = np.clip(np.digitize(pass_df["x"],    x_bins) - 1, 0, nx - 1)
    pass_df["from_y"] = np.clip(np.digitize(pass_df["y"],    y_bins) - 1, 0, ny - 1)
    pass_df["to_x"]   = np.clip(np.digitize(pass_df["endX"], x_bins) - 1, 0, nx - 1)
    pass_df["to_y"]   = np.clip(np.digitize(pass_df["endY"], y_bins) - 1, 0, ny - 1)

    # 8) Aggregate flows
    flows = (
        pass_df.groupby(["from_x", "from_y", "to_x", "to_y"])
        .size()
        .reset_index(name="count")
        .sort_values("count", ascending=False)
        .reset_index(drop=True)
    )

    flows_plot = flows[flows["count"] >= int(min_passes)].copy()

    # 9) Zone centers
    x_centers = (x_bins[:-1] + x_bins[1:]) / 2.0
    y_centers = (y_bins[:-1] + y_bins[1:]) / 2.0

    flows_plot["sx"] = flows_plot["from_x"].map(lambda i: float(x_centers[int(i)]))
    flows_plot["sy"] = flows_plot["from_y"].map(lambda j: float(y_centers[int(j)]))
    flows_plot["ex"] = flows_plot["to_x"].map(lambda i: float(x_centers[int(i)]))
    flows_plot["ey"] = flows_plot["to_y"].map(lambda j: float(y_centers[int(j)]))

    # 10) Draw arrows
    if len(flows_plot):
        max_cnt = float(flows_plot["count"].max())
        base_rgba = np.array(to_rgba(team_color), dtype=float)

        def _width(c):
            return (float(c) / max_cnt) * float(lw_max)

        def _alpha(c):
            return (float(c) / max_cnt) * (float(alpha_max) - float(alpha_min)) + float(alpha_min)

        for _, r in flows_plot.iterrows():
            # skip same-zone
            if (r["sx"] == r["ex"]) and (r["sy"] == r["ey"]):
                continue

            lw = _width(r["count"])
            a  = _alpha(r["count"])
            rgba = base_rgba.copy()
            rgba[3] = a

            if curved:
                con = f"arc3,rad={float(curvature)}"
                patch = FancyArrowPatch(
                    (r["sx"], r["sy"]),
                    (r["ex"], r["ey"]),
                    connectionstyle=con,
                    arrowstyle="-|>",
                    mutation_scale=float(arrow_scale),
                    lw=lw,
                    color=rgba,
                    zorder=3,
                )
            else:
                patch = FancyArrowPatch(
                    (r["sx"], r["sy"]),
                    (r["ex"], r["ey"]),
                    arrowstyle="-|>",
                    mutation_scale=float(arrow_scale),
                    lw=lw,
                    color=rgba,
                    zorder=3,
                )

            ax.add_patch(patch)

    # 11) Title (Arabic fixed)
    if title_ar is None:
        title_ar = f"{team_name} - {_ar('خريطة تدفّق التمريرات')} ({nx}×{ny})"
    ax.set_title(_ar(title_ar), fontsize=18, fontweight="bold", color=team_color)

    # ✅ 12) Direction arrow under the pitch (HOME→right, AWAY→left) (not inverted)
    y_under = -0.08
    if is_home:
        ax.annotate(
            "", xy=(0.70, y_under), xytext=(0.30, y_under),
            xycoords="axes fraction", textcoords="axes fraction",
            arrowprops=dict(arrowstyle="-|>", lw=2.8, color=team_color),
            zorder=20,
        )
        ax.text(0.50, y_under + 0.02, _ar("اتجاه اللعب →"),
                transform=ax.transAxes, ha="center", va="bottom",
                fontsize=12, color=team_color, weight="bold")
    else:
        ax.annotate(
            "", xy=(0.30, y_under), xytext=(0.70, y_under),
            xycoords="axes fraction", textcoords="axes fraction",
            arrowprops=dict(arrowstyle="-|>", lw=2.8, color=team_color),
            zorder=20,
        )
        ax.text(0.50, y_under + 0.02, _ar("← اتجاه اللعب"),
                transform=ax.transAxes, ha="center", va="bottom",
                fontsize=12, color=team_color, weight="bold")

    # ✅ 13) Arabic explanation UNDER the map (inside the figure, not Streamlit markdown)
    

    ax.axis("off")
    return fig



#################################################################3
import matplotlib.patheffects as path_effects

def Chance_creating_zone(ax, df, team_name, ateam, col, bg_color, line_color, col1, col2, hteamName):
    from matplotlib import patheffects
    from matplotlib.colors import LinearSegmentedColormap

    def ar(text):
        return str(text)

    # ✅ المؤثرات البصرية للنصوص
    path_eff = [patheffects.Stroke(linewidth=3, foreground=bg_color), patheffects.Normal()]

    green = '#00FF00'   # تمريرة حاسمة
    violet = '#8F00FF'  # تمريرة مفتاحية

    # ✅ تصفية البيانات لصناعة الفرص
    ccp = df[(df['type_value_Assist'] == 210) &
             (df['teamName'] == team_name) &
             (df['type'].str.contains('Pass|BallTouch', na=False))]

    # ✅ خريطة لونية حسب لون الفريق
    custom_cmap = LinearSegmentedColormap.from_list("custom", [bg_color, col], N=20)

    # ✅ رسم الملعب
    pitch = Pitch(pitch_type='uefa', line_color=line_color, pitch_color=bg_color,
                  corner_arcs=True, line_zorder=2, linewidth=2)
    pitch.draw(ax=ax)
    ax.set_facecolor(bg_color)
    ax.set_xlim(-0.5, 105.5)

    # ✅ عكس الاتجاه إذا كان الفريق ضيف
    if team_name == ateam:
        ax.invert_xaxis()
        ax.invert_yaxis()

    # ✅ لا توجد فرص
    if ccp.empty:
        ax.text(52.5, 34, ar("لا توجد فرص مصنوعة"), fontsize=22, color='red', ha='center')
        ax.set_title(ar(f"{team_name}\nخريطة صناعة الفرص"), color=line_color, fontsize=25, fontweight='bold')
        return

    # ✅ خريطة حرارية
    bin_stat = pitch.bin_statistic(ccp['x'], ccp['y'], bins=(6, 5), statistic='count', normalize=False)
    pitch.heatmap(bin_stat, ax=ax, cmap=custom_cmap, edgecolors='#f8f8f8')

    # ✅ رسم التمريرات
    total_cc = 0
    for _, row in ccp.iterrows():
        color = green if row.get('assist') == 1 else violet
        pitch.lines(row['x'], row['y'], row['endX'], row['endY'],
                    color=color, comet=True, lw=3, zorder=3, ax=ax)
        ax.scatter(row['endX'], row['endY'], s=40, linewidth=1,
                   color=bg_color, edgecolor=color, zorder=4)
        total_cc += 1

    # ✅ كتابة الأرقام داخل الخريطة الحرارية
    pitch.label_heatmap(bin_stat, color=line_color, fontsize=20, ax=ax,
                        ha='center', va='center', str_format='{:.0f}', path_effects=path_eff)

    # ✅ الشرح العلوي والسفلي حسب الفريق
    if col == col1:
        ax.text(52.5, -2, ar("بنفسجي = تمريرة مفتاحية   |   أخضر = تمريرة حاسمة"),
                color=col1, size=15, ha='right', va='center', path_effects=path_eff)
        ax.text(52.5, 70, ar(f" مجموع الفرص المصنوعة = {total_cc}"),
                color=col, fontsize=15, ha='center', va='center', path_effects=path_eff)
        ax.set_title(ar(f"{hteamName}\nخريطة صناعة الفرص"), color=col1,
                     fontsize=25, fontweight='bold', path_effects=path_eff)
    else:
        ax.text(52.5, 70.5, ar("بنفسجي = تمريرة مفتاحية   |   أخضر = تمريرة حاسمة"),
                color=col2, size=15, ha='left', va='center', path_effects=path_eff)
        ax.text(52.5, -2, ar(f" مجموع الفرص المصنوعة = {total_cc}"),
                color=col, fontsize=15, ha='center', va='center', path_effects=path_eff)
        ax.set_title(ar(f"{team_name}\nخريطة صناعة الفرص"), color=col2,
                     fontsize=25, fontweight='bold', path_effects=path_eff)



import matplotlib.patheffects as path_effects

import matplotlib.patheffects as path_effects
from mplsoccer import Pitch
import matplotlib.patheffects as path_effects
from mplsoccer import Pitch
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.patheffects as path_effects

# ألوان أساسية
bg_color = '#f5f5f5'
line_color = '#000000'
col1 = '#ff4b44'   # لون الفريق الأول
col2 = '#00a0de'   # لون الفريق الثاني

# تأثيرات النصوص
path_eff = [path_effects.Stroke(linewidth=3, foreground=bg_color), path_effects.Normal()]

# خريطة الألوان بناءً على لون الفريق (بدون color_team1 أو color_team2)
pearl_earring_cmaph = LinearSegmentedColormap.from_list("Pearl Earring H", [bg_color, col1], N=20)
pearl_earring_cmapa = LinearSegmentedColormap.from_list("Pearl Earring A", [bg_color, col2], N=20)


def Pass_end_zone(ax, df, team_name, ateam, col, bg_color, line_color, col1, col2, hteamName):
    

    def ar(text):
        return str(text)

    path_eff = [path_effects.Stroke(linewidth=3, foreground=bg_color), path_effects.Normal()]

    # تصفية التمريرات الناجحة
    df_pass = df[(df['teamName'] == team_name) & 
                 (df['type'] == 'Pass') & 
                 (df['outcomeType'] == 'Successful')]

    # إعداد الملعب
    pitch = Pitch(pitch_type='uefa', line_color=line_color, goal_type='box', goal_alpha=.5,
                  corner_arcs=True, line_zorder=2, pitch_color=bg_color, linewidth=2)
    pitch.draw(ax=ax)
    ax.set_xlim(-0.5, 105.5)
    ax.set_ylim(-0.5, 68.5)
    ax.set_facecolor(bg_color)

    # عكس الاتجاه إذا كان الفريق ضيف
    if team_name == ateam:
        ax.invert_xaxis()
        ax.invert_yaxis()

    # خريطة حرارية لتوزيع نهاية التمريرات (x, y)
    if df_pass.empty:
        ax.text(52.5, 34, ar("لا توجد تمريرات ناجحة"), color='red', fontsize=22, ha='center')
        return

    # إنشاء خريطة حرارية من تمريرات الفريق
    bin_statistic = pitch.bin_statistic(df_pass['endX'], df_pass['endY'], bins=(6, 5), statistic='count', normalize=False)
    total_passes = bin_statistic['statistic'].sum()

    # إنشاء خريطة الألوان المخصصة حسب لون الفريق
    custom_cmap = LinearSegmentedColormap.from_list("custom", [bg_color, col], N=256)

    # رسم الخريطة الحرارية
    pitch.heatmap(bin_statistic, ax=ax, cmap=custom_cmap, edgecolors='gray')

    # كتابة النسب المئوية داخل كل مربع
    percent_stat = np.where(bin_statistic['statistic'] > 0,
                            bin_statistic['statistic'] / total_passes,
                            0)
    bin_statistic['statistic'] = percent_stat  # استبدال بالقيم المئوية
    pitch.label_heatmap(bin_statistic, color=line_color, fontsize=20, ax=ax,
                        ha='center', va='center', str_format='{:.0%}', path_effects=path_eff)

    # عنوان لكل فريق بلونه
    if col == col1:
        ax.set_title(ar(f"{hteamName}\nخريطة نهاية التمريرات"), color=col1,
                     fontsize=25, fontweight='bold', path_effects=path_eff)
    else:
        ax.set_title(ar(f"{team_name}\nخريطة نهاية التمريرات"), color=col2,
                     fontsize=25, fontweight='bold', path_effects=path_eff)
def plot_congestion(ax, df_match, hteamName, ateamName, col1, col2, bg_color=None, line_color=None):
    # هنا ترسم مباشرة على ax
    ax.set_facecolor(bg_color)
    # بقية الكود...


    # ✅ تدرج لوني بين الفريقين
    pcmap = LinearSegmentedColormap.from_list("DominanceCmap", [col2, 'lightgray', col1], N=20)

    # تصفية الأحداث
    df1 = df_match[(df_match['teamName'] == hteamName) &
                   (~df_match['type'].str.contains('SubstitutionOff|SubstitutionOn|Challenge|Card')) &
                   (df_match['type_value_Corner taken'] != 6) &
                   (df_match['type_value_Free kick taken'] != 5)]

    df2 = df_match[(df_match['teamName'] == ateamName) &
                   (~df_match['type'].str.contains('SubstitutionOff|SubstitutionOn|Challenge|Card')) &
                   (df_match['type_value_Corner taken'] != 6) &
                   (df_match['type_value_Free kick taken'] != 5)]

    # ✅ عكس الاتجاه للفريق الثاني
    df2['x'] = 105 - df2['x']
    df2['y'] = 68 - df2['y']

    # رسم الملعب
    pitch = Pitch(pitch_type='uefa', corner_arcs=True, pitch_color=bg_color, line_color=line_color, linewidth=2)
    pitch.draw(ax=ax)
    ax.set_ylim(-0.5, 68.5)
    ax.set_xlim(-0.5, 105.5)

    # تقسيم الملعب
    bin_statistic1 = pitch.bin_statistic(df1.x, df1.y, bins=(6, 5), statistic='count', normalize=False)
    bin_statistic2 = pitch.bin_statistic(df2.x, df2.y, bins=(6, 5), statistic='count', normalize=False)

    # تحديد مركز كل مربع
    cx = np.tile(np.linspace(8.75, 96.25, 6), 5)
    cy = np.repeat([61.2, 47.6, 34.0, 20.4, 6.8], 6)
    df_cong = pd.DataFrame({'cx': cx, 'cy': cy})

    # حساب السيطرة
    hd_values = []
    for i in range(5):
        for j in range(6):
            stat1 = bin_statistic1['statistic'][i, j]
            stat2 = bin_statistic2['statistic'][i, j]
            if stat1 + stat2 == 0:
                hd_values.append(0.5)
            elif (stat1 / (stat1 + stat2)) > 0.55:
                hd_values.append(1)
            elif (stat1 / (stat1 + stat2)) < 0.45:
                hd_values.append(0)
            else:
                hd_values.append(0.5)

    df_cong['hd'] = hd_values

    # رسم الخريطة
    bin_stat = pitch.bin_statistic(df_cong.cx, df_cong.cy, bins=(6, 5), values=df_cong['hd'], statistic='sum', normalize=False)
    pitch.heatmap(bin_stat, ax=ax, cmap=pcmap, edgecolors='black', lw=0.5, zorder=3, alpha=0.85)

    # ✅ خطوط التقسيم
    for i in range(1, 6):
        ax.vlines(i * (105 / 6), ymin=0, ymax=68, color=line_color, lw=2, ls='--', zorder=5)
    for i in range(1, 5):
        ax.hlines(i * (68 / 5), xmin=0, xmax=105, color=line_color, lw=2, ls='--', zorder=5)

    # ✅ النص العلوي المعرب
    txt = str(f"< {hteamName} >     مناطق متنازع عليها     < {ateamName} >")
    ax_text(52.5, 71,
            s=txt,
            highlight_textprops=[{'color': col1}, {'color': col2}],
            color='gray', fontsize=18, ha='center', va='center', ax=ax)

    # ✅ عنوان الرسم
    title = str(" مناطق السيطرة على الملعب")
    ax.set_title(title, color=line_color, fontsize=30, fontweight='bold', y=1.075)

    # ✅ اتجاه الهجوم
    right_arrow = str("اتجاه الهجوم")
    ax.text(0, -3, right_arrow + " --->", color=col1, fontsize=13, ha='left', va='center')
    left_arrow = str("اتجاه الهجوم")
    ax.text(105, -3, "<--- " + left_arrow, color=col2, fontsize=13, ha='right', va='center')

    






def ar_text(txt: str) -> str:
    """تصحيح عرض النص العربي داخل matplotlib."""
    return str(str(txt))






def _safe_ar(s):
    try:
        return ar_text(s)
    except Exception:
        return str(s)

def lighten_color(color, amount=0.45):
    c = to_rgba(color); h,l,s = colorsys.rgb_to_hls(*c[:3])
    l = min(1, l + amount * (1 - l))
    r,g,b = colorsys.hls_to_rgb(h,l,s)
    return (r,g,b,c[3])

def darken_color(color, amount=0.35):
    c = to_rgba(color); h,l,s = colorsys.rgb_to_hls(*c[:3])
    l = max(0, l - amount * l)
    r,g,b = colorsys.hls_to_rgb(h,l,s)
    return (r,g,b,c[3])

def draw_pass_sonar(
    df_match,
    team_name,
    base_color="#0099ff",
    selected_jerseys=None,
    startingXI=None,
    n_bins=20,
    thresholds=(3, 5),
    show_text_explainer=False
):
    # البحث عن عمود رقم القميص
    jersey_cols = ['jerseyNumber', 'value_Jersey number.x', 'value_Jersey number.y']
    jersey_col = next((c for c in jersey_cols if c in df_match.columns), None)

    # تصفية تمريرات الفريق
    passes = df_match[
        (df_match['teamName'].astype(str).str.strip() == str(team_name).strip()) &
        (df_match['type'].astype(str).str.lower() == 'pass')
    ].copy()

    if startingXI:
        passes = passes[passes['name'].isin(startingXI)]

    # فلترة بناءً على أرقام القمصان المختارة
    if selected_jerseys and jersey_col:
        jn = pd.to_numeric(
            passes[jersey_col].astype(str).str.replace(r'\.0$', '', regex=True),
            errors='coerce'
        )
        targets = pd.to_numeric(pd.Series(selected_jerseys), errors='coerce')
        passes = passes[jn.isin(targets.dropna().astype(int))]

    if passes.empty:
        fig, ax = plt.subplots(figsize=(13, 8))
        ax.set_facecolor('#0e1117'); ax.axis('off')
        ax.text(0.5, 0.5, _safe_ar(f"لا توجد تمريرات لفريق {team_name}"),
                color='white', ha='center', va='center', fontsize=14)
        return fig

    # ضمان الإحداثيات
    if 'end_x' not in passes.columns or 'end_y' not in passes.columns:
        if {'endX','endY'}.issubset(passes.columns):
            passes['end_x'] = pd.to_numeric(passes['endX'], errors='coerce')
            passes['end_y'] = pd.to_numeric(passes['endY'], errors='coerce')
        else:
            raise ValueError("لا توجد أعمدة end_x/end_y أو endX/endY.")

    for c in ['x', 'y', 'end_x', 'end_y']:
        passes[c] = pd.to_numeric(passes[c], errors='coerce')
    passes = passes.dropna(subset=['x', 'y', 'end_x', 'end_y'])

    # الطول والزاوية
    passes['length'] = np.hypot(passes['end_x'] - passes['x'], passes['end_y'] - passes['y'])
    passes['angle'] = np.arctan2(passes['end_y'] - passes['y'], passes['end_x'] - passes['x'])

    # تقسيم الزوايا
    bins = np.linspace(-np.pi, np.pi, n_bins + 1)
    passes['angle_bin'] = pd.cut(passes['angle'], bins=bins, labels=False, include_lowest=True)

    # تجميع البيانات
    sonar_df = passes.groupby(['name', 'angle_bin'], as_index=False).agg(
        length=('length', 'mean'),
        amount=('length', 'size')
    )
    avg_pos = passes.groupby('name', as_index=False).agg(x=('x', 'mean'), y=('y', 'mean'))
    sonar_df = sonar_df.merge(avg_pos, on='name', how='left')

    # رسم الملعب
    pitch = Pitch(pitch_type='uefa', pitch_color='#0e1117', line_color='#c7d5cc')
    fig, ax = pitch.draw(figsize=(13, 8))
    fig.set_facecolor('#0e1117')

    ax.set_title(_safe_ar(f"خريطة سونار التمريرات — {team_name}"),
                 color='white', fontsize=20, pad=20)
    ax.text(60, -5, _safe_ar("كل قطاع يمثل اتجاه وعدد التمريرات.\nاللون يعكس كثافة التمرير."),
            color='white', fontsize=11, ha='center')

    # تدرج ألوان الفريق
    low_c = lighten_color(base_color, 0.45)
    mid_c = to_rgba(base_color)
    high_c = darken_color(base_color, 0.35)

    # رسم القطاعات
    for player, pdf in sonar_df.groupby('name'):
        px, py = float(pdf['x'].iloc[0]), float(pdf['y'].iloc[0])
        for _, r in pdf.iterrows():
            if pd.isna(r['angle_bin']):
                continue
            angle_center = -np.pi + (r['angle_bin'] + 0.5) * (2 * np.pi / n_bins)
            theta1 = np.degrees(angle_center - (np.pi / n_bins))
            theta2 = np.degrees(angle_center + (np.pi / n_bins))

            amt = int(r['amount'])
            if amt < thresholds[0]:
                color = low_c
            elif amt < thresholds[1]:
                color = mid_c
            else:
                color = high_c

            wedge = Wedge(
                center=(px, py),
                r=max(4, r['length'] * 0.16),
                theta1=theta1, theta2=theta2,
                facecolor=color, edgecolor='black', alpha=0.65
            )
            ax.add_patch(wedge)

        ax.text(px, py, str(player), ha='center', va='center', fontsize=8, color='white')

    # وسيلة الإيضاح
    legend_patches = [
        plt.Line2D([0], [0], color=low_c, lw=6, label=_safe_ar(f"قليل (<{thresholds[0]})")),
        plt.Line2D([0], [0], color=mid_c, lw=6, label=_safe_ar(f"متوسط ({thresholds[0]}–{thresholds[1]})")),
        plt.Line2D([0], [0], color=high_c, lw=6, label=_safe_ar(f"كثير (>{thresholds[1]})")),
    ]
    ax.legend(handles=legend_patches, title=_safe_ar("عدد التمريرات"),
              title_fontsize=10, fontsize=9, loc='upper right')

    if show_text_explainer:
        ax.text(60, -10,
                _safe_ar(" الأخضر الفاتح = تمريرات قليلة (<{a})\n الأخضر المتوسط = تمريرات متوسطة ({a}–{b})\n✅ الأخضر الداكن = تمريرات كثيرة (>{b})"
                         .format(a=thresholds[0], b=thresholds[1])),
                color='white', fontsize=10, ha='center', va='top')

    return fig



import matplotlib.colors as mc


    # دفاع (أفتح)، وسط (أوسط)، هجوم (أغمق)
def three_shades(base_hex, levels=(0.65, 0.80, 1.00)):
        r, g, b = mc.to_rgb(base_hex)

        def clamp01(x):
            x = float(x)
            return 0.0 if x < 0 else (1.0 if x > 1 else x)

        def blend(t):
            t = clamp01(t)
            # t=1 → اللون الأساسي، t=0 → أبيض
            return mc.to_hex((1 - (1 - r) * t,
                              1 - (1 - g) * t,
                              1 - (1 - b) * t))
        d, m, a = levels
        return blend(d), blend(m), blend(a)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from mplsoccer import Pitch

from matplotlib.patches import Rectangle
from mplsoccer import Pitch

from matplotlib.patches import Rectangle
from mplsoccer import Pitch

from matplotlib.patches import Rectangle, Circle

def draw_team_thirds_with_direction(ax, team_name, thirds_data,
                                    color_def, color_mid, color_att,
                                    attack_right=True):
    """
    thirds_data: {'Def': .., 'Mid': .., 'Att': ..}
    يعرض كنِسَب صحيحة ويضمن المجموع = 100%.
    """

    # --- تحويل القيم لأعداد صحيحة مجموعها 100 ---
    import numpy as np
    keys = ['Def','Mid','Att']
    vals = np.array([float(thirds_data.get(k, 0)) for k in keys], dtype=float)
    total = vals.sum()
    if total <= 0:
        Ndef, Nmid, Natt = 0, 0, 0
    else:
        raw = vals * (100.0/total) if total != 100 else vals
        base = np.floor(raw).astype(int)
        remain = 100 - base.sum()
        if remain > 0:
            idx = np.argsort(-(raw-base))[:remain]
            base[idx] += 1
        Ndef, Nmid, Natt = base.tolist()

    # طبقات الرسم
    z_shade, z_pitch, z_text = 0, 3, 4

    L, W = 120, 80

    # --- التظليل (خلف الخطوط) ---
    if attack_right:
        shades = [(0, color_def), (40, color_mid), (80, color_att)]
        txts   = [(20, Ndef), (60, Nmid), (100, Natt)]
    else:
        shades = [(0, color_att), (40, color_mid), (80, color_def)]
        txts   = [(20, Natt), (60, Nmid), (100, Ndef)]

    for x, c in shades:
        ax.add_patch(Rectangle((x, 0), 40, W, facecolor=c, alpha=0.35,
                               edgecolor='none', zorder=z_shade))

    # --- خطوط الملعب فوق التظليل ---
    ax.add_patch(Rectangle((0,0), L, W, fill=False, linewidth=2, zorder=z_pitch))
    ax.plot([L/2, L/2], [0, W], color='black', linewidth=2, zorder=z_pitch)

    ax.add_patch(Rectangle((0, (W/2)-18),   18, 36, fill=False, linewidth=2, zorder=z_pitch))
    ax.add_patch(Rectangle((L-18, (W/2)-18),18, 36, fill=False, linewidth=2, zorder=z_pitch))

    ax.add_patch(Rectangle((0, (W/2)-6),    6, 12, fill=False, linewidth=2, zorder=z_pitch))
    ax.add_patch(Rectangle((L-6,(W/2)-6),   6, 12, fill=False, linewidth=2, zorder=z_pitch))

    ax.add_patch(Rectangle((-2, (W/2)-2), 2, 4, fill=False, linewidth=2, zorder=z_pitch))
    ax.add_patch(Rectangle((L,  (W/2)-2), 2, 4, fill=False, linewidth=2, zorder=z_pitch))

    ax.add_patch(Circle((L/2, W/2), 10, fill=False, linewidth=2, zorder=z_pitch))
    ax.plot(L/2, W/2, 'o', color='black', zorder=z_pitch)

    # --- النصوص والسهام (أعلى الطبقات) ---
    for x, v in txts:
        ax.text(x, W/2, f"{int(v)}%", ha='center', va='center',
                fontsize=22, weight='bold', zorder=z_text)

    if attack_right:
        ax.annotate("", xy=(110, 75), xytext=(90, 75),
                    arrowprops=dict(arrowstyle='-|>', lw=2.0, color=shades[2][1]), zorder=z_text)
        ax.text(100, 77, "اتجاه لعب →", ha='center', va='bottom',
                fontsize=11, color=shades[2][1], zorder=z_text)
    else:
        ax.annotate("", xy=(10, 75), xytext=(30, 75),
                    arrowprops=dict(arrowstyle='-|>', lw=2.0, color=shades[0][1]), zorder=z_text)
        ax.text(20, 77, "← اتجاه لعب", ha='center', va='bottom',
                fontsize=11, color=shades[0][1], zorder=z_text)

    ax.set_title(str(team_name), fontsize=14)
    ax.set_aspect('equal')
    ax.axis('off')


#st.write(sorted(df_match.columns.tolist()))


def ar_text(text):
    """إرجاع النص العربي بشكل صحيح لعرضه في matplotlib."""
    return str(text)


def plot_pass_sequence_by_id(df_team, seq_id, team_color, ax, bg_color="#ffffff", line_color="#000000"):
    # تمريرات هذه السلسلة (الناجحة فقط) مرتبة زمنيًا
    seq = (
        df_team[(df_team['seq_id'] == seq_id) & (df_team['is_pass'])]
        .copy()
        .sort_values('tsec')
    )
    # حذف الصفوف التي ينقصها إحداثيات
    seq = seq.dropna(subset=['x','y','endX','endY'])
    if seq.empty:
        ax.set_title(ar_text("لا توجد إحداثيات صالحة لهذه السلسلة"), fontsize=11)
        return

    pitch = VerticalPitch(pitch_type='uefa', pitch_color=bg_color, line_color=line_color, linewidth=2, pad_bottom=20)
    pitch.draw(ax=ax)

    pitch.lines(seq.x, seq.y, seq.endX, seq.endY, comet=True, lw=3, color=team_color, ax=ax, zorder=2)
    pitch.scatter(seq.endX, seq.endY, s=50, c=bg_color, ec=team_color, lw=2, ax=ax, zorder=3)

    first = seq.iloc[0]
    pitch.scatter([first.x],[first.y], s=110, c=team_color, ec=line_color, lw=1.2, ax=ax, zorder=4)

    start_t, end_t = int(seq['tsec'].min()), int(seq['tsec'].max())
    ax.set_title(
        ar_text(f"سلسلة: {len(seq)} تمريرة\n"
                f"{start_t//60:02d}:{start_t%60:02d} → {end_t//60:02d}:{end_t%60:02d}"),
        fontsize=11
    )




def plot_longest_pass_sequence(df, team_name, color, ax, bg_color, line_color, gap=10, threshold=6):
    # تصفية بيانات الفريق
    d = df[df['teamName'] == team_name].copy()

    # تحويل القيم الرقمية
    for c in ['minute','second','x','y','endX','endY']:
        d[c] = pd.to_numeric(d[c], errors='coerce')

    # ترتيب الأحداث
    d = d.sort_values(['minute','second']).reset_index(drop=True)

    # حساب الوقت بالثواني
    d['tsec'] = d['minute']*60 + d['second']

    # تحديد التمريرات الناجحة
    d['is_pass'] = (d['type'] == 'Pass') & (d['outcomeType'] == 'Successful')

    # تقسيم السلاسل بناءً على الفجوة الزمنية
    d['new_seq'] = (d['tsec'].diff().fillna(0).abs() > gap).astype(int)
    d['seq_id']  = d['new_seq'].cumsum()

    # ملخص السلاسل
    g = d.groupby('seq_id').agg(
        start=('tsec','min'),
        end=('tsec','max'),
        passes=('is_pass','sum')
    ).reset_index()

    # اختيار فقط السلاسل التي تتجاوز الحد الأدنى
    g = g[g['passes'] >= threshold].sort_values(['passes','start'], ascending=[False, True]).reset_index(drop=True)

    # إذا ما فيه سلاسل
    if g.empty:
        ax.set_title(ar_text(f"{team_name} — لا توجد سلاسل تمرير كافية"), fontsize=12)
        return

    # اختيار أطول سلسلة
    longest_id = g.iloc[0]['seq_id']
    seq = d[(d['seq_id'] == longest_id) & (d['is_pass'])].copy()

    # رسم الملعب
    pitch = VerticalPitch(pitch_type='uefa', pitch_color=bg_color, line_color=line_color, linewidth=2, pad_bottom=20)
    pitch.draw(ax=ax)

    # رسم التمريرات
    pitch.lines(seq.x, seq.y, seq.endX, seq.endY, comet=True, lw=3, color=color, ax=ax, zorder=2)
    pitch.scatter(seq.endX, seq.endY, s=50, c=bg_color, ec=color, lw=2, ax=ax, zorder=3)

    # تمييز أول تمريرة
    first = seq.iloc[0]
    pitch.scatter([first.x],[first.y], s=110, c=color, ec=line_color, lw=1.2, ax=ax, zorder=4)

    # عنوان الرسم بالعربي
    start_t, end_t = int(seq['tsec'].min()), int(seq['tsec'].max())
    ax.set_title(
        ar_text(f"{team_name}\nأطول سلسلة: {len(seq)} تمريرة\n"
                f"{start_t//60:02d}:{start_t%60:02d} → {end_t//60:02d}:{end_t%60:02d}"),
        fontsize=11
    )

def plot_pass_sequence_by_id(df_team, seq_id, team_color, ax, bg_color="#ffffff", line_color="#000000"):
    # تصفية التمريرات الناجحة في هذه السلسلة
    seq = (
        df_team[(df_team['seq_id'] == seq_id) & (df_team['is_pass'])]
        .copy()
        .sort_values('tsec')
    )
    # حذف الصفوف ذات الإحداثيات الناقصة فقط
    seq = seq.dropna(subset=['x', 'y', 'endX', 'endY'])
    if seq.empty:
        ax.set_title(ar_text("لا توجد إحداثيات صالحة لهذه السلسلة"), fontsize=11)
        return

    pitch = VerticalPitch(
        pitch_type='uefa', pitch_color=bg_color,
        line_color=line_color, linewidth=2, pad_bottom=20
    )
    pitch.draw(ax=ax)

    pitch.lines(seq.x, seq.y, seq.endX, seq.endY, comet=True, lw=3, color=team_color, ax=ax, zorder=2)
    pitch.scatter(seq.endX, seq.endY, s=50, c=bg_color, ec=team_color, lw=2, ax=ax, zorder=3)

    # أول تمريرة
    first = seq.iloc[0]
    pitch.scatter([first.x], [first.y], s=110, c=team_color, ec=line_color, lw=1.2, ax=ax, zorder=4)

    # وقت البداية والنهاية
    start_t, end_t = int(seq['tsec'].min()), int(seq['tsec'].max())
    ax.set_title(
        ar_text(f"سلسلة: {len(seq)} تمريرة\n"
                f"{start_t//60:02d}:{start_t%60:02d} → {end_t//60:02d}:{end_t%60:02d}"),
        fontsize=11
    )

# === أرقام القمصان + الرسم المحدث للسلسلة ===


def _label_positions_from_seq(seq_all: pd.DataFrame):
    """يختار نقطة تمثيلية لكل لاعب (متوسط x/y و endX/endY)، ويعيد label=jersey أو أول حرفين من الاسم."""
    pts = []
    for _, r in seq_all.iterrows():
        pid   = r.get("playerId", np.nan)
        jnum  = r.get("jerseyNumber", np.nan)
        pname = str(r.get("name","")).strip()
        if pd.notna(r.get("x")) and pd.notna(r.get("y")):
            pts.append((pid, jnum, pname, float(r["x"]),   float(r["y"])))
        if pd.notna(r.get("endX")) and pd.notna(r.get("endY")):
            pts.append((pid, jnum, pname, float(r["endX"]), float(r["endY"])))
    if not pts:
        return pd.DataFrame(columns=["playerId","label","x","y"])
    dfp = pd.DataFrame(pts, columns=["playerId","jerseyNumber","name","x","y"])
    def _lbl(g):
        j = g["jerseyNumber"].dropna()
        if len(j):
            return str(int(pd.to_numeric(j.iloc[0], errors="coerce")))
        nm = str(g["name"].iloc[0]).strip()
        return nm[:2].upper() if nm else "?"
    lab = dfp.groupby("playerId").apply(
        lambda g: pd.Series({"label": _lbl(g), "x": g["x"].mean(), "y": g["y"].mean()})
    ).reset_index()
    return lab

def plot_pass_sequence_by_id(
    df_team, seq_id, team_color, ax,
    bg_color="#ffffff", line_color="#000000",
    show_carries=True, show_end_marker=True,
    show_numbers=True
):
    """يرسم السلسلة (تمريرات ناجحة + carries اختياري) ويظهر أرقام القمصان/أسماء مختصرة للمشاركين."""
    seq_all = df_team[df_team["seq_id"] == seq_id].copy()
    if seq_all.empty:
        pitch = VerticalPitch(pitch_type="uefa", pitch_color=bg_color, line_color=line_color, linewidth=2, pad_bottom=20)
        pitch.draw(ax=ax)
        ax.set_title("لا توجد أحداث لهذه السلسلة", fontsize=11)
        return

    for c in ["minute","second","x","y","endX","endY","tsec","jerseyNumber"]:
        if c in seq_all.columns: seq_all[c] = pd.to_numeric(seq_all[c], errors="coerce")
    if "type" in seq_all.columns:        seq_all["type"] = seq_all["type"].astype(str)
    if "outcomeType" in seq_all.columns: seq_all["outcomeType"] = seq_all["outcomeType"].astype(str)
    seq_all = seq_all.sort_values("tsec")

    seq_pass  = seq_all[(seq_all["type"].str.lower()=="pass") & (seq_all["outcomeType"].str.lower()=="successful")].copy()
    seq_carry = seq_all[seq_all["type"].str.lower()=="carry"].copy() if show_carries else seq_all.iloc[0:0].copy()

    for df_ in (seq_pass, seq_carry):
        if not df_.empty: df_.dropna(subset=["x","y","endX","endY"], inplace=True)

    pitch = VerticalPitch(pitch_type="uefa", pitch_color=bg_color, line_color=line_color, linewidth=2, pad_bottom=20)
    pitch.draw(ax=ax)

    drew_any = False
    if not seq_pass.empty:
        pitch.lines(seq_pass.x, seq_pass.y, seq_pass.endX, seq_pass.endY, comet=True, lw=3, color=team_color, ax=ax, zorder=2)
        pitch.scatter(seq_pass.endX, seq_pass.endY, s=50, c=bg_color, ec=team_color, lw=2, ax=ax, zorder=3)
        drew_any = True
    if show_carries and not seq_carry.empty:
        pitch.lines(seq_carry.x, seq_carry.y, seq_carry.endX, seq_carry.endY, comet=False, lw=2.5, color=team_color,
                    ax=ax, linestyle="--", alpha=0.6, zorder=2)
        pitch.scatter(seq_carry.endX, seq_carry.endY, s=36, c=bg_color, ec=team_color, lw=1.5, ax=ax, alpha=0.6, zorder=3)
        drew_any = True
    if not drew_any:
        ax.set_title("لا توجد إحداثيات صالحة للتمريرات/الحمل في هذه السلسلة", fontsize=11)

    seq_first = pd.concat([seq_pass, seq_carry], ignore_index=True).sort_values("tsec")
    if not seq_first.empty:
        first = seq_first.iloc[0]
        pitch.scatter([first.x], [first.y], s=110, c=team_color, ec=line_color, lw=1.2, ax=ax, zorder=4)

    if show_end_marker and not seq_all.empty:
        last = seq_all.iloc[-1]
        lx, ly = last.get("endX", np.nan), last.get("endY", np.nan)
        if np.isnan(lx) or np.isnan(ly):
            lx, ly = last.get("x", np.nan), last.get("y", np.nan)
        last_type = str(last.get("type","")).lower()
        last_out  = str(last.get("outcomeType","")).lower()
        if last_type == "shot":
            marker, ms, alpha = "*", 220, 0.95
        elif last_out not in ("successful","na","") and last_type in ("pass","carry","dribble","take on"):
            marker, ms, alpha = "X", 140, 0.9
        else:
            marker, ms, alpha = "s", 90, 0.9
        if not (np.isnan(lx) or np.isnan(ly)):
            ax.scatter(lx, ly, s=ms, marker=marker, c=team_color, edgecolors=line_color, linewidths=1.3, alpha=alpha, zorder=5)
            ax.text(lx, ly, " نهاية", fontsize=9, color=line_color, ha="left", va="bottom", zorder=6)

    labels = pd.DataFrame()
    if show_numbers and ("playerId" in seq_all.columns):
        labels = _label_positions_from_seq(seq_all)
        for _, r in labels.iterrows():
            ax.scatter(r["x"], r["y"], s=210, c=bg_color, edgecolors=line_color, linewidths=1.0, zorder=6)
            ax.text(r["x"], r["y"], str(r["label"]), ha="center", va="center", fontsize=10,
                    color=team_color, fontweight="bold", zorder=7)

    if not seq_first.empty:
        start_t = int(seq_first["tsec"].min())
        end_t   = int(seq_all["tsec"].max())
        n_pass  = len(seq_pass)
        n_carry = len(seq_carry) if show_carries else 0
        ax.set_title(
            f"سلسلة: {n_pass} تمريرة" + (f" + {n_carry} Carry" if n_carry else "") +
            f"\n{start_t//60:02d}:{start_t%60:02d} → {end_t//60:02d}:{end_t%60:02d}",
            fontsize=11
        )

    try:
        fig = ax.figure
        bbox = ax.get_position()
        pass_count  = len(seq_pass)
        carry_count = len(seq_carry)
        end_str = "غير متوفر" if ('lx' not in locals() or np.isnan(lx) or np.isnan(ly)) else f"({lx:.1f}, {ly:.1f})"
        fig.text(
            x=(bbox.x0 + bbox.x1) / 2, y=bbox.y0 - 0.02,
            s=f" التمريرات: {pass_count} |  الـCarry: {carry_count} |  اللاعبين المشاركون: {len(labels) if show_numbers and not labels.empty else '—'} |  نهاية السلسلة: {end_str}",
            ha="center", va="top", fontsize=10, color="#222"
        )
    except Exception:
        pass

def extract_pass_sequences(df, team_name, gap=10, threshold=6):
    d = df[df['teamName'] == team_name].copy()
    if d.empty:
        return d.assign(tsec=np.nan, is_pass=False, seq_id=np.nan), pd.DataFrame(columns=['seq_id', 'start', 'end', 'passes'])

    # تحويل الأعمدة الرقمية
    for c in ['minute', 'second', 'x', 'y', 'endX', 'endY']:
        if c in d.columns:
            d[c] = pd.to_numeric(d[c], errors='coerce')

    d = d.sort_values(['minute', 'second']).reset_index(drop=True)

    # حساب الوقت بالثواني
    d['tsec'] = d['minute'].fillna(0) * 60 + d['second'].fillna(0)

    # تحديد التمريرات الناجحة
    d['is_pass'] = (d['type'] == 'Pass') & (d['outcomeType'] == 'Successful')

    # تحديد بداية كل سلسلة
    d['new_seq'] = (d['tsec'].diff().fillna(0).abs() > gap).astype(int)
    d['seq_id'] = d['new_seq'].cumsum()

    # تجميع السلاسل
    seqs = d.groupby('seq_id', as_index=False).agg(
        start=('tsec', 'min'),
        end=('tsec', 'max'),
        passes=('is_pass', 'sum')
    )

    # فلترة السلاسل حسب الحد الأدنى للتمريرات
    seqs = seqs[seqs['passes'] >= threshold] \
             .sort_values(['passes', 'start'], ascending=[False, True]) \
             .reset_index(drop=True)

    return d, seqs


def _count_participants(seq):
    # نحاول تغطية أشهر أسماء الأعمدة
    pairs = [
        ("playerName", "recipientName"),
        ("name", "recipientName"),
        ("player", "toPlayer"),
        ("from", "to"),
        ("passer", "recipient"),
        ("player_name", "pass_recipient_name"),
    ]
    names = set()
    for a, b in pairs:
        if a in seq.columns:
            names |= set(seq[a].dropna().astype(str).str.strip())
        if b in seq.columns:
            names |= set(seq[b].dropna().astype(str).str.strip())
    # fallback: لو ما وجدنا أعمدة مستقبل، نعتمد على الممرر فقط
    if not names and "name" in seq.columns:
        names = set(seq["name"].dropna().astype(str).str.strip())
    # إزالة الفراغات والقيم الفارغة
    names = {n for n in names if n and n.lower() != "nan"}
    return len(names)


def make_ai_comment_longest(df, team_name, gap=10, threshold=6):
    """يرجع تعليق AI نصي لأطول سلسلة تمريرات ناجحة للفريق المحدد."""
    d = df[df['teamName'] == team_name].copy()
    if d.empty:
        return f"### تحليل AI — {team_name}\n\nلا توجد بيانات لهذا الفريق."

    # تحويل القيم للأرقام
    for c in ['minute','second','x','y','endX','endY']:
        if c in d.columns:
            d[c] = pd.to_numeric(d[c], errors='coerce')

    # حساب الزمن
    d = d.sort_values(['minute','second']).reset_index(drop=True)
    d['tsec'] = d['minute'].fillna(0)*60 + d['second'].fillna(0)
    d['is_pass'] = (d['type'] == 'Pass') & (d['outcomeType'] == 'Successful')

    # تقسيم السلاسل
    d['new_seq'] = (d['tsec'].diff().fillna(0).abs() > gap).astype(int)
    d['seq_id']  = d['new_seq'].cumsum()

    # ملخص السلاسل
    g = d.groupby('seq_id', as_index=False).agg(
        start=('tsec','min'),
        end=('tsec','max'),
        passes=('is_pass','sum')
    ).sort_values(['passes','start'], ascending=[False, True])

    g = g[g['passes'] >= threshold]
    if g.empty:
        return f"### تحليل AI — {team_name}\n\nلا توجد سلسلة تتجاوز الحد الأدنى ({threshold} تمريرات)."

    # أطول سلسلة
    longest_id = int(g.iloc[0]['seq_id'])
    seq = d[(d['seq_id'] == longest_id) & (d['is_pass'])].copy().sort_values('tsec')
    if seq.empty:
        return f"### تحليل AI — {team_name}\n\nتعذر استخراج تفاصيل السلسلة."

    start_t, end_t = int(seq['tsec'].min()), int(seq['tsec'].max())
    duration = max(1, end_t - start_t)
    tempo = (len(seq) / duration) * 60

    try:
        players = _count_participants(seq)
    except:
        players = seq['name'].nunique() if 'name' in seq.columns else None

    def fmt_duration_ar(seconds):
        m, s = divmod(int(seconds), 60)
        if m and s:   return f"{m} دقيقة و {s} ثانية"
        if m:         return f"{m} دقيقة"
        return f"{s} ثانية"

    dur_str = fmt_duration_ar(duration)

    bullets = [
        f"**أطول سلسلة:** {len(seq)} تمريرة خلال {dur_str} (≈ {tempo:.1f} تمريرة/دقيقة).",
        f"**الزمن:** {start_t//60:02d}:{start_t%60:02d} → {end_t//60:02d}:{end_t%60:02d}.",
        f"**شرط الفجوة:** ≤ {gap} ثوانٍ."
    ]
    if players:
        bullets.insert(1, f"**عدد اللاعبين المشاركين:** {players}.")

    style_hint = "استحواذ منظم وبناء لعب هادئ." if tempo < 20 else "إيقاع سريع وتمريرات متعاقبة."
    bullets.append(f"**الطابع العام للسلسلة:** {style_hint}")

    return "### تحليل AI — " + team_name + "\n\n" + "\n\n".join(bullets)

# === دالة ترسم شبكة كل سلاسل الفريق ===
def plot_team_sequences_grid(df_period, team_name, team_color,
                             bg_color="#ffffff", line_color="#000000",
                             gap=10, threshold=6,
                             ncols=3, page=1, per_page=9):
    """
    ترسم شبكة ملاعب، كل ملعب يمثل سلسلة تمريرات ناجحة (≥ threshold) للفريق.
    - يدعم ترقيم الصفحات page/per_page.
    - يبقي الملعب ظاهر حتى لو ما فيه سلاسل (مع عنوان توضيحي).
    """
    # استخراج السلاسل
    df_team, seqs = extract_pass_sequences(df_period, team_name, gap=gap, threshold=threshold)

    # لو ما في سلاسل… نعرض ملعب فاضي بعنوان مبرر
    if seqs.empty:
        fig, ax = plt.subplots(figsize=(7, 9), facecolor=bg_color)
        pitch = VerticalPitch(pitch_type='uefa', pitch_color=bg_color,
                              line_color=line_color, linewidth=2, pad_bottom=20)
        pitch.draw(ax=ax)
        ax.set_title(ar_text(f"{team_name} — لا توجد سلاسل تمرير كافية (≥ {threshold} تمريرات)"), fontsize=12)
        return fig

    # ترقيم الصفحات
    total = len(seqs)
    max_page = max(1, int(np.ceil(total / per_page)))
    page = int(np.clip(page, 1, max_page))
    start = (page - 1) * per_page
    end   = min(total, start + per_page)
    show  = seqs.iloc[start:end].reset_index(drop=True)

    # شبكة
    n = len(show)
    nrows = int(np.ceil(n / ncols))
    fig, axes = plt.subplots(nrows, ncols,
                             figsize=(6*ncols, 8*nrows),
                             facecolor=bg_color,
                             constrained_layout=True)
    axes = np.array(axes).reshape(-1)

    # رسم كل سلسلة في ملعب مستقل
    for i, row in enumerate(show.itertuples(index=False)):
        ax = axes[i]
        try:
            plot_pass_sequence_by_id(df_team, int(row.seq_id), team_color, ax, bg_color, line_color)
            # توصيف مختصر تحت كل ملعب
            minutes = f"{int(row.start)//60:02d}:{int(row.start)%60:02d} → {int(row.end)//60:02d}:{int(row.end)%60:02d}"
            ax.set_xlabel(ar_text(f"{team_name} — سلسلة #{int(row.seq_id)} • {int(row.passes)} تمريرات • {minutes}"),
                          fontsize=9)
        except Exception as e:
            ax.axis("off")
            ax_text(x=0.02, y=0.95, s=f"ERR: {e}", ax=ax, highlight_textprops=[])
    # إخفاء المحاور الفارغة
    for j in range(i+1, len(axes)):
        axes[j].axis("off")

    # عنوان علوي بسيط يوضح نطاق العرض
    fig.suptitle(ar_text(f"كل السلاسل — {team_name}  (عرض {start+1}–{end} من {total})"),
                 fontsize=12, y=0.995)

    return fig

          
#  دالة تعريب النصوص
# ========= 🇦🇪 أدوات العربية =========
import arabic_reshaper
from bidi.algorithm import get_display
def ar_text(txt: str) -> str:
    return str(str(txt))



def _safe_count(d, col, value=None, contains=None):
    if col not in d.columns:
        return 0.0
    s = d[col].astype(str).str.lower()
    if value is not None:
        return (s == str(value).lower()).sum()
    if contains is not None:
        return s.str.contains(contains, regex=True).sum()
    # لو عمود عددي ونبغى مجموع قيمه
    return pd.to_numeric(d[col], errors="coerce").fillna(0).sum()

# Helpers آمنة للأعمدة الرقمية التي قد تكون غير موجودة
def _num_series(d: pd.DataFrame, key: str) -> pd.Series:
    """ترجع Series رقمية للعمود إن وُجد، وإلا Series فاضية (لتجنّب fillna على int)."""
    return pd.to_numeric(d[key], errors='coerce') if key in d.columns else pd.Series([], dtype='float64')

def _safe_sum_numeric(d: pd.DataFrame, key: str) -> float:
    """مجموع آمن لعمود رقمي (أو 0 إن لم يوجد)."""
    s = _num_series(d, key)
    if s.empty:
        return 0.0
    return float(s.fillna(0).replace([np.inf, -np.inf], 0).sum())

# ===== المقاييس =====
def _shots(d):          return _safe_count(d, 'type', value='shot') + _safe_count(d, 'type', value='savedshot') + _safe_count(d, 'type', value='missedshots') + _safe_count(d, 'type', value='shotonpost')
def _goals(d):          return _safe_count(d, 'type', value='goal')
def _passes(d):         return _safe_count(d, 'type', value='pass')
def _pass_success(d):   return _safe_count(d, 'outcomeType', value='successful') if 'outcomeType' in d.columns else 0.0
def _key_pass(d):       return _safe_count(d, 'type', value='keypass') if 'type' in d.columns else 0.0

# <-- تم التصحيح هنا
def _xa(d):             return _safe_sum_numeric(d, 'xA')
def _xt(d):             return _safe_sum_numeric(d, 'xT')

def _dribbles_won(d):   return _safe_count(d, 'outcomeType', value='won') if 'duelType' in d.columns or 'outcomeType' in d.columns else 0.0

# خذ بالك: ممكن عمود type_value_Interception ما يكون موجود
def _interceptions(d):  return _safe_count(d, 'type', value='interception') + ( _safe_sum_numeric(d, 'type_value_Interception') if 'type_value_Interception' in d.columns else 0.0 )

def _tackles(d):        return _safe_count(d, 'type', value='tackle') + ( _safe_sum_numeric(d, 'type_value_Tackle') if 'type_value_Tackle' in d.columns else 0.0 )

def _crosses(d):
    if 'type_value_Cross' in d.columns:
        return _safe_sum_numeric(d, 'type_value_Cross')
    return _safe_count(d, 'subType', contains='cross|عرضي|عرضية')

def _prog_passes(d):
    if not {'x','y'}.issubset(d.columns) or not ({'end_x','end_y'}.issubset(d.columns) or {'endX','endY'}.issubset(d.columns)):
        return 0.0
    ex = pd.to_numeric(d.get('end_x', d.get('endX')), errors='coerce')
    ey = pd.to_numeric(d.get('end_y', d.get('endY')), errors='coerce')
    x  = pd.to_numeric(d.get('x'), errors='coerce')
    y  = pd.to_numeric(d.get('y'), errors='coerce')
    is_pass = d['type'].astype(str).str.lower().eq('pass')
    return ((is_pass) & ((ex - x) >= 10)).sum()

def _prog_carries(d):
    if not {'x','y','type'}.issubset(d.columns): return 0.0
    is_carry = d['type'].astype(str).str.lower().eq('carry')
    ex = pd.to_numeric(d.get('end_x', d.get('endX')), errors='coerce')
    x  = pd.to_numeric(d.get('x'), errors='coerce')
    return ((is_carry) & ((ex - x) >= 8)).sum()

def _box_receives(d):
    ex = pd.to_numeric(d.get('end_x', d.get('endX')), errors='coerce')
    ey = pd.to_numeric(d.get('end_y', d.get('endY')), errors='coerce')
    if ex.isna().all():
        return 0.0
    return ((ex > 88) & (ey.between(14, 54))).sum()

def _box_passes(d):
    if 'type' not in d.columns: return 0.0
    ex = pd.to_numeric(d.get('end_x', d.get('endX')), errors='coerce')
    ey = pd.to_numeric(d.get('end_y', d.get('endY')), errors='coerce')
    is_pass = d['type'].astype(str).str.lower().eq('pass')
    return (is_pass & (ex > 88) & (ey.between(14, 54))).sum()
# =========  مقاييس دفاعية إضافية (آمنة) =========

def _tackles_won(d):
    if not {'type','outcomeType'}.issubset(d.columns): return 0.0
    t = d['type'].astype(str).str.lower().eq('tackle')
    ok = d['outcomeType'].astype(str).str.lower().eq('successful')
    return (t & ok).sum()

def _tackles_lost(d):
    if not {'type','outcomeType'}.issubset(d.columns): return 0.0
    t = d['type'].astype(str).str.lower().eq('tackle')
    bad = d['outcomeType'].astype(str).str.lower().eq('unsuccessful')
    return (t & bad).sum()

def _ball_recoveries(d):
    # دعم عمود عددي إن وُجد
    if 'type_value_BallRecovery' in d.columns:
        return _safe_sum_numeric(d, 'type_value_BallRecovery')
    return _safe_count(d, 'type', value='ballrecovery')

def _clearances(d):
    if 'type_value_Clearance' in d.columns:
        return _safe_sum_numeric(d, 'type_value_Clearance')
    return _safe_count(d, 'type', value='clearance')

def _blocked_shots(d):
    # أحيانًا تكون BlockedShot أو ShotBlocked
    return (_safe_count(d, 'type', value='blockedshot')
            + _safe_count(d, 'type', value='shotblocked'))

def _blocked_passes(d):
    if 'type_value_BlockedPass' in d.columns:
        return _safe_sum_numeric(d, 'type_value_BlockedPass')
    return _safe_count(d, 'type', value='blockedpass')

def _aerials_won(d):
    if not {'type','outcomeType'}.issubset(d.columns): return 0.0
    a = d['type'].astype(str).str.lower().eq('aerial')
    ok = d['outcomeType'].astype(str).str.lower().eq('successful')
    return (a & ok).sum()

def _aerials_lost(d):
    if not {'type','outcomeType'}.issubset(d.columns): return 0.0
    a = d['type'].astype(str).str.lower().eq('aerial')
    bad = d['outcomeType'].astype(str).str.lower().eq('unsuccessful')
    return (a & bad).sum()

def _aerials_total(d):
    if 'type' not in d.columns: return 0.0
    return d['type'].astype(str).str.lower().eq('aerial').sum()

def _defensive_duel_won(d):
    # بعض المنصات تسميها Challenge
    if not {'type','outcomeType'}.issubset(d.columns): return 0.0
    ch = d['type'].astype(str).str.lower().eq('challenge')
    ok = d['outcomeType'].astype(str).str.lower().eq('successful')
    return (ch & ok).sum()

def _pressures(d):
    # إذا لم يوجد عمود Pressure نبحث نصيًا
    if 'type' in d.columns:
        return d['type'].astype(str).str.lower().eq('pressure').sum()
    return _safe_count(d, 'action', contains='pressure|ضغط')

def _fouls_committed(d):
    return (_safe_count(d, 'type', value='foul')
            + _safe_count(d, 'subType', contains='foul|خطأ'))

def _errors_to_shot_or_goal(d):
    # يدعم أعمدة رقمية إن وُجدت
    for col in ['type_value_Error','error_to_shot','error_to_goal']:
        if col in d.columns:
            return _safe_sum_numeric(d, col)
    return _safe_count(d, 'subType', contains='error|خطأ')

def _long_pass_success(d):
    # تمريرات >30م ناجحة
    if not {'x'}.issubset(d.columns): return 0.0
    ex = pd.to_numeric(d.get('end_x', d.get('endX')), errors='coerce')
    ey = pd.to_numeric(d.get('end_y', d.get('endY')), errors='coerce')
    x  = pd.to_numeric(d.get('x'), errors='coerce')
    y  = pd.to_numeric(d.get('y'), errors='coerce')
    if ex.isna().all() or x.isna().all(): return 0.0
    length = np.hypot(ex - x, ey - y)
    is_pass = d['type'].astype(str).str.lower().eq('pass') if 'type' in d.columns else False
    ok = d.get('outcomeType', '').astype(str).str.lower().eq('successful') if 'outcomeType' in d.columns else True
    return (is_pass & ok & (length >= 30)).sum()

METRIC_MAP = {
    #  المقاييس الهجومية
    "تمريرات":                 _passes,
    "تمريرات ناجحة":           _pass_success,
    "تمريرات مفتاحية":         _key_pass,
    "الكرات العرضية":          _crosses,
    "xA صناعة":                _xa,
    "xT إجمالي":               _xt,
    "تمريرات تقدمية":          _prog_passes,
    "حملات تقدمية":            _prog_carries,
    "مراوغات ناجحة":           _dribbles_won,
    "تسديدات":                 _shots,
    "أهداف":                   _goals,
    "استلامات في منطقة الجزاء": _box_receives,
    "تمريرات داخل الصندوق":     _box_passes,

    #  المقاييس الدفاعية
    "اعتراضات":                _interceptions,
    "استخلاص كرات":            _tackles,
    "افتكاكات ناجحة":          _tackles_won,
    "افتكاكات غير ناجحة":      _tackles_lost,
    "استرجاع كرات":            _ball_recoveries,
    "تشتيت/إبعاد":             _clearances,
    "اعتراض تسديدة":           _blocked_shots,
    "اعتراض تمريرة (بلوك)":     _blocked_passes,
    "الكرات الهوائية (فوز)":    _aerials_won,
    "الكرات الهوائية (خسارة)":  _aerials_lost,
    "الكرات الهوائية (إجمالي)": _aerials_total,
    "التحامات دفاعية ناجحة":    _defensive_duel_won,
    "ضغط على حامل الكرة":       _pressures,
    "أخطاء مُرتكبة":            _fouls_committed,
    "تمريرات طويلة ناجحة":      _long_pass_success,
}


# =========  استخراج قيَم لاعب =========
def compute_player_metrics(df_team: pd.DataFrame, player_name: str, metric_names: list[str]) -> dict:
    d = df_team[df_team['name'] == player_name].copy()
    out = {}
    for m in metric_names:
        func = METRIC_MAP.get(m)
        out[m] = float(func(d)) if func else 0.0
    return out

# =========  رسم الرادار (عربي) =========
import matplotlib.pyplot as plt
def plot_radar_ar(p1_vals: dict, p2_vals: dict, player1: str, player2: str,
                  normalize: str = "pair", team_df: pd.DataFrame | None = None,
                  title: str = "مقارنة لاعبين"):

    labels = list(p1_vals.keys())
    v1 = np.array([p1_vals[l] for l in labels], dtype=float)
    v2 = np.array([p2_vals[l] for l in labels], dtype=float)

    # تطبيع (pair أو team أو none)
    if normalize in ("pair", "team"):
        mins, maxs = [], []
        for m in labels:
            if normalize == "pair":
                arr = np.array([p1_vals[m], p2_vals[m]], dtype=float)
            else:
                # كل لاعبي نفس الفريق
                arr = []
                for pl in team_df['name'].dropna().unique():
                    arr.append(METRIC_MAP[m](team_df[team_df['name'] == pl]))
                arr = np.array(arr, dtype=float) if len(arr) else np.array([0,1], dtype=float)
            mins.append(arr.min())
            maxs.append(arr.max() if arr.max() > arr.min() else arr.min()+1e-9)
        mins = np.array(mins); maxs = np.array(maxs)
        v1 = (v1 - mins) / (maxs - mins)
        v2 = (v2 - mins) / (maxs - mins)

    # إغلاق الدائرة
    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]
    v1 = np.concatenate([v1, [v1[0]]])
    v2 = np.concatenate([v2, [v2[0]]])

    fig = plt.figure(figsize=(7.5, 7.5))
    ax = plt.subplot(111, polar=True)
    ax.set_facecolor("#0e1117")
    fig.patch.set_facecolor("#0e1117")

    # محاور وعناوين
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_rlabel_position(0)
    ax.tick_params(colors="white")
    ax.spines["polar"].set_color("#c7d5cc")
    ax.set_title(ar_text(title), color="white", pad=20, fontsize=16, fontweight="bold")

    # تسميات المحاور بالعربي (مع تصحيح اتجاه)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels([ar_text(t) for t in labels], color="white", fontsize=11)

    # رسومات
    ax.plot(angles, v1, linewidth=2, label=player1)
    ax.fill(angles, v1, alpha=0.25)
    ax.plot(angles, v2, linewidth=2, label=player2)
    ax.fill(angles, v2, alpha=0.25)

    lg = ax.legend(loc="upper right", bbox_to_anchor=(1.15, 1.15), facecolor="#0e1117", labelcolor="white")
    for txt in lg.get_texts(): txt.set_color("white")
    return fig

# =========  دالة عليا: رادار مقارنة كما هي =========
def draw_players_radar(df_match, team_name, p1, p2, metrics, normalize="pair"):
    # تحضير إطار بيانات الفريق
    team_df = df_match[df_match['teamName'] == team_name].copy()
    team_df['name'] = team_df['name'].astype(str)

    # احسب القيم الخام للاعبين
    p1_vals = compute_player_metrics(team_df, p1, metrics)
    p2_vals = compute_player_metrics(team_df, p2, metrics)

    # دالة مساعدة تبني Series آمنة لكل مقياس من جميع لاعبي الفريق
    def team_series_for_metric(metric):
        players = team_df['name'].dropna().unique().tolist()
        vals = []
        for pl in players:
            v = compute_player_metrics(team_df, pl, [metric]).get(metric, 0.0)
            # ضمان رقم float
            try:
                v = float(v)
            except:
                v = 0.0
            vals.append(v)
        s = pd.Series(vals, index=players, dtype='float64')
        s = s.fillna(0.0).replace([np.inf, -np.inf], 0.0)
        return s

    # طَبّع القيم حسب الاختيار
    p1_norm, p2_norm = [], []
    for m in metrics:
        v1 = float(p1_vals.get(m, 0.0) or 0.0)
        v2 = float(p2_vals.get(m, 0.0) or 0.0)

        if normalize == "team":
            s = team_series_for_metric(m)
            max_v = float(s.max()) if len(s) else 0.0
            if max_v > 0:
                p1_norm.append(v1 / max_v)
                p2_norm.append(v2 / max_v)
            else:
                p1_norm.append(0.0); p2_norm.append(0.0)

        elif normalize == "pair":
            denom = max(v1, v2)
            if denom > 0:
                p1_norm.append(v1 / denom)
                p2_norm.append(v2 / denom)
            else:
                p1_norm.append(0.0); p2_norm.append(0.0)

        else:  # "none"
            # مقياس مباشر (قد يختلف كبيراً بين المقاييس)
            p1_norm.append(v1)
            p2_norm.append(v2)

    # ——— رسم الرادار ———
    # تجهيز الزوايا
    labels = metrics
    N = len(labels)
    angles = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
    p1_plot = p1_norm + [p1_norm[0]]
    p2_plot = p2_norm + [p2_norm[0]]
    angles_plot = angles + [angles[0]]

    fig = plt.figure(figsize=(7, 7))
    ax = plt.subplot(111, polar=True)
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    ax.set_thetagrids(np.degrees(angles), labels, fontsize=10)

    # حد تلقائي للمحور عند التطبيع
    if normalize in ("team", "pair"):
        ax.set_ylim(0, 1)

    ax.plot(angles_plot, p1_plot, linewidth=2, linestyle='-', label=p1)
    ax.fill(angles_plot, p1_plot, alpha=0.20)
    ax.plot(angles_plot, p2_plot, linewidth=2, linestyle='-', label=p2)
    ax.fill(angles_plot, p2_plot, alpha=0.20)

    ax.grid(True, linestyle='--', alpha=0.4)
    ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
    title_txt = f"رادار مقارنة لاعبين — {team_name}"
    ax.set_title(title_txt, fontsize=13, pad=20)
    return fig

from highlight_text import ax_text 
    #  اختيار نوع التحليل العام
st.markdown("### اختر نوع التحليل")
analysis_type = st.radio(
    "حدد القسم",
    options=["تحليل الفريق", "تحليل لاعب", "إحصائيات المباراة", "أفضل اللاعبين", "أطول سلسلة تمريرات ناجحة"],
    horizontal=True
)

if analysis_type == "أطول سلسلة تمريرات ناجحة":
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from mplsoccer import VerticalPitch

    st.markdown("### أطول سلسلة تمريرات ناجحة لكل فريق")

    df_src = st.session_state.get('df_match', df_match)
    if df_src is None or df_src.empty:
        st.warning("لا توجد بيانات مباراة محمّلة بعد.")
        st.stop()

    df_long = df_src.copy()

    # إعدادات التحكم
    gap = st.slider("⏱ الفجوة الزمنية بين الأحداث (ثواني)", 5, 20, 10, 1)
    threshold = st.slider("الحد الأدنى لعدد التمريرات في السلسلة", 3, 20, 6, 1)

    # تنظيف أعمدة شائعة
    for c in ['teamName','type','outcomeType','minute','second','x','y','endX','endY']:
        if c in df_long.columns:
            if c in ['minute','second','x','y','endX','endY']:
                df_long[c] = pd.to_numeric(df_long[c], errors='coerce')
            else:
                df_long[c] = df_long[c].astype(str).str.strip()

    # اختيار الفترة
    time_mode = st.radio("اختر الفترة الزمنية",
                         ["كامل المباراة", "الشوط الأول", "الشوط الثاني", "فترة مخصصة"],
                         horizontal=True)
    start_min, end_min = 0, 90
    if time_mode == "الشوط الأول":
        end_min = 45
    elif time_mode == "الشوط الثاني":
        start_min = 45
    elif time_mode == "فترة مخصصة":
        c1, c2 = st.columns(2)
        start_min = c1.number_input("بداية الفترة (دقيقة)", 0, 90, 0)
        end_min   = c2.number_input("نهاية الفترة (دقيقة)", 0, 90, 45)

    df_period = df_long[(df_long['minute'] >= start_min) & (df_long['minute'] < end_min)].copy()
    if df_period.empty:
        st.info("لا توجد أحداث في الفترة المختارة.")
        st.stop()

    with st.expander("ألوان العرض", expanded=False):
        home_color = st.color_picker("لون الفريق المستضيف", '#0099ff')
        away_color = st.color_picker("لون الفريق الضيف",   '#ff4d4d')

    def longest_success_chain(df_team, gap_sec=10, min_len=6):
        d = df_team.sort_values(['minute','second']).copy()
        d['t'] = d['minute']*60 + d['second'].fillna(0)
        d = d[(d['type'] == 'Pass') & (d['outcomeType'] == 'Successful')].copy()
        if d.empty: 
            return None
        chains, cur = [], [d.iloc[0]]
        for i in range(1, len(d)):
            if (d.iloc[i]['t'] - d.iloc[i-1]['t']) <= gap_sec:
                cur.append(d.iloc[i])
            else:
                chains.append(pd.DataFrame(cur))
                cur = [d.iloc[i]]
        if cur: chains.append(pd.DataFrame(cur))
        chains = [c for c in chains if len(c) >= min_len]
        if not chains:
            return None
        chains.sort(key=len, reverse=True)
        return chains[0]

    def plot_chain(chain_df, color):
        pitch = VerticalPitch(pitch_type='opta', line_zorder=2)
        fig, ax = pitch.draw(figsize=(7, 10))
        # لا نص عربي داخل الشكل — فقط الأسهم
        for _, r in chain_df.iterrows():
            if pd.notna(r['x']) and pd.notna(r['y']) and pd.notna(r['endX']) and pd.notna(r['endY']):
                pitch.arrows(r['x'], r['y'], r['endX'], r['endY'],
                             ax=ax, width=2, headwidth=8, headaxislength=8,
                             zorder=3, alpha=0.9, color=color)
        return fig

    teams = df_period['teamName'].dropna().unique().tolist()
    colA, colB = st.columns(2)

    if teams:
        team_home = teams[0]
        chain_home = longest_success_chain(df_period[df_period['teamName'] == team_home], gap, threshold)
        with colA:
            if chain_home is None:
                st.markdown(f"**{team_home}**")
                st.info("لا توجد سلسلة تحقق الشرط.")
            else:
                n_home = len(chain_home)
                st.markdown(f"**{team_home} — أطول سلسلة تمريرات ناجحة: {n_home} تمريرة**")
                fig_home = plot_chain(chain_home, home_color)
                st.pyplot(fig_home, use_container_width=True)

    if len(teams) > 1:
        team_away = teams[1]
        chain_away = longest_success_chain(df_period[df_period['teamName'] == team_away], gap, threshold)
        with colB:
            if chain_away is None:
                st.markdown(f"**{team_away}**")
                st.info("لا توجد سلسلة تحقق الشرط.")
            else:
                n_away = len(chain_away)
                st.markdown(f"**{team_away} — أطول سلسلة تمريرات ناجحة: {n_away} تمريرة**")
                fig_away = plot_chain(chain_away, away_color)
                st.pyplot(fig_away, use_container_width=True)


    
    # ====== نهاية الدوال المساعدة ======

    # اختيار وضع العرض
  


if analysis_type == "أفضل اللاعبين":
    st.markdown("### 👥 اختر اللاعبين لتحليل الأداء")

    #  اختيار ألوان الفريقين
    with st.expander(" ألوان الفريقين", expanded=True):
        col1 = st.color_picker(" لون الفريق المستضيف", '#0099ff', key="top_color1")
        col2 = st.color_picker(" لون الفريق الضيف", '#ff4d4d', key="top_color2")
        line_color = st.color_picker(" لون النصوص والخطوط", "#000000", key="top_line_color")
        bg_color = st.color_picker(" لون الخلفية", "#ffffff", key="top_bg_color")

    # 👥 أسماء اللاعبين
    hpnames = homedf['name'].dropna().unique()
    apnames = awaydf['name'].dropna().unique()

    home_unique_players = homedf['name'].unique()
    away_unique_players = awaydf['name'].unique()

    #  اختيار الحراس
    if 'position' in homedf.columns and 'position' in awaydf.columns:
        home_goalkeepers = homedf[homedf['position'] == 'Goalkeeper']['name'].dropna().unique().tolist()
        away_goalkeepers = awaydf[awaydf['position'] == 'Goalkeeper']['name'].dropna().unique().tolist()
    else:
        st.warning(" لا يوجد عمود 'position' لتحديد الحراس، سيتم عرض جميع اللاعبين للاختيار.")
        home_goalkeepers = homedf['name'].dropna().unique().tolist()
        away_goalkeepers = awaydf['name'].dropna().unique().tolist()


    st.markdown("<h5 style='text-align: center;'> اختر حارس الفريق المستضيف</h5>", unsafe_allow_html=True)
    homeGK = st.selectbox("", home_goalkeepers, key="homeGK", index=None, on_change=reset_confirmed)

    st.markdown("<h5 style='text-align: center;'> اختر حارس الفريق الضيف</h5>", unsafe_allow_html=True)
    awayGK = st.selectbox("", away_goalkeepers, key="awayGK", index=None, on_change=reset_confirmed)


    st.markdown("<h5 style='text-align: center;'>اختر مهاجم الفريق المستضيف</h5>", unsafe_allow_html=True)
    home_Forward = st.selectbox("", hpnames, key='home_fwd', index=None, on_change=reset_confirmed)

    st.markdown("<h5 style='text-align: center;'>اختر مهاجم الفريق الضيف</h5>", unsafe_allow_html=True)
    away_Forward = st.selectbox("", apnames, key='away_fwd', index=None, on_change=reset_confirmed)

    league_name = st.text_area(" أدخل اسم البطولة", key='league_name', on_change=reset_confirmed)
    confirm = st.button(" تأكيد المدخلات")

    if confirm:
            st.session_state.confirmed = True

    if st.session_state.get('confirmed', False):
            #  تجهيز البيانات
            df_match = df_match.sort_values(by=['teamName', 'minute', 'second']).reset_index(drop=True)

            #  إنشاء عمود مستقبل التمريرة
            df_match['pass_receiver'] = (
                df_match[df_match['type'] == 'Pass']
                .groupby('teamName')['name']
                .shift(-1)
            )
            df_match['pass_receiver'] = df_match['pass_receiver'].fillna('No')

            #  اختصارات الأسماء
            def get_short_name(full_name):
                if pd.isna(full_name): return full_name
                parts = full_name.split()
                if len(parts) == 1: return full_name
                elif len(parts) == 2: return parts[0][0] + ". " + parts[1]
                else: return parts[0][0] + ". " + parts[1][0] + ". " + " ".join(parts[2:])
            df_match['shortName'] = df_match['name'].apply(get_short_name)

            #  توليد رسم أفضل اللاعبين
            
            fig, axs = plt.subplots(4, 3, figsize=(35, 35), facecolor=bg_color,
                        gridspec_kw={'wspace': 0.2, 'hspace': 0.2})
            

            
            
            
            home_player_passmap(axs[0, 0])
            passer_bar(axs[0, 1])
            away_player_passmap(axs[0, 2])
            home_passes_recieved(axs[1, 0])
            sh_sq_bar(axs[1, 1])
            away_passes_recieved(axs[1, 2])
            home_player_def_acts(axs[2, 0])
            defender_bar(axs[2, 1])
            away_player_def_acts(axs[2, 2])
            home_gk(axs[3, 0])
            threat_creators(axs[3, 1])
            away_gk(axs[3, 2])
            from highlight_text import fig_text


            #  النصوص النهائية
            highlight_text = [{'color': col1}, {'color': col2}]
            fig_text(0.5, 0.97, f"<{hteamName} {hgoal_count}> - <{agoal_count} {ateamName}>", 
                     color=line_color, fontsize=30, fontweight='bold',
                     highlight_textprops=highlight_text, ha='center', va='center', ax=fig)

            fig.text(0.5, 0.95, f"{league_name} |  Top Players of the Match", color=line_color, fontsize=30, ha='center', va='center')
            fig.text(0.5, 0.93, f"Data from: Opta  |  made by: @Turadi_7", color=line_color, fontsize=22.5, ha='center', va='center')
            fig.text(0.125,0.097, 'Attacking Direction ------->', color=col1, fontsize=25, ha='left', va='center')
            fig.text(0.9,0.097, '<------- Attacking Direction', color=col2, fontsize=25, ha='right', va='center')
        
            st.write('Top Players of the Match')
            st.pyplot(fig)

            #  تحليل لاعب معين بعد عرض أفضل اللاعبين
            st.markdown("###  تحليل تفصيلي للاعب من المباراة")

# جمع أسماء اللاعبين المشاركين في المباراة من الفريقين
            all_players = df_match[df_match['teamName'].isin([hteamName, ateamName])]['name'].dropna().unique().tolist()

# اختيار لاعب
            selected_player = st.selectbox("اختر اللاعب لتحليله", all_players, key="selected_top_player")

# عرض التحليل إذا تم اختيار لاعب
            if selected_player:
               generate_player_dahsboard(selected_player, hteamName, hgoal_count, ateamName, agoal_count)

      

import matplotlib.pyplot as plt  # إذا ما كان مستورد فوق

df_match = st.session_state.get('df_match')
hteam = st.session_state.get('hteam')
ateam = st.session_state.get('ateam')

if df_match is None or hteam is None or ateam is None:
    st.warning(" اختر البطولة ← الجولة ← المباراة أولًا، ثم ارجع لقسم التحليلات.")
    st.stop()

if analysis_type == "تحليل الفريق":
    st.markdown("#### اختر نوع تحليل الفريق")

    team_analysis_type = st.selectbox(
    "نوع تحليل الفريق",
    options=[
        "شبكة التمريرات",
        "مصفوفة التمريرات",
        "KMeans",
        "خريطة الكثافة",
        "xT لأفضل اللاعبين",
        "Pass Sonar",
        "Field Tilt",
        "توزيع اللعب عبر أثلاث الملعب"
    ],
    key="team_analysis_type"
)

    selected_team_analysis = st.selectbox(
        "اختر الفريق",
        [hteam, ateam],
        key="selected_team_analysis"
    )
    opponent_team = hteam if selected_team_analysis == ateam else ateam

    # ألوان أساسية للفريقين
    home_color = st.color_picker("لون الفريق المستضيف", "#0099ff", key="home_color")
    away_color = st.color_picker("لون الفريق الضيف", "#ff4d4d", key="away_color")

    # ألوان عامة
    matrix_color_low  = st.color_picker("لون مصفوفة التمريرات (قيمة منخفضة)", "#b5ffe1", key="matrix_low")
    matrix_color_high = st.color_picker("لون مصفوفة التمريرات (قيمة مرتفعة)", "#ff8fab", key="matrix_high")
    line_color        = st.color_picker("لون خطوط التمرير العادية", "#808080", key="line_color")
    highlight_color   = st.color_picker("لون خطوط التمرير المميزة", "#ff0000", key="highlight_color")
    node_edge_color   = st.color_picker("لون حواف دوائر اللاعبين", "#00ccff", key="node_edge_color")

    # =========================
    # شبكة التمريرات
    # =========================
    if team_analysis_type == "شبكة التمريرات":
        try:
            fig_net, ai_net_comment = draw_static_passing_network(
                df_match,
                selected_team_analysis,
                opponent_team,
                bg_color="#ffffff",
                line_color=line_color,
                highlight_color=highlight_color,
                node_edge_color=node_edge_color
            )
            st.pyplot(fig_net, use_container_width=True)
            if ai_net_comment:
                st.markdown(ai_net_comment)
        except Exception as e:
            st.error(f"خطأ في رسم شبكة التمريرات: {e}")

    # =========================
    # مصفوفة التمريرات
    # =========================
    elif team_analysis_type == "مصفوفة التمريرات":
        try:
            fig_matrix, ai_matrix_comment = draw_pass_matrix_arabic(
                df_match,
                selected_team_analysis,
                color_low=matrix_color_low,
                color_high=matrix_color_high
            )
            st.pyplot(fig_matrix, use_container_width=True)
            if ai_matrix_comment:
                st.markdown(ai_matrix_comment)
        except Exception as e:
            st.error(f"خطأ في مصفوفة التمريرات: {e}")

    # =========================
    # KMeans
    # =========================
    elif team_analysis_type == "KMeans":
        try:
            fig_kmeans = draw_kmeans_pass_clusters_single_team(df_match, selected_team_analysis)
            st.pyplot(fig_kmeans, use_container_width=True)
            st.markdown(f"تم تحديد 6 تجمعات لتمريرات فريق **{selected_team_analysis}**.")
        except Exception as e:
            st.error(f"خطأ في KMeans: {e}")

        st.markdown(
            """
<div dir="rtl" style="text-align: right;">
<h3>ما هو تحليل KMeans في كرة القدم؟</h3>
<p>تحليل <b>KMeans</b> يُقسّم التمريرات إلى تجمعات حسب التشابه في البداية/النهاية والاتجاه، لإبراز أنماط اللعب.</p>
</div>
""",
            unsafe_allow_html=True,
        )

    # =========================
    # Field Tilt
    # =========================
    elif team_analysis_type == "Field Tilt":
        try:
            fig_ft, stats = draw_field_tilt_both_teams(
                df_match,
                hteam,
                ateam,
                team_col="teamName",
                home_color=home_color,
                away_color=away_color,
            )
            st.pyplot(fig_ft, use_container_width=True)
            st.caption(f"Final-third counts — {hteam}: {stats['home_count']} | {ateam}: {stats['away_count']}")
        except Exception as e:
            st.error(f"خطأ في Field Tilt: {e}")

    # =========================
    # خريطة الكثافة
    # =========================
    elif team_analysis_type == "خريطة الكثافة":
        show_both = st.toggle("عرض بداية التمريرات للفريقين معًا", value=False, key="density_show_both")

        if show_both:
            try:
                fig_density = draw_pass_start_density_both_teams(
                    df_match,
                    hteam,
                    ateam,
                    home_color=home_color,
                    away_color=away_color,
                )
                st.pyplot(fig_density, use_container_width=True)
            except Exception as e:
                st.error(f"خطأ في خريطة الكثافة (الفريقين): {e}")
        else:
            team_color = home_color if selected_team_analysis == hteam else away_color
            try:
                fig_density = draw_pass_start_density_map(
                    df_match,
                    selected_team_analysis,
                    color=team_color,
                )
                st.pyplot(fig_density, use_container_width=True)
            except Exception as e:
                st.error(f"خطأ في خريطة الكثافة (فريق واحد): {e}")

    # =========================
    # xT لأفضل اللاعبين
    # =========================
    elif team_analysis_type == "xT لأفضل اللاعبين":
        xt_color = st.color_picker("لون xT", "#0099ff", key="xt_color")
        try:
            fig_xt = draw_xt_heatmaps_top_players(
                df_match,
                selected_team_analysis,
                base_color=xt_color,
            )
            st.pyplot(fig_xt, use_container_width=True)
        except Exception as e:
            st.error(f"خطأ في xT: {e}")

        st.markdown(
            """
<div dir="rtl" style="text-align: right;">
<ul>
<li>أكثر 6 لاعبين من حيث مجموع xT.</li>
<li>تلوين الكثافة حسب مواقع التهديد.</li>
<li>إبراز مساهمة كل لاعب في الخطورة الهجومية.</li>
</ul>
</div>
""",
            unsafe_allow_html=True,
        )

    # =========================
    # Pass Sonar
    # =========================
    elif team_analysis_type == "Pass Sonar":
        st.markdown("### Pass Sonar")

        team_for_sonar = st.radio("اختر الفريق", [hteam, ateam], horizontal=True, key="sonar_team")
        base_color = home_color if team_for_sonar == hteam else away_color

        use_starting = st.checkbox("تحديد تشكيلة يدوياً", value=False, key="sonar_use_starting")
        startingXI = None
        if use_starting:
            team_players = sorted(
                df_match[df_match["teamName"] == team_for_sonar]["name"].dropna().unique().tolist()
            )
            startingXI = st.multiselect("اختر اللاعبين", team_players, key="sonar_startingXI")

        try:
            fig = draw_pass_sonar(
                df_match,
                team_for_sonar,
                base_color=base_color,
                startingXI=startingXI,
            )
            st.pyplot(fig, use_container_width=True)

            st.markdown(
                """
<div dir="rtl" style="text-align: right;">
<p>سونار التمريرات يوضّح اتجاه وعدد وكثافة تمريرات كل لاعب عبر قطاعات زاوية.</p>
</div>
""",
                unsafe_allow_html=True,
            )
        except Exception as e:
            st.error(f"خطأ في رسم Pass Sonar: {e}")
            with st.expander("Debug"):
                st.write("columns:", sorted(df_match.columns.tolist()))
                st.write(df_match.head())

    # =========================
    # توزيع اللعب عبر أثلاث الملعب
    # =========================
    elif team_analysis_type.strip() in ("توزيع اللعب عبر أثلاث الملعب", "أثلاث الملعب"):
        import numpy as np
        import matplotlib.pyplot as plt
        from matplotlib.patches import Rectangle, Circle
        import matplotlib.colors as mc

        # تدرجات لونية (دفاع ← وسط ← هجوم)
        def three_shades(base_hex: str):
            r, g, b = mc.to_rgb(base_hex)
            def blend(t: float):
                return mc.to_hex((1 - (1 - r) * t, 1 - (1 - g) * t, 1 - (1 - b) * t))
            return blend(0.65), blend(0.80), blend(1.00)

        # رسم ملعب + التظليل + السهم
        def draw_team_thirds_with_direction(ax, team_name, thirds_data,
                                            color_def, color_mid, color_att,
                                            attack_right: bool = True):
            # تحويل النِّسب إلى أعداد صحيحة مجموعها 100
            keys = ["Def", "Mid", "Att"]
            vals = np.array([float(thirds_data.get(k, 0)) for k in keys], dtype=float)
            total = vals.sum()
            if total <= 0:
                Ndef, Nmid, Natt = 0, 0, 0
            else:
                raw = vals * (100.0 / total) if total != 100 else vals
                base = np.floor(raw).astype(int)
                remain = 100 - base.sum()
                if remain > 0:
                    idx = np.argsort(-(raw - base))[:remain]
                    base[idx] += 1
                Ndef, Nmid, Natt = base.tolist()

            z_shade, z_pitch, z_text = 0, 3, 4
            L, W = 120, 80

            # التظليل
            if attack_right:
                shades = [(0, color_def), (40, color_mid), (80, color_att)]
                txts   = [(20, Ndef), (60, Nmid), (100, Natt)]
            else:
                shades = [(0, color_att), (40, color_mid), (80, color_def)]
                txts   = [(20, Natt), (60, Nmid), (100, Ndef)]
            for x, c in shades:
                ax.add_patch(
                    Rectangle((x, 0), 40, W, facecolor=c, alpha=0.55, edgecolor="none", zorder=z_shade)
                )

            # خطوط الملعب
            ax.add_patch(Rectangle((0, 0), L, W, fill=False, linewidth=2, zorder=z_pitch))
            ax.plot([L / 2, L / 2], [0, W], color="black", linewidth=2, zorder=z_pitch)
            ax.add_patch(Rectangle((0, (W / 2) - 18), 18, 36, fill=False, linewidth=2, zorder=z_pitch))
            ax.add_patch(Rectangle((L - 18, (W / 2) - 18), 18, 36, fill=False, linewidth=2, zorder=z_pitch))
            ax.add_patch(Rectangle((0, (W / 2) - 6), 6, 12, fill=False, linewidth=2, zorder=z_pitch))
            ax.add_patch(Rectangle((L - 6, (W / 2) - 6), 6, 12, fill=False, linewidth=2, zorder=z_pitch))
            ax.add_patch(Rectangle((-2, (W / 2) - 2), 2, 4, fill=False, linewidth=2, zorder=z_pitch))
            ax.add_patch(Rectangle((L, (W / 2) - 2), 2, 4, fill=False, linewidth=2, zorder=z_pitch))
            ax.add_patch(Circle((L / 2, W / 2), 10, fill=False, linewidth=2, zorder=z_pitch))
            ax.plot(L / 2, W / 2, "o", color="black", zorder=z_pitch)

            # النِّسب
            for x, v in txts:
                ax.text(x, W / 2, f"{int(v)}%", ha="center", va="center",
                        fontsize=22, weight="bold", zorder=z_text)

            # سهم اتجاه اللعب
            if attack_right:
                ax.annotate(
                    "", xy=(110, 75), xytext=(90, 75),
                    arrowprops=dict(arrowstyle="-|>", lw=2.0, color=color_att),
                    zorder=z_text,
                )
                ax.text(100, 77, "اتجاه لعب →", ha="center", va="bottom",
                        fontsize=11, color=color_att, zorder=z_text)
            else:
                ax.annotate(
                    "", xy=(10, 75), xytext=(30, 75),
                    arrowprops=dict(arrowstyle="-|>", lw=2.0, color=color_att),
                    zorder=z_text,
                )
                ax.text(20, 77, "← اتجاه لعب", ha="center", va="bottom",
                        fontsize=11, color=color_att, zorder=z_text)

            ax.set_title(str(team_name), fontsize=14)
            ax.set_aspect("equal")
            ax.axis("off")

        # خيار مواجهة الفريقين
        face_opt = st.toggle("جعل الفريقين متقابلين", value=True, key="thirds_face_each_other")

        try:
            # اختيار عمود X
            X = "endX" if "endX" in df_match.columns else "x"
            df_tmp = df_match.copy()
            df_tmp[X] = pd.to_numeric(df_tmp[X], errors="coerce")

            # تصفية أنواع الأحداث
            use_types = ["Pass", "Carry", "Dribble", "BallRecovery", "Shot", "Cross", "TakeOn"]
            if "type" in df_tmp.columns:
                df_tmp = df_tmp[df_tmp["type"].astype(str).isin(use_types)]
            if "teamName" not in df_tmp.columns:
                st.warning("الملف يفتقد عمود teamName.")
                st.stop()

            d = df_tmp[["teamName", X]].dropna()
            if d.empty:
                st.warning("لا توجد بيانات كافية لحساب أثلاث الملعب.")
            else:
                max_x = float(d[X].max())
                left_third  = max_x / 3.0
                right_third = 2.0 * max_x / 3.0

                def thirds_for(team, attack_right: bool = True):
                    t = d.loc[d["teamName"] == team, X]
                    if t.empty:
                        return {"Def": 0, "Mid": 0, "Att": 0}
                    if attack_right:   # يهاجم لليمين
                        Def = (t < left_third).sum()
                        Mid = ((t >= left_third) & (t < right_third)).sum()
                        Att = (t >= right_third).sum()
                    else:              # يهاجم لليسار
                        Att = (t <= left_third).sum()
                        Mid = ((t > left_third) & (t <= right_third)).sum()
                        Def = (t > right_third).sum()
                    tot = int(Def + Mid + Att)
                    if tot == 0:
                        return {"Def": 0, "Mid": 0, "Att": 0}
                    p = np.array([Def, Mid, Att], dtype=float) * (100.0 / tot)
                    base = np.floor(p).astype(int)
                    rem = 100 - base.sum()
                    if rem > 0:
                        idx = np.argsort(-(p - base))[:rem]
                        base[idx] += 1
                    return {"Def": int(base[0]), "Mid": int(base[1]), "Att": int(base[2])}

                # اتجاه العرض
                home_attack_right = True
                away_attack_right = (not face_opt)

                home_thirds = thirds_for(hteam, attack_right=home_attack_right)
                away_thirds = thirds_for(ateam, attack_right=away_attack_right)

                # الرسم
                fig, axes = plt.subplots(1, 2, figsize=(14, 6))
                h_def, h_mid, h_att = three_shades(home_color)
                a_def, a_mid, a_att = three_shades(away_color)

                draw_team_thirds_with_direction(
                    axes[0], hteam, home_thirds, h_def, h_mid, h_att, home_attack_right
                )
                draw_team_thirds_with_direction(
                    axes[1], ateam, away_thirds, a_def, a_mid, a_att, away_attack_right
                )

                # عنوان عام (تصحيح عربي اختياري)
                def ar(t): return str(t)

                fig.suptitle(ar("توزيع اللعب عبر أثلاث الملعب") + f" — {hteam} ضد {ateam}", fontsize=14)
                st.pyplot(fig, use_container_width=True)

        except Exception as e:
            st.error(f"خطأ في أثلاث الملعب: {e}")









elif analysis_type == "إحصائيات المباراة":

    with st.expander("خريطة التسديدات وتحليل الزخم", expanded=True):

        col1 = st.color_picker("لون الفريق الأول", "#0099ff", key="color1")
        col2 = st.color_picker("لون الفريق الثاني", "#ff4d4d", key="color2")
        bg_color = st.color_picker("لون الخلفية", "#ffffff", key="bg_color")
        line_color = st.color_picker("لون الخط", "#000000", key="line_color")

        analysis_option = st.selectbox(
            "اختر نوع التحليل",
            [
                "إحصائيات عامة",
                "خريطة التسديدات",
                "خريطة المرمى",
                "تحليل الزخم",
                "شبكة التمريرات",
                "تدفق التمريرات",   # ✅ تمت الإضافة هنا
                "خريطة الكتلة الدفاعية",
                "التحولات العالية",
                "التمريرات التقدمية",
                "الحمولات التقدمية",
                "الإدخالات في الثلث النهائي",
                "إدخالات منطقة الجزاء",
                "نهاية التمريرات",
                "مناطق خلق الفرص",
                "Zone14 والمساحات النصفية",
                "الكرات العرضية",
                "مناطق السيطرة (Zone Dominance)",
                "التقرير الكامل (Report 1 + Report 2)"
            ],
            key="match_stats_analysis_option"
        )

        try:
            # =========================
            # 1) إحصائيات عامة
            # =========================
            if analysis_option == "إحصائيات عامة":
                fig, ax = plt.subplots(figsize=(10, 6))
                plotting_match_stats(ax, df_match, hteam, ateam, col1, col2, bg_color, line_color)
                st.pyplot(fig)

            # =========================
            # 2) خريطة التسديدات
            # =========================
            elif analysis_option == "خريطة التسديدات":
                fig = draw_shotmap_both_teams(df_match, hteam, ateam, col1, col2, bg_color, line_color)
                st.pyplot(fig)

            # =========================
            # 3) خريطة المرمى
            # =========================
            elif analysis_option == "خريطة المرمى":
                Shotsdf = df_match[df_match["type"].isin(["Goal", "SavedShot", "ShotOnPost", "MissedShots"])].reset_index(drop=True)
                fig, ax = plt.subplots(figsize=(14, 8))
                plot_goalPost(ax, Shotsdf, hteam, ateam, col1, col2, bg_color, line_color)
                st.pyplot(fig)

            # =========================
            # 4) تحليل الزخم
            # =========================
            elif analysis_option == "تحليل الزخم":
                fig, ax = plt.subplots(figsize=(12, 5))
                momentum_func = generate_and_plot_momentum(df_match, hteam, ateam, col1, col2, bg_color, line_color)
                momentum_func(ax)
                st.pyplot(fig)

            # =========================
            # 5) شبكة التمريرات
            # =========================
            elif analysis_option == "شبكة التمريرات":
                fig_net, axs = plt.subplots(1, 2, figsize=(22, 9))

                pass_network(axs[0], hteam, col1, hteam, df_match, bg_color, line_color, ar)
                pass_network(axs[1], ateam, col2, hteam, df_match, bg_color, line_color, ar)  # الضيف (X مقلوب داخل دالتك)

                fig_net.suptitle(ar("تحليل شبكة التمريرات وتمركز اللاعبين"), fontsize=22, color="black", fontweight="bold")
                st.pyplot(fig_net)

                st.markdown(
                    """
<div dir="rtl" style="text-align:right; font-family: 'Tahoma', sans-serif;">
<h3>📌 شرح العناصر في الشكل</h3>
<ul>
<li><b>الكتلة المظللة:</b> شريط طولي يحدّد ممر التقدّم الأكثر استخدامًا بين خطي الفريق أثناء الاستحواذ (تحديد مكاني).</li>
<li><b>العمودية:</b> تصف اتجاه التمريرات نحو مرمى الخصم مقارنة بالتمريرات العرضية/الخلفية. الأعلى = لعب مباشر.</li>
<li><b>المسافة الطولية:</b> مقياس (بالمتر) لتباعد خطوط الفريق طوليًا أثناء الاستحواذ. صغيرة = تقارب، كبيرة = انتشار.</li>
</ul>
</div>
""",
                    unsafe_allow_html=True
                )

                st.markdown(
                    """
<div dir="rtl" style="text-align: right; font-family: 'Tahoma', sans-serif;">
<h3>📌 قراءة مشتركة</h3>
<ul>
<li><b>عمودية مرتفعة + كتلة نشطة:</b> تقدم مباشر ومتكرر عبر ممر محدد.</li>
<li><b>مسافة كبيرة + عمودية منخفضة:</b> انتشار طولي مع تدوير وبناء بطيء.</li>
<li><b>مسافة صغيرة + عمودية عالية:</b> فريق مضغوط لكن يهاجم بسرعة (ضغط/تحولات).</li>
<li><b>مسافة صغيرة + عمودية منخفضة:</b> استحواذ آمن قصير في مساحات ضيقة.</li>
</ul>
</div>
""",
                    unsafe_allow_html=True
                )

            # =========================
            # 6) تدفق التمريرات (Pass Flow 5x5)
            # =========================
            elif analysis_option == "تدفق التمريرات":

                selected_team_flow = st.selectbox(
                    "اختر الفريق لتدفق التمريرات",
                    [hteam, ateam],
                    key="selected_team_flow"
                )

                min_flow_passes = st.slider(
                    "الحد الأدنى لعدد التمريرات بين Zone و Zone",
                    min_value=1,
                    max_value=20,
                    value=3,
                    step=1,
                    key="min_flow_passes"
                )

                curved_flow = st.toggle("خطوط منحنية", value=True, key="curved_flow")

                team_color = col1 if selected_team_flow == hteam else col2

                try:
                    # ✅ الدالة ترجع fig فقط
                    fig_flow = draw_pass_flow_map(
                        df_match,
                        team_name=selected_team_flow,
                        hteamName=hteam,
                        team_color=team_color,
                        bg_color=bg_color,
                        line_color=line_color,
                        grid=(5, 5),
                        min_passes=int(min_flow_passes),
                        curved=bool(curved_flow),
                        curvature=0.25,
                        lw_max=8,
                        arrow_scale=18,
                        title_ar=f"{selected_team_flow} - خريطة تدفق التمريرات (5×5)"
                    )

                    st.pyplot(fig_flow, use_container_width=True)

                    # ✅ شرح عربي مختصر تحت الرسم
                    st.markdown(
                        """
<div dir="rtl" style="text-align:right; font-family: 'Tahoma', sans-serif;">
<h3>📌 ماذا تمثل خريطة تدفق التمريرات؟</h3>
<ul>
<li><b>تقسيم 5×5:</b> الملعب مقسّم إلى 25 منطقة (Zones).</li>
<li><b>الأسهم:</b> تمثل انتقال الكرة بالتمرير <b>من Zone إلى Zone</b>.</li>
<li><b>سمك السهم:</b> كلما زاد السمك زاد <b>عدد التمريرات</b> على نفس المسار.</li>
<li><b>شفافية السهم:</b> الأعلى شفافية = مسار أكثر تكرارًا/أهمية.</li>
<li><b>اتجاه اللعب:</b> السهم الصغير يوضح جهة هجوم الفريق (حسب كونه مستضيف/ضيف).</li>
</ul>
<p style="color:#666; font-size:90%;">
قراءة سريعة: إذا ظهرت أسهم سميكة متكررة في جانب واحد، فهذا يعني أن الفريق يعتمد على تلك القناة في بناء اللعب والتقدم.
</p>
</div>
""",
                        unsafe_allow_html=True
                    )

                except Exception as e:
                    st.error(f"خطأ في خريطة تدفق التمريرات: {e}")
                    with st.expander("Debug"):
                        st.write("columns:", sorted(df_match.columns.tolist()))
                        st.write(df_match.head())

            # =========================
            # 7) خريطة الكتلة الدفاعية
            # =========================
            elif analysis_option == "خريطة الكتلة الدفاعية":
                fig, axs = plt.subplots(1, 2, figsize=(20, 8))

                defensive_heatmap(axs[0], hteam, col1, df_match, bg_color, line_color)
                axs[0].set_title(ar(f"{hteam} - التدخلات الدفاعية"), fontsize=14, color=col1)

                defensive_heatmap(axs[1], ateam, col2, df_match, bg_color, line_color)
                axs[1].set_title(ar(f"{ateam} - التدخلات الدفاعية"), fontsize=14, color=col2)

                st.pyplot(fig)

            # =========================
            # 8) التحولات العالية
            # =========================
            elif analysis_option == "التحولات العالية":
                fig, ax = plt.subplots(figsize=(22, 10))
                HighTO(ax, df_match, hteam, ateam, col1, col2, bg_color, line_color)
                st.pyplot(fig)

            # =========================
            # 9) التمريرات التقدمية
            # =========================
            elif analysis_option == "التمريرات التقدمية":
                fig, axs = plt.subplots(1, 2, figsize=(22, 9))

                draw_progressive_pass_map(axs[0], hteam, col1, line_color)
                axs[0].set_title(ar(f"{hteam} - التمريرات التقدمية"), fontsize=20, color=col1)

                draw_progressive_pass_map(axs[1], ateam, col2, line_color)
                axs[1].set_title(ar(f"{ateam} - التمريرات التقدمية"), fontsize=20, color=col2)

                st.pyplot(fig)

            # =========================
            # 10) الحمولات التقدمية
            # =========================
            elif analysis_option == "الحمولات التقدمية":
                st.markdown("<h3 style='text-align: center;'>خريطة الحمولات التقدمية</h3>", unsafe_allow_html=True)

                fig, axs = plt.subplots(1, 2, figsize=(20, 8))
                draw_progressive_carry_map(axs[0], hteam, col1, line_color)
                draw_progressive_carry_map(axs[1], ateam, col2, line_color)
                st.pyplot(fig)

            # =========================
            # 11) الإدخالات في الثلث النهائي
            # =========================
            elif analysis_option == "الإدخالات في الثلث النهائي":
                fig, axs = plt.subplots(1, 2, figsize=(22, 9))

                Final_third_entry(axs[0], df_match, hteam, col1, bg_color, line_color, hteam, ateam, is_away=False)
                axs[0].set_title(ar(f"{hteam} - الإدخالات في الثلث النهائي"), fontsize=20, color=col1)

                Final_third_entry(axs[1], df_match, ateam, col2, bg_color, line_color, hteam, ateam, is_away=True)
                axs[1].set_title(ar(f"{ateam} - الإدخالات في الثلث النهائي"), fontsize=20, color=col2)

                st.pyplot(fig)

            # =========================
            # 12) إدخالات منطقة الجزاء
            # =========================
            elif analysis_option == "إدخالات منطقة الجزاء":
                fig, axs = plt.subplots(1, 2, figsize=(24, 10))

                box_entry(axs[0], df_match, hteam, hteam, ateam, col1, bg_color, line_color, is_away=False)
                axs[0].set_title(ar(f"{hteam} - إدخالات منطقة الجزاء"), fontsize=20, color=col1)

                box_entry(axs[1], df_match, ateam, hteam, ateam, col2, bg_color, line_color, is_away=True)
                axs[1].set_title(ar(f"{ateam} - إدخالات منطقة الجزاء"), fontsize=20, color=col2)

                st.pyplot(fig)

            # =========================
            # 13) نهاية التمريرات
            # =========================
            elif analysis_option == "نهاية التمريرات":
                fig, axs = plt.subplots(1, 2, figsize=(20, 8))

                Pass_end_zone(
                    axs[0], df_match, hteam, ateam,
                    col=col1, bg_color=bg_color, line_color=line_color,
                    col1=col1, col2=col2, hteamName=hteam
                )
                Pass_end_zone(
                    axs[1], df_match, ateam, ateam,
                    col=col2, bg_color=bg_color, line_color=line_color,
                    col1=col1, col2=col2, hteamName=hteam
                )

                st.pyplot(fig)

            # =========================
            # 14) مناطق خلق الفرص
            # =========================
            elif analysis_option == "مناطق خلق الفرص":
                fig_cc, axs_cc = plt.subplots(1, 2, figsize=(24, 10))

                Chance_creating_zone(
                    axs_cc[0], df_match, hteam, ateam,
                    col=col1, bg_color=bg_color, line_color=line_color,
                    col1=col1, col2=col2, hteamName=hteam
                )
                Chance_creating_zone(
                    axs_cc[1], df_match, ateam, ateam,
                    col=col2, bg_color=bg_color, line_color=line_color,
                    col1=col1, col2=col2, hteamName=hteam
                )

                st.pyplot(fig_cc)

            # =========================
            # 15) Zone14 والمساحات النصفية
            # =========================
            elif analysis_option == "Zone14 والمساحات النصفية":
                fig, axs = plt.subplots(1, 2, figsize=(24, 10))

                zone14hs(axs[0], df_match, hteam, col1, bg_color, line_color, hteam, ateam)
                axs[0].set_title(ar(f"{hteam} - المنطقة 14 والمساحات النصفية"), fontsize=14, color=col1)

                zone14hs(axs[1], df_match, ateam, col2, bg_color, line_color, hteam, ateam)
                axs[1].set_title(ar(f"{ateam} - المنطقة 14 والمساحات النصفية"), fontsize=14, color=col2)

                st.pyplot(fig)

            # =========================
            # 16) الكرات العرضية
            # =========================
            elif analysis_option == "الكرات العرضية":
                fig, ax = plt.subplots(figsize=(22, 10))
                Crosses(ax, df_match, hteam, ateam, col1, col2, bg_color, line_color)
                st.pyplot(fig)

            # =========================
            # 17) مناطق السيطرة
            # =========================
            elif analysis_option == "مناطق السيطرة (Zone Dominance)":
                fig, ax = plt.subplots(figsize=(20, 10))
                plot_congestion(ax, df_match, hteam, ateam, col1, col2, bg_color, line_color)
                st.pyplot(fig)

            # =========================
            # 18) التقرير الكامل
            # =========================
            elif analysis_option == "التقرير الكامل (Report 1 + Report 2)":
                try:
                    with st.spinner("يتم توليد التقرير الكامل..."):

                        # -------- تقرير 1 --------
                        fig1, axs1 = plt.subplots(4, 3, figsize=(38, 38), facecolor=bg_color)

                        pass_network(axs1[0, 0], hteam, col1, hteam, df_match, bg_color, line_color, ar)
                        draw_shotmap_both_teams(df_match, hteam, ateam, col1, col2, bg_color, line_color, ax=axs1[0, 1])
                        pass_network(axs1[0, 2], ateam, col2, hteam, df_match, bg_color, line_color, ar)

                        defensive_heatmap(axs1[1, 0], hteam, col1, df_match, bg_color, line_color)
                        Shotsdf = df_match[df_match["type"].isin(["Goal", "SavedShot", "ShotOnPost", "MissedShots"])].reset_index(drop=True)
                        plot_goalPost(axs1[1, 1], Shotsdf, hteam, ateam, col1, col2, bg_color, line_color)
                        defensive_heatmap(axs1[1, 2], ateam, col2, df_match, bg_color, line_color)

                        draw_progressive_pass_map(axs1[2, 0], hteam, col1, line_color)
                        generate_and_plot_momentum(df_match, hteam, ateam, col1, col2, bg_color, line_color)(axs1[2, 1])
                        draw_progressive_pass_map(axs1[2, 2], ateam, col2, line_color)

                        draw_progressive_carry_map(axs1[3, 0], hteam, col1, line_color)
                        plotting_match_stats(axs1[3, 1], df_match, hteam, ateam, col1, col2, bg_color, line_color)
                        draw_progressive_carry_map(axs1[3, 2], ateam, col2, line_color)

                        fig_text(0.5, 1.03, "Full Match Tactical Report", color=line_color, fontsize=28, ha="center", ax=fig1)
                        fig_text(0.5, 0.99, "Report 1", color="#090909", fontsize=30, fontweight="bold", ha="center", ax=fig1)
                        fig_text(0.5, 0.97, "Data: Opta | Created by: @Turadi_7", color="#080808", fontsize=20, ha="center", ax=fig1)

                        # -------- تقرير 2 --------
                        fig2, axs2 = plt.subplots(4, 3, figsize=(38, 38), facecolor=bg_color)

                        Final_third_entry(axs2[0, 0], df_match, hteam, col1, bg_color, line_color, hteam, ateam, is_away=False)
                        box_entry_both(axs2[0, 1], df_match, hteam, ateam, col1, col2, bg_color, line_color)
                        Final_third_entry(axs2[0, 2], df_match, ateam, col2, bg_color, line_color, hteam, ateam, is_away=True)

                        zone14hs(axs2[1, 0], df_match, hteam, col1, bg_color, line_color, hteam, ateam)
                        Crosses(axs2[1, 1], df_match, hteam, ateam, col1, col2, bg_color, line_color)
                        zone14hs(axs2[1, 2], df_match, ateam, col2, bg_color, line_color, hteam, ateam)

                        Pass_end_zone(axs2[2, 0], df_match, hteam, ateam, col=col1, bg_color=bg_color, line_color=line_color, col1=col1, col2=col2, hteamName=hteam)
                        HighTO(axs2[2, 1], df_match, hteam, ateam, col1, col2, bg_color, line_color)
                        Pass_end_zone(axs2[2, 2], df_match, ateam, ateam, col=col2, bg_color=bg_color, line_color=line_color, col1=col1, col2=col2, hteamName=hteam)

                        Chance_creating_zone(axs2[3, 0], df_match, hteam, ateam, col=col1, bg_color=bg_color, line_color=line_color, col1=col1, col2=col2, hteamName=hteam)
                        plot_congestion(axs2[3, 1], df_match, hteam, ateam, col1, col2, bg_color, line_color)
                        Chance_creating_zone(axs2[3, 2], df_match, ateam, ateam, col=col2, bg_color=bg_color, line_color=line_color, col1=col1, col2=col2, hteamName=hteam)

                        fig_text(0.5, 0.98, "Full Match Tactical Report", color=line_color, fontsize=28, ha="center", ax=fig2)
                        fig_text(0.5, 0.95, "Report 2", color="#030303", fontsize=30, fontweight="bold", ha="center", ax=fig2)
                        fig_text(0.5, 0.92, "Data: Opta | Created by: @Turadi_7", color="#090909", fontsize=20, ha="center", ax=fig2)

                        col1_, col2_ = st.columns(2)
                        with col1_:
                            st.markdown("#### التقرير الأول")
                            st.pyplot(fig1)
                        with col2_:
                            st.markdown("#### التقرير الثاني")
                            st.pyplot(fig2)

                except Exception as e:
                    st.error(f"حدث خطأ أثناء توليد التقريرين: {e}")

        except Exception as e:
            st.error(f"حدث خطأ أثناء عرض التحليل: {e}")


elif analysis_type == "تحليل لاعب":
    st.markdown("### 👤 تحليل لاعب محدد")

    selected_team_player = st.selectbox(" اختر الفريق", [hteam, ateam], key="xt_player_team")

    player_list = (
        df_match[df_match['teamName'] == selected_team_player]['shortName']
        .dropna().unique().tolist()
    )
    selected_player = st.selectbox(" اختر اللاعب", sorted(player_list), key="xt_selected_player")

    # =============== خريطة xT (تمرير + حمل) ===============
    with st.expander(" خريطة xT للتمريرات والحملات", expanded=True):
        xtmap_color = st.color_picker(" لون التمريرات", "#88CCF9", key="xtmap_color")
        try:
            fig_xtmap = draw_xt_pass_and_carry_map(
                df_match,
                player_name=selected_player,
                team_name=selected_team_player,
                base_color=xtmap_color,
            )
            st.pyplot(fig_xtmap)
            st.markdown(f" تم عرض خريطة xT للاعب {selected_player} من فريق {selected_team_player}.")
        except Exception as e:
            st.error(f" خطأ في رسم خريطة xT للاعب: {e}")


        st.markdown("""
<div dir="rtl" style="text-align: right;">
<h3> ما هي خريطة xT؟</h3>
<p>
تمثل هذه الخريطة التهديد المتوقع (Expected Threat - xT) الناتج من تمريرات أو حملات اللاعب.<br>
كل سهم يعكس حركة الكرة من موقع إلى آخر في الملعب، ويُظهر فوقه مقدار التغيير في التهديد الناتج عن هذه الحركة.
</p>

<h4> <b>لماذا نستخدم المعادلة:</b></h4>
<p>
نحسب التهديد الناتج من التمريرة أو الحملة باستخدام المعادلة:<br>
<b>xT = xT(النقطة النهائية) - xT(النقطة الابتدائية)</b>
</p>

<h4> <b>السبب:</b></h4>
<p>
هذه المعادلة تقيس "الفرق في الخطورة" بين المكان الذي بدأت فيه الكرة والمكان الذي انتهت إليه.<br>
فإذا زادت قيمة xT بعد التمريرة أو الحملة، فهذا يعني أن اللاعب <b>اقترب من منطقة أكثر تهديدًا</b> على المرمى.
</p>

<p>
 <b>قيمة موجبة:</b> تعني أن الحركة <b>أنتجت تهديدًا</b>.<br>
 <b>قيمة سالبة:</b> تعني أن اللاعب <b>تراجع أو ابتعد عن مناطق التهديد</b> (غالبًا ما يتم تجاهلها أو إظهارها بلون رمادي).
</p>

<p>
 تساعد هذه الخريطة المدربين والمحللين على تحديد الأماكن التي ينجح فيها اللاعب في <b>زيادة التهديد على الخصم</b>.
</p>
</div>
""", unsafe_allow_html=True)







    # =============== الخريطة الحرارية وتمريرات اللاعب ===============
    with st.expander(" الخريطة الحرارية وتمريرات اللاعب", expanded=False):
        try:
            from scipy.ndimage import gaussian_filter

            player_data = df_match[
                (df_match['shortName'] == selected_player) &
                df_match['x'].notnull() & df_match['y'].notnull()
            ]

            if player_data.empty:
                st.warning(f" لا توجد تحركات مسجلة للاعب: {selected_player}")
            else:
                # Heatmap
                pitch = Pitch(pitch_type='uefa', pitch_color='#22312b', line_color='#efefef', line_zorder=2)
                fig, ax = pitch.draw(figsize=(10, 7))
                fig.set_facecolor('#22312b')
                ax.annotate(xy=(0.42, 0.001), xytext=(0.60, 0.001), text='',
                            arrowprops=dict(arrowstyle='<|-, head_length=0.2, head_width=0.12',
                                            linewidth=0.7, color='w', fc='#f2f2f2', zorder=4),
                            xycoords='axes fraction')
                ax.annotate(xy=(0.44, -0.031), text='Attacking direction', xycoords='axes fraction',
                            size=8.2, color='w', weight="bold")

                bin_statistic = pitch.bin_statistic(player_data.x, player_data.y, statistic='count', bins=(25, 25))
                bin_statistic['statistic'] = gaussian_filter(bin_statistic['statistic'], sigma=1.5)
                heatmap = pitch.heatmap(bin_statistic, ax=ax, cmap='hot', edgecolors='#22312b')
                cbar = fig.colorbar(heatmap, ax=ax, shrink=0.6)
                cbar.outline.set_edgecolor('#efefef')
                cbar.ax.yaxis.set_tick_params(color='#efefef')
                plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='#efefef')

                ax.set_title(ar(f"الخريطة الحرارية وتحليل تمريرات {selected_player}"), fontsize=16, color='white', weight='bold')
                st.pyplot(fig)

                # تمريرات اللاعب
                st.markdown(" *خريطة تمريرات اللاعب*")
                player_passes = player_data[player_data['type'] == 'Pass']
                success = player_passes[player_passes['outcomeType'] == 'Successful']
                fail = player_passes[player_passes['outcomeType'] == 'Unsuccessful']

                pitch = Pitch(pitch_type='uefa', pitch_color='white', line_color='black', line_zorder=2)
                fig2, ax2 = pitch.draw(figsize=(10, 7))
                ax2.annotate(xy=(0.42, 0.001), xytext=(0.60, 0.001), text='',
                             arrowprops=dict(arrowstyle='<|-, head_length=0.2, head_width=0.12',
                                             linewidth=0.7, color='black', fc='black', zorder=4),
                             xycoords='axes fraction')
                ax2.annotate(xy=(0.44, -0.015), text='Attacking direction', xycoords='axes fraction',
                             size=8.2, color='black', weight="bold")

                pitch.arrows(success['x'], success['y'], success['endX'], success['endY'],
                             ax=ax2, color='green', width=2, headwidth=3, label=ar(" تمريرات ناجحة"))
                pitch.arrows(fail['x'], fail['y'], fail['endX'], fail['endY'],
                             ax=ax2, color='red', width=2, headwidth=3, alpha=0.6, label=ar(" تمريرات خاطئة"))

                ax2.set_title(ar(f"تحليل تمريرات {selected_player}"), fontsize=14, weight='bold')
                total_passes = len(player_passes)
                successful_passes = len(success)
                failed_passes = len(fail)
                accuracy = (successful_passes / total_passes * 100) if total_passes > 0 else 0
                stats_text = f" عدد التمريرات الناجحة: {successful_passes}     الخاطئة: {failed_passes}    📊 المجموع: {total_passes}    🎯 الدقة: {accuracy:.1f}%"
                ax2.text(0.5, 0.97, ar(stats_text), transform=ax2.transAxes,
                         ha='center', va='bottom', fontsize=11, color='black', fontweight='bold')
                ax2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.03), ncol=2, fontsize=12,
                           frameon=False, handlelength=2.5)
                st.pyplot(fig2)
        except Exception as e:
            st.error(f" خطأ أثناء عرض الخريطة الحرارية أو التمريرات: {e}")

    # =========================
    #  🛰️ رادار مقارنة لاعبين — SAVEN style
    # =========================
    # دعم نص عربي مضبوط للرسم
    try:
        from bidi.algorithm import get_display
        import arabic_reshaper
        def ar_text(t): return str(str(t))
    except Exception:
        def ar_text(t): return str(t)

    # ——— دوال المقاييس (يفترض METRIC_MAP موجود عندك) ———
    def compute_player_metrics(df_team: pd.DataFrame, player_name: str, metric_names: list[str]) -> dict:
        d = df_team[df_team['name'] == player_name].copy()
        out = {}
        for m in metric_names:
            func = METRIC_MAP.get(m)
            out[m] = float(func(d)) if func else 0.0
        return out

    def _series_for_metric_both_teams(df_both, metric):
        """سلسلة قيم لكل لاعب لدى الفريقين لاستخدامها في تطبيع 'teams'."""
        players = df_both['name'].dropna().unique().tolist()
        vals = []
        for pl in players:
            v = compute_player_metrics(df_both, pl, [metric]).get(metric, 0.0)
            try: vals.append(float(v))
            except: vals.append(0.0)
        s = pd.Series(vals, index=players, dtype='float64')
        s = s.fillna(0.0).replace([np.inf, -np.inf], 0.0)
        return s

    def draw_players_radar_saven(df_match, p1, p2, metrics, normalize="pair",
                                 title=None, footer_label="SAVEN",
                                 df_both_for_norm=None):
        # قيم خام (من كامل df_match حتى لا تُصفَّر قيم لاعب الضيف)
        p1_vals = compute_player_metrics(df_match, p1, metrics)
        p2_vals = compute_player_metrics(df_match, p2, metrics)

        # تطبيع
        p1_norm, p2_norm = [], []
        for m in metrics:
            v1 = float(p1_vals.get(m, 0.0) or 0.0)
            v2 = float(p2_vals.get(m, 0.0) or 0.0)

            if normalize == "teams":
                s = _series_for_metric_both_teams(df_both_for_norm, m) if df_both_for_norm is not None else pd.Series([v1, v2])
                mx = float(s.max()) if len(s) else 0.0
                if mx > 0:
                    p1_norm.append(v1 / mx); p2_norm.append(v2 / mx)
                else:
                    p1_norm += [0.0]; p2_norm += [0.0]
            elif normalize == "pair":
                mx = max(v1, v2)
                if mx > 0:
                    p1_norm.append(v1 / mx); p2_norm.append(v2 / mx)
                else:
                    p1_norm += [0.0]; p2_norm += [0.0]
            else:  # none
                p1_norm.append(v1); p2_norm.append(v2)

        # إعداد الرادار
        labels = [ar_text(l) for l in metrics]
        N = len(labels)
        angles = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
        angles_plot = angles + [angles[0]]
        p1_plot = p1_norm + [p1_norm[0]]
        p2_plot = p2_norm + [p2_norm[0]]
        # ألوان وهوية
        bg_top = (9/255, 30/255, 22/255)
        bg_bottom = (3/255, 16/255, 12/255)
        ring_color = (1,1,1,0.08)
        grid_color = (1,1,1,0.10)
        lbl_color  = (1,1,1,0.90)
        color_p1 = (0.95, 0.95, 0.95, 1.0)
        fill_p1  = (0.95, 0.95, 0.95, 0.20)
        color_p2 = (0.98, 0.77, 0.06, 1.0)
        fill_p2  = (0.98, 0.77, 0.06, 0.20)
        
        fig = plt.figure(figsize=(9.5, 9.5), dpi=160)
        # خلفية متدرجة
        ax_bg = fig.add_axes([0,0,1,1])
        grad = np.linspace(0,1,512).reshape(-1,1)
        cmap = plt.matplotlib.colors.LinearSegmentedColormap.from_list("", [bg_bottom, bg_top])
        ax_bg.imshow(np.hstack([grad]*3), extent=[0,1,0,1], origin='lower', cmap=cmap)
        ax_bg.axis("off")

        # عنوان علوي
        main_title = title or f"Comparison"
        fig.text(0.05, 0.94, ar_text(main_title), color="white", fontsize=20, fontweight="bold")

        # لوحة الرادار
        ax = fig.add_axes([0.06, 0.20, 0.88, 0.68], polar=True)
        ax.set_theta_offset(np.pi/2)
        ax.set_theta_direction(-1)
        ax.set_facecolor((0,0,0,0))

        # حلقات
        if normalize in ("pair","teams"):
            rmax = 1.0
        else:
            rmax = max(1.0, float(max(p1_plot + p2_plot)))
        ax.set_ylim(0, rmax)
        for r in np.linspace(ax.get_rmin(), ax.get_rmax(), 6)[1:]:
            ax.plot(np.linspace(0,2*np.pi,360), [r]*360, color=ring_color, lw=1)

        # شبكة/تسميات
        ax.set_thetagrids(np.degrees(angles), labels)
        for spine in ax.spines.values():
            spine.set_color(grid_color)
        ax.tick_params(colors=lbl_color, labelsize=15)
        ax.tick_params(axis='x', pad=15, colors=lbl_color, labelsize=12)  # ← عدّل pad (مثلاً 10–18) حسب ما يناسبك

        ax.grid(color=grid_color, linestyle='-', lw=1, alpha=0.25)

        


        # رسم اللاعبَين
        ax.plot(angles_plot, p1_plot, color=color_p1, lw=2.4)
        ax.fill(angles_plot, p1_plot, color=fill_p1)
        ax.plot(angles_plot, p2_plot, color=color_p2, lw=2.4)
        ax.fill(angles_plot, p2_plot, color=fill_p2)

        # وسيلة إيضاح
       
        legend_ax = fig.add_axes([0.04, 0.075, 0.82, 0.10])   # كان 0.92 عرضًا؛ صغّرناه لترك فراغ يمين

        legend_ax.set_facecolor((0,0,0,0)); legend_ax.axis("off")
        legend_ax.plot([0.08, 0.16], [0.5, 0.5], color=color_p1, lw=6, solid_capstyle='round')
        legend_ax.text(0.18, 0.5, p1, color="white", va='center', fontsize=13)
        legend_ax.plot([0.48, 0.56], [0.5, 0.5], color=color_p2, lw=6, solid_capstyle='round')
        legend_ax.text(0.57, 0.5, p2, color="white", va='center', fontsize=13, ha='left')

        # ختم SAVEN
        fig.text(0.93, 0.055, footer_label, color="white", fontsize=13, fontweight="bold")
        return fig

    # ============== دمج واجهة الرادار ==============
    with st.expander("رادار مقارنة لاعبين", expanded=False):
        cA, cB = st.columns(2)
        p_home = cA.selectbox(" لاعب المستضيف", 
                              sorted(df_match[df_match['teamName'] == hteam]['name'].dropna().unique().tolist()),
                              key="saven_radar_p1")
        p_away = cB.selectbox(" لاعب الضيف", 
                              sorted(df_match[df_match['teamName'] == ateam]['name'].dropna().unique().tolist()),
                              key="saven_radar_p2")

        default_metrics = ["تمريرات", "تمريرات ناجحة", "تمريرات تقدمية", "تسديدات", "أهداف", "xA صناعة"]
        metrics = st.multiselect(" المقاييس", list(METRIC_MAP.keys()),
                                 default=default_metrics, key="saven_radar_metrics")

        

        if st.button("ارسم الرادار", use_container_width=True):
            try:
                both_df = df_match[df_match['teamName'].isin([hteam, ateam])].copy()
                fig = draw_players_radar_saven(
                    df_match,
                    p1=p_home, p2=p_away,
                    metrics=metrics,
                   
                    title=f"{p_home} ({hteam})  vs  {p_away} ({ateam})",
                    footer_label="SAVEN",
                    df_both_for_norm=both_df
                )
                st.pyplot(fig, use_container_width=True)
                st.caption("القيم تُطبّع حسب اختيارك. اختر «على مستوى لاعبي الفريقين» لتطبيع كل مقياس مقارنةً بأعلى قيمة بين جميع لاعبي الفريقين في المباراة.")
            except Exception as e:
                st.error(f"حدث خطأ أثناء رسم الرادار: {e}")














