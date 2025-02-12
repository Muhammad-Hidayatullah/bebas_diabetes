import streamlit as st
from assets import database as db
import datetime
from fpdf import FPDF
import time
import pandas as pd
import re


st.title("Riwayat")
st.subheader("Riwayat Pemeriksaan Kesehatan")

def buat_laporan_riwayat(nama_lengkap, username_pengguna, tanggal_lahir, tanggal_pemeriksaan, jenis_kelamin, alamat,
                 pekerjaan, email, risiko_diabetes, usia_di_atas_40_tahun, riwayat_keluarga_diabetes, riwayat_diabetes_gestasional,
                 riwayat_lahir_di_bawah_2_koma_5_gram, konsumsi_alkohol, kurang_aktivitas, merokok, pola_makan_buruk,
                 kurang_tidur, tinggi_badan, berat_badan, lingkar_perut, indeks_massa_tubuh, tekanan_darah, HDL, LDL, trigliserida,
                 total_kolestrol_darah, gula_darah_sewaktu, gula_darah_puasa, gula_darah_2_jam_setelah_makan, diagnosis_penyakit_tertentu, relasi_penyakit_dan_gejala):
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
        daftar_gejala_terpilih = gejala_terpilih.split("; ")
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
                daftar_gejala = daftar_gejala.split("; ")
            
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
    lihat_df_pemeriksaan_kesehatan = df_pemeriksaan_kesehatan_pasien
    
    lihat_df_pemeriksaan_kesehatan.drop(columns=["ID Pemeriksaan", "ID Pasien", "Nama Pasien"], inplace=True)
    
    tabel_html_pemeriksaan_kesehatan_pasien = lihat_df_pemeriksaan_kesehatan.to_html(index=False, escape=False)

    st.markdown(style_tabel + tabel_html_pemeriksaan_kesehatan_pasien, unsafe_allow_html=True)

st.subheader("Riwayat Diagnosis Penyakit")
df_diagnosis_penyakit = db.get_diagnosis_penyakit(st.session_state.kode_pasien)
if df_diagnosis_penyakit is None:
    st.write("--")
else:
    df_diagnosis_penyakit = pd.DataFrame(df_diagnosis_penyakit)
    
    lihat_df_diagnosis_penyakit = df_diagnosis_penyakit
    
    lihat_df_diagnosis_penyakit.drop(columns=["ID Diagnosis", "ID Pasien", "Nama Pasien"], inplace = True)
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
        usia_di_atas_40_tahun = row["Usia Di Atas 40 Tahun"]
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
            file_pdf = buat_laporan_riwayat(st.session_state.nama_lengkap, st.session_state.username_pengguna, st.session_state.tanggal_lahir, tanggal_pemeriksaan, st.session_state.jenis_kelamin, st.session_state.alamat,
                    st.session_state.pekerjaan, st.session_state.email, risiko_diabetes, usia_di_atas_40_tahun, riwayat_keluarga_diabetes, riwayat_diabetes_gestasional,
                    riwayat_lahir_di_bawah_2_koma_5_gram, konsumsi_alkohol, kurang_aktivitas, merokok, pola_makan_buruk,
                    kurang_tidur, tinggi_badan, berat_badan, lingkar_perut, indeks_massa_tubuh, tekanan_darah, HDL, LDL, trigliserida,
                    total_kolestrol, gula_darah_sewaktu, gula_darah_puasa, gula_darah_2_jam_setelah_makan, df_diagnosis_penyakit_tertentu, relasi_penyakit_dan_gejala)

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