import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PyPDF2 import PdfReader

# إعداد الصفحة
st.set_page_config(page_title="AI Resume Analyzer Pro", page_icon="📄", layout="wide")

st.title("📄 AI Resume Analyzer Pro")
st.subheader("حلل سيرتك الذاتية واعرف توافقك مع مهارات سوق العمل")

# 1. خيار رفع الملف أو كتابة النص
uploaded_file = st.file_uploader("ارفع سيرتك الذاتية (PDF)", type="pdf")
text_input = st.text_area("أو الصق نص السيرة الذاتية هنا مباشرة:", height=150)

# مهارات سوق العمل المستهدفة (قائمة الـ 100%)
target_skills = [
    "Python", "SQL", "Machine Learning", "Data Analysis", "Communication", 
    "Project Management", "Excel", "Streamlit", "Pandas", "Git", "GitHub", "Plotly",
    "NumPy", "Scikit-Learn", "Power BI", "Data Visualization", "EDA", "Statistical Analysis"
]

if st.button("تحليل الآن 🔍"):
    resume_text = ""
    
    # استخراج النص من الـ PDF لو موجود
    if uploaded_file is not None:
        pdf_reader = PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            content = page.extract_text()
            if content:
                resume_text += content
    elif text_input:
        resume_text = text_input

    if resume_text:
        # البحث عن المهارات المكتشفة
        found_skills = [skill for skill in target_skills if skill.lower() in resume_text.lower()]
        
        # حساب السكور
        score = (len(found_skills) / len(target_skills)) * 100

        # تقسيم الصفحة لنتائج
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("### 📊 تقييم السيرة الذاتية")
            st.metric("نسبة التوافق (ATS Score)", f"{int(score)}%")
            st.progress(int(score))
            
            if score == 100:
                st.balloons()
                st.success("تهانينا! سيرتك الذاتية مطابقة تماماً لمتطلبات الوظيفة!")
            elif score > 70:
                st.info("سيرة ذاتية قوية جداً، يمكنك إضافة المهارات الناقصة للوصول للكمال.")
            else:
                st.warning("حاول إضافة المزيد من الكلمات المفتاحية لزيادة فرصك.")

            st.markdown("### ✅ المهارات المكتشفة")
            for f in found_skills:
                st.write(f"- {f}")
            
            # إظهار المهارات الناقصة لمساعدة المستخدم
            missing_skills = list(set(target_skills) - set(found_skills))
            if missing_skills:
                with st.expander("💡 مهارات ينصح بإضافتها:"):
                    for m in missing_skills:
                        st.write(f"- {m}")

        with col2:
            st.markdown("### ☁️ سحابة الكلمات (WordCloud)")
            try:
                wc = WordCloud(background_color="white", width=800, height=500).generate(resume_text)
                fig, ax = plt.subplots()
                ax.imshow(wc, interpolation='bilinear')
                ax.axis("off")
                st.pyplot(fig)
            except:
                st.error("عذراً، النص غير كافٍ لإنشاء سحابة كلمات.")
    else:
        st.warning("من فضلك ارفع ملف PDF أو الصق نص الـ CV أولاً!")