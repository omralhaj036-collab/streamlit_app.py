import streamlit as st
import requests

# --- إعدادات الصفحة ---
st.set_page_config(page_title="Atheer AI Pro", layout="wide", initial_sidebar_state="collapsed")

# --- إدارة التنقل (Navigation Logic) ---
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- التصميم الفاخر (مطابق للصورة 100%) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #000000 !important;
        font-family: 'Cairo', sans-serif;
        direction: rtl;
    }

    /* خلفية الجزيئات النيوتنية المتحركة */
    .particles-bg {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: radial-gradient(circle at center, #1a1a1a 0%, #000 100%);
        z-index: -1;
    }

    /* شعار أثير الذهبي (الدرع الكبير) */
    .atheer-shield {
        width: 180px;
        height: 180px;
        margin: 0 auto 30px;
        background: linear-gradient(135deg, #d4af37 0%, #f9f295 45%, #b38728 70%, #f9f295 100%);
        border-radius: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 0 30px rgba(212, 175, 55, 0.5);
        clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
    }

    /* هندسة النوافذ (Grid) */
    .main-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        max-width: 800px;
        margin: 0 auto;
    }

    /* تصميم النافذة الذهبية (مثل الصورة) */
    .icon-box {
        background: rgba(20, 20, 20, 0.9);
        border: 2px solid #d4af37;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        transition: 0.3s;
        cursor: pointer;
        height: 140px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        clip-path: polygon(15% 0, 85% 0, 100% 15%, 100% 85%, 85% 100%, 15% 100%, 0 85%, 0 15%);
        box-shadow: inset 0 0 15px rgba(212, 175, 55, 0.1);
    }

    .icon-box:hover {
        background: #d4af37;
        box-shadow: 0 0 30px #d4af37;
    }

    .icon-box:hover h3, .icon-box:hover i {
        color: #000 !important;
    }

    .icon-box i {
        font-size: 2.5rem;
        color: #d4af37;
        margin-bottom: 10px;
    }

    .icon-box h3 {
        color: #d4af37;
        font-size: 0.8rem;
        font-weight: bold;
        margin: 0;
    }

    /* صفحة الاشتراك الزجاجية الزرقاء */
    .sub-page {
        background: rgba(0, 50, 100, 0.2);
        backdrop-filter: blur(20px);
        border: 2px solid #00f2ff;
        border-radius: 30px;
        padding: 50px;
        max-width: 600px;
        margin: 50px auto;
        text-align: center;
        box-shadow: 0 0 50px rgba(0, 242, 255, 0.3);
    }

    /* أزرار سترمليت المخفية */
    .stButton>button {
        background: transparent;
        border: none;
        color: transparent;
        width: 100%;
        height: 140px;
        position: absolute;
        top: 0; left: 0;
        z-index: 10;
    }
</style>
<div class="particles-bg"></div>
""", unsafe_allow_html=True)

# --- الصفحة الرئيسية (Home) ---
if st.session_state.page == 'home':
    # اللوجو
    st.markdown('<div class="atheer-shield"><h1 style="color:#000; font-size:1.5rem; text-align:center;">أثير<br>للتقنية</h1></div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#d4af37; letter-spacing:5px; margin-bottom:50px;">ATHEER TECHNOLOGY SOLUTIONS</p>', unsafe_allow_html=True)

    # النوافذ (Grid)
    col1, col2, col3 = st.columns(3)
    
    items = [
        {"icon": "🛡️", "title": "حماية المتجر الذكي", "id": "ai"},
        {"icon": "⚙️", "title": "تحسين محركات البحث", "id": "ai"},
        {"icon": "🧠", "title": "تشخيص الأنظمة", "id": "ai"},
        {"icon": "📊", "title": "تحليلات المبيعات", "id": "ai"},
        {"icon": "📈", "title": "المسار الرقمي", "id": "ai"},
        {"icon": "👤", "title": "الهوية الرقمية", "id": "ai"},
        {"icon": "👁️", "title": "الرؤى", "id": "ai"},
        {"icon": "🎓", "title": "الخبرة", "id": "ai"},
        {"icon": "💎", "title": "باقة الاشتراك", "id": "sub"}, # هذا الزر سينقلنا لصفحة الاشتراك
    ]

    for i, item in enumerate(items):
        with [col1, col2, col3][i % 3]:
            st.markdown(f"""
                <div class="icon-box">
                    <div style="font-size:2.5rem;">{item['icon']}</div>
                    <h3>{item['title']}</h3>
                </div>
            """, unsafe_allow_html=True)
            if st.button("", key=f"btn_{i}"):
                if item['id'] == 'sub':
                    st.session_state.page = 'subscription'
                    st.rerun()
                else:
                    st.session_state.active_tool = item['title']

# --- صفحة الاشتراك (Subscription) ---
elif st.session_state.page == 'subscription':
    st.markdown("""
        <div class="sub-page">
            <h1 style="color:#00f2ff; text-shadow:0 0 15px #00f2ff;">اشتراك النخبة</h1>
            <p style="color:#fff; font-size:1.2rem;">وصول كامل لجميع حلول أثير للتقنية</p>
            <div style="font-size:3.5rem; font-weight:900; color:#d4af37; margin:20px 0;">49$</div>
            <div style="background:rgba(0,0,0,0.5); padding:20px; border-radius:15px; border:1px solid #d4af37; text-align:right;">
                <p style="color:#d4af37;">Payoneer: SADAM.ALHAJ007@GMAIL.COM</p>
                <p style="color:#34a853; font-size:0.8rem;">USDT: TKCvNEvz59717dp5QZbrwCqCzTQqjrNxCX</p>
            </div>
            <br>
            <p style="color:#fff;">يرجى إرسال إيصال الدفع لتفعيل العضوية</p>
    """, unsafe_allow_html=True)
    
    if st.button("العودة للرئيسية"):
        st.session_state.page = 'home'
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- محرك الذكاء الاصطناعي (عند الضغط على النوافذ الأخرى) ---
if 'active_tool' in st.session_state and st.session_state.page == 'home':
    st.markdown(f'<div style="max-width:800px; margin:20px auto; padding:20px; border:1px solid #d4af37; color:#d4af37; border-radius:15px; background:rgba(212,175,55,0.05);">تم تفعيل وحدة: {st.session_state.active_tool} <br> جاري تهيئة التشخيص الذكي...</div>', unsafe_allow_html=True)
