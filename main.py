import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PyPDF2 import PdfReader # مكتبة قراءة الـ PDF

st.set_page_config(page_title="AI Resume Analyzer Pro", page_icon="📄")

st.title("📄 AI Resume Analyzer Pro")
st.subheader("ارفع الـ CV بتاعك وشوف الذكاء الاصطناعي هيقولك إيه!")

# 1. خاصية رفع الملف


uploaded_file = st.file_uploader("ارفع سيرتك الذاتية (PDF)", type="pdf")

# 2. تحويل الـ PDF لنص
resume_text = ""
if uploaded_file is not None:
    pdf_reader = PdfReader(uploaded_file)
    for page in pdf_reader.pages:
        resume_text += page.extract_text()

# لو مرفعش ملف، ممكن يكتب نص عادي
if not resume_text:
    resume_text = st.text_area("أو الصق نص السيرة الذاتية هنا:", height=150)

if st.button("بدء التحليل الشامل 🔍"):
    if resume_text:
        # حساب السكور (Score) بشكل بسيط
        skills = ["Python", "SQL", "Machine Learning", "Data Analysis", "Communication", "Project Management", "Excel"]
        found_skills = [s for s in skills if s.lower() in resume_text.lower()]
        score = (len(found_skills) / len(skills)) * 100

        # عرض النتائج
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("### 📊 تقييم الـ CV")
            st.metric("قوة السيرة الذاتية", f"{int(score)}%")
            st.progress(int(score))
            
            st.markdown("### ✅ المهارات المكتشفة")
            if found_skills:
                for f in found_skills:
                    st.success(f)
            else:
                st.info("لم نجد مهارات تقنية معروفة، حاول إضافة كلمات مفتاحية أكتر.")
        
        with col2:
            st.markdown("### ☁️ سحابة الكلمات")
            wc = WordCloud(background_color="white", width=800, height=500).generate(resume_text)
            fig, ax = plt.subplots()
            ax.imshow(wc, interpolation='bilinear')
            ax.axis("off")
            st.pyplot(fig)
    else:
        st.warning("دخل ملف PDF أو اكتب نص عشان نبدأ!")