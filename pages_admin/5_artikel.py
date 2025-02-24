import streamlit as st
from assets import database as db
import time

st.title("ARTIKEL")
df_artikel = db.fetch_artikel()

df_artikel_html = df_artikel.to_html(index=False, escape=False)
st.markdown(st.session_state.style_tabel + df_artikel_html, unsafe_allow_html=True)

pilihan_artikel = st.selectbox("Pilih Opsi untuk Artikel", ("Tambah", "Update", "Hapus"))

if pilihan_artikel == "Tambah":
    nama_website = st.text_input("Masukkan nama website: ")
    link_gambar = st.text_input("Masukkan link gambar: ")
    judul_artikel = st.text_input("Masukkan judul artikel: ")
    nama_penulis = st.text_input("Masukkan nama penulis: ")
    tanggal_artikel = st.date_input("Masukkan tanggal artikel dibuat: ")
    link_artikel = st.text_input("Masukkan link artikel di sini: ")
    if st.button("Tambah Artikel"):
        db.add_artikel(nama_website, link_gambar, judul_artikel, nama_penulis, tanggal_artikel, link_artikel)
        st.success("Artikel Berhasil Ditambahkan")
        time.sleep(2)
        st.rerun()
if pilihan_artikel == "Update":
    id_artikel = st.selectbox("Pilih id artikel: ", options=df_artikel["id_artikel"], index=0)
    
    nama_website_default = df_artikel.loc[df_artikel["id_artikel"] == id_artikel, "nama_website"].values[0]
    nama_website = st.text_input("Masukkan nama website baru: ", nama_website_default)
    
    link_gambar_default = df_artikel.loc[df_artikel["id_artikel"] == id_artikel, "link_gambar"].values[0]
    link_gambar = st.text_input("Masukkan link gambar baru: ", link_gambar_default)
    
    judul_artikel_default = df_artikel.loc[df_artikel["id_artikel"] == id_artikel, "judul_artikel"].values[0]
    judul_artikel = st.text_input("Masukkan judul artikel baru: ", link_gambar_default)
    
    
    nama_penulis_default = df_artikel.loc[df_artikel["id_artikel"] == id_artikel, "nama_penulis"].values[0]
    nama_penulis = st.text_input("Masukkan nama penulis baru: ", nama_penulis_default)
    
    tanggal_artikel_default = df_artikel.loc[df_artikel["id_artikel"] == id_artikel, "tanggal_artikel"].values[0]
    tanggal_artikel = st.date_input("Masukkan tanggal artikel baru: ", tanggal_artikel_default)
    
    link_artikel_default = df_artikel.loc[df_artikel["id_artikel"] == id_artikel, "link_artikel"].values[0]
    link_artikel = st.text_input("Masukkan link artikel baru: ", link_artikel_default)
    
    if st.button("Update Artikel"):
        db.update_artikel(nama_website, link_gambar, judul_artikel, nama_penulis, tanggal_artikel, link_artikel, id_artikel)
        st.success("Berhasil Update Artikel!")
        time.sleep(2)
        st.rerun()

if pilihan_artikel == "Hapus":
    id_artikel = st.selectbox("Masukkan ID artikel yang ingin dihapus: ", options=df_artikel["id_artikel"], index=0)
    if st.button("Hapus Artikel"):
        db.hapus_artikel(id_artikel)
        st.success("Berhasil Hapus Artikel!")
        time.sleep(2)
        st.rerun()
