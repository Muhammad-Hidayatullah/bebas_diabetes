import streamlit as st
from assets import database as db
import datetime
from fpdf import FPDF
import time
import pandas as pd
import re
from assets import format_laporan as fl

st.title("Riwayat")
st.subheader("Riwayat Pemeriksaan Kesehatan")

style_tabel = """
<style>
    table {
        width: 100%;
        border-collapse: collapse;
        font-family: Arial, sans-serif;
        font-size: 12px;
    }
    th {
        background-color: green;
        color: white;
        padding: 10px;
        text-align: left;
    }
    td {
        background-color: white;
        padding: 10px;
        border: 1px solid #ddd;
        text-align: left;
    }
    tr:nth-child(even) td {
        background-color: #f9f9f9; /* Light gray for alternating rows */
    }
</style>
"""




df_pemeriksaan_kesehatan_pasien = db.fetch_pemeriksaan_kesehatan_pasien(st.session_state.kode_pasien)
if df_pemeriksaan_kesehatan_pasien is None:
    st.write("--")
else:
    df_pemeriksaan_kesehatan_pasien = pd.DataFrame(df_pemeriksaan_kesehatan_pasien)
    lihat_df_pemeriksaan_kesehatan = df_pemeriksaan_kesehatan_pasien.copy()
    
    lihat_df_pemeriksaan_kesehatan.drop(columns=["ID Pemeriksaan", "ID Pasien", "Nama Pasien"], inplace=True)
    
    tabel_html_pemeriksaan_kesehatan_pasien = lihat_df_pemeriksaan_kesehatan.to_html(index=False, escape=False)

    st.markdown(style_tabel + tabel_html_pemeriksaan_kesehatan_pasien, unsafe_allow_html=True)

st.subheader("Riwayat Diagnosis Penyakit")
df_diagnosis_penyakit = db.get_diagnosis_penyakit(st.session_state.kode_pasien)
if df_diagnosis_penyakit is None:
    st.write("--")
else:
    df_diagnosis_penyakit = pd.DataFrame(df_diagnosis_penyakit)
    
    lihat_df_diagnosis_penyakit = df_diagnosis_penyakit.copy()
    
    lihat_df_diagnosis_penyakit.drop(columns=["ID Diagnosis", "ID Pasien", "Nama Pasien", "Gejala Terpilih"], inplace = True)
    tabel_html_diagnosis_penyakit = lihat_df_diagnosis_penyakit.to_html(index=False, escape=False)

      
    st.markdown(style_tabel + tabel_html_diagnosis_penyakit, unsafe_allow_html=True)
    
    

if df_pemeriksaan_kesehatan_pasien is not None or df_diagnosis_penyakit is not None:
    #Opsi untu hapus atau unduh
    opsi = st.selectbox("Pilih Opsi: ", ("Unduh", "Hapus"))

    #tanggal_pemeriksaan = st.selectbox("Pilih tanggal: ", options=df_diagnosis_penyakit["Tanggal Diagnosis"].unique())

    options = sorted(set(df_diagnosis_penyakit["Tanggal Diagnosis"].unique()) | set(df_pemeriksaan_kesehatan_pasien["Tanggal Pemeriksaan"].unique()))

    tanggal_pemeriksaan = st.selectbox("Pilih tanggal:", options)


    #tanggal_pemeriksaan = pd.to_datetime(tanggal_pemeriksaan)
    df_pemeriksaan_kesehatan_pasien_tertentu = df_pemeriksaan_kesehatan_pasien.loc[df_pemeriksaan_kesehatan_pasien["Tanggal Pemeriksaan"] == tanggal_pemeriksaan]


    if not df_pemeriksaan_kesehatan_pasien_tertentu.empty:
        row = df_pemeriksaan_kesehatan_pasien_tertentu.iloc[0]  # Get first row safely
        risiko_diabetes = row["Risiko Diabetes"]
        usia_di_atas_45_tahun = row["Usia Di Atas 45 Tahun"]
        riwayat_keluarga_diabetes = row["Riwayat Keluarga Diabetes"]
        riwayat_diabetes_gestasional = row["Riwayat Diabetes Gestasional"]
        riwayat_lahir_di_bawah_2_koma_5_gram = row["Riwayat Berat Badan Lahir Rendah"]
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
        total_kolestrol = str(row["Total Kolesterol"])
    else:
        st.write("Tidak ada data untuk tanggal yang dipilih.")



    df_diagnosis_penyakit_tertentu = df_diagnosis_penyakit.loc[df_diagnosis_penyakit["Tanggal Diagnosis"] == tanggal_pemeriksaan]



    row = df_diagnosis_penyakit_tertentu.iloc[0]  # Get first
    gejala_terpilih = row["Gejala Terpilih"]


    diagnosis_penyakit_tertentu = df_diagnosis_penyakit_tertentu.iloc[:, 3:]



    #diagnosis_penyakit_tertentu = diagnosis_penyakit_tertentu.drop("Gejala Terpilih", axis=1)

    #Relasi Penyakit dan Gejala
    data_relasi = db.fetch_relasi_nama_penyakit_dan_nama_gejala()
    relasi_penyakit_dan_gejala = {}
    for penyakit, gejala in data_relasi:
        if penyakit not in relasi_penyakit_dan_gejala:
            relasi_penyakit_dan_gejala[penyakit] = []  # Buat list kosong jika penyakit belum ada
        relasi_penyakit_dan_gejala[penyakit].append(gejala) 




    if opsi == "Unduh":
        if st.button("Unduh Laporan"):
            file_pdf = fl.buat_laporan_riwayat(st.session_state.kode_pasien, st.session_state.nama_lengkap, st.session_state.username_pengguna, st.session_state.tanggal_lahir, tanggal_pemeriksaan, st.session_state.jenis_kelamin, st.session_state.alamat,
                    st.session_state.pekerjaan, st.session_state.email, risiko_diabetes, usia_di_atas_45_tahun, riwayat_keluarga_diabetes, riwayat_diabetes_gestasional,
                    riwayat_lahir_di_bawah_2_koma_5_gram, konsumsi_alkohol, kurang_aktivitas, merokok, pola_makan_buruk,
                    kurang_tidur, tinggi_badan, berat_badan, lingkar_perut, indeks_massa_tubuh, tekanan_darah, HDL, LDL, trigliserida,
                    total_kolestrol, gula_darah_sewaktu, gula_darah_puasa, gula_darah_2_jam_setelah_makan, gejala_terpilih, df_diagnosis_penyakit_tertentu, relasi_penyakit_dan_gejala)

            #base64_pdf = b64encode(file_pdf).decode("utf-8")
            #pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="400" type="application/pdf">'

            #st.markdown(pdf_display, unsafe_allow_html=True)
            
            
            st.download_button(
                label="Download PDF",
                data=file_pdf,
                file_name = "Laporan Kesehatan_"+st.session_state.nama_lengkap+ "_"+str(tanggal_pemeriksaan)+".pdf",
                mime="application/pdf"
            )
    if opsi == "Hapus":
        if st.button("Hapus"):
            db.hapus_pemeriksaan_kesehatan_dan_diagnosis(tanggal_pemeriksaan)
            st.success("Pemeriksaan Kesehatan dan Diagnosis Berhasil Dihapus")
            time.sleep(2)
            st.rerun()
