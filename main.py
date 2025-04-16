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


informasi_sistem = st.Page(
    page="pages/2_informasi_sistem.py",
    title="Informasi Sistem",
    icon = ":material/wysiwyg:",
)


artikel = st.Page(
    page="pages/3_artikel.py",
    title="Artikel",
    icon=":material/library_books:",
)

bantuan = st.Page(
    page="pages/4_bantuan.py",
    title="Bantuan",
    icon=":material/help:",
)

login_pengguna = st.Page(
    page="pages/5_login_pengguna.py",
    title = "Login Pengguna",
    icon = ":material/login:",
)



#Halaman untuk pengguna
data_pengguna = st.Page(
    page="pages_pengguna/1_data_pengguna.py",
    title="Profil Pengguna",
    icon=":material/account_circle:",
)

diagnosis = st.Page(
    page="pages_pengguna/2_diagnosis.py",
    title = "Diagnosis",
    icon=":material/medical_services:",
)

riwayat = st.Page(
    page="pages_pengguna/3_riwayat.py",
    title="Riwayat",
    icon=":material/history:",
)

log_out = st.Page(
    page="pages_pengguna/4_log_out.py",
    title="Log Out",
    icon=":material/logout:",
)




if "masuk_website" not in st.session_state:
    st.session_state.masuk_website = None

if st.session_state.masuk_website == None:
    st.session_state.pg = st.navigation(pages=[home_website, informasi_sistem,
                                               artikel, bantuan, login_pengguna])
    
    
    st.session_state.pg.run()
    

    

if st.session_state.masuk_website == "Pengguna":
    st.session_state.pg = st.navigation(pages=[data_pengguna, diagnosis, riwayat, log_out])
    st.session_state.pg.run()




