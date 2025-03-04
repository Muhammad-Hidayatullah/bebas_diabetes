import streamlit as st
from assets import database as db
import time
import datetime
import re
import pandas as pd
from fpdf import FPDF
from assets import format_laporan as fl


df_pengguna = db.fetch_pengguna()
st.title("LAPORAN")

st.subheader("PEMERIKSAAN KESEHATAN")
df_pemeriksaan_kesehatan = db.fetch_pemeriksaan_kesehatan()
lihat_df_pemeriksaan_kesehatan_html = df_pemeriksaan_kesehatan.to_html(index=False, escape=False)
st.markdown(st.session_state.style_tabel + lihat_df_pemeriksaan_kesehatan_html, unsafe_allow_html=True)


st.subheader("HASIL DIAGNOSIS KOMPLIKASI")
df_diagnosis_penyakit = db.fetch_diagnosis_penyakit_admin()
lihat_df_diagnosis_penyakit = df_diagnosis_penyakit.copy()

rows_per_page = st.selectbox("Tampilkan baris:", [10, 20, 50], index=0)
lihat_df_diagnosis_penyakit.drop(columns=["Gejala Terpilih"], inplace=True)
lihat_df_diagnosis_penyakit = lihat_df_diagnosis_penyakit.head(rows_per_page)

df_diagnosis_penyakit_html = lihat_df_diagnosis_penyakit.to_html(index=False, escape=False)
st.markdown(st.session_state.style_tabel + df_diagnosis_penyakit_html, unsafe_allow_html=True)


# Show table with selected number of rows


    
pilihan = st.selectbox("Pilih yang ingin dilakukan", options=["Unduh Hasil", "Hapus Hasil"])

id_pengguna = st.selectbox("Pilih ID Pengguna", options=df_pemeriksaan_kesehatan["ID Pengguna"].unique(), index=0)
tanggal = st.selectbox("Pilih tanggal", options=df_pemeriksaan_kesehatan.loc[df_pemeriksaan_kesehatan["ID Pengguna"] == id_pengguna, "Tanggal Pemeriksaan"], index=0)

df_pengguna_tertentu = df_pengguna[df_pengguna["ID Pengguna"] == id_pengguna]

df_pemeriksaan_kesehatan_pengguna_tertentu = df_pemeriksaan_kesehatan[(df_pemeriksaan_kesehatan["ID Pengguna"] == id_pengguna) & (df_pemeriksaan_kesehatan["Tanggal Pemeriksaan"] == tanggal)]
df_diagnosis_penyakit_tertentu = df_diagnosis_penyakit[(df_diagnosis_penyakit["ID Pengguna"] == id_pengguna) & (df_diagnosis_penyakit["Tanggal Diagnosis"] == tanggal)]


if pilihan == "Unduh Hasil":
    
    if not df_diagnosis_penyakit_tertentu.empty:
        row = df_pengguna_tertentu.iloc[0]
        username = row["Username"]
        nama_pengguna = row["Nama pengguna"]
        jenis_kelamin = row["Jenis Kelamin"]
        alamat = row["Alamat"]
        email = row["Email"]
        pekerjaan = row["Pekerjaan"]
        tanggal_lahir = row["Tanggal Lahir"]
        
        
    
    
    
    if not df_pemeriksaan_kesehatan_pengguna_tertentu.empty:
    
        row = df_pemeriksaan_kesehatan_pengguna_tertentu.iloc[0]  # Get first row safely
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
    nama_pengguna_terpilih = row["Nama pengguna"].iloc[0]
    

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
        file_pdf = fl.buat_laporan_riwayat(id_pengguna, nama_pengguna, username, tanggal_lahir, tanggal, jenis_kelamin, alamat,
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
            file_name = "Laporan Kesehatan_"+nama_pengguna_terpilih+ "_"+str(tanggal)+".pdf",
            mime="application/pdf"
        )


if pilihan == "Hapus Hasil":
    if st.button("Hapus"):
        db.hapus_hasil_pemeriksaan_dan_diagnosis_penyakit_admin(id_pengguna, tanggal)
        st.success("Data Berhasil Terhapus")
        time.sleep(2)
        st.rerun()
        st.write("Hello")
