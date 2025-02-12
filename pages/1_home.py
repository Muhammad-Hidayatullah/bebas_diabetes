import streamlit as st
from assets import database as db





pg_bg_img = """
<style> 
[data-testid="stAppViewContainer"]{
    background-image: url("https://images.unsplash.com/photo-1576091160550-2173dba999ef?q=80&w=1770&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;
}

[data-testid="stHeader"]{
    background-color: rgba(0, 0, 0, 0);
}


</style>

"""

st.markdown(pg_bg_img, unsafe_allow_html=True)


col1, col2 = st.columns([8, 1])

with col1:
    st.title("SELAMAT DATANG!")

with col2:
    st.markdown(
        '<a href="https://bebas-diabetes.streamlit.app/login_pengguna" target="_self" style="font-size:16px;">Login Disini</a>',
        unsafe_allow_html=True
    )
    
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





    
