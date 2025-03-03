import streamlit as st
from assets import database as db
import time



st.title("PENYAKIT")
penyakit_df = db.fetch_penyakit()
penyakit_df_html = penyakit_df.to_html(index=False, escape=False)
st.markdown(st.session_state.style_tabel + penyakit_df_html, unsafe_allow_html=True)

pilihan_penyakit = st.selectbox("Pilih Opsi untuk Penyakit", options=["Tambah Penyakit", "Update Penyakit", "Hapus Penyakit"])

if pilihan_penyakit == "Tambah Penyakit":
    id_komplikasi_penyakit = st.text_input("Masukkan kode penyakit: ", db.menambah_id_komplikasi_penyakit_default())
    nama_penyakit = st.text_input("Masukkan nama penyakit: ")
    penjelasan = st.text_input("Masukkan penjelasan penyakit: ")
    solusi = st.text_area("Masukkan solusi penyakit: ")
    if st.button("Tambah"):
        db.add_komplikasi_penyakit(id_komplikasi_penyakit, nama_penyakit, penjelasan, solusi)
        time.sleep(2)
        st.rerun()


if pilihan_penyakit == "Update Penyakit":
    
    df_penyakit = db.fetch_penyakit()
    
    kol_id_komplikasi_penyakit = df_penyakit["id_komplikasi_penyakit"]
    
    id_komplikasi_penyakit =st.selectbox("Masukkan kode komplikasi penyakit: ", options=kol_id_komplikasi_penyakit, index=0)
    
    nama_penyakit_default = df_penyakit.loc[df_penyakit["id_komplikasi_penyakit"] == id_komplikasi_penyakit, "nama_penyakit"].values[0]
    nama_penyakit = st.text_input("Masukkan nama komplikasi penyakit baru: ", nama_penyakit_default)
    
    nama_penjelasan_default = df_penyakit.loc[df_penyakit["id_komplikasi_penyakit"] == id_komplikasi_penyakit, "penjelasan"].values[0]
    penjelasan = st.text_input("Masukkan penjelasan penyakit baru: ", nama_penjelasan_default)
    
    
    solusi_default = df_penyakit.loc[df_penyakit["id_komplikasi_penyakit"] == id_komplikasi_penyakit, "solusi"].values[0]
    solusi = st.text_area("Masukkan solusi penyakit baru: ", solusi_default)
    if st.button("Update"):
        db.update_komplikasi_penyakit(id_komplikasi_penyakit, nama_penyakit, penjelasan, solusi)
        time.sleep(2)
        st.rerun()
        

if pilihan_penyakit == "Hapus Penyakit":
    df_penyakit = db.fetch_penyakit()
    
    kol_id_komplikasi_penyakit = df_penyakit["id_komplikasi_penyakit"]
    
    id_komplikasi_penyakit =st.selectbox("Masukkan kode penyakit yang ingin dihapus: ", options=kol_id_komplikasi_penyakit, index=0)
    
    if st.button("Hapus"):
        db.hapus_komplikasi_penyakit(id_komplikasi_penyakit)
        time.sleep(2)
        st.rerun()
