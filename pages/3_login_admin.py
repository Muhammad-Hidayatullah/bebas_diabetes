import streamlit as st
from assets import database as db
import time
from fpdf import FPDF
import io


st.subheader("ADMIN")
admin_df = db.fetch_admin()
st.dataframe(admin_df)

pilihan_admin = st.selectbox("Pilih Opsi untuk Admin", ("Tambah Admin", "Hapus Admin"))
if pilihan_admin == "Tambah Admin":
    input_username = st.text_input("Masukkan username admin:")
    input_nama = st.text_input("Masukkan nama: ")
    input_password = st.text_input("Masukkan password:", type="password")
    if st.button(label="Tambah"):
        db.insert_admin(input_username, input_nama, input_password)
        time.sleep(2)
        st.rerun()
    
if pilihan_admin == "Hapus Admin":
    kol_id_admin = admin_df[admin_df["username_admin"] != "Admin"]["username_admin"]
    
    pilih_username = st.selectbox("Pilih Admin untuk dihapus", options=kol_id_admin, index=0)
    if st.button("Hapus"):
        db.hapus_admin(pilih_username)
        time.sleep(2)
        st.rerun()
