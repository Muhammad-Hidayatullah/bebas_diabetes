import streamlit as st
from assets import database as db
import time

st.logo("assets/logo_diabetes.png", size="large")
st.html("""
  <style>
    [alt=Logo] {
      height: 6rem;
    }
  </style>
        """)
st.logo("assets/logo_diabetes.png", size="large")

home_website = st.Page(
    page="pages/1_home.py",
    title="Home",
    icon=":material/home:",
)


informasi_diabetes_tipe_2 = st.Page(
    page="pages/2_diabetes_tipe_2.py",
    title="Diabetes Tipe 2",
    icon=":material/glucose:",
)

diagnosis_diabetes_tipe_2 = st.Page(
    page="pages/3_diagnosis_diabetes_tipe_2.py",
    title="Diagnosis Diabetes Tipe 2",
    icon=":material/diagnosis:",
)

admin = st.Page(
    page="pages/4_login_admin.py",
    title="Admin",
    icon=":material/diagnosis:",
)

artikel = st.Page(
    page="pages/5_artikel.py",
    title="Artikel",
    icon=":material/library_books:",
)

bantuan = st.Page(
    page="pages/6_bantuan.py",
    title="Bantuan",
    icon=":material/help:",
)




home_website_admin = st.Page(
    page="pages_admin/1_home_admin.py",
    title="Home",
    icon=":material/home:",
)   

halaman_admin = st.Page(
    page="pages_admin/2_admin.py",
    title="Admin",
    icon=":material/shield_person:",
)  

halaman_penyakit = st.Page(
    page="pages_admin/3_penyakit.py",
    title="Penyakit",
    icon=":material/microbiology:",
)

halaman_gejala = st.Page(
    page="pages_admin/4_gejala.py",
    title="Gejala",
    icon=":material/symptoms:",
)

halaman_relasi_dan_gejala = st.Page(
    page="pages_admin/5_relasi_penyakit_dan_gejala.py",
    title="Relasi Penyakit dan Gejala",
    icon=":material/fact_check:",
)

halaman_artikel = st.Page(
    page="pages_admin/6_artikel.py",
    title="Artikel",
    icon=":material/article:",
)

halaman_pasien = st.Page(
    page="pages_admin/7_pasien.py",
    title="Pasien",
    icon=":material/patient_list:",
)

halaman_log_out = st.Page(
    page="pages_admin/8_log_out.py",
    title="Log Out",
    icon=":material/logout:"
)


if "masuk_website_admin" not in st.session_state:
    st.session_state.masuk_website_admin = None

if st.session_state.masuk_website_admin == None:
    st.session_state.pg = st.navigation(pages=[home_website, informasi_diabetes_tipe_2, diagnosis_diabetes_tipe_2, 
                                               artikel, admin, bantuan])
    st.session_state.pg.run()
    
if st.session_state.masuk_website_admin == True:
    st.session_state.pg = st.navigation(pages=[home_website_admin, halaman_admin, halaman_penyakit,
                                               halaman_gejala, halaman_relasi_dan_gejala, 
                                               halaman_pasien, halaman_artikel, halaman_log_out])
    st.session_state.pg.run()



