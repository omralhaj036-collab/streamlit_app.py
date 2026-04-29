import streamlit as st
import requests
import json

# --- إعدادات الصفحة ---
st.set_page_config(page_title="Atheer Technology | أثير للتقنية", layout="wide")

# --- التصميم الفاخر (CSS المتقدم لمحاكاة الصورة) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* الخلفية الإلكترونية المتحركة */
    .stApp {
        background: #000;
        background-image: 
            radial-gradient(circle at 20% 30%, rgba(212, 175, 55, 0.15) 0%, transparent 50%),
            url('https://www.transparenttextures.com/patterns/carbon-fibre.png');
        font-family: 'Cairo', sans-serif;
    }

    /* تأثير الخطوط النيوتنية */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: url('https://www.transparenttextures.com/patterns/microfab.png');
        opacity: 0.2;
        z-index: -1;
        animation: pulse 5s infinite alternate;
    }

    @keyframes pulse { from { opacity: 0.1; } to { opacity: 0.3; } }

    /* الشعار الذهبي الكبير */
    .main-header {
        text-align: center;
        padding: 20px;
        background: linear-gradient(180deg, #d4af37 0%, #8a6d3b 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 4.5rem !important;
        font-weight: 900;
        filter: drop-shadow(0 0 15px rgba(212, 175, 55, 0.5));
    }

    /* شبكة النوافذ (مطابقة للصورة) */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 25px;
        max-width: 900px;
        margin: auto;
        direction: rtl;
    }

    /* تصميم النافذة الذهبية (مثل الصورة تماماً) */
    .nav-card {
        background: rgba(20, 20, 20, 0.8);
        border: 2px solid #d4af37;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        position: relative;
        transition: 0.3s ease;
        cursor: pointer;
        box-shadow: 0 0 10px rgba(212, 175, 55, 0.2);
        clip-path: polygon(10% 0, 90% 0, 100% 15%, 100% 85%, 90% 100%, 10% 100%, 0 85%, 0 15%);
    }

    .nav-card:hover {
        background: rgba(212, 175, 55, 0.1);
        transform: scale(1.05);
        box-shadow: 0 0 25px #d4af37;
    }

    .nav-card i {
        color: #d4af37;
        font-size: 2.5rem;
        display: block;
        margin-bottom: 10px;
    }

    .nav-card h3 {
        color: #d4af37;
        font-size: 0.85rem;
        font-weight: bold;
        margin: 0;
    }

    /* إخفاء أزرار سترمليت الافتراضية لجعلها تبدو كأنها جزء من البطاقة */
    .stButton > button {
        opacity: 0;
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        z-index: 10;
        cursor: pointer;
    }

    /* صندوق النتائج الذكي */
    .bot-response {
        background: rgba(0,0,0,0.9);
        border: 2px solid #d4af37;
        color: #fff;
        padding: 30px;
        border-radius: 20px;
        margin-top: 30px;
        box-shadow: 0 0 30px rgba(212, 175, 55, 0.3);
        direction: rtl;
        font-size: 1.1rem;
    }
</style>
""", unsafe_allow_html=True)

# --- محرك البوت الذكي (Groq) ---
def atheer_bot(category, prompt):
    api_key = "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"
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": f"أنت خبير تقني في منصة أثير للتقنية. مهمتك هي: {category}. أجب بذكاء واحترافية."},
            {"role": "user", "content": prompt}
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return "⚠️ عذراً، نوافذ أثير تتطلب اتصالاً أقوى.. حاول مجدداً."

# --- الواجهة البرمجية ---

st.markdown("<h1 class='main-header'>أثير للتقنية</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#d4af37; letter-spacing:4px; font-weight:bold;'>ATHEER TECHNOLOGY SOLUTIONS</p>", unsafe_allow_html=True)

# تعريف النوافذ كما في الصورة
windows = [
    {"icon": "🛡️", "title": "حماية المتجر الذكي", "task": "تأمين المتاجر الإلكترونية وحمايتها"},
    {"icon": "⚙️", "title": "تحسين محركات البحث", "task": "تحليل SEO وتحسين الظهور"},
    {"icon": "🧠", "title": "تشخيص الأنظمة بالذكاء الاصطناعي", "task": "إصلاح المشاكل التقنية المعقدة"},
    {"icon": "💹", "title": "تحليلات المبيعات الذكية", "task": "تحليل البيانات وزيادة الربح"},
    {"icon": "📈", "title": "المسار الرقمي الاستراتيجي", "task": "رسم خطط التحول الرقمي"},
    {"icon": "👤", "title": "بناء الهوية الرقمية", "task": "تصميم وتطوير العلامة التجارية"},
    {"icon": "👁️", "title": "الرؤى", "task": "تقديم رؤى استراتيجية للمستقبل"},
    {"icon": "💎", "title": "باقة الاشتراك المحترف", "task": "تقديم عروض الاشتراك VIP"},
    {"icon": "🤖", "title": "بوت ذكي", "task": "مساعد ذكي شامل لخدمتك"}
]

# رسم النوافذ (Grid)
st.markdown("<div class='grid-container'>", unsafe_allow_html=True)
cols = st.columns(3)

for i, win in enumerate(windows):
    with cols[i % 3]:
        # عرض الشكل الجمالي
        st.markdown(f"""
            <div class='nav-card'>
                <div style='font-size: 2.5rem;'>{win['icon']}</div>
                <h3>{win['title']}</h3>
            </div>
        """, unsafe_allow_html=True)
        
        # تفعيل الزر المخفي للعمل
        if st.button("Open", key=f"win_{i}"):
            st.session_state.active_win = win

st.markdown("</div>", unsafe_allow_html=True)

# تفعيل البوت عند الضغط على أي نافذة
if 'active_win' in st.session_state:
    st.markdown("<br><hr style='border-color:#d4af37;'>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center; color:#d4af37;'>وحدة: {st.session_state.active_win['title']}</h2>", unsafe_allow_html=True)
    
    user_query = st.text_input("صف المشكلة أو الطلب هنا ليقوم البوت بمعالجته:", placeholder="مثلاً: كيف أحمي متجري من الاختراق؟")
    
    if st.button("بدء التشخيص الذكي ⚡"):
        if user_query:
            with st.spinner('جاري الاتصال بالعقل الاصطناعي لأثير...'):
                ans = atheer_bot(st.session_state.active_win['task'], user_query)
                st.markdown(f"<div class='bot-response'>{ans}</div>", unsafe_allow_html=True)

# التذييل (بيانات الدفع الخاصة بك)
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown(f"""
    <div style='text-align:center; padding:30px; background:rgba(212,175,55,0.05); border-radius:50px;'>
        <p style='color:#d4af37; font-weight:bold;'>SADAM.ALHAJ007@GMAIL.COM : Payoneer</p>
        <p style='color:#34a853; font-size:0.8rem;'>USDT: TKCvNEvz59717dp5QZbrwCqCzTQqjrNxCX</p>
    </div>
""", unsafe_allow_html=True)
