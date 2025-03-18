import streamlit as st

import pandas as pd
from assets import database as db
st.title("Informasi Sistem")




pg_bg_img = """
<style> 
[data-testid="stAppViewContainer"]{
    background-image: url("https://plus.unsplash.com/premium_photo-1668487826910-6a9ae2365d1b?q=80&w=1712&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;
}

[data-testid="stHeader"]{
    background-color: rgba(0, 0, 0, 0);
}


</style>

"""

st.markdown(pg_bg_img, unsafe_allow_html=True)
data_faktor_risiko = {
    "Jenis Risiko": [
        "Tidak Bisa Diubah", "Tidak Bisa Diubah", "Tidak Bisa Diubah", "Tidak Bisa Diubah", "Tidak Bisa Diubah",
        "Tidak Bisa Diubah", "Bisa Diubah", "Bisa Diubah", "Bisa Diubah", "Bisa Diubah",
        "Bisa Diubah", "Bisa Diubah", "Bisa Diubah", "Bisa Diubah", "Bisa Diubah", "Bisa Diubah"
    ],
    "Faktor Risiko": [
        "Usia", "Riwayat Keluarga", "Riwayat Penyakit", "Riwayat Penyakit", "Riwayat Penyakit",
        "Riwayat Lahir", "Merokok", "Pola Makan", "Alkohol", "Tidur",
        "Aktivitas", "Berat Badan", "Gula Darah", "Lingkar Perut", "Tekanan Darah Tinggi", "Kolesterol"
    ],
    "Kondisi": [
        "Usia > 40 tahun dan semakin tua usia maka risiko akan semakin naik.",
        "Terdapat anggota keluarga dekat atau first-degree relative seperti orang tua dan saudara kandung yang terkena penyakit Diabetes Mellitus Tipe 2",
        "Riwayat melahirkan bayi dengan Berat Badan Lahir (BBL) > 4 kg atau terkena Diabetes Mellitus Gestasional (DMG) (wanita saja).",
        "Sindrom Ovarium Polikistik (PCOS) (wanita saja).",
        "Riwayat penyakit kardiovaskular.",
        "Lahir dengan Berat Badan Lahir (BBL) < 2,5 kg atau terlahir prematur.",
        "Suka merokok.",
        "Makanan yang mengandung gula, garam, dan lemak tinggi serta rendah serat.",
        "Minum alkohol berlebihan > 28 gram atau > 4 botol bir dalam sehari.",
        "Kurang tidur atau mengalami gangguan tidur dengan waktu tidur < 6 jam.",
        "Kurang olahraga dan aktivitas fisik dengan < 150 menit per minggu.",
        "Berat badan berlebih (Indeks Massa Tubuh > 23 kg/m2).",
        "Normal: GDS 70-139 mg/dL, GDP 70-99 mg/dL, GD2PP 70-139 mg/dL.\n"
        "Prediabetes: GDS 140-199 mg/dL, GDP 100-125 mg/dL, GD2PP 140-199 mg/dL.\n"
        "Diabetes: GDS ≥ 200 mg/dL, GDP ≥126 mg/dL, GD2PP ≥ 200 mg/dL.",
        "Obesitas sentral dengan lingkar perut ≥ 90 cm (pria) dan ≥ 80 cm (wanita).",
        "Hipertensi dengan tekanan darah Sistolik ≥ 140 dan/atau tekanan darah Diastolik ≥ 90.",
        "Dislipidemia: HDL < 30 mg/dL, LDL > 130 mg/dL, trigliserida > 200 mg/dL, Kolesterol total > 220 mg/dL.",
    ]
}


df_faktor_risiko = pd.DataFrame(data_faktor_risiko)

st.subheader("Deskripsi Sistem")
st.write("Sistem ini dirancang untuk memprediksi penyakit Diabetes Mellitus Tipe 2 menggunakan sistem pakar dengan metode Forward Chaining")

st.subheader("Teknologi yang Digunakan")
st.write("""
         1. Bahasa Pemrograman Python
         2. Framework Streamlit
         3. Database MariaDB atau MySQL
         """)


df_faktor_risiko_html = df_faktor_risiko.to_html(index=False, escape=False)
st.subheader("Faktor-Faktor Risiko")
st.markdown(st.session_state.style_tabel_aturan + df_faktor_risiko_html, unsafe_allow_html=True)
st.write("")
st.subheader("Aturan Komplikasi Penyakit")

relasi_penyakit_dan_gejala_aturan = db.fetch_relasi_penyakit_dan_gejala_aturan()

relasi_penyakit_dan_gejala_aturan_html = relasi_penyakit_dan_gejala_aturan.to_html(index=False, escape=False)

st.markdown(st.session_state.style_tabel_aturan + relasi_penyakit_dan_gejala_aturan_html, unsafe_allow_html=True)
