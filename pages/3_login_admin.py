import streamlit as st
from assets import database as db
import time


if "logged_in_admin" not in st.session_state:
    st.session_state.logged_in_admin = False
    st.session_state.username = ""

with st.form("login-admin"):
    if not st.session_state.logged_in_admin:
        st.title("Halaman Login Admin")
        
        # Input username dan password hanya terlihat jika belum login
        input_username = st.text_input("Masukkan username admin:")
        input_password = st.text_input("Masukkan password:", type="password")
        
        if st.form_submit_button(label="Login"):
            # Validasi login
            if db.check_admin(input_username, input_password) == True:
        
                st.session_state.logged_in_admin = True
                st.session_state.masuk_website = "Admin"
                st.session_state.username = input_username
                st.success(f"Login berhasil! Selamat datang, {input_username}.")
                time.sleep(2)
                st.rerun()
                
            else:
                st.error("Username atau password salah.")
            

    
    

            

    
    


    


    
    
