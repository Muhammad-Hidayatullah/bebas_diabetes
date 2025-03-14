import streamlit as st
from assets import database as db
import time

st.title("RELASI PENYAKIT DAN GEJALA")
st.subheader("PENYAKIT")
penyakit_df = db.fetch_penyakit()
penyakit_df_html = penyakit_df.to_html(index=False, escape=False)
st.markdown(st.session_state.style_tabel + penyakit_df_html, unsafe_allow_html=True)

st.subheader("GEJALA")
gejala_df = db.fetch_gejala()
gejala_df_html = gejala_df.to_html(index=False, escape=False)
st.markdown(st.session_state.style_tabel + gejala_df_html, unsafe_allow_html=True)

st.subheader("RELASI PENYAKIT DAN GEJALA")
df_relasi_penyakit_dan_gejala = db.fetch_relasi_penyakit_dan_gejala_full()
relasi_penyakit_dan_gejala_df_html = df_relasi_penyakit_dan_gejala.to_html(index=False, escape=False)
st.markdown(st.session_state.style_tabel + relasi_penyakit_dan_gejala_df_html, unsafe_allow_html=True)


pilihan_relasi = st.selectbox("Pilih Opsi untuk Relasi Penyakit dan Gejala: ", options=["Tambah Relasi", "Update Relasi", "Hapus Relasi"])

df_penyakit = db.fetch_penyakit()
kol_id_penyakit = df_penyakit["id_komplikasi_penyakit"]

df_gejala = db.fetch_gejala()
kol_id_gejala = df_gejala["id_gejala"]


if pilihan_relasi == "Tambah Relasi":
    id_komplikasi_penyakit = st.selectbox("Masukkan kode penyakit: ", options=kol_id_penyakit, index=0)
    id_gejala = st.selectbox("Masukkan kode gejala: ", options=kol_id_gejala, index=0)
    if st.button("Tambah Relasi"):
        db.add_relasi_penyakit_dan_gejala(id_komplikasi_penyakit, id_gejala)
        time.sleep(2)
        st.rerun()
if pilihan_relasi == "Update Relasi":
    id_komplikasi_penyakit = st.selectbox("Masukkan kode penyakit: ", options=kol_id_penyakit, index=0)
    id_gejala = st.selectbox("Masukkan kode gejala: ", options=df_relasi_penyakit_dan_gejala[df_relasi_penyakit_dan_gejala["id_komplikasi_penyakit"] == id_komplikasi_penyakit]["id_gejala"], index=0)
    
    id_komplikasi_penyakit_baru = st.selectbox("Masukkan kode penyakit baru: ", options=kol_id_penyakit)
    id_gejala_baru = st.selectbox("Masukkan kode gejala baru: ", options=kol_id_gejala, index=0)
    
    if st.button("Update Relasi"):
        db.update_relasi_penyakit_dan_gejala(id_komplikasi_penyakit, id_gejala, id_gejala_baru)
        time.sleep(2)
        st.rerun()

if pilihan_relasi == "Hapus Relasi":
    id_komplikasi_penyakit = st.selectbox("Masukkan kode penyakit: ", options=df_relasi_penyakit_dan_gejala["id_komplikasi_penyakit"].unique(), index=0)
    id_gejala = st.selectbox("Masukkan kode gejala: ", options=df_relasi_penyakit_dan_gejala[df_relasi_penyakit_dan_gejala["id_komplikasi_penyakit"] == id_komplikasi_penyakit]["id_gejala"], index=0)
    if st.button("Hapus Relasi"):
        db.hapus_relasi_penyakit_dan_gejala(id_komplikasi_penyakit, id_gejala)
        time.sleep(2)
        st.rerun()
