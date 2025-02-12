import streamlit as st
from assets import database as db
import datetime
from fpdf import FPDF
import time
import pandas as pd
import re


    



    
    
def validasi_email_regex(email):
    regex = r'^[a-zA-Z0-9_.+-]+@gmail\.com$'
    return re.match(regex, email) is not None



def validasi_password(password):
    return len(password) >= 7  # Minimum length of 6 characters


if "lanjut" not in st.session_state:
    st.session_state.lanjut = 0
    
    
if st.session_state.lanjut == 0:
    with st.form("form_data_pasien"):
        st.title("Data Pasien")
        
        if "data_pasien" not in st.session_state:
            st.session_state.data_pasien = []
        
        st.session_state.data_pasien = db.get_data_pasien(st.session_state.username_pengguna)
        
        # Mengambil data dari database
        st.session_state.kode_pasien = st.session_state.data_pasien[0]
        st.session_state.username_pengguna = st.session_state.data_pasien[1]
        st.session_state.password_pengguna = st.session_state.data_pasien[2]
        st.session_state.nama_lengkap = st.session_state.data_pasien[3]
        st.session_state.jenis_kelamin = st.session_state.data_pasien[4]
        st.session_state.alamat = st.session_state.data_pasien[5]
        st.session_state.email = st.session_state.data_pasien[6]
        st.session_state.pekerjaan = st.session_state.data_pasien[7]
        st.session_state.tanggal_lahir = st.session_state.data_pasien[8]
        
        
        
        
        st.write("Kode Pasien       : " + st.session_state.kode_pasien)
        st.write("Username          : " + st.session_state.username_pengguna)
        st.write("Password          : " + len(st.session_state.password_pengguna) * "*")
        st.write("Nama Lengkap      : " + st.session_state.nama_lengkap)
        st.write("Jenis Kelamin     : " + st.session_state.jenis_kelamin)
        st.write("Alamat            : " + st.session_state.alamat)
        st.write("Email             : " + st.session_state.email)
        st.write("Pekerjaan         : " + st.session_state.pekerjaan)
        st.write("Tanggal Lahir     : " + str(st.session_state.tanggal_lahir))


        
        if "update_data" not in st.session_state:
            st.session_state.update_data = 0

        
            
        if st.form_submit_button(label="Update Data"):
            st.session_state.update_data = 1
                
            
        if st.session_state.update_data == 1:
            password_pengguna = st.text_input("Masukkan password Anda: ", type="password")
            if st.form_submit_button("Klik"):
                if db.check_pengguna(st.session_state.username_pengguna, password_pengguna) == True:
                    st.session_state.lanjut = 2
                    st.session_state.update_data = 0
                    st.rerun()
                else:
                    st.warning("Password yang Anda masukkan salah!")













    