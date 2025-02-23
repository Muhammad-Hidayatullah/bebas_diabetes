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
        
        
        
        st.title("Data Pasien")
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

        st.write("")
        st.write("")

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

if st.session_state.lanjut == 2:
    update_data_berhasil = False
    with st.form("form-update-data-pasien"):
        st.title("Update Data Pasien")
        st.warning("Apabila ada nilai yang tidak ingin diubah, jangan diganti!")
        username = st.text_input("Masukkan username baru: ", value=st.session_state.username_pengguna)
        password = st.text_input("Masukkan password baru: ", type= "password", value=st.session_state.password_pengguna)
        nama = st.text_input("Masukkan nama lengkap baru: ", value=st.session_state.nama_lengkap)
        jenis_kelamin = st.radio("Jenis Kelamin: ", ("LAKI-LAKI", "PEREMPUAN"), horizontal=True, index=("LAKI-LAKI", "PEREMPUAN").index(st.session_state.jenis_kelamin))
        alamat = st.text_input("Masukkan alamat baru: ", value=st.session_state.alamat)
        email = st.text_input("Masukkan email baru: ", value=st.session_state.email)
        

        pekerjaan = st.selectbox("Masukkan pekerjaan baru: ", options=st.session_state.pekerjaan_pekerjaan, index=st.session_state.pekerjaan_pekerjaan.index(st.session_state.pekerjaan)) 
        
        
        tanggal_lahir = st.date_input("Masukkan tanggal lahir: (y-m-d)", min_value=datetime.date(1900, 1, 1), max_value=datetime.datetime.now(), value=st.session_state.tanggal_lahir)
        
        
        col1, col2 = st.columns(2)
        validation_errors = False
        with col1:
            if st.form_submit_button(label="Kembali"):
                st.session_state.lanjut = 0
                st.rerun()
                
        with col2:
            update_data_berhasil = False
            if st.form_submit_button(label="Update"):

                
                validation_errors = []
                
                if db.cek_username(username) == True and username != st.session_state.username_pengguna:
                    validation_errors.append("Username sudah terdaftar")

                    
                if db.cek_email(email) == True and email != st.session_state.email:
                    validation_errors.append("Email Sudah Terdaftar")
                # Check if username is provided
                if not st.session_state.username_pengguna:
                    validation_errors.append("Username tidak boleh kosong.")

                # Check if password is provided and meets the length requirement
                if not password or not validasi_password(password):
                    validation_errors.append("Password harus lebih dari 6 karakter.")

                # Check if full name is provided
                if not nama:
                    validation_errors.append("Nama lengkap tidak boleh kosong.")

                # Check if email is provided and valid
                if not email or not validasi_email_regex(email):
                    validation_errors.append("Email tidak valid. Pastikan menggunakan format yang benar (@gmail.com).")

                # Check if address is provided
                if not alamat:
                    validation_errors.append("Alamat tidak boleh kosong.")

                # Display validation errors
        if validation_errors:
            for error in validation_errors:
                st.error(error)
        else:
            update_data_berhasil = True
            db.update_pengguna(username, password, nama, jenis_kelamin, alamat, email, pekerjaan, tanggal_lahir, st.session_state.username_pengguna)
            
                    
            
        if update_data_berhasil == True:
            st.success("Update Data Anda Berhasil!.")
            st.session_state.username_pengguna = username
            st.session_state.lanjut = 0
            time.sleep(2)
            st.rerun()
        
    
