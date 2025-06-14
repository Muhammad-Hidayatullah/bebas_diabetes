import streamlit as st
from assets import database as db

st.session_state.style_tabel_aturan = """
<style>
    table {
        width: 100%;
        border-collapse: collapse;
        font-family: Arial, sans-serif;
        font-size: 12px;
    }
    th {
        background-color: #93C572;
        color: white;
        font-weight: bold;
        text-align: left;
        padding: 20px;
    }
    
    td {
        background-color: white;
        padding: 10px;
        border: 1px solid #ddd;
        text-align: left;
    }
    tr:nth-child(even) td {
        background-color: #f9f9f9;
    }
</style>
"""



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


col1, col2 = st.columns([9, 3])

with col1:
    st.title("SELAMAT DATANG!")

with col2:
    st.markdown(
        '<a href="https://bebasdaridiabetes.streamlit.app/login_pengguna" target="_self" style="font-size:20px;">Login Disini</a>',
        unsafe_allow_html=True
    )
    
col1, col2 = st.columns(2)

with col1:
 
    st.image("./assets/dokter_pria.jpg", width=300)
    

with col2:
    text = """
    <div style="text-align: justify;">
        Selamat datang di Website Sistem Pakar Untuk Memprediksi Penyakit Diabetes Mellitus Tipe 2 (Studi Kasus: Puskesmas Kecamatan Taman Sari) ! Situs ini dibuat agar
        Anda memeriksa kesehatan dengan sistem diagnosis dini penyakit diabetes tipe 2. Mari bersama-sama menjaga kesehatan dan
        menerapkan pola hidup sehat untuk mencegah penyakit, demi kebahagiaan Anda dan pribadi. 
    </div>
    """
    st.markdown(text, unsafe_allow_html=True)



st.write("")



st.markdown("<p style='color: red;'>Disclaimer</p>", unsafe_allow_html=True)


st.write(
"""
Sistem ini menggunakan data faktor risiko dan penyakit yang bersumber dari **Buku Pedoman Pengelolaan dan Pencegahan Diabetes Mellitus Tipe 2 Dewasa di Indonesia (2021)** yang diterbitkan oleh **PB Perkeni**, serta referensi dari berbagai studi pustaka lainnya.

⚠️ **Catatan Penting:**  
Sistem pakar ini **bukan pengganti peran dokter**. Hasil analisis yang diberikan hanya untuk membantu dalam memahami faktor risiko dan kemungkinan komplikasi diabetes tipe 2. Untuk diagnosis dan penanganan yang lebih akurat, konsultasikan dengan tenaga medis profesional.
"""
)





    
