import streamlit as st
from assets import database as db
import time


st.title("GEJALA")
gejala_df = db.fetch_gejala()
gejala_df_html = gejala_df.to_html(index=False, escape=False)
st.markdown(st.session_state.style_tabel + gejala_df_html, unsafe_allow_html=True)

pilihan_gejala = st.selectbox("Pilih Opsi untuk Gejala: ", options=["Tambah Gejala", "Update Gejala", "Hapus Gejala"])


df_gejala = db.fetch_gejala()
kol_id_gejala = df_gejala["id_gejala"]

if pilihan_gejala == "Tambah Gejala":
    id_gejala = st.text_input("Masukkan kode gejala: ", db.menambah_id_gejala_default())
    nama_gejala = st.text_input("Masukkan nama gejala: ")
    if st.button("Tambah Gejala"):
        db.add_gejala(id_gejala, nama_gejala)
        time.sleep(2)
        st.rerun()

if pilihan_gejala == "Update Gejala":
    id_gejala = st.selectbox("Masukkan kode gejala: ", options=kol_id_gejala, index=0)
    
    nama_gejala_default = df_gejala.loc[df_gejala["id_gejala"] == id_gejala, "nama_gejala"].values[0]
    nama_gejala = st.text_input("Masukkan nama gejala baru: ", nama_gejala_default)
    if st.button("Update"):
        db.update_gejala(id_gejala, nama_gejala)
        time.sleep(2)
        st.rerun()
    
if pilihan_gejala == "Hapus Gejala":
    id_gejala = st.selectbox("Masukkan kode gejala yang ingin dihapus: ", options=kol_id_gejala, index=0)
    if st.button("Hapus"):
        db.hapus_gejala(id_gejala)
        time.sleep(2)
        st.rerun()
