import streamlit as st
from assets import database as db
import time
import datetime
import re
import pandas as pd
from fpdf import FPDF
from assets import format_laporan as fl

st.subheader("DATA PASIEN")
df_pasien = db.fetch_pasien()
df_pasien_html = df_pasien.to_html(index=False, escape=False)
st.markdown(st.session_state.style_tabel + df_pasien_html, unsafe_allow_html=True)


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

def validasi_password(password):
    return len(password) >= 7

def validasi_email_regex(email):
    regex = r'^[a-zA-Z0-9_.+-]+@gmail\.com$'
    return re.match(regex, email) is not None

pilihan_yang_ingin_dilakukan = st.selectbox("Pilih Opsi: ", ("Pasien", "Hasil"))


pilihan_pasien = st.selectbox("Opsi Yang Ingin Dilakukan Pada Data Pasien: ", ("Tambah", "Update", "Hapus"))
if pilihan_pasien == "Tambah":
    st.subheader("Tambah Data Pasien")
    username_pengguna = st.text_input("Masukkan username: ")
    password_pengguna = st.text_input("Masukkan password: ", type="password")
    nama = st.text_input("Nama Lengkap: ")
    jenis_kelamin = st.radio("Jenis Kelamin", ("LAKI-LAKI", "PEREMPUAN"))
    tanggal_lahir = st.date_input("Masukkan tanggal lahir: (y-m-d)", min_value=datetime.date(1900, 1, 1), max_value=datetime.datetime.now())
    
    
    pekerjaan = st.selectbox("Pekerjaan: ", options=st.session_state.pekerjaan_pekerjaan)
    if pekerjaan == "Lainnya":
        pekerjaan_lainnya = st.text_input("Pekerjaan: ")
        pekerjaan = pekerjaan_lainnya
    
    
    email = st.text_input("Masukkan email: ")
    alamat = st.text_input("Alamat Tempat Tinggal: ")

    
    if st.button(label="Daftar"):
        cek_validasi_data_pasien = db.check_data_registrasi_pasien(username_pengguna, email, password_pengguna, nama, alamat)
        
        if cek_validasi_data_pasien == True:
            st.success("Data valid.")
            db.add_pasien(db.menambah_id_pasien_default(), username_pengguna, password_pengguna, nama, jenis_kelamin, alamat, email, pekerjaan, tanggal_lahir)
            time.sleep(2)
            st.rerun()
        
if pilihan_pasien == "Update":
    st.subheader("Update Data Pasien")
    id_pasien = st.selectbox("Pilih ID Pasien: ", options=df_pasien["ID Pasien"], index=0)
    
    username_default = df_pasien.loc[df_pasien["ID Pasien"] == id_pasien, "Username"].values[0]
    username = st.text_input("Masukkan username baru: ", value=username_default)
    
    password_default = df_pasien.loc[df_pasien["ID Pasien"] == id_pasien, "Password"].values[0]
    password = st.text_input("Masukkan password baru: ", type= "password", value=password_default)
    
    nama_default = df_pasien.loc[df_pasien["ID Pasien"] == id_pasien, "Nama Pasien"].values[0]
    nama = st.text_input("Masukkan nama lengkap baru: ", value=nama_default)
    
    jenis_kelamin_default = df_pasien.loc[df_pasien["ID Pasien"] == id_pasien, "Jenis Kelamin"].values[0]
    jenis_kelamin = st.radio("Jenis Kelamin: ", ("LAKI-LAKI", "PEREMPUAN"), horizontal=True, index=("LAKI-LAKI", "PEREMPUAN").index(jenis_kelamin_default))
    
    
    alamat_default = df_pasien.loc[df_pasien["ID Pasien"] == id_pasien, "Alamat"].values[0]
    alamat = st.text_input("Masukkan alamat baru: ", value=alamat_default)
    
    email_default = df_pasien.loc[df_pasien["ID Pasien"] == id_pasien, "Email"].values[0]
    email = st.text_input("Masukkan email baru: ", value=email_default)
    
    pekerjaan_default = df_pasien.loc[df_pasien["ID Pasien"] == id_pasien, "Pekerjaan"].values[0]
    pekerjaan = st.selectbox("Masukkan pekerjaan baru: ", options=st.session_state.pekerjaan_pekerjaan, index=st.session_state.pekerjaan_pekerjaan.index(pekerjaan_default)) 
    if pekerjaan == "Lainnya":
        pekerjaan_lainnya = st.text_input("Masukkan pekerjaan baru: ")
        pekerjaan = pekerjaan_lainnya
    
    tanggal_lahir_default = df_pasien.loc[df_pasien["ID Pasien"] == id_pasien, "Tanggal Lahir"].values[0]
    tanggal_lahir = st.date_input("Masukkan tanggal lahir: (y-m-d)", min_value=datetime.date(1900, 1, 1), max_value=datetime.datetime.now(), value=tanggal_lahir_default)

    if st.button("Update"):
        cek_update_data_pasien = db.check_update_data_pasien(username, email, password, nama, alamat)
        if cek_update_data_pasien == True:
            st.success("Update Data Berhasil.")
            db.update_pengguna(username, password, nama, jenis_kelamin, alamat, email, pekerjaan, tanggal_lahir, username_default)
            time.sleep(2)
            st.rerun()
if pilihan_pasien == "Hapus":
    st.subheader("Hapus Data Pasien")
    id_pasien = st.selectbox("Pilih ID Pasien: ", options=df_pasien["ID Pasien"], index=0)
    
    if st.button("Hapus"):
        hapus_data_pasien = db.hapus_data_pasien(id_pasien)
        st.success("Berhasil Hapus Data Pasien")
        time.sleep(2)
        st.rerun()
    st.write("**Catatan Penting**: Apabila data pasien dihapus maka hasil diagnosisnya juga akan terhapus")


