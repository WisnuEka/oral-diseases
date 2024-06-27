import streamlit as st # type: ignore

st.title("Hasil Deteksi")

st.markdown("![Alt Text](https://cobradental.co.id/wp-content/uploads/2021/08/cara-mencegah-dan-mengobati-karies-gigi-pada-anak-1.jpg)")
st.text("caries")
# Membuat 3 kolom
col1, col2, col3 = st.columns(3)

# Menempatkan setiap link di kolom yang berbeda
with col1:
    st.page_link("pages/caries_report_page.py", label="Caries Report")
    
with col2:
    st.page_link("pages/ulcer_report_page.py", label="Ulcer (Sariawan) Report")
    
with col3:
    st.page_link("pages/gingivitis_report_page.py", label="Gingivitis Report")
