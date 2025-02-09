import streamlit as st
from assets import database as db
import time
import datetime
import re
import pandas as pd
from fpdf import FPDF

st.subheader("DATA PASIEN")
df_pasien = db.fetch_pasien()
st.write(df_pasien)

st.subheader("PEMERIKSAAN KESEHATAN")
df_pemeriksaan_kesehatan = db.fetch_pemeriksaan_kesehatan()
st.write(df_pemeriksaan_kesehatan)

st.subheader("HASIL DIAGNOSIS KOMPLIKASI")
df_diagnosis_penyakit = db.fetch_diagnosis_penyakit()
st.write(df_diagnosis_penyakit)





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
        id_pasien = st.selectbox("Pilih ID Pasien: ", options=df_pasien["id_pasien"], index=0)
        
        username_default = df_pasien.loc[df_pasien["id_pasien"] == id_pasien, "username"].values[0]
        username = st.text_input("Masukkan username baru: ", value=username_default)
        
        password_default = df_pasien.loc[df_pasien["id_pasien"] == id_pasien, "password"].values[0]
        password = st.text_input("Masukkan password baru: ", type= "password", value=password_default)
        
        nama_default = df_pasien.loc[df_pasien["id_pasien"] == id_pasien, "nama_pasien"].values[0]
        nama = st.text_input("Masukkan nama lengkap baru: ", value=nama_default)
        
        jenis_kelamin_default = df_pasien.loc[df_pasien["id_pasien"] == id_pasien, "jenis_kelamin"].values[0]
        jenis_kelamin = st.radio("Jenis Kelamin: ", ("LAKI-LAKI", "PEREMPUAN"), horizontal=True, index=("LAKI-LAKI", "PEREMPUAN").index(jenis_kelamin_default))
        
        
        alamat_default = df_pasien.loc[df_pasien["id_pasien"] == id_pasien, "alamat"].values[0]
        alamat = st.text_input("Masukkan alamat baru: ", value=alamat_default)
        
        email_default = df_pasien.loc[df_pasien["id_pasien"] == id_pasien, "email"].values[0]
        email = st.text_input("Masukkan email baru: ", value=email_default)
        
        pekerjaan_default = df_pasien.loc[df_pasien["id_pasien"] == id_pasien, "pekerjaan"].values[0]
        pekerjaan = st.selectbox("Masukkan pekerjaan baru: ", options=st.session_state.pekerjaan_pekerjaan, index=st.session_state.pekerjaan_pekerjaan.index(pekerjaan_default)) 
        if pekerjaan == "Lainnya":
            pekerjaan_lainnya = st.text_input("Masukkan pekerjaan baru: ")
            pekerjaan = pekerjaan_lainnya
        
        tanggal_lahir_default = df_pasien.loc[df_pasien["id_pasien"] == id_pasien, "tanggal_lahir"].values[0]
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
        id_pasien = st.selectbox("Pilih ID Pasien: ", options=df_pasien["id_pasien"], index=0)
        
        if st.button("Hapus"):
            hapus_data_pasien = db.hapus_data_pasien(id_pasien)
            st.success("Berhasil Hapus Data Pasien")
            time.sleep(2)
            st.rerun()
        st.write("**Catatan Penting**: Apabila data pasien dihapus maka hasil diagnosisnya juga akan terhapus")




