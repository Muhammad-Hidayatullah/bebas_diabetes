import streamlit as st
from assets import database as db

st.markdown(
    """
    <style>
    .top-right {
        position: absolute;
        top: 10px;
        right: 10px;
        font-size: 16px;
    }
    </style>
    <a href="https://your-login-page.com" class="top-right">Login Disini</a>
    """,
    unsafe_allow_html=True
)

st.title("SELAMAT DATANG!")
col1, col2 = st.columns(2)

with col1:
 
    st.image("./assets/dokter_pria.jpg", width=300)

with col2:
    text = """
    <div style="text-align: justify;">
        Selamat datang di Website Sistem Pakar Penyakit Diabetes Mellitus Tipe 2 Kami! Situs ini dibuat agar
        Anda memeriksa kesehatan dengan sistem diagnosis dini penyakit diabetes tipe 2. Mari bersama-sama menjaga kesehatan dan
        menerapkan pola hidup sehat untuk mencegah penyakit, demi kebahagiaan Anda dan pribadi. 
    </div>
    """
    st.markdown(text, unsafe_allow_html=True)





    
