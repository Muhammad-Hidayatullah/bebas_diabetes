import streamlit as st
from assets import database as db
import time


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""
    
if not st.session_state.logged_in:
    st.title("Halaman Login Admin")
    
    # Input username dan password hanya terlihat jika belum login
    input_username = st.text_input("Masukkan username admin:")
    input_password = st.text_input("Masukkan password:", type="password")
    
    if st.button(label="Login"):
        # Validasi login
        if db.check_admin(input_username, input_password) == True:
    
            st.session_state.logged_in = True
            st.session_state.masuk_website_admin = 1
            st.session_state.username = input_username
            st.success(f"Login berhasil! Selamat datang, {input_username}.")
            time.sleep(2)
            st.rerun()
            
        else:
            st.error("Username atau password salah.")
            

    
    


    


    
    