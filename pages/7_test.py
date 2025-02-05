import streamlit as st
from fpdf import FPDF

def buat_laporan_riwayat(nama_lengkap):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=16, style="B")
    pdf.cell(200, 10, txt="Laporan Hasil Pemeriksaan", ln=True, align="C")
    pdf.ln()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Nama: {nama_lengkap}", ln=True)
    
    return pdf

st.title("Generate PDF Report")

# Input data
nama = st.text_input("Masukkan Nama")

if st.button("Buat Laporan"):
    pdf = buat_laporan_riwayat(nama)
    pdf_output = "laporan.pdf"
    pdf.output(pdf_output)

    # Read PDF as binary
    with open(pdf_output, "rb") as f:
        pdf_bytes = f.read()

    st.download_button(
        label="Unduh Laporan PDF",
        data=pdf_bytes,
        file_name="laporan_pemeriksaan.pdf",
        mime="application/pdf"
    )