def buat_laporan_riwayat(nama_lengkap, username_pengguna, tanggal_lahir, tanggal_pemeriksaan, jenis_kelamin, alamat,
                 pekerjaan, email, risiko_diabetes, usia_di_atas_40_tahun, riwayat_keluarga_diabetes, riwayat_diabetes_gestasional,
                 riwayat_lahir_di_bawah_2_koma_5_gram, konsumsi_alkohol, kurang_aktivitas, merokok, pola_makan_buruk,
                 kurang_tidur, tinggi_badan, berat_badan, lingkar_perut, indeks_massa_tubuh, tekanan_darah, HDL, LDL, trigliserida,
                 total_kolestrol_darah, gula_darah_sewaktu, gula_darah_puasa, gula_darah_2_jam_setelah_makan, gejala_terpilih, diagnosis_penyakit_tertentu, relasi_penyakit_dan_gejala):
    pdf = FPDF()
    pdf.add_page()
    
    pdf.image("assets/logo_diabetes.png", x=10, y=8, w=30)  # Adjust x, y, and w for logo position and size
    pdf.image("assets/puskesmas_pkc_taman_sari.jpeg", x=170, y=8, w=30)
    
    # Menambahkan judul
    pdf.set_font("Arial", size=18, style="B")
    pdf.cell(200, 15, txt="LAPORAN HASIL PEMERIKSAAN ", ln=True, align='C')
    
    pdf.ln() 
    
    pdf.set_font("Arial", size=13, style="B")
    pdf.cell(75, 10, txt="Data Pasien", ln=True)
    pdf.set_font("Arial", size=10)
    

    data_pribadi = [
        ['Nama: ', nama_lengkap],
        ["Username: ", username_pengguna],
        ["Tanggal Lahir: ", str(tanggal_lahir)],
        ["Tanggal Pemeriksaan", str(tanggal_pemeriksaan)],
        ['Jenis Kelamin: ', jenis_kelamin],
        ['Alamat: ', alamat],
        ['Pekerjaan: ', pekerjaan],
        ['Email: ', email],
        ["Risiko Diabetes Tipe 2: ", risiko_diabetes]
    ]
    for row in data_pribadi:
        pdf.cell(75, 10, row[0], 1)  # First column
        pdf.cell(120, 10, row[1], 1)  # Second column
        pdf.ln()  # Move to the next line

      # Return PDF as a string
    pdf.ln()    
    
    pdf.set_font("Arial", size=13, style="B")
    pdf.cell(75, 10, txt="Faktor Tidak Bisa Diubah", ln=True)
    pdf.set_font("Arial", size=10)
    
    pola_gaya_hidup = [
        ["Usia di atas 45 tahun: ", usia_di_atas_40_tahun],
        ["Riwayat Keluarga Diabetes: ", riwayat_keluarga_diabetes],
        ["Riwayat Diabetes Gestasional: ", riwayat_diabetes_gestasional],
        ["Riwayat Lahir <2,5 kg atau Prematur: ", riwayat_lahir_di_bawah_2_koma_5_gram],
    ]
    
    
    for row in pola_gaya_hidup:
        pdf.cell(75, 10, row[0], 1)  # First column
        pdf.cell(120, 10, row[1], 1)  # Second column
        pdf.ln()
    
    pdf.ln()
    pdf.set_font("Arial", size=13, style="B")
    pdf.cell(75, 10, txt="Pola Gaya Hidup", ln=True)
    pdf.set_font("Arial", size=10)
    pola_gaya_hidup = [
        ["Konsumsi Alkohol: ", konsumsi_alkohol],
        ["Kurang Aktivitas Fisik: ", kurang_aktivitas],
        ["Kebiasaan Merokok: ", merokok],
        ["Pola Makan Buruk : ", pola_makan_buruk],
        ["Tidur Tidak Berkualitas: ", kurang_tidur],
        
    ]
    for row in pola_gaya_hidup:
        pdf.cell(75, 10, row[0], 1)  # First column
        pdf.cell(120, 10, row[1], 1)  # Second column
        pdf.ln()
    
    pdf.ln()
    
    pdf.set_font("Arial", size=13, style="B")
    pdf.cell(75, 10, txt="Pemeriksaan Fisik", ln=True)
    pdf.set_font("Arial", size=10)
    
    pemeriksaan_fisik = [
        ["Parameter", "Hasil", "Nilai Normal"],
        ["Tinggi Badan: ", str(tinggi_badan)+" cm", "-"],
        ["Berat Badan: ", str(berat_badan)+" kg", "-"],
        ["Lingkar Perut: ", str(lingkar_perut)+" cm", " Pria <90cm , Wanita <80cm"],
        ["Indeks Massa Tubuh: ", str(indeks_massa_tubuh)+" kg/m2", " <25 kg/m2"],
    ]
    
    for row in pemeriksaan_fisik:
        pdf.cell(50, 10, row[0], 1)  # First column
        pdf.cell(50, 10, row[1], 1)
        pdf.cell(60, 10, row[2], 1)# Second column
        pdf.ln()
    
    pdf.ln()
    pdf.set_font("Arial", size=13, style="B")
    pdf.cell(75, 10, txt="Hasil Tekanan Darah dan Kolestrol Darah", ln=True)
    pdf.set_font("Arial", size=10)
    hasil_laboratorium = [
        
        ["Parameter", "Hasil", "Nilai Normal"],
        ["Tekanan Darah: ", str(tekanan_darah)+ " mmHg", " <140/90 mmHg"],
        ["HDL : ", str(HDL)+" mg/dL", " >=40 mg/dL"],
        ["LDL : ", str(LDL)+" mg/dL", " <=100 mg/dL"],
        ["Trigliserida : ", str(trigliserida)+" mg/dL", " <=150 mg/dL"],
        ["Total Kolestrol Darah: ", str(total_kolestrol_darah)+" mg/dL", " <=240 mg/dL"],
    ]
   
    
    for row in hasil_laboratorium:
        pdf.cell(50, 10, row[0], 1)  # First column
        pdf.cell(50, 10, row[1], 1) # Second column
        pdf.cell(50, 10, row[2], 1)
        pdf.ln()
    
    pdf.ln()
    
    pdf.set_font("Arial", size=13, style="B")
    pdf.cell(75, 10, txt="Hasil Laboratorium", ln=True)
    pdf.set_font("Arial", size=10)
    hasil_laboratorium = [
        ["Parameter", "Nilai", "Nilai Normal"],
        ["Gula Darah Sewaktu (GDS): ", str(gula_darah_sewaktu)+" mg/dL", " <140 mg/dL"],
        ["Gula Darah Puasa (GDP): ", str(gula_darah_puasa)+" mg/dL", " <100 mg/dL"],
        ["Gula Darah 2 Jam Setelah Makan (GD2PP): ", str(gula_darah_2_jam_setelah_makan)+" mg/dL", " <140 mg/dL"],

    ]
    
    for row in hasil_laboratorium:
        pdf.cell(90, 10, row[0], 1)
        pdf.cell(50, 10, row[1], 1) 
        pdf.cell(50, 10, row[2], 1) 
        pdf.ln()
    
    pdf.ln(120)
    
    
    
    pdf.set_font("Arial", size=18, style="B")
    pdf.cell(75, 10, txt="Diagnosis Komplikasi Penyakit", ln=True)
    
    pdf.set_font("Arial", size=13, style="B")
    pdf.cell(75, 10, txt="Gejala-Gejala Terpilih", ln=True)
    pdf.set_font("Arial", size=10)
    
    if gejala_terpilih:
        daftar_gejala_terpilih = gejala_terpilih.split(", ")
        for i, gejala in enumerate(daftar_gejala_terpilih, start=1):
            pdf.cell(200, 10, txt=f"{i}. {gejala}", ln=True)
        
    else:            
        pdf.cell(200, 10, txt="--", ln=True)
        
    pdf.ln()
    
    pdf.set_font("Arial", size=13, style="B")
    pdf.cell(75, 10, txt="Komplikasi Penyakit", ln=True)
    pdf.set_font("Arial", size=10)
    if diagnosis_penyakit_tertentu is not None:
        for index, row in diagnosis_penyakit_tertentu.iterrows():  
            if row['Nama Penyakit'] is None:
                pdf.set_font("Arial", size=10)
                pdf.cell(200, 10, txt=f"--", ln=True)
            else:
                pdf.set_font("Arial", size=10, style="B")
                pdf.cell(200, 10, txt=f"{row['Nama Penyakit']} : {row['Persentase Kecocokan']:.2f}%", ln=True)
                pdf.set_font("Arial", size=10)
                pdf.cell(200, 10, txt=f"{db.get_penjelasan_penyakit(row['Nama Penyakit'])}", ln=True)
            
            pdf.set_font("Arial", size=10, style="B")
            pdf.cell(200, 10, txt=f"Gejala yang Cocok", ln=True)
            
            
            pdf.set_font("Arial", size=10)
            
            
            daftar_gejala = row['Gejala Cocok']
            if daftar_gejala is None:
                pdf.cell(200, 10, txt=f"-", ln=True)
            else:
                daftar_gejala = daftar_gejala.split(", ")
            
                for i, gejala_cocok in enumerate(daftar_gejala, start=1):
                    pdf.cell(200, 10, txt=f"{i}. {gejala_cocok}", ln=True)
                
        
            pdf.set_font("Arial", size=10, style="B")
            pdf.cell(200, 10, txt=f"Gejala Penyakit", ln=True)
            pdf.set_font("Arial", size=10)
            
            if row['Nama Penyakit'] is None:
                pdf.cell(200, 10, txt=f"-", ln=True)
            else:
                if relasi_penyakit_dan_gejala is not None:
                    gejala_penyakit = relasi_penyakit_dan_gejala[row['Nama Penyakit']]
                    
                    for i, gejala in enumerate(gejala_penyakit, start=1):
                        pdf.cell(200, 10, txt=f"{i}. {gejala}", ln=True)
        
                #Solusi
                pdf.set_font("Arial", size=10, style="B")
                pdf.cell(200, 10, txt=f"Solusi Penyakit", ln=True)
                pdf.set_font("Arial", size=10)
                
                solusi_penyakit = db.get_solusi_penyakit(row['Nama Penyakit'])
                solusi_penyakit = solusi_penyakit.split(";")
                daftar_solusi = []
                for frasa in solusi_penyakit:
                    daftar_solusi.append(frasa.strip())

                # Loop untuk menampilkan dengan nomor urut
                for i, frasa in enumerate(daftar_solusi, start=1):
                    pdf.cell(200, 10, txt=f"{i}. {frasa}", ln=True)
                
                pdf.ln(50)
    else:
        pdf.cell(200, 10, txt="Tidak ada penyakit yang cocok", ln=True)
    
    return bytes(pdf.output())



