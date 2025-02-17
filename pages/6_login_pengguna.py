import streamlit as st
from assets import database as db
import time
import datetime
import re


def variabel_awal_pasien():
    st.session_state.next = -2
    st.session_state.kode_pasien = ""
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
    variabel_awal_pasien()
    
with st.form("login-pasien"):
    if not st.session_state.logged_in_pengguna:
        st.title("Halaman Login Pengguna")
        
        # Input username dan password hanya terlihat jika belum login
        st.session_state.username_pengguna = st.text_input("Masukkan username:")
        input_password = st.text_input("Masukkan password:", type="password")
        
        if st.form_submit_button(label="Login"):
            # Validasi login
            
            if db.check_pengguna(st.session_state.username_pengguna, input_password) == True:
                
                st.session_state.logged_in_pengguna = True
                st.session_state.masuk_website = "Pengguna"
                st.success(f"Login berhasil! Selamat datang, {st.session_state.username_pengguna}.")
                time.sleep(2)
                st.rerun()
                
            else:
                st.error("Username atau password salah.")
            
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

with st.form("registrasi-pasien"):
    if st.session_state.logged_in_pengguna == "Registrasi":
        st.title("Registrasi")
        st.write("Silahkan lakukan registrasi")
        st.session_state.username_pengguna = ""
        st.session_state.username_pengguna = st.text_input("Masukkan username: ")
        password_pengguna = ""
        password_pengguna = st.text_input("Masukkan password: ", type="password")
        
        
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
            cek_validasi_data_pasien = db.check_data_registrasi_pasien(st.session_state.username_pengguna, email, password_pengguna, st.session_state.nama, alamat)
                
            if cek_validasi_data_pasien == True:
                st.success("Data valid.")
                db.add_pasien(db.menambah_id_pasien_default(), st.session_state.username_pengguna, password_pengguna, st.session_state.nama, jenis_kelamin, alamat, email, pekerjaan, tanggal_lahir)
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


    


    
    
