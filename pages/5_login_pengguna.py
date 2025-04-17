import streamlit as st
from assets import database as db
import time
import datetime
import re
from assets import fungsi_pemeriksaan

def variabel_awal_pengguna():
    st.session_state.next = -2
    st.session_state.kode_pengguna = ""
    st.session_state.nama = ""
    st.session_state.username_pengguna = ""
    st.session_state.password_pengguna = ""
    st.session_state.tanggal_lahir = datetime.date.today()
    st.session_state.pekerjaan = ""
    st.session_state.email = ""
    # sesuai KTP
    st.session_state.pekerjaan_pekerjaan = [
    "Belum / Tidak Bekerja",
    "Mengurus Rumah Tangga",
    "Pelajar / Mahasiswa",
    "Pensiunan",
    "Pegawai Negeri Sipil",
    "Tentara Nasional Indonesia",
    "Kepolisian RI",
    "Perdagangan",
    "Petani / Pekebun",
    "Peternak",
    "Nelayan / Perikanan",
    "Industri",
    "Konstruksi",
    "Transportasi",
    "Karyawan Swasta",
    "Karyawan BUMN",
    "Karyawan BUMD",
    "Karyawan Honorer",
    "Buruh Harian Lepas",
    "Buruh Tani / Perkebunan",
    "Buruh Nelayan / Perikanan",
    "Buruh Peternakan",
    "Pembantu Rumah Tangga",
    "Tukang Cukur",
    "Tukang Listrik",
    "Tukang Batu",
    "Tukang Kayu",
    "Tukang Sol Sepatu",
    "Tukang Las / Pandai Besi",
    "Tukang Jahit",
    "Penata Rambut",
    "Penata Rias",
    "Penata Busana",
    "Mekanik",
    "Tukang Gigi",
    "Seniman",
    "Tabib",
    "Paraji",
    "Perancang Busana",
    "Penterjemah",
    "Imam Masjid",
    "Pendeta",
    "Pastur",
    "Wartawan",
    "Ustadz / Mubaligh",
    "Juru Masak",
    "Promotor Acara",
    "Anggota DPR-RI",
    "Anggota DPD",
    "Anggota BPK",
    "Presiden",
    "Wakil Presiden",
    "Anggota Mahkamah Konstitusi",
    "Anggota Kabinet / Kementerian",
    "Duta Besar",
    "Gubernur",
    "Wakil Gubernur",
    "Bupati",
    "Wakil Bupati",
    "Walikota",
    "Wakil Walikota",
    "Anggota DPRD Propinsi",
    "Anggota DPRD Kabupaten / Kota",
    "Dosen",
    "Guru",
    "Pilot",
    "Pengacara",
    "Notaris",
    "Arsitek",
    "Akuntan",
    "Konsultan",
    "Dokter",
    "Bidan",
    "Perawat",
    "Apoteker",
    "Psikiater / Psikolog",
    "Penyiar Televisi",
    "Penyiar Radio",
    "Pelaut",
    "Peneliti",
    "Sopir",
    "Pialang",
    "Paranormal",
    "Pedagang",
    "Perangkat Desa",
    "Kepala Desa",
    "Biarawati",
    "Wiraswasta",
    "Anggota Lembaga Tinggi",
    "Artis",
    "Atlit",
    "Cheff",
    "Manajer",
    "Tenaga Tata Usaha",
    "Operator",
    "Pekerja Pengolahan", 
    "Kerajinan",
    "Teknisi",
    "Asisten Ahli",
    "Lainnya"
    ]

    
    st.session_state.tanggal_pemeriksaan = datetime.date.today()
    st.session_state.alamat = ""
    st.session_state.jenis_kelamin = "LAKI-LAKI"




if "logged_in_pengguna" not in st.session_state:
    st.session_state.logged_in_pengguna = False
    st.session_state.username = ""
    fungsi_pemeriksaan.variabel_awal_pengguna()
    

    
    
with st.form("login-pengguna"):
    if not st.session_state.logged_in_pengguna:
        st.title("Login Pengguna")
        berhasil_login = 0
        # Input username dan password hanya terlihat jika belum login
        st.session_state.username_pengguna = st.text_input("Masukkan username:", placeholder="username")
        input_password = st.text_input("Masukkan password:", type="password", placeholder="password")
        
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.form_submit_button(label="Login"):
                # Validasi login
                
                if db.check_pengguna(st.session_state.username_pengguna, input_password) == True:
                    berhasil_login = 1
                    
                    
                else:
                    berhasil_login = 2
                    
        if berhasil_login == 1:
            st.session_state.logged_in_pengguna = True
            st.session_state.masuk_website = "Pengguna"
            st.success(f"Login berhasil! Selamat datang, {st.session_state.username_pengguna}.")
            time.sleep(2)
            st.rerun()
        if berhasil_login == 2:
            st.error("Username atau password salah.")
                    
        with col3:
            if st.form_submit_button(label="Reset Password"):
                st.session_state.logged_in_pengguna = "Reset Password"
                st.rerun()
                
            
        st.write("")
        st.write("")
        st.write("")
        st.write("")
            
        st.write("Belum memiliki akun? Klik tombol registrasi di bawah ini!")
        if st.form_submit_button(label="Registrasi"):
            st.session_state.logged_in_pengguna = "Registrasi"
            st.rerun()


