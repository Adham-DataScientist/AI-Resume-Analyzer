import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄")

st.title("📄 AI Resume Analyzer")
st.subheader("حلل سيرتك الذاتية بضغطة زر")

# 1. مكان رفع الملف أو كتابة النص
text_input = st.text_area("أو الصق نص السيرة الذاتية هنا مباشرة:", height=200)

if st.button("تحليل الآن 🔍"):
    if text_input:
        # 2. تقسيم الصفحة لنتائج
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### ✅ المهارات المكتشفة")
            # هنا ممكن نعمل بحث عن كلمات معينة
            skills = ["Python", "SQL", "Machine Learning", "Communication", "Management"]
            found = [s for s in skills if s.lower() in text_input.lower()]
            for f in found:
                st.success(f)
        
        with col2:
            st.markdown("### ☁️ سحابة الكلمات")
            # صنع الـ WordCloud
            wc = WordCloud(background_color="white").generate(text_input)
            fig, ax = plt.subplots()
            ax.imshow(wc, interpolation='bilinear')
            ax.axis("off")
            st.pyplot(fig)
    else:
        st.warning("من فضلك دخل نص الـ CV أولاً!")