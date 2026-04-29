import streamlit as st
import requests

# --- إعدادات الصفحة الفنية ---
st.set_page_config(page_title="Atheer Technology | أثير للتقنية", layout="wide")

# --- الهندسة البصرية (CSS) لمحاكاة الصورة تماماً ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');

    /* خلفية نيوتنية إلكترونية متحركة */
    .stApp {
        background-color: #050505;
        background-image: 
            radial-gradient(circle at 50% 50%, rgba(212, 175, 55, 0.1) 0%, transparent 80%),
            url('https://www.transparenttextures.com/patterns/dark-matter.png');
        font-family: 'Cairo', sans-serif;
        overflow-x: hidden;
    }

    /* تأثير الجزيئات الذهبية المتطايرة */
    .particles {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        z-index: -1;
        background: url('https://cdn.pixabay.com/photo/2016/11/21/13/04/black-1845214_1280.jpg');
        opacity: 0.1;
    }

    /* تصميم اللوجو الرئيسي (أثير للتقنية) */
    .main-logo {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 250px;
        filter: drop-shadow(0 0 15px #d4af37);
        padding-bottom: 30px;
    }

    /* هندسة الأزرار الذهبية (مطابقة للصورة) */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 20px;
        padding: 20px;
        direction: rtl;
    }

    .gold-button {
        background: linear-gradient(135deg, rgba(40, 40, 40, 0.9) 0%, rgba(10, 10, 10, 1) 100%);
        border: 2px solid #d4af37;
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        transition: 0.4s all ease;
        cursor: pointer;
        position: relative;
        overflow: hidden;
        box-shadow: 0 5px 15px rgba(0,0,0,0.5), inset 0 0 10px rgba(212, 175, 55, 0.2);
    }

    .gold-button:hover {
        transform: translateY(-10px) scale(1.05);
        border-color: #fff;
        box-shadow: 0 0 30px rgba(212, 175, 55, 0.6);
    }

    .gold-button img {
        width: 50px;
        margin-bottom: 15px;
        filter: sepia(1) saturate(5) hue-rotate(10deg); /* تحويل الأيقونات للون ذهبي */
    }

    .gold-button h3 {
        color: #d4af37;
        font-size: 0.9rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 0 2px 4px rgba(0,0,0,0.5);
    }

    /* نظام الإشعاع الميكانيكي في الخلفية */
    .circuit-lines {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: url('https://www.transparenttextures.com/patterns/microfab.png');
        opacity: 0.05;
        z-index: -1;
    }
    </style>

    <div class="circuit-lines"></div>
    """, unsafe_allow_html=True)

# --- محرك الذكاء الاصطناعي (Groq) للتشخيص والحلول ---
def call_atheer_ai(task, query):
    api_key = "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"
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": f"أنت خبير في {task}. قدم حلولاً تقنية احترافية لأثير للتقنية."},
            {"role": "user", "content": query}
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        return response.json()['choices'][0]['message']['content']
    except:
        return "جاري الاتصال بقاعدة بيانات أثير..."

# --- واجهة المستخدم الرئيسية ---

# اللوجو (استبدال الرابط برابط صورتك إذا رغبت)
st.markdown("<h1 style='text-align:center; color:#d4af37; font-size:3rem; text-shadow: 0 0 20px #d4af37;'>أثير للتقنية</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888; letter-spacing:3px;'>ATHEER TECHNOLOGY SOLUTIONS</p>", unsafe_allow_html=True)

# شبكة الأزرار (مطابقة تماماً للصورة)
cols = st.columns(3)

buttons = [
    {"icon": "🔍", "title": "تشخيص الأنظمة بالذكاء الاصطناعي", "task": "إصلاح الأنظمة المعقدة"},
    {"icon": "👤", "title": "بناء الهوية الرقمية الذكية", "task": "تطوير العلامات التجارية"},
    {"icon": "🛡️", "title": "حماية المتجر الذكي", "task": "الأمن السيبراني للمتاجر"},
    {"icon": "📈", "title": "تحسين محركات البحث الذكي", "task": "SEO التقني"},
    {"icon": "📊", "title": "تحليلات المبيعات الذكية", "task": "تحليل البيانات"},
    {"icon": "🚀", "title": "المسار الرقمي الاستراتيجي", "task": "التخطيط الاستراتيجي"},
    {"icon": "👁️", "title": "الرؤى", "task": "استشراف المستقبل التقني"},
    {"icon": "🎓", "title": "الخبرة", "task": "الاستشارات التقنية"},
    {"icon": "💎", "title": "باقة الاشتراك المحترف", "task": "المميزات المدفوعة"},
    {"icon": "🤖", "title": "بوت خدمة العملاء الذكي", "task": "أتمتة خدمة العملاء"},
    {"icon": "📱", "title": "التواصل", "task": "دعم العملاء"}
]

# توزيع الأزرار في المنصة
for i, btn in enumerate(buttons):
    with cols[i % 3]:
        st.markdown(f"""
            <div class="gold-button">
                <div style="font-size: 2.5rem; margin-bottom:10px;">{btn['icon']}</div>
                <h3>{btn['title']}</h3>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"دخول {i}", key=f"btn_{i}", help=f"اضغط لتفعيل {btn['title']}"):
            st.session_state.current_task = btn['task']
            st.session_state.show_input = True

# منطقة العمل (المحرك الذكي)
if 'show_input' in st.session_state:
    st.markdown("---")
    query = st.text_input(f"وحدة {st.session_state.current_task}: أدخل تفاصيل النظام أو الهوية المطلوبة")
    if st.button("بدء المعالجة الذكية"):
        with st.spinner("جاري تشخيص النظام..."):
            res = call_atheer_ai(st.session_state.current_task, query)
            st.markdown(f"""
                <div style="background:rgba(212,175,55,0.1); border:1px solid #d4af37; padding:20px; border-radius:15px; color:#fff;">
                    {res}
                </div>
            """, unsafe_allow_html=True)

# بيانات التواصل (بناءً على طلبك السابق)
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
    <div style="text-align:center; border-top:1px solid #333; padding:20px;">
        <p style="color:#d4af37;">Payoneer: SADAM.ALHAJ007@GMAIL.COM</p>
        <p style="color:#34a853; font-size:0.8rem;">USDT: TKCvNEvz59717dp5QZbrwCqCzTQqjrNxCX</p>
    </div>
""", unsafe_allow_html=True)