def validasi_email_regex(email):
    regex = r'^[a-zA-Z0-9_.+-]+@gmail\.com$'
    return re.match(regex, email) is not None

def validasi_password(password):
    return len(password) >= 7  # Minimum length of 6 characters





with st.form("reset-password"):
    if st.session_state.logged_in_pengguna == "Reset Password":
        st.title("Lupa Password")
        st.session_state.input_username = st.text_input("Masukkan username Anda: ", placeholder = "username")
        st.session_state.input_email = st.text_input("Masukkan email Anda:", placeholder = "email")
        
        validitas_email = 0
        
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.form_submit_button("Lanjut"):
                cek_username_email_pengguna = db.cek_lupa_password_pengguna(st.session_state.input_username, st.session_state.input_email)
                
                if not validasi_email_regex(st.session_state.input_email):
                    validitas_email = 1
                   
                else:
                    validitas_email = 2
                    
        if validitas_email == 1:
            st.error("Email tidak valid. Pastikan menggunakan format yang benar (@gmail.com)!")
        
        if validitas_email == 2:
            if cek_username_email_pengguna == True:
                st.session_state.logged_in_pengguna = "Ganti Password"
                st.success("Username dan Email Pengguna Ditemukan")
                time.sleep(2)
                st.rerun()
            else:
                st.error("Username dan Email tersebut tidak ditemukan!")
                
with st.form("Ganti Password"):
    if st.session_state.logged_in_pengguna == "Ganti Password":
       
        st.title("Ganti Password Pengguna")
        input_password_baru = st.text_input("Masukkan password baru: ", type="password", placeholder="password baru")
        input_password_baru_ulang = st.text_input("Ulangi password baru: ", type="password", placeholder="ulangi password baru")
        if st.form_submit_button("Ganti Password"):
            if input_password_baru == input_password_baru_ulang:
                db.reset_password_pengguna(input_password_baru, st.session_state.input_username, st.session_state.input_email)
                st.success("Password Berhasil Diganti Dengan Password Baru")
                time.sleep(2)
                st.session_state.logged_in_pengguna = False
                st.rerun()
            else:
                st.error("Password Baru dan Password Baru Ulang Tidak Sama!")
        





with st.form("registrasi-pengguna"):
    if st.session_state.logged_in_pengguna == "Registrasi":
        st.title("Registrasi")
        st.write("Silahkan lakukan registrasi")
        st.session_state.username_pengguna = ""
        st.session_state.username_pengguna = st.text_input("Masukkan username: ")
        password_pengguna = ""
        password_pengguna = st.text_input("Masukkan password: ", type="password")
        
        st.session_state.nama = ""
        st.session_state.nama = st.text_input("Nama Lengkap: ", value=st.session_state.nama)
        jenis_kelamin = st.radio("Jenis Kelamin", ("LAKI-LAKI", "PEREMPUAN"), horizontal=True, index=("LAKI-LAKI", "PEREMPUAN").index(st.session_state.jenis_kelamin))
        tanggal_lahir = st.date_input("Masukkan tanggal lahir: (y-m-d)", min_value=datetime.date(1900, 1, 1), max_value=datetime.datetime.now())
        
        
        pekerjaan = st.selectbox("Pekerjaan: ", options=st.session_state.pekerjaan_pekerjaan)
        if pekerjaan == "Lainnya":
            pekerjaan_lainnya = st.text_input("Pekerjaan: ")
            pekerjaan = pekerjaan_lainnya
        
        
        email = st.text_input("Masukkan email: ", value=st.session_state.email)
        
        alamat = st.text_input("Alamat Tempat Tinggal: ", value=st.session_state.alamat)

        
        if st.form_submit_button(label="Registrasi"):
            cek_validasi_data_pengguna = db.check_data_registrasi_pengguna(st.session_state.username_pengguna, email, password_pengguna, st.session_state.nama, tanggal_lahir, alamat)
                
            if cek_validasi_data_pengguna == True:
                st.success("Berhasil melakukan registrasi.")
                enkripsi_password = db.enkripsi_password(password_pengguna)
                db.add_pengguna(db.menambah_id_pengguna_default(), st.session_state.username_pengguna, enkripsi_password, st.session_state.nama, jenis_kelamin, alamat, email, pekerjaan, tanggal_lahir)
                time.sleep(2)
                st.session_state.logged_in_pengguna = False
                st.rerun()
                
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        
        st.write("Sudah memiliki akun? Klik tombol Login di bawah ini!")
        if st.form_submit_button(label="Login"):
            st.session_state.logged_in_pengguna = False
            st.rerun()


    


    
    
