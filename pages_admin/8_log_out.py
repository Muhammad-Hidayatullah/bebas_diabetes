import streamlit as st
import time

st.write("Klik Tombol Ini Untuk Logout")

if st.button("Logout"):
    # Kode untuk melakukan logout
    # Kembali ke menu awal
    st.session_state.masuk_website_admin = None
    
    #Memunculkan kembali login admin
    st.session_state.logged_in = False
    
    #mengosongkan username
    st.session_state.username = ""
    st.success("Anda Berhasil Logut")
    time.sleep(2)
    st.rerun()