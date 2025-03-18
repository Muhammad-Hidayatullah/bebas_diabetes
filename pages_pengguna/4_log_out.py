import streamlit as st

import time
from assets import fungsi_pemeriksaan


st.title("Logout")

st.write("Klik tombol logout untuk keluar dari aplikasi")

if st.button("Log Out"):
    st.success("Anda Berhasil Logout")
    st.session_state.masuk_website = None
    st.session_state.logged_in_pengguna = False

    fungsi_pemeriksaan.variabel_awal_pengguna()
    fungsi_pemeriksaan.awal_pemeriksaan()
    time.sleep(2)
    st.rerun()
