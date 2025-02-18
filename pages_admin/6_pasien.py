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

st.subheader("PEMERIKSAAN KESEHATAN")
df_pemeriksaan_kesehatan = db.fetch_pemeriksaan_kesehatan()
df_pemeriksaan_kesehatan_html = df_pemeriksaan_kesehatan.to_html(index=False, escape=False)
st.markdown(st.session_state.style_tabel + df_pemeriksaan_kesehatan_html, unsafe_allow_html=True)


st.subheader("HASIL DIAGNOSIS KOMPLIKASI")
df_diagnosis_penyakit = db.fetch_diagnosis_penyakit_admin()
lihat_df_diagnosis_penyakit = df_diagnosis_penyakit.copy()
lihat_df_diagnosis_penyakit.drop(columns=["Gejala Terpilih"], inplace=True)
df_diagnosis_penyakit_html = lihat_df_diagnosis_penyakit.to_html(index=False, escape=False)
st.markdown(st.session_state.style_tabel + df_diagnosis_penyakit_html, unsafe_allow_html=True)





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

if pilihan_yang_ingin_dilakukan == "Pasien":
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


if pilihan_yang_ingin_dilakukan == "Hasil":
    
    pilihan = st.selectbox("Pilih yang ingin dilakukan", options=["Unduh Hasil", "Update Hasil", "Hapus Hasil"])
    
    id_pasien = st.selectbox("Pilih ID pasien", options=df_pemeriksaan_kesehatan["ID Pasien"].unique(), index=0)
    tanggal = st.selectbox("Pilih tanggal", options=df_pemeriksaan_kesehatan.loc[df_pemeriksaan_kesehatan["ID Pasien"] == id_pasien, "Tanggal Pemeriksaan"], index=0)
    
    df_pasien_tertentu = df_pasien[df_pasien["ID Pasien"] == id_pasien]
    
    df_pemeriksaan_kesehatan_pasien_tertentu = df_pemeriksaan_kesehatan[(df_pemeriksaan_kesehatan["ID Pasien"] == id_pasien) & (df_pemeriksaan_kesehatan["Tanggal Pemeriksaan"] == tanggal)]
    df_diagnosis_penyakit_tertentu = df_diagnosis_penyakit[(df_diagnosis_penyakit["ID Pasien"] == id_pasien) & (df_diagnosis_penyakit["Tanggal Diagnosis"] == tanggal)]
    
    
    if pilihan == "Unduh Hasil":
        st.subheader("Unduh Laporan Kesehatan")
        
        if not df_diagnosis_penyakit_tertentu.empty:
            row = df_pasien_tertentu.iloc[0]
            username = row["Username"]
            nama_pasien = row["Nama Pasien"]
            jenis_kelamin = row["Jenis Kelamin"]
            alamat = row["Alamat"]
            email = row["Email"]
            pekerjaan = row["Pekerjaan"]
            tanggal_lahir = row["Tanggal Lahir"]
            
            
        
        
        
        if not df_pemeriksaan_kesehatan_pasien_tertentu.empty:
        
            row = df_pemeriksaan_kesehatan_pasien_tertentu.iloc[0]  # Get first row safely
            risiko_diabetes = row["Risiko Diabetes"]
            usia_di_atas_40_tahun = row["Usia di Atas 40 Tahun"]
            riwayat_keluarga_diabetes = row["Riwayat Keluarga Diabetes"]
            riwayat_diabetes_gestasional = row["Riwayat Diabetes Gestasional"]
            riwayat_lahir_di_bawah_2_koma_5_gram = row["Riwayat Lahir Berat Badan Lahir Rendah"]
            konsumsi_alkohol = row["Konsumsi Alkohol"]
            kurang_aktivitas = row["Kurang Aktivitas"]
            merokok = row["Merokok"]
            pola_makan_buruk = row["Pola Makan Buruk"]
            kurang_tidur = row["Kurang Tidur"]
            tinggi_badan = str(row["Tinggi Badan"])
            berat_badan = str(row["Berat Badan"])
            lingkar_perut = str(row["Lingkar Perut"])
            indeks_massa_tubuh = str(row["Indeks Massa Tubuh"])
            gula_darah_sewaktu = str(row["Gula Darah Sewaktu"])
            gula_darah_puasa = str(row["Gula Darah Puasa"])
            gula_darah_2_jam_setelah_makan = str(row["Gula Darah 2 Jam Setelah Makan"])
            tekanan_darah = str(row["Tekanan Darah"])
            HDL = str(row["HDL"])
            LDL = str(row["LDL"])
            trigliserida = str(row["Trigliserida"])
            total_kolestrol = str(row["Total Kolestrol"])
                        
            
        else:
            st.write("Tidak ada data untuk tanggal yang dipilih.")
            
        df_diagnosis_penyakit_tertentu = df_diagnosis_penyakit.loc[df_diagnosis_penyakit["Tanggal Diagnosis"] == tanggal]



        row = df_diagnosis_penyakit_tertentu.head(1)
        
        gejala_terpilih = row["Gejala Terpilih"].iloc[0]
        nama_pasien = row["Nama Pasien"].iloc[0]
       
      

        diagnosis_penyakit_tertentu = df_diagnosis_penyakit_tertentu.iloc[:, 3:]



        #diagnosis_penyakit_tertentu = diagnosis_penyakit_tertentu.drop("Gejala Terpilih", axis=1)

        #Relasi Penyakit dan Gejala
        data_relasi = db.fetch_relasi_nama_penyakit_dan_nama_gejala()
        relasi_penyakit_dan_gejala = {}
        for penyakit, gejala in data_relasi:
            if penyakit not in relasi_penyakit_dan_gejala:
                relasi_penyakit_dan_gejala[penyakit] = []  # Buat list kosong jika penyakit belum ada
            relasi_penyakit_dan_gejala[penyakit].append(gejala) 

        

        if st.button("Unduh Laporan"):
            file_pdf = fl.buat_laporan_riwayat(id_pasien, nama_pasien, username, tanggal_lahir, tanggal, jenis_kelamin, alamat,
                    pekerjaan, email, risiko_diabetes, usia_di_atas_40_tahun, riwayat_keluarga_diabetes, riwayat_diabetes_gestasional,
                    riwayat_lahir_di_bawah_2_koma_5_gram, konsumsi_alkohol, kurang_aktivitas, merokok, pola_makan_buruk,
                    kurang_tidur, tinggi_badan, berat_badan, lingkar_perut, indeks_massa_tubuh, tekanan_darah, HDL, LDL, trigliserida,
                    total_kolestrol, gula_darah_sewaktu, gula_darah_puasa, gula_darah_2_jam_setelah_makan, gejala_terpilih, df_diagnosis_penyakit_tertentu, relasi_penyakit_dan_gejala)

            #base64_pdf = b64encode(file_pdf).decode("utf-8")
            #pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="400" type="application/pdf">'

            #st.markdown(pdf_display, unsafe_allow_html=True)
            
            
            st.download_button(
                label="Download PDF",
                data=file_pdf,
                file_name = "Laporan Kesehatan_"+nama_pasien+ "_"+str(tanggal)+".pdf",
                mime="application/pdf"
            )
            
            
            
        if pilihan == "Update Hasil":
            st.subheader("Update Laporan Kesehatan")
            
        
        if pilihan == "Hapus Hasil":
            st.subheader("Hapus Laporan Kesehatan")
            if st.button("Hapus"):
                db.hapus_hasil_pemeriksaan_dan_diagnosis_penyakit_admin(id_pasien, tanggal)
                st.success("Data Berhasil Terhapus")
                time.sleep(2)
                st.rerun()
                st.write("Hello")
    
    