if pilihan_yang_ingin_dilakukan == "Hasil":
    
    pilihan = st.selectbox("Pilih yang ingin dilakukan", options=["Unduh Hasil", "Update Hasil", "Hapus Hasil"])
    
    id_pasien = st.selectbox("Pilih ID pasien", options=df_pemeriksaan_kesehatan["id_pasien"].unique(), index=0)
    tanggal = st.selectbox("Pilih tanggal", options=df_pemeriksaan_kesehatan.loc[df_pemeriksaan_kesehatan["id_pasien"] == id_pasien, "tanggal_pemeriksaan"], index=0)
    
    df_pemeriksaan_kesehatan_tertentu = df_pemeriksaan_kesehatan[(df_pemeriksaan_kesehatan["id_pasien"] == id_pasien) & (df_pemeriksaan_kesehatan["tanggal_pemeriksaan"] == tanggal)]
    df_diagnosis_penyakit_tertentu = df_diagnosis_penyakit[(df_diagnosis_penyakit["id_pasien"] == id_pasien) & (df_diagnosis_penyakit["tanggal_diagnosis"] == tanggal)]
    
    st.write(df_pemeriksaan_kesehatan_tertentu)
    st.write(df_diagnosis_penyakit_tertentu)
        
    if pilihan == "Unduh Hasil":
        st.subheader("Unduh Laporan Kesehatan")
        
    
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
    
    
