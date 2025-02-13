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



pg_bg_img = """
<style> 

[data-testid="stSidebar"]{
    background-image: url("https://images.unsplash.com/photo-1581159186721-b68b78da4ec9?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;
}
</style>

"""

st.markdown(pg_bg_img, unsafe_allow_html=True)



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



admin = st.Page(
    page="pages/3_login_admin.py",
    title="Admin",
    icon=":material/diagnosis:",
)

artikel = st.Page(
    page="pages/4_artikel.py",
    title="Artikel",
    icon=":material/library_books:",
)

bantuan = st.Page(
    page="pages/5_bantuan.py",
    title="Bantuan",
    icon=":material/help:",
)

login_pengguna = st.Page(
    page="pages/6_login_pengguna.py",
    title = "Login Pengguna",
    icon = ":material/login:",
)


#Halaman untuk Pasien
data_pasien = st.Page(
    page="pages_pasien/1_data_pasien.py",
    title="Data Pasien",
    icon=":material/account_circle:",
)

pemeriksaan_kesehatan = st.Page(
    page="pages_pasien/2_pemeriksaan_kesehatan.py",
    title = "Pemeriksaan Faktor Risiko",
    icon=":material/medical_services:",
)

riwayat = st.Page(
    page="pages_pasien/3_riwayat.py",
    title="Riwayat",
    icon=":material/history:",
)

log_out = st.Page(
    page="pages_pasien/4_log_out.py",
    title="Log Out",
    icon=":material/logout:",
)

#Halaman untuk admin
home_website_admin = st.Page(
    page="pages_admin/1_home_admin.py",
    title="Home",
    icon=":material/home:",
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





if "masuk_website" not in st.session_state:
    st.session_state.masuk_website = None

if st.session_state.masuk_website == None:
    st.session_state.pg = st.navigation(pages=[home_website, informasi_diabetes_tipe_2, 
                                               artikel, admin, bantuan, login_pengguna])
    st.session_state.pg.run()
    
if st.session_state.masuk_website == "Admin":
    st.session_state.pg = st.navigation(pages=[halaman_penyakit, halaman_gejala, halaman_relasi_dan_gejala, 
                                               halaman_pasien, halaman_artikel, halaman_log_out])
    st.session_state.pg.run()
    

if st.session_state.masuk_website == "Pengguna":
    st.session_state.pg = st.navigation(pages=[data_pasien, pemeriksaan_kesehatan, riwayat, log_out])
    st.session_state.pg.run()




