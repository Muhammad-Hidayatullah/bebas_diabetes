import streamlit as st
from fpdf import FPDF
import datetime
from assets import database as db
import time
from base64 import b64encode
import re
import pandas as pd
st.html("""
  <style>
    [alt=Logo] {
      height: 6rem;
    }
  </style>
        """)
st.logo("assets/logo_diabetes.png", size="large")

#st.title("DIAGNOSIS PENYAKIT DIABETES MELLITUS TIPE 2", anchor=False)
def variabel_awal():
    st.session_state.next = -2
    st.session_state.kode_pasien = ""
    st.session_state.nama = ""
    st.session_state.username_pengguna = ""
    st.session_state.password_pengguna = ""
    st.session_state.tanggal_lahir = datetime.date.today()
    st.session_state.pekerjaan = ""
    st.session_state.email = ""
    
    
    # sesuai KTP
    st.session_state.pekerjaan_pekerjaan = [
    "Belum / Tidak Bekerja",
    "Mengurus Rumah Tangga",
    "Pelajar / Mahasiswa",
    "Pensiunan",
    "Pegawai Negeri Sipil",
    "Tentara Nasional Indonesia",
    "Kepolisian RI",
    "Perdagangan",
    "Petani / Pekebun",
    "Peternak",
    "Nelayan / Perikanan",
    "Industri",
    "Konstruksi",
    "Transportasi",
    "Karyawan Swasta",
    "Karyawan BUMN",
    "Karyawan BUMD",
    "Karyawan Honorer",
    "Buruh Harian Lepas",
    "Buruh Tani / Perkebunan",
    "Buruh Nelayan / Perikanan",
    "Buruh Peternakan",
    "Pembantu Rumah Tangga",
    "Tukang Cukur",
    "Tukang Listrik",
    "Tukang Batu",
    "Tukang Kayu",
    "Tukang Sol Sepatu",
    "Tukang Las / Pandai Besi",
    "Tukang Jahit",
    "Penata Rambut",
    "Penata Rias",
    "Penata Busana",
    "Mekanik",
    "Tukang Gigi",
    "Seniman",
    "Tabib",
    "Paraji",
    "Perancang Busana",
    "Penterjemah",
    "Imam Masjid",
    "Pendeta",
    "Pastur",
    "Wartawan",
    "Ustadz / Mubaligh",
    "Juru Masak",
    "Promotor Acara",
    "Anggota DPR-RI",
    "Anggota DPD",
    "Anggota BPK",
    "Presiden",
    "Wakil Presiden",
    "Anggota Mahkamah Konstitusi",
    "Anggota Kabinet / Kementerian",
    "Duta Besar",
    "Gubernur",
    "Wakil Gubernur",
    "Bupati",
    "Wakil Bupati",
    "Walikota",
    "Wakil Walikota",
    "Anggota DPRD Propinsi",
    "Anggota DPRD Kabupaten / Kota",
    "Dosen",
    "Guru",
    "Pilot",
    "Pengacara",
    "Notaris",
    "Arsitek",
    "Akuntan",
    "Konsultan",
    "Dokter",
    "Bidan",
    "Perawat",
    "Apoteker",
    "Psikiater / Psikolog",
    "Penyiar Televisi",
    "Penyiar Radio",
    "Pelaut",
    "Peneliti",
    "Sopir",
    "Pialang",
    "Paranormal",
    "Pedagang",
    "Perangkat Desa",
    "Kepala Desa",
    "Biarawati",
    "Wiraswasta",
    "Anggota Lembaga Tinggi",
    "Artis",
    "Atlit",
    "Cheff",
    "Manajer",
    "Tenaga Tata Usaha",
    "Operator",
    "Pekerja Pengolahan", 
    "Kerajinan",
    "Teknisi",
    "Asisten Ahli",
    "Lainnya"
    ]

    
    
    st.session_state.tanggal_pemeriksaan = datetime.date.today()
    st.session_state.alamat = ""
    st.session_state.jenis_kelamin = "LAKI-LAKI"
    
    # Pemeriksaan fisik
    st.session_state.berat_badan = 0.0
    st.session_state.tinggi_badan = 0.0
    st.session_state.lingkar_perut = 0.0
    
    # Faktor Tidak Bisa Diubah
    st.session_state.usia_di_atas_40_tahun = "TIDAK"
    st.session_state.riwayat_keluarga_diabetes = "TIDAK"
    st.session_state.riwayat_diabetes_gestasional = "TIDAK"
    st.session_state.riwayat_lahir_di_bawah_2_koma_5_gram = "TIDAK"
    
    # Kebiasaan Hidup
    st.session_state.konsumsi_alkohol = "TIDAK"
    st.session_state.kurang_aktivitas = "TIDAK"
    st.session_state.kurang_tidur = "TIDAK"
    st.session_state.merokok = "TIDAK"
    st.session_state.pola_makan_buruk = "TIDAK"
    
    
    # Pemeriksaan Lab
    st.session_state.gula_darah_sewaktu = 0.0
    st.session_state.gula_darah_puasa = 0.0
    st.session_state.gula_darah_2_jam_setelah_makan = 0.0
    st.session_state.tekanan_darah = "0/0"
    st.session_state.sistole, st.session_state.diastole = st.session_state.tekanan_darah.split("/")
    st.session_state.HDL = 0.0
    st.session_state.LDL = 0.0
    st.session_state.trigliserida = 0.0
    st.session_state.total_kolestrol = 0.0
    st.session_state.total_kolestrol_darah = 0.0 # rumusnya: LDL + HDL + 1/5 Trigliserida
    
    # Risiko
    st.session_state.risiko_diabetes = "RENDAH"
    





# inisialisasi session state sudah daftar
if "sudah_daftar" not in st.session_state:
    st.session_state.sudah_daftar = False
    
# inisialisasi session state langkah-langkah pengisian formulir sampai gejala
if "next" not in st.session_state:
    

        
    variabel_awal()
    
if st.session_state.next == -2:
    st.session_state.tanggal_lahir = db.get_tanggal_lahir_pasien("andigunawan01", "andi123")
    st.title("Login")
    st.write("Silahkan Login terlebih dahulu")
    st.session_state.username_pengguna = st.text_input("Masukkan username: ")
    st.session_state.password_pengguna = st.text_input("Masukkan password: ", type="password")
    
    
    if st.button(label="Login"):
        if db.check_pengguna(st.session_state.username_pengguna, st.session_state.password_pengguna) == True:
            
            #tanggal lahir pasien
            st.session_state.tanggal_lahir = db.get_tanggal_lahir_pasien(st.session_state.username_pengguna, st.session_state.password_pengguna)
            
            st.session_state.next = 0
            st.success(f"Login berhasil! Selamat datang, {st.session_state.username_pengguna}.")
            time.sleep(2)
            st.rerun()
            
        else:
            st.error("Username atau password salah.")
    
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    st.write("Belum memiliki akun? Klik tombol registrasi di bawah ini!")
    if st.button(label="Registrasi"):
        
        
        st.session_state.next = -1
        st.rerun()
        
        
        
def validasi_email_regex(email):
    regex = r'^[a-zA-Z0-9_.+-]+@gmail\.com$'
    return re.match(regex, email) is not None

def validasi_password(password):
    
    return len(password) >= 7  # Minimum length of 6 characters

if st.session_state.next == -1:
    st.title("Registrasi")
    st.write("Silahkan lakukan registrasi")
    st.session_state.username_pengguna = ""
    st.session_state.username_pengguna = st.text_input("Masukkan username: ")
    password_pengguna = ""
    password_pengguna = st.text_input("Masukkan password: ", type="password")
    
    nama = ""
    nama = st.text_input("Nama Lengkap: ", value=st.session_state.nama)
    jenis_kelamin = st.radio("Jenis Kelamin", ("LAKI-LAKI", "PEREMPUAN"), horizontal=True, index=("LAKI-LAKI", "PEREMPUAN").index(st.session_state.jenis_kelamin))
    tanggal_lahir = st.date_input("Masukkan tanggal lahir: (y-m-d)", min_value=datetime.date(1900, 1, 1), max_value=datetime.datetime.now())
    
    
    pekerjaan = st.selectbox("Pekerjaan: ", options=st.session_state.pekerjaan_pekerjaan)
    if pekerjaan == "Lainnya":
        pekerjaan_lainnya = st.text_input("Pekerjaan: ")
        pekerjaan = pekerjaan_lainnya
    
    
    email = st.text_input("Masukkan email: ", value=st.session_state.email)
    
    alamat = st.text_input("Alamat Tempat Tinggal: ", value=st.session_state.alamat)

    
    if st.button(label="Registrasi"):
        cek_validasi_data_pasien = db.check_data_registrasi_pasien(st.session_state.username_pengguna, email, password_pengguna, nama, alamat)
            
        if cek_validasi_data_pasien == True:
            st.success("Data valid.")
            db.add_pasien(db.menambah_id_pasien_default(), st.session_state.username_pengguna, password_pengguna, nama, jenis_kelamin, alamat, email, pekerjaan, tanggal_lahir)
            time.sleep(2)
            st.session_state.next = -2
            st.rerun()
            
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    st.write("Sudah memiliki akun? Klik tombol Login di bawah ini!")
    if st.button(label="Login"):
        st.session_state.next = -2
        st.rerun()
            
            
if st.session_state.next == 0:
    with st.form("form_data_pasien"):
        st.title("Data Pasien")
        
        if "data_pasien" not in st.session_state:
            st.session_state.data_pasien = []
        
        st.session_state.data_pasien = db.get_data_pasien(st.session_state.username_pengguna)
        
        
        # Mengambil data dari database
        st.session_state.kode_pasien = st.session_state.data_pasien[0]
        st.session_state.username_pengguna = st.session_state.data_pasien[1]
        st.session_state.password_pengguna = st.session_state.data_pasien[2]
        st.session_state.nama_lengkap = st.session_state.data_pasien[3]
        st.session_state.jenis_kelamin = st.session_state.data_pasien[4]
        st.session_state.alamat = st.session_state.data_pasien[5]
        st.session_state.email = st.session_state.data_pasien[6]
        st.session_state.pekerjaan = st.session_state.data_pasien[7]
        st.session_state.tanggal_lahir = st.session_state.data_pasien[8]
        
        
        
        
        st.write("Kode Pasien       : " + st.session_state.kode_pasien)
        st.write("Username          : " + st.session_state.username_pengguna)
        st.write("Password          : " + len(st.session_state.password_pengguna) * "*")
        st.write("Nama Lengkap      : " + st.session_state.nama_lengkap)
        st.write("Jenis Kelamin     : " + st.session_state.jenis_kelamin)
        st.write("Alamat            : " + st.session_state.alamat)
        st.write("Email             : " + st.session_state.email)
        st.write("Pekerjaan         : " + st.session_state.pekerjaan)
        st.write("Tanggal Lahir     : " + str(st.session_state.tanggal_lahir))


        
        if "update_data" not in st.session_state:
            st.session_state.update_data = 0
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.form_submit_button(label="Logout"):
                st.session_state.next = -2
                variabel_awal()
                st.rerun()
        
        with col2:
            if st.form_submit_button(label="Riwayat"):
                st.session_state.next = 100
                st.rerun()
                
        with col3:
            if st.form_submit_button(label="Update Data"):
                st.session_state.update_data = 1
                
            
        if st.session_state.update_data == 1:
            password_pengguna = st.text_input("Masukkan password Anda: ", type="password")
            if st.form_submit_button("Klik"):
                if db.check_pengguna(st.session_state.username_pengguna, password_pengguna) == True:
                    st.session_state.next = 101
                    st.rerun()
                else:
                    st.warning("Password yang Anda masukkan salah!")
                    
        
        
        with col4:
            if st.form_submit_button(label="Lanjut Ke Pemeriksaan"):
                st.session_state.next = 1
                st.rerun()
            
            
def buat_laporan_riwayat(nama_lengkap, username_pengguna, tanggal_lahir, tanggal_pemeriksaan, jenis_kelamin, alamat,
                 pekerjaan, email, risiko_diabetes, usia_di_atas_40_tahun, riwayat_keluarga_diabetes, riwayat_diabetes_gestasional,
                 riwayat_lahir_di_bawah_2_koma_5_gram, konsumsi_alkohol, kurang_aktivitas, merokok, pola_makan_buruk,
                 kurang_tidur, tinggi_badan, berat_badan, lingkar_perut, indeks_massa_tubuh, tekanan_darah, HDL, LDL, trigliserida,
                 total_kolestrol_darah, gula_darah_sewaktu, gula_darah_puasa, gula_darah_2_jam_setelah_makan, diagnosis_penyakit_tertentu, relasi_penyakit_dan_gejala):
    pdf = FPDF()
    pdf.add_page()
    
    pdf.image("assets/logo_diabetes.png", x=10, y=8, w=30)  # Adjust x, y, and w for logo position and size
    pdf.image("assets/puskesmas_pkc_taman_sari.jpeg", x=170, y=8, w=30)
    
    # Menambahkan judul
    pdf.set_font("Arial", size=18, style="B")
    pdf.cell(200, 15, txt="LAPORAN HASIL PEMERIKSAAN ", ln=True, align='C')
    
    pdf.ln() 
    
    pdf.set_font("Arial", size=13, style="B")
    pdf.cell(75, 10, txt="Data Pasien", ln=True)
    pdf.set_font("Arial", size=10)
    

    data_pribadi = [
        ['Nama: ', nama_lengkap],
        ["Username: ", username_pengguna],
        ["Tanggal Lahir: ", str(tanggal_lahir)],
        ["Tanggal Pemeriksaan", str(tanggal_pemeriksaan)],
        ['Jenis Kelamin: ', jenis_kelamin],
        ['Alamat: ', alamat],
        ['Pekerjaan: ', pekerjaan],
        ['Email: ', email],
        ["Risiko Diabetes Tipe 2: ", risiko_diabetes]
    ]
    for row in data_pribadi:
        pdf.cell(75, 10, row[0], 1)  # First column
        pdf.cell(120, 10, row[1], 1)  # Second column
        pdf.ln()  # Move to the next line

      # Return PDF as a string
    pdf.ln()    
    
    pdf.set_font("Arial", size=13, style="B")
    pdf.cell(75, 10, txt="Faktor Tidak Bisa Diubah", ln=True)
    pdf.set_font("Arial", size=10)
    
    pola_gaya_hidup = [
        ["Usia di atas 45 tahun: ", usia_di_atas_40_tahun],
        ["Riwayat Keluarga Diabetes: ", riwayat_keluarga_diabetes],
        ["Riwayat Diabetes Gestasional: ", riwayat_diabetes_gestasional],
        ["Riwayat Lahir <2,5 kg atau Prematur: ", riwayat_lahir_di_bawah_2_koma_5_gram],
    ]
    
    
    for row in pola_gaya_hidup:
        pdf.cell(75, 10, row[0], 1)  # First column
        pdf.cell(120, 10, row[1], 1)  # Second column
        pdf.ln()
    
    pdf.ln()
    pdf.set_font("Arial", size=13, style="B")
    pdf.cell(75, 10, txt="Pola Gaya Hidup", ln=True)
    pdf.set_font("Arial", size=10)
    pola_gaya_hidup = [
        ["Konsumsi Alkohol: ", konsumsi_alkohol],
        ["Kurang Aktivitas Fisik: ", kurang_aktivitas],
        ["Kebiasaan Merokok: ", merokok],
        ["Pola Makan Buruk : ", pola_makan_buruk],
        ["Tidur Tidak Berkualitas: ", kurang_tidur],
        
    ]
    for row in pola_gaya_hidup:
        pdf.cell(75, 10, row[0], 1)  # First column
        pdf.cell(120, 10, row[1], 1)  # Second column
        pdf.ln()
    
    pdf.ln()
    
    pdf.set_font("Arial", size=13, style="B")
    pdf.cell(75, 10, txt="Pemeriksaan Fisik", ln=True)
    pdf.set_font("Arial", size=10)
    
    pemeriksaan_fisik = [
        ["Parameter", "Hasil", "Nilai Normal"],
        ["Tinggi Badan: ", str(tinggi_badan)+" cm", "-"],
        ["Berat Badan: ", str(berat_badan)+" kg", "-"],
        ["Lingkar Perut: ", str(lingkar_perut)+" cm", " Pria <90cm , Wanita <80cm"],
        ["Indeks Massa Tubuh: ", str(indeks_massa_tubuh)+" kg/m2", " <25 kg/m2"],
    ]
    
    for row in pemeriksaan_fisik:
        pdf.cell(50, 10, row[0], 1)  # First column
        pdf.cell(50, 10, row[1], 1)
        pdf.cell(60, 10, row[2], 1)# Second column
        pdf.ln()
    
    pdf.ln()
    pdf.set_font("Arial", size=13, style="B")
    pdf.cell(75, 10, txt="Hasil Tekanan Darah dan Kolestrol Darah", ln=True)
    pdf.set_font("Arial", size=10)
    hasil_laboratorium = [
        
        ["Parameter", "Hasil", "Nilai Normal"],
        ["Tekanan Darah: ", str(tekanan_darah)+ " mmHg", " <140/90 mmHg"],
        ["HDL : ", str(HDL)+" mg/dL", " >=40 mg/dL"],
        ["LDL : ", str(LDL)+" mg/dL", " <=100 mg/dL"],
        ["Trigliserida : ", str(trigliserida)+" mg/dL", " <=150 mg/dL"],
        ["Total Kolestrol Darah: ", str(total_kolestrol_darah)+" mg/dL", " <=240 mg/dL"],
    ]
   
    
    for row in hasil_laboratorium:
        pdf.cell(50, 10, row[0], 1)  # First column
        pdf.cell(50, 10, row[1], 1) # Second column
        pdf.cell(50, 10, row[2], 1)
        pdf.ln()
    
    pdf.ln()
    
    pdf.set_font("Arial", size=13, style="B")
    pdf.cell(75, 10, txt="Hasil Laboratorium", ln=True)
    pdf.set_font("Arial", size=10)
    hasil_laboratorium = [
        ["Parameter", "Nilai", "Nilai Normal"],
        ["Gula Darah Sewaktu (GDS): ", str(gula_darah_sewaktu)+" mg/dL", " <140 mg/dL"],
        ["Gula Darah Puasa (GDP): ", str(gula_darah_puasa)+" mg/dL", " <100 mg/dL"],
        ["Gula Darah 2 Jam Setelah Makan (GD2PP): ", str(gula_darah_2_jam_setelah_makan)+" mg/dL", " <140 mg/dL"],

    ]
    
    for row in hasil_laboratorium:
        pdf.cell(90, 10, row[0], 1)
        pdf.cell(50, 10, row[1], 1) 
        pdf.cell(50, 10, row[2], 1) 
        pdf.ln()
    
    pdf.ln(120)
    
    
    
    pdf.set_font("Arial", size=18, style="B")
    pdf.cell(75, 10, txt="Diagnosis Komplikasi Penyakit", ln=True)
    
    pdf.set_font("Arial", size=13, style="B")
    pdf.cell(75, 10, txt="Gejala-Gejala Terpilih", ln=True)
    pdf.set_font("Arial", size=10)
    
    if gejala_terpilih:
        daftar_gejala_terpilih = gejala_terpilih.split(", ")
        for i, gejala in enumerate(daftar_gejala_terpilih, start=1):
            pdf.cell(200, 10, txt=f"{i}. {gejala}", ln=True)
        
    else:            
        pdf.cell(200, 10, txt="-", ln=True)
        
    pdf.ln()
    
    pdf.set_font("Arial", size=13, style="B")
    pdf.cell(75, 10, txt="Komplikasi Penyakit", ln=True)
    pdf.set_font("Arial", size=10)
    if diagnosis_penyakit_tertentu is not None:
        for index, row in diagnosis_penyakit_tertentu.iterrows():
            
    
            
            
            if row['Nama Penyakit'] is None:
                pdf.set_font("Arial", size=10)
                pdf.cell(200, 10, txt=f"-", ln=True)
            else:
                pdf.set_font("Arial", size=10, style="B")
                pdf.cell(200, 10, txt=f"{row['Nama Penyakit']} : {row['Persentase Kecocokan']:.2f}%", ln=True)
                pdf.set_font("Arial", size=10)
                pdf.cell(200, 10, txt=f"{db.get_penjelasan_penyakit(row['Nama Penyakit'])}", ln=True)
            
            pdf.set_font("Arial", size=10, style="B")
            pdf.cell(200, 10, txt=f"Gejala yang Cocok", ln=True)
            
            
            pdf.set_font("Arial", size=10)
            
            
            daftar_gejala = row['Gejala Cocok']
            if daftar_gejala is None:
                pdf.cell(200, 10, txt=f"-", ln=True)
            else:
                daftar_gejala = daftar_gejala.split(", ")
            
                for i, gejala_cocok in enumerate(daftar_gejala, start=1):
                    pdf.cell(200, 10, txt=f"{i}. {gejala_cocok}", ln=True)
                
        
            pdf.set_font("Arial", size=10, style="B")
            pdf.cell(200, 10, txt=f"Gejala Penyakit", ln=True)
            pdf.set_font("Arial", size=10)
            
            if row['Nama Penyakit'] is None:
                pdf.cell(200, 10, txt=f"-", ln=True)
            else:
                if relasi_penyakit_dan_gejala is not None:
                    gejala_penyakit = relasi_penyakit_dan_gejala[row['Nama Penyakit']]
                    
                    for i, gejala in enumerate(gejala_penyakit, start=1):
                        pdf.cell(200, 10, txt=f"{i}: {gejala}", ln=True)
        
                #Solusi
                pdf.set_font("Arial", size=10, style="B")
                pdf.cell(200, 10, txt=f"Solusi Penyakit", ln=True)
                pdf.set_font("Arial", size=10)
                
                solusi_penyakit = db.get_solusi_penyakit(row['Nama Penyakit'])
                solusi_penyakit = solusi_penyakit.split(";")
                daftar_solusi = []
                for frasa in solusi_penyakit:
                    daftar_solusi.append(frasa.strip())

                # Loop untuk menampilkan dengan nomor urut
                for i, frasa in enumerate(daftar_solusi, start=1):
                    pdf.cell(200, 10, txt=f"{i}. {frasa}", ln=True)
                
                pdf.ln(50)
    else:
        pdf.cell(200, 10, txt="Tidak ada penyakit yang cocok", ln=True)
    
    return pdf.output(dest="S").encode("latin1")


    

   
if st.session_state.next == 100:
    st.title("Riwayat Pengguna")
    st.subheader("Riwayat Pemeriksaan Kesehatan")
    df_pemeriksaan_kesehatan_pasien = db.fetch_pemeriksaan_kesehatan_pasien(st.session_state.kode_pasien)
    if df_pemeriksaan_kesehatan_pasien is None:
        st.write("--")
    else:
        df_pemeriksaan_kesehatan_pasien = pd.DataFrame(df_pemeriksaan_kesehatan_pasien)
        st.write(df_pemeriksaan_kesehatan_pasien)

    st.subheader("Riwayat Diagnosis Penyakit")
    df_diagnosis_penyakit = db.get_diagnosis_penyakit(st.session_state.kode_pasien)
    if df_diagnosis_penyakit is None:
        st.write("--")
    else:
        df_diagnosis_penyakit = pd.DataFrame(df_diagnosis_penyakit)
        st.write(df_diagnosis_penyakit)
        
        
        #Opsi untu hapus atau unduh
        opsi = st.selectbox("Pilih Opsi: ", ("Unduh", "Hapus"))
        
        tanggal_pemeriksaan = st.selectbox("Pilih tanggal: ", options=df_diagnosis_penyakit["Tanggal Diagnosis"].unique())
    
        #tanggal_pemeriksaan = pd.to_datetime(tanggal_pemeriksaan)
        df_pemeriksaan_kesehatan_pasien_tertentu = df_pemeriksaan_kesehatan_pasien.loc[df_pemeriksaan_kesehatan_pasien["Tanggal Pemeriksaan"] == tanggal_pemeriksaan]
        st.write(df_pemeriksaan_kesehatan_pasien_tertentu)
        
        if not df_pemeriksaan_kesehatan_pasien_tertentu.empty:
            row = df_pemeriksaan_kesehatan_pasien_tertentu.iloc[0]  # Get first row safely
            risiko_diabetes = row["Risiko Diabetes"]
            usia_di_atas_40_tahun = row["Usia Di Atas 40 Tahun"]
            riwayat_keluarga_diabetes = row["Riwayat Keluarga Diabetes"]
            riwayat_diabetes_gestasional = row["Riwayat Diabetes Gestasional"]
            riwayat_lahir_di_bawah_2_koma_5_gram = row["Riwayat Berat Badan Lahir Rendah"]
            konsumsi_alkohol = row["Konsumsi Alkohol"]
            kurang_aktivitas = row["Kurang Aktivitas"]
            merokok = row["Merokok"]
            pola_makan_buruk = row["Pola Makan Buruk"]
            kurang_tidur = row["Kurang Tidur"]
            tinggi_badan = str(row["Tinggi Badan"])
            berat_badan = str(row["Berat Badan"])
            lingkar_perut = str(row["Lingkar Perut"])
            indeks_massa_tubuh = str(row["Indeks Massa Tubuh"])
            gula_darah_sewaktu = str(row["Gula Darah Sewaktu"])
            gula_darah_puasa = str(row["Gula Darah Puasa"])
            gula_darah_2_jam_setelah_makan = str(row["Gula Darah 2 Jam Setelah Makan"])
            tekanan_darah = str(row["Tekanan Darah"])
            HDL = str(row["HDL"])
            LDL = str(row["LDL"])
            trigliserida = str(row["Trigliserida"])
            total_kolestrol = str(row["Total Kolesterol"])
        else:
            st.write("Tidak ada data untuk tanggal yang dipilih.")

        
        df_diagnosis_penyakit_tertentu = df_diagnosis_penyakit.loc[df_diagnosis_penyakit["Tanggal Diagnosis"] == tanggal_pemeriksaan]
        st.write(df_diagnosis_penyakit_tertentu)

        
        row = df_diagnosis_penyakit_tertentu.iloc[0]  # Get first
        gejala_terpilih = row["Gejala Terpilih"]
        
        
        diagnosis_penyakit_tertentu = df_diagnosis_penyakit_tertentu.iloc[:, 3:]
        diagnosis_penyakit_tertentu = diagnosis_penyakit_tertentu.drop("Gejala Terpilih", axis=1)
        
        #Relasi Penyakit dan Gejala
        data_relasi = db.fetch_relasi_nama_penyakit_dan_nama_gejala()
        relasi_penyakit_dan_gejala = {}
        for penyakit, gejala in data_relasi:
            if penyakit not in relasi_penyakit_dan_gejala:
                relasi_penyakit_dan_gejala[penyakit] = []  # Buat list kosong jika penyakit belum ada
            relasi_penyakit_dan_gejala[penyakit].append(gejala) 
        
        
       
        if opsi == "Unduh":
            if st.button("Unduh Laporan"):
                file_pdf = buat_laporan_riwayat(st.session_state.nama_lengkap, st.session_state.username_pengguna, st.session_state.tanggal_lahir, tanggal_pemeriksaan, st.session_state.jenis_kelamin, st.session_state.alamat,
                        st.session_state.pekerjaan, st.session_state.email, risiko_diabetes, usia_di_atas_40_tahun, riwayat_keluarga_diabetes, riwayat_diabetes_gestasional,
                        riwayat_lahir_di_bawah_2_koma_5_gram, konsumsi_alkohol, kurang_aktivitas, merokok, pola_makan_buruk,
                        kurang_tidur, tinggi_badan, berat_badan, lingkar_perut, indeks_massa_tubuh, tekanan_darah, HDL, LDL, trigliserida,
                        total_kolestrol, gula_darah_sewaktu, gula_darah_puasa, gula_darah_2_jam_setelah_makan, diagnosis_penyakit_tertentu, relasi_penyakit_dan_gejala)

                with open("report.pdf", "wb") as f:
                    f.write(file_pdf)

                with open("report.pdf", "rb") as f:
                    base64_pdf = base64.b64encode(f.read()).decode("utf-8")

                pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="400" type="application/pdf">'
                st.markdown(pdf_display, unsafe_allow_html=True)

                st.write(f"PDF size: {len(file_pdf)} bytes")  # Debugging

                
                st.download_button(
                    label="Download PDF",
                    data=file_pdf,
                    file_name = "Laporan Kesehatan_"+st.session_state.nama_lengkap+ "_"+str(tanggal_pemeriksaan)+".pdf",
                    mime="application/pdf"
                )
        if opsi == "Hapus":
            if st.button("Hapus"):
                db.hapus_pemeriksaan_kesehatan_dan_diagnosis(tanggal_pemeriksaan)
                st.success("Pemeriksaan Kesehatan dan Diagnosis Berhasil Dihapus")
                time.sleep(2)
                st.rerun()
        
    
    if st.button("Kembali"):
        st.session_state.next = 0
        st.rerun()
    
    
    
if st.session_state.next == 101:
    with st.form("form-update-data-pasien"):
        st.title("Update Data Pasien")
        st.warning("Apabila ada nilai yang tidak ingin diubah, jangan diganti!")
        username = st.text_input("Masukkan username baru: ", value=st.session_state.username_pengguna)
        password = st.text_input("Masukkan password baru: ", type= "password", value=st.session_state.password_pengguna)
        nama = st.text_input("Masukkan nama lengkap baru: ", value=st.session_state.nama_lengkap)
        jenis_kelamin = st.radio("Jenis Kelamin: ", ("LAKI-LAKI", "PEREMPUAN"), horizontal=True, index=("LAKI-LAKI", "PEREMPUAN").index(st.session_state.jenis_kelamin))
        alamat = st.text_input("Masukkan alamat baru: ", value=st.session_state.alamat)
        email = st.text_input("Masukkan email baru: ", value=st.session_state.email)
        

        pekerjaan = st.selectbox("Masukkan pekerjaan baru: ", options=st.session_state.pekerjaan_pekerjaan, index=st.session_state.pekerjaan_pekerjaan.index(st.session_state.pekerjaan)) 
        tanggal_lahir = st.date_input("Masukkan tanggal lahir: (y-m-d)", min_value=datetime.date(1900, 1, 1), max_value=datetime.datetime.now(), value=st.session_state.tanggal_lahir)
        
        
        col1, col2 = st.columns(2)
        
        with col2:
            if st.form_submit_button(label="Update"):

                
                validation_errors = []
                
                if db.cek_username(username) == True and username != st.session_state.username_pengguna:
                    validation_errors.append("Username sudah terdaftar")

                    
                if db.cek_email(email) == True and email != st.session_state.email:
                    validation_errors.append("Email Sudah Terdaftar")
                # Check if username is provided
                if not st.session_state.username_pengguna:
                    validation_errors.append("Username tidak boleh kosong.")

                # Check if password is provided and meets the length requirement
                if not password or not validasi_password(password):
                    validation_errors.append("Password harus lebih dari 6 karakter.")

                # Check if full name is provided
                if not nama:
                    validation_errors.append("Nama lengkap tidak boleh kosong.")

                # Check if email is provided and valid
                if not email or not validasi_email_regex(email):
                    validation_errors.append("Email tidak valid. Pastikan menggunakan format yang benar (@gmail.com).")

                # Check if address is provided
                if not alamat:
                    validation_errors.append("Alamat tidak boleh kosong.")

                # Display validation errors
                if validation_errors:
                    for error in validation_errors:
                        st.error(error)
                else:
                    st.success("Update Data Anda Berhasil!.")
                    db.update_pengguna(username, password, nama, jenis_kelamin, alamat, email, pekerjaan, tanggal_lahir, st.session_state.username_pengguna)
                    
                    st.session_state.username_pengguna = username
                    st.session_state.next = 0
                    st.session_state.update_data = 0
                    time.sleep(2)
                    st.rerun()
        with col1:
            if st.form_submit_button(label="Kembali"):
                st.session_state.next = 0
                st.rerun()
            
            
if st.session_state.next == 1:
    
    st.session_state.faktor_risiko_1 = 0
    st.session_state.daftar_faktor_risiko_1 = []
    
    with st.form(key="form_faktor_tidak_bisa_diubah"):
        st.subheader("Faktor Tidak Bisa Diubah")


        #st.session_state.usia = st.session_state.tanggal_lahir - st.session_state.tanggal_pemeriksaan
        
        st.session_state.usia = (st.session_state.tanggal_pemeriksaan - st.session_state.tanggal_lahir).days
        st.session_state.usia = st.session_state.usia // 360
        

        st.write(st.session_state.usia, "tahun")
        
        if st.session_state.usia > 40:
            st.session_state.usia_di_atas_40_tahun = "YA"
            st.session_state.faktor_risiko_1 = st.session_state.faktor_risiko_1 + 1
            st.session_state.daftar_faktor_risiko_1.append("Usia >45 tahun")
        else:
            st.session_state.usia_di_atas_40_tahun = "TIDAK"
        
        
        st.session_state.usia_di_atas_40_tahun = st.radio("Usia di atas 45 tahun", ("TIDAK", "YA"), horizontal=True, index=("TIDAK", "YA").index(st.session_state.usia_di_atas_40_tahun))
        
            
            
        st.session_state.riwayat_keluarga_diabetes = st.radio("Riwayat Keluarga Diabetes", ("TIDAK", "YA"), horizontal=True, index=("TIDAK", "YA").index(st.session_state.riwayat_keluarga_diabetes))
        
        jenis_kelamin = db.get_jenis_kelamin(st.session_state.username_pengguna)
        if jenis_kelamin == "PEREMPUAN":
            st.session_state.riwayat_diabetes_gestasional = st.radio("Riwayat Melahirkan Bayi > 4 kg atau Terkena Diabetes Mellitus Gestasional", ("TIDAK", "YA"), horizontal=True, index=("TIDAK", "YA").index(st.session_state.riwayat_diabetes_gestasional))
        else:
            st.session_state.riwayat_diabetes_gestasional = "TIDAK"
            
        st.session_state.riwayat_lahir_berat_badan_lahir_rendah = st.radio("Riwayat Lahir <2,5 kg atau terlahir prematur", ("TIDAK", "YA"), horizontal=True, index=("TIDAK", "YA").index(st.session_state.riwayat_lahir_di_bawah_2_koma_5_gram))
        
        
        
        if st.session_state.riwayat_keluarga_diabetes == "YA":
            st.session_state.faktor_risiko_1 = st.session_state.faktor_risiko_1 + 1
            st.session_state.daftar_faktor_risiko_1.append("Riwayat Keluarga Diabetes")
        if jenis_kelamin == "PEREMPUAN" and st.session_state.riwayat_diabetes_gestasional == "YA":
            st.session_state.faktor_risiko_1 = st.session_state.faktor_risiko_1 + 1
            st.session_state.daftar_faktor_risiko_1.append("Riwayat Melahirkan Bayi > 4 kg atau Terkena Diabetes Mellitus Gestasional")
        if st.session_state.riwayat_lahir_di_bawah_2_koma_5_gram == "YA":
            st.session_state.faktor_risiko_1 = st.session_state.faktor_risiko_1 + 1
            st.session_state.daftar_faktor_risiko_1.append("Riwayat Lahir di bawah 2,5 kg")
    
        col1, col2 = st.columns(2)
        with col1:
            if st.form_submit_button("Kembali"):
                st.session_state.next = 0
                st.session_state.update_data = 0
                st.rerun()
        with col2:
            if st.form_submit_button("Lanjut"):
                st.session_state.total_faktor_risiko = st.session_state.faktor_risiko_1
                st.session_state.next = 2
                st.rerun()
     
     
def cek_validasi_tekanan_darah(tekanan_darah):
    pola = r'^\d{1,3}/\d{1,3}$'
    return bool(re.match(pola, tekanan_darah))
   
if st.session_state.next == 2:
    
    st.session_state.faktor_risiko_2 = 0
    st.session_state.daftar_faktor_risiko_2 = []
    
    with st.form(key="form_faktor_bisa_diubah"):
        st.subheader("Pemeriksaan Gaya Hidup")
        st.session_state.konsumsi_alkohol = st.radio("Konsumsi Alkohol", ("TIDAK", "YA"), horizontal=True, index=("TIDAK", "YA").index(st.session_state.konsumsi_alkohol))
        st.session_state.kurang_aktivitas = st.radio("Kurang Aktivitas Fisik (< 150 menit/minggu)", ("TIDAK", "YA"), horizontal=True, index=("TIDAK", "YA").index(st.session_state.kurang_aktivitas))
        st.session_state.merokok = st.radio("Kebiasaan Merokok", ("TIDAK", "YA"), horizontal=True, index=("TIDAK", "YA").index(st.session_state.merokok))
        st.session_state.pola_makan_buruk = st.radio("Pola Makan Buruk (Tinggi gula, garam, dan lemak; rendah serat; serta jarang makan sayur dan buah)", ("TIDAK", "YA"), horizontal=True, index=("TIDAK", "YA").index(st.session_state.pola_makan_buruk))
        st.session_state.kurang_tidur = st.radio("Kurang tidur/gangguan tidur/tidur tidak berkualitas < 6 jam", ("TIDAK", "YA"), horizontal=True, index=("TIDAK", "YA").index(st.session_state.kurang_tidur))
        
        if st.session_state.konsumsi_alkohol == "YA":
            st.session_state.faktor_risiko_2 = st.session_state.faktor_risiko_2 + 1
            st.session_state.daftar_faktor_risiko_2.append("Konsumsi Alkohol")
        if st.session_state.kurang_aktivitas == "YA":
            st.session_state.faktor_risiko_2 = st.session_state.faktor_risiko_2 + 1
            st.session_state.daftar_faktor_risiko_2.append("Kurang Aktivitas")
        if st.session_state.merokok == "YA":
            st.session_state.faktor_risiko_2 = st.session_state.faktor_risiko_2 + 1
            st.session_state.daftar_faktor_risiko_2.append("Aktif Merokok")
        if st.session_state.pola_makan_buruk == "YA":
            st.session_state.faktor_risiko_2 = st.session_state.faktor_risiko_2 + 1
            st.session_state.daftar_faktor_risiko_2.append("Pola Makan Buruk (Tinggi gula, garam, dan lemak; rendah serat; serta jarang makan sayur dan buah)")
        if st.session_state.kurang_tidur == "YA":
            st.session_state.faktor_risiko_2 = st.session_state.faktor_risiko_2 + 1
            st.session_state.daftar_faktor_risiko_2.append("Kurang tidur/gangguan tidur/tidur tidak berkualitas < 6 jam")
        
        st.markdown("---")
        
        st.subheader("Pemeriksaan Fisik")
        st.session_state.tinggi_badan = st.number_input("Tinggi Badan (cm): ", min_value=0.0, max_value=999.0, value=st.session_state.tinggi_badan)
        st.session_state.berat_badan = st.number_input("Berat Badan (kg): ", min_value=0.0, max_value=999.0, value=st.session_state.berat_badan)
        st.session_state.lingkar_perut = st.number_input("Lingkar perut (cm): ", min_value=0.0, max_value=240.0, step=None, value=st.session_state.lingkar_perut)
        
        
        
        st.session_state.indeks_massa_tubuh = 0.0
        if st.session_state.berat_badan == 0.0 or st.session_state.tinggi_badan == 0.0:
            st.session_state.indeks_massa_tubuh = 0.0
        else:
            st.session_state.indeks_massa_tubuh = st.session_state.berat_badan/((st.session_state.tinggi_badan) ** 2) * 10000
            st.session_state.indeks_massa_tubuh = round(st.session_state.indeks_massa_tubuh, 1)
            
        if st.session_state.indeks_massa_tubuh > 25.0:
            st.session_state.faktor_risiko_2 = st.session_state.faktor_risiko_2 + 1
            kelebihan_berat_badan = "Kelebihan Berat Badan: " + str(st.session_state.indeks_massa_tubuh) + " kg/m2"
            st.session_state.daftar_faktor_risiko_2.append(kelebihan_berat_badan)
            
        if st.session_state.jenis_kelamin == "PEREMPUAN" and st.session_state.lingkar_perut >= 80.0:
            st.session_state.faktor_risiko_2 = st.session_state.faktor_risiko_2 + 1
            obesitas_sentral = "Obesitas Sentral: " + str(st.session_state.lingkar_perut) + " cm"
            st.session_state.daftar_faktor_risiko_2.append(obesitas_sentral)
            
        if st.session_state.jenis_kelamin == "LAKI-LAKI" and st.session_state.lingkar_perut >= 90.0:
            st.session_state.faktor_risiko_2 = st.session_state.faktor_risiko_2 + 1
            obesitas_sentral = "Obesitas Sentral: " + str(st.session_state.lingkar_perut) + " cm"
            st.session_state.daftar_faktor_risiko_2.append(obesitas_sentral)
        
        
        st.markdown("---")
        
        st.subheader("Pemeriksaan Tekanan dan Kolestrol Darah")

        st.session_state.tekanan_darah = st.text_input("Tekanan Darah (mmHg): ", value=st.session_state.tekanan_darah)
        
        cek_tekanan_darah = 0
            
        st.session_state.HDL = st.number_input("HDL (mg/dL): ", min_value=0.0, max_value=999.0, value=st.session_state.HDL)
        st.session_state.LDL = st.number_input("LDL (mg/dL): ", min_value=0.0, max_value=999.0, value=st.session_state.LDL)
        st.session_state.trigliserida = st.number_input("Trigliserida (mg/dL): ", min_value=0.0, max_value=999.0, value=st.session_state.trigliserida)
        st.session_state.total_kolestrol = st.number_input("Total Kolestrol Darah (mg/dL) (Kosongkan saja apabila HDL, LDL, dan trigliserida terisi): ", min_value=0.0, max_value=999.0, value=st.session_state.total_kolestrol)
        
        
        st.session_state.total_kolestrol_darah = st.session_state.HDL + st.session_state.LDL + (st.session_state.trigliserida/5.0)
        

        
        #Jika total kolestrol darah tinggi > 240.0
        
        if st.session_state.total_kolestrol_darah > 240.0 or st.session_state.total_kolestrol > 240.0 or (st.session_state.HDL != 0 and st.session_state.HDL <= 35.0 or st.session_state.LDL >= 100.0 or st.session_state.trigliserida >= 250.0):
            st.session_state.faktor_risiko_2 = st.session_state.faktor_risiko_2 + 1
            
            disiplidemia = "Disiplidemia: "
            if st.session_state.total_kolestrol_darah > 0:
                st.session_state.total_kolestrol = st.session_state.total_kolestrol_darah
                disiplidemia = disiplidemia + "Total Kolestrol Tinggi sebesar " +str(st.session_state.total_kolestrol) + " mg/dL dengan rumus Total Kolestrol = HDL + LDL + Trigliserida/5, "
            else:
                disiplidemia = disiplidemia + "Total Kolestrol Tinggi sebesar " + str(st.session_state.total_kolestrol) + " mg/dL"
                
             
        
        #Jika mengalami disiplidemia dengan HDL <= 35 dan/atau LDL >= 100 dan/atau trigliserida ≥  250.0
            
            
            if st.session_state.HDL <= 35.0 and st.session_state.total_kolestrol_darah > 0.0:
                disiplidemia = disiplidemia + "HDL = " + str(st.session_state.HDL) + " mg/dL, "
            if st.session_state.LDL >= 100.0:
                disiplidemia = disiplidemia + "LDL = " + str(st.session_state.LDL) + " mg/dL, "
            if st.session_state.trigliserida >= 250.0:
                disiplidemia = disiplidemia + "dan Trigliserida = " + str(st.session_state.trigliserida) + " mg/dL "
            
            st.session_state.daftar_faktor_risiko_2.append(disiplidemia)

        col1, col2 = st.columns(2)
        
        with col1:
            if st.form_submit_button("Kembali"):
                
                st.session_state.next = 1
                st.rerun()
        with col2:
            if st.form_submit_button("Next"):
                
                if cek_validasi_tekanan_darah(st.session_state.tekanan_darah) == False or st.session_state.tekanan_darah == "":
                    cek_tekanan_darah = 1
                    
        
                if cek_validasi_tekanan_darah(st.session_state.tekanan_darah) == True:
                    st.session_state.sistole, st.session_state.diastole = st.session_state.tekanan_darah.split("/")
                    st.session_state.sistole = int(st.session_state.sistole)
                    st.session_state.diastole = int(st.session_state.diastole)
                    if st.session_state.sistole < st.session_state.diastole:
                        cek_tekanan_darah = 2
                    if st.session_state.sistole >= 140 or st.session_state.diastole >= 90:
                        st.session_state.faktor_risiko_2 = st.session_state.faktor_risiko_2 + 1
                        hipertensi = "Hipertensi: " + st.session_state.tekanan_darah + " mmHg"
                        st.session_state.daftar_faktor_risiko_2.append(hipertensi)
                
                if cek_tekanan_darah == 0:
                    st.session_state.next = 3
                    st.rerun()
        

        if cek_tekanan_darah == 1:
            st.error("Tekanan Darah Anda Salah! Buat dengan format : 120/80")
        if cek_tekanan_darah == 2:
            st.error("Tekanan darah anda salah! Yang pertama harus lebih besar daripada yang kedua dengan format: 120/80 bukan 80/120!")
        
if st.session_state.next == 3:
    
    st.session_state.daftar_faktor_risiko = []
    
    if st.session_state.daftar_faktor_risiko_1:
        st.session_state.daftar_faktor_risiko.extend(st.session_state.daftar_faktor_risiko_1)

    if st.session_state.daftar_faktor_risiko_2:
        st.session_state.daftar_faktor_risiko.extend(st.session_state.daftar_faktor_risiko_2)
            
    #menghitung total faktor risiko
    st.session_state.total_faktor_risiko = st.session_state.faktor_risiko_1 + st.session_state.faktor_risiko_2
    
    with st.form(key="hitung_total_faktor_risiko"):
        st.subheader("Total Faktor Risiko Anda: " + str(st.session_state.total_faktor_risiko))
        
        
        if st.session_state.total_faktor_risiko == 0:
            st.success("Anda Tidak Memiliki Faktor Risiko dan Risiko Rendah Terkena Diabetes Mellitus Tipe 2")
            
        if st.session_state.total_faktor_risiko == 1 or st.session_state.total_faktor_risiko == 2:
            st.warning("Anda Memiliki 1 atau 2 Faktor Risiko dan Risiko Menengah Terkena Diabetes Mellitus Tipe 2")
            
        if st.session_state.total_faktor_risiko >= 3:
            st.error("Anda Memiliki Faktor Risiko ≥3 dan Risiko Tinggi Terkena Diabetes Mellitus Tipe 2")
            
        for i in st.session_state.daftar_faktor_risiko:
            st.warning(i)
        
        
        col1, col2 = st.columns(2)
        with col1:
            if st.form_submit_button("Kembali"):
                st.session_state.next = 2
                st.session_state.daftar_faktor_risiko = []
                st.rerun()
        with col2:
            if st.form_submit_button("Lanjut Pemeriksaan Gula Darah"):
                st.session_state.next = 4
                st.rerun()
        

if st.session_state.next == 4:
    with st.form(key="form_pemeriksaan_gula_darah"):

        st.subheader("Pemeriksaan Gula Darah")
        st.session_state.gula_darah_sewaktu = st.number_input("Gula Darah Sewaktu (mg/dL): ", min_value=0.0, max_value=999.0, value=st.session_state.gula_darah_sewaktu)
        st.session_state.gula_darah_puasa = st.number_input("Gula Darah Puasa (mg/dL): ", min_value=0.0, max_value=999.0, value=st.session_state.gula_darah_puasa)
        st.session_state.gula_darah_2_jam_setelah_makan = st.number_input("Gula Darah 2 Jam Setelah Makan (mg/dL): ", min_value=0.0, max_value=1000.0, value=st.session_state.gula_darah_2_jam_setelah_makan)

        
        if st.form_submit_button("Kembali"):
            
            st.session_state.next = 3
            st.rerun()
            
        if st.form_submit_button("Lanjut"):
            
            st.session_state.next = 5
            st.rerun()
    
if st.session_state.next == 5:
    with st.form(key="form_tingkat_risiko"):
        
        st.subheader("Hasil Tingkat Risiko Berdasarkan Faktor Risiko dan Pemeriksaan Gula Darah")
        # Faktor Risiko 0
        if (st.session_state.gula_darah_sewaktu >= 200.0 or 
            st.session_state.gula_darah_puasa >= 126.0 or 
            st.session_state.gula_darah_2_jam_setelah_makan >= 200.0) and st.session_state.total_faktor_risiko == 0:
            
            st.error("Risiko tinggi, gula darah sudah masuk ke dalam level yang tinggi meskipun tidak memiliki faktor risiko. Anda disarankan untuk segera berkonsultasi dengan dokter")
            st.session_state.risiko_diabetes = "TINGGI"

        elif (140 <= st.session_state.gula_darah_sewaktu < 200.0 or 
            100 <= st.session_state.gula_darah_puasa < 126.0 or 
            140 <= st.session_state.gula_darah_2_jam_setelah_makan < 200.0) and st.session_state.total_faktor_risiko == 0:
            st.warning("Risiko menengah, tidak ada faktor risiko namun gula sudah masuk ke dalam level prediabetes. Disarankan untuk mengikuti Tes Toleransi Glukosa Oral (TTGO) dan berkonsultasi dengan dokter")
            st.session_state.risiko_diabetes = "MENENGAH"

        elif (st.session_state.gula_darah_sewaktu < 140.0 and 
            st.session_state.gula_darah_puasa < 100.0 and 
            st.session_state.gula_darah_2_jam_setelah_makan < 140.0) and st.session_state.total_faktor_risiko == 0:
            st.success("Risiko rendah, gula darah normal dan tidak ada faktor risiko")
            st.session_state.risiko_diabetes = "RENDAH"
    
        # Faktor Risiko 1 atau 2
        if (st.session_state.gula_darah_sewaktu >= 200.0 or st.session_state.gula_darah_puasa >= 126.0 or st.session_state.gula_darah_2_jam_setelah_makan >= 200.0) and st.session_state.total_faktor_risiko == 1 or st.session_state.total_faktor_risiko == 2:
            st.error("Risiko sangat tinggi, gula darah sudah masuk ke dalam level yang tinggi dan terdapat faktor risiko. Anda sangat disarankan untuk segera berkonsultasi dengan dokter karena Anda berkemungkinan terkena Diabetes Mellitus Tipe 2")
            st.session_state.risiko_diabetes = "SANGAT TINGGI"
        
        elif (st.session_state.gula_darah_sewaktu >= 140.0 and st.session_state.gula_darah_sewaktu < 200.0 or st.session_state.gula_darah_puasa >= 100.0 and st.session_state.gula_darah_puasa < 126.0 or st.session_state.gula_darah_2_jam_setelah_makan >= 140.0 and st.session_state.gula_darah_2_jam_setelah_makan < 200.0) and st.session_state.total_faktor_risiko == 1 or st.session_state.total_faktor_risiko == 2:
            st.warning("Risiko tinggi, gula darah sudah mencapai level prediabetes. Disarankan untuk mengikuti Tes Toleransi Glukosa Oral (TTGO) dan berkonsultasi dengan dokter")     
            st.session_state.risiko_diabetes = "TINGGI"
        elif (st.session_state.gula_darah_sewaktu < 140.0 or st.session_state.gula_darah_puasa < 100.0 or st.session_state.gula_darah_2_jam_setelah_makan < 140.0) and st.session_state.total_faktor_risiko == 1 or st.session_state.total_faktor_risiko == 2:
            st.success("Risiko menengah, gula darah normal namun terdapat faktor risiko")
            st.session_state.risiko_diabetes = "MENENGAH"
             
        # Faktor Risiko Lebih Dari 2
        if (st.session_state.gula_darah_sewaktu >= 200.0 or st.session_state.gula_darah_puasa >= 126.0 or st.session_state.gula_darah_2_jam_setelah_makan >= 200.0) and st.session_state.total_faktor_risiko >= 3:
            st.write("Diagnosis:")
            st.error("Risiko sangat tinggi, Anda memiliki banyak faktor risiko dan level gula darah yang tinggi. Sangat disarankan untuk segera berkonsultasi dengan dokter karena berdasarkan semua indikator Anda sudah terkena Diabetes Mellitus Tipe 2")
            st.session_state.risiko_diabetes = "SANGAT TINGGI"
        elif (st.session_state.gula_darah_sewaktu >= 140.0 and st.session_state.gula_darah_sewaktu < 200.0 or st.session_state.gula_darah_puasa >= 100.0 and st.session_state.gula_darah_puasa < 126.0 or st.session_state.gula_darah_2_jam_setelah_makan >= 140.0 and st.session_state.gula_darah_2_jam_setelah_makan < 200.0) and st.session_state.total_faktor_risiko >= 3:
            st.write("Diagnosis:")
            st.warning("Risiko tinggi, Anda memiliki banyak faktor risiko dan gula sudah masuk ke dalam level prediabetes. Disarankan untuk mengikuti Tes Toleransi Glukosa Oral (TTGO) dan berkonsultasi dengan dokter")     
            st.session_state.risiko_diabetes = "TINGGI"
        elif (st.session_state.gula_darah_sewaktu < 140.0 or st.session_state.gula_darah_puasa < 100.0 or st.session_state.gula_darah_2_jam_setelah_makan < 140.0) and st.session_state.total_faktor_risiko >= 3:
            st.write("Diagnosis:")
            st.warning("Risiko menengah, gula darah normal namun banyak faktor risiko lebih dari atau sama dengan 3 yang dapat menyebabkan Diabetes Mellitus Tipe di masa yang akan datang")
            st.session_state.risiko_diabetes = "MENENGAH"
        
        st.write("")
             
        st.write("Gula Darah Sewaktu (GDS): " + str(st.session_state.gula_darah_sewaktu) + " mg/dL")
        if st.session_state.gula_darah_sewaktu >= 200.0:
            st.error("Gula Darah Sewaktu Tinggi Berada di Nilai ≥200 mg/dL!")
        if st.session_state.gula_darah_sewaktu >= 140.0 and st.session_state.gula_darah_sewaktu < 200:
            st.warning("Gula Darah Sewaktu Berada di Level Prediabetes Antara 140 dan 199 mg/dL!")
        if st.session_state.gula_darah_sewaktu < 140.0:
            st.success("Gula Darah Sewaktu Aman di <140 mg/dL!")
        
        
        
        st.write("Gula Darah Puasa (GDP): " + str(st.session_state.gula_darah_puasa) + " mg/dL")
        if st.session_state.gula_darah_puasa >= 126.0:
            st.error("Gula Darah Puasa Tinggi Berada di Nilai ≥126 mg/dL!")
        if st.session_state.gula_darah_puasa >= 100.0 and st.session_state.gula_darah_puasa < 126.0:
            st.warning("Gula Darah Puasa Berada Di Level Prediabetes Antara 100 dan 125 mg/dL!")
        if st.session_state.gula_darah_puasa < 100.0:
            st.success("Gula Darah Puasa Aman di <100 mg/dL!")
        
        
        st.write("Gula Darah 2 Jam Setelah Makan: " + str(st.session_state.gula_darah_2_jam_setelah_makan) + " mg/dL")
        if st.session_state.gula_darah_2_jam_setelah_makan >= 200.0:
            st.error("Gula Darah 2 Jam Setelah Makan Tinggi Berada di Nilai ≥200 mg/dL!")
        if st.session_state.gula_darah_2_jam_setelah_makan >= 140.0 and st.session_state.gula_darah_2_jam_setelah_makan < 200.0:
            st.warning("Gula Darah 2 Jam Setelah Makan Berada Di Level Prediabetes Antara 140 dan 199 mg/dL!")
        if st.session_state.gula_darah_2_jam_setelah_makan < 140.0:
            st.success("Gula Darah 2 Jam Setelah Makan Anda Aman di <140 mg/dL!")
        
        
        if st.form_submit_button("Kembali"):
            st.session_state.next = 4
            st.rerun()
            
        if st.form_submit_button("Lanjut Pemeriksaan Komplikasi"):
            st.session_state.next = 6
            st.rerun()
        


if st.session_state.next == 6:
    with st.form(key="form_pemeriksaan_komplikasi"):
        st.subheader("Piih Gejala yang Anda Alami")
        col1, col2, col3 = st.columns(3)
        df_gejala = db.fetch_gejala()
        st.session_state.gejala_terpilih = []
        
        for index, row in df_gejala.iterrows():
            if index % 3 == 0:
                with col1:
                    if st.checkbox(row["nama_gejala"]):
                        st.session_state.gejala_terpilih.append(row["nama_gejala"])
            if index % 3 == 1:
                with col2:
                    if st.checkbox(row["nama_gejala"]):
                        st.session_state.gejala_terpilih.append(row["nama_gejala"])
            if index % 3 == 2:
                with col3:
                    if st.checkbox(row["nama_gejala"]):
                        st.session_state.gejala_terpilih.append(row["nama_gejala"])
        

        col1, col2 = st.columns(2)
        
        with col1:
            if st.form_submit_button("Kembali"):
                st.session_state.next = 5
                st.rerun()
        with col2:
            if st.form_submit_button("Lanjut"):
                st.session_state.next = 8
                st.rerun()
            
      

if st.session_state.next == 7:
    with st.form("form-yakin-sudah"):
        st.subheader("Apakah Anda sudah yakin dengan gejala yang Anda pilih? Jika Anda menekan Sudah, Anda tidak akan bisa kembali lagi")
        if st.form_submit_button("Belum"):
            st.session_state.next = 6
            st.rerun()
        if st.form_submit_button("Sudah"):
            st.session_state.next = 8
            st.rerun()
            
    
    
    
def forward_chaining(fakta, aturan):
    # Fakta yang diketahui
    
    fakta = set(fakta)
    
    # Kemungkinan penyakit
    kemungkinan_penyakit = {}
    
    for penyakit, gejala_penyakit in aturan.items():
        # Hitung gejala yang cocok
        gejala_cocok = fakta.intersection(gejala_penyakit)
        tingkat_kecocokan = len(gejala_cocok) / len(gejala_penyakit)
        
        # Simpan hasil (penyakit, tingkat kecocokan, gejala cocok)
        kemungkinan_penyakit[penyakit] = {
            "tingkat_kecocokan": tingkat_kecocokan,
            "gejala_cocok": gejala_cocok,
            "gejala_penyakit" : gejala_penyakit,
        }
    
    # Filter penyakit dengan tingkat kecocokan tinggi (contoh: > 50%)
    hasil = {
        penyakit: data
        for penyakit, data in kemungkinan_penyakit.items()
        if data["tingkat_kecocokan"] >= 0.5
    }
    
    return hasil



if st.session_state.next == 8:
    if "hasil_diagnosis" not in st.session_state:
        st.session_state.hasil_diagnosis = {}
    st.title("Diagnosis Komplikasi Penyakit")
    catatan = False
    with st.form(key="form_hasil_komplikasi"):    
        st.subheader("Gejala-Gejala Yang Terpilih")
        
        for i, gejala_terpilih in enumerate(st.session_state.gejala_terpilih, start=1):
            st.write(f"{i}. {gejala_terpilih}")
        
        if not st.session_state.gejala_terpilih:
            st.write("Tidak Ada Gejala yang Terpilih")
            
        
        st.subheader("Komplikasi Penyakit")
        
        # Ambil data relasi dari database             
        data_relasi = db.fetch_relasi_nama_penyakit_dan_nama_gejala()
        
        #Relasi Penyakit dan Gejala
        relasi_dict = {}
        for penyakit, gejala in data_relasi:
            if penyakit not in relasi_dict:
                relasi_dict[penyakit] = []  # Buat list kosong jika penyakit belum ada
            relasi_dict[penyakit].append(gejala)  # Tambahkan gejala ke list penyakit tersebut
       
       
       
        if st.session_state.gejala_terpilih:
            st.session_state.hasil_diagnosis = forward_chaining(st.session_state.gejala_terpilih, relasi_dict)
       
            if st.session_state.hasil_diagnosis:
                
                for penyakit, data in st.session_state.hasil_diagnosis.items():
                    kecocokan = data["tingkat_kecocokan"] * 100
                    gejala_cocok = "; ".join(data["gejala_cocok"])
                    gejala_penyakit = "; ".join(data["gejala_penyakit"])
                    
             
                    st.write(f"**{penyakit}: {kecocokan:.2f}%**")
                    st.write(db.get_penjelasan_penyakit(penyakit))
                    
                    st.write("**Gejala yang Cocok**")
                    st.write(gejala_cocok)
                    st.write("**Gejala Penyakit**")
                    st.write(gejala_penyakit)
                    
                    solusi_penyakit = db.get_solusi_penyakit(penyakit)
                    
                    #frasa_list = [frasa.strip() for frasa in solusi_penyakit.split(",")]
                    
                    # Pecah string berdasarkan koma
                    solusi_penyakit = solusi_penyakit.split(";")

                    # Bersihkan spasi di setiap frasa
                    st.session_state.daftar_solusi = []
                    
                    for frasa in solusi_penyakit:
                        st.session_state.daftar_solusi.append(frasa.strip())

                    st.write("**Solusi**")
                    # Loop untuk menampilkan dengan nomor urut
                    for i, frasa in enumerate(st.session_state.daftar_solusi, start=1):
                        st.write(f"{i}. {frasa}")
                    
                    
                    st.write("")                              
                catatan = True
            
                    
            else:
                st.write("Tidak ditemukan komplikasi yang cocok.")
                
        else:
            st.write("Tidak ada gejala yang bisa diproses.")


        if catatan == True:
            st.warning("**Catatan Penting**: Anda Harus Tetap Berkunjung Ke Dokter Spesialis untuk Mendapatkan Pengobatan dan Solusi Lebih Lanjut!")
        
        # Nanti di hapus saja
        if st.form_submit_button("Kembali"):
            st.session_state.next = 6
            
            st.rerun()
        
        if st.form_submit_button("Selesai"):
            
            
            
            st.session_state.next = 9

            id_pemeriksaan_default = db.menambah_id_pemeriksaan_kesehatan_default()
            db.add_pemeriksaan_kesehatan(id_pemeriksaan_default, db.get_id_pasien(st.session_state.username_pengguna), st.session_state.risiko_diabetes, datetime.datetime.now())
            db.add_pemeriksaan_faktor_permanen(id_pemeriksaan_default, st.session_state.usia_di_atas_40_tahun, st.session_state.riwayat_keluarga_diabetes, st.session_state.riwayat_diabetes_gestasional, st.session_state.riwayat_lahir_berat_badan_lahir_rendah)
            db.add_pemeriksaan_fisik(id_pemeriksaan_default, st.session_state.tinggi_badan, st.session_state.berat_badan, st.session_state.lingkar_perut, st.session_state.indeks_massa_tubuh)
            db.add_pemeriksaan_laboratorium(id_pemeriksaan_default, st.session_state.gula_darah_sewaktu, st.session_state.gula_darah_puasa, st.session_state.gula_darah_2_jam_setelah_makan, st.session_state.tekanan_darah, st.session_state.HDL, st.session_state.LDL, st.session_state.trigliserida, st.session_state.total_kolestrol)
            db.add_kebiasaan_hidup(id_pemeriksaan_default, st.session_state.konsumsi_alkohol, st.session_state.kurang_aktivitas, st.session_state.merokok, st.session_state.pola_makan_buruk, st.session_state.kurang_tidur)
            
            
            if st.session_state.gejala_terpilih is not None:
                st.session_state.hasil_diagnosis = forward_chaining(st.session_state.gejala_terpilih, relasi_dict)
                gejala_terpilih = ", ".join(st.session_state.gejala_terpilih)
                
                
                if st.session_state.hasil_diagnosis:
                    
                    for penyakit, data in st.session_state.hasil_diagnosis.items():
                        kecocokan = data["tingkat_kecocokan"] * 100
                        gejala_cocok = ", ".join(data["gejala_cocok"])
                        gejala_penyakit = ", ".join(data["gejala_penyakit"])
                        
                        
                                    
                        db.insert_diagnosis_penyakit(db.menambah_id_diagnosis_default(), st.session_state.data_pasien[0], db.get_id_penyakit(penyakit), gejala_terpilih, gejala_cocok, kecocokan, datetime.date.today())
                        
                else:   
                    st.success("Tidak ada penyakit yang terdeteksi")             
                    db.insert_diagnosis_penyakit(db.menambah_id_diagnosis_default(), st.session_state.data_pasien[0], None, gejala_terpilih, None, None, datetime.date.today())
                    
            else:
                db.insert_diagnosis_penyakit(db.menambah_id_diagnosis_default(), st.session_state.data_pasien[0], None, None, None, None, datetime.datetime.now())
            
            
            st.success("Pemeriksaan Kesehatan Berhasil dan Telah Tersimpan!")
            time.sleep(2)
            
            st.rerun()
    



def buat_laporan():
    pdf = FPDF()
    pdf.add_page()
    
    pdf.image("assets/logo_diabetes.png", x=10, y=8, w=30)  # Adjust x, y, and w for logo position and size
    pdf.image("assets/puskesmas_pkc_taman_sari.jpeg", x=170, y=8, w=30)
    
    # Menambahkan judul
    pdf.set_font("Arial", size=18, style="B")
    pdf.cell(200, 15, txt="LAPORAN HASIL PEMERIKSAAN ", ln=True, align='C')
    
    pdf.ln() 
    
    pdf.set_font("Arial", size=13, style="B")
    pdf.cell(75, 10, txt="Data Pasien", ln=True)
    pdf.set_font("Arial", size=10)
    

    data_pribadi = [
        ['Nama: ', st.session_state.nama_lengkap],
        ["Username: ", st.session_state.username_pengguna],
        ["Tanggal Lahir: ", str(st.session_state.tanggal_lahir)],
        ["Tanggal Pemeriksaan", str(st.session_state.tanggal_pemeriksaan)],
        ['Jenis Kelamin: ', st.session_state.jenis_kelamin],
        ['Alamat: ', st.session_state.alamat],
        ['Pekerjaan: ', st.session_state.pekerjaan],
        ['Email: ', st.session_state.email],
        ["Risiko Diabetes Tipe 2: ", st.session_state.risiko_diabetes]
    ]
    for row in data_pribadi:
        pdf.cell(75, 10, row[0], 1)  # First column
        pdf.cell(120, 10, row[1], 1)  # Second column
        pdf.ln()  # Move to the next line

      # Return PDF as a string
    pdf.ln()    
    
    pdf.set_font("Arial", size=13, style="B")
    pdf.cell(75, 10, txt="Faktor Tidak Bisa Diubah", ln=True)
    pdf.set_font("Arial", size=10)
    
    pola_gaya_hidup = [
        ["Usia di atas 45 tahun: ", st.session_state.usia_di_atas_40_tahun],
        ["Riwayat Keluarga Diabetes: ", st.session_state.riwayat_keluarga_diabetes],
        ["Riwayat Diabetes Gestasional: ", st.session_state.riwayat_diabetes_gestasional],
        ["Riwayat Lahir <2,5 kg atau Prematur: ", st.session_state.riwayat_lahir_di_bawah_2_koma_5_gram ],
    ]
    
    
    for row in pola_gaya_hidup:
        pdf.cell(75, 10, row[0], 1)  # First column
        pdf.cell(120, 10, row[1], 1)  # Second column
        pdf.ln()
    
    pdf.ln()
    pdf.set_font("Arial", size=13, style="B")
    pdf.cell(75, 10, txt="Pola Gaya Hidup", ln=True)
    pdf.set_font("Arial", size=10)
    pola_gaya_hidup = [
        ["Konsumsi Alkohol: ", st.session_state.konsumsi_alkohol],
        ["Kurang Aktivitas Fisik: ", st.session_state.kurang_aktivitas],
        ["Kebiasaan Merokok: ", st.session_state.merokok],
        ["Pola Makan Buruk : ", st.session_state.pola_makan_buruk],
        ["Tidur Tidak Berkualitas: ", st.session_state.kurang_tidur],
        
    ]
    for row in pola_gaya_hidup:
        pdf.cell(75, 10, row[0], 1)  # First column
        pdf.cell(120, 10, row[1], 1)  # Second column
        pdf.ln()
    
    pdf.ln()
    
    pdf.set_font("Arial", size=13, style="B")
    pdf.cell(75, 10, txt="Pemeriksaan Fisik", ln=True)
    pdf.set_font("Arial", size=10)
    
    pemeriksaan_fisik = [
        ["Parameter", "Hasil", "Nilai Normal"],
        ["Tinggi Badan: ", str(st.session_state.tinggi_badan)+" cm", "-"],
        ["Berat Badan: ", str(st.session_state.berat_badan)+" kg", "-"],
        ["Lingkar Perut: ", str(st.session_state.lingkar_perut)+" cm", " Pria <90cm , Wanita <80cm"],
        ["Indeks Massa Tubuh: ", str( st.session_state.indeks_massa_tubuh)+" kg/m2", " <25 kg/m2"],
    ]
    
    for row in pemeriksaan_fisik:
        pdf.cell(50, 10, row[0], 1)  # First column
        pdf.cell(50, 10, row[1], 1)
        pdf.cell(60, 10, row[2], 1)# Second column
        pdf.ln()
    
    pdf.ln()
    pdf.set_font("Arial", size=13, style="B")
    pdf.cell(75, 10, txt="Hasil Tekanan Darah dan Kolestrol Darah", ln=True)
    pdf.set_font("Arial", size=10)
    hasil_laboratorium = [
        
        ["Parameter", "Hasil", "Nilai Normal"],
        ["Tekanan Darah: ", str(st.session_state.tekanan_darah)+" mmHg", " <140/90 mmHg"],
        ["HDL : ", str(st.session_state.HDL)+" mg/dL", " >=40 mg/dL"],
        ["LDL : ", str(st.session_state.LDL)+" mg/dL", " <=100 mg/dL"],
        ["Trigliserida : ", str(st.session_state.trigliserida)+" mg/dL", " <=150 mg/dL"],
        ["Total Kolestrol Darah: ", str(st.session_state.total_kolestrol_darah)+" mg/dL", " <=240 mg/dL"],
    ]
   
    
    for row in hasil_laboratorium:
        pdf.cell(50, 10, row[0], 1)  # First column
        pdf.cell(50, 10, row[1], 1) # Second column
        pdf.cell(50, 10, row[2], 1)
        pdf.ln()
    
    pdf.ln()
    
    pdf.set_font("Arial", size=13, style="B")
    pdf.cell(75, 10, txt="Hasil Laboratorium", ln=True)
    pdf.set_font("Arial", size=10)
    hasil_laboratorium = [
        ["Parameter", "Nilai", "Nilai Normal"],
        ["Gula Darah Sewaktu (GDS): ", str(st.session_state.gula_darah_sewaktu)+" mg/dL", " <140 mg/dL"],
        ["Gula Darah Puasa (GDP): ", str(st.session_state.gula_darah_puasa)+" mg/dL", " <100 mg/dL"],
        ["Gula Darah 2 Jam Setelah Makan (GD2PP): ", str(st.session_state.gula_darah_2_jam_setelah_makan)+" mg/dL", " <140 mg/dL"],

    ]
    
    for row in hasil_laboratorium:
        pdf.cell(90, 10, row[0], 1)
        pdf.cell(50, 10, row[1], 1) 
        pdf.cell(50, 10, row[2], 1) 
        pdf.ln()
    
    pdf.ln(120)
    
    pdf.set_font("Arial", size=18, style="B")
    pdf.cell(75, 10, txt="Diagnosis Komplikasi Penyakit", ln=True)
    
    pdf.set_font("Arial", size=13, style="B")
    pdf.cell(75, 10, txt="Gejala-Gejala Terpilih", ln=True)
    pdf.set_font("Arial", size=10)
    
    if st.session_state.gejala_terpilih:
        for i, gejala in enumerate(st.session_state.gejala_terpilih, start=1):
            pdf.cell(200, 10, txt=f"{i}. {gejala}", ln=True)
        
    else:            
        pdf.cell(200, 10, txt="-", ln=True)
        
    pdf.ln()
    
    pdf.set_font("Arial", size=13, style="B")
    pdf.cell(75, 10, txt="Komplikasi Penyakit", ln=True)
    pdf.set_font("Arial", size=10)
    
    if st.session_state.hasil_diagnosis:
        for penyakit, data in st.session_state.hasil_diagnosis.items():
            kecocokan = data["tingkat_kecocokan"] * 100
            gejala_cocok = "; ".join(data["gejala_cocok"])
            gejala_penyakit = "; ".join(data["gejala_penyakit"])
            
            
            pdf.set_font("Arial", size=10, style="B")
            pdf.cell(200, 10, txt=f"{penyakit} : {kecocokan:.2f}%", ln=True)
            
            pdf.set_font("Arial", size=10)
            pdf.cell(200, 10, txt=f"{db.get_penjelasan_penyakit(penyakit)}", ln=True)
            
            pdf.set_font("Arial", size=10, style="B")
            pdf.cell(200, 10, txt=f"Gejala yang Cocok", ln=True)
            
            pdf.set_font("Arial", size=10)
            pisah_gejala_cocok = gejala_cocok.split("; ")
            
            for i, gejala in enumerate(pisah_gejala_cocok, start=1):
                
                pdf.cell(200, 10, txt=f"{i} : {gejala}", ln=True)
            
           
            pdf.set_font("Arial", size=10, style="B")
            pdf.cell(200, 10, txt=f"Gejala Penyakit", ln=True)
            pdf.set_font("Arial", size=10)
            
            pisah_gejala_penyakit = gejala_penyakit.split(", ")
            for i, gejala_penyakit in enumerate(pisah_gejala_penyakit, start=1):
                pdf.cell(200, 10, txt=f"{i}: {gejala_penyakit}", ln=True)
            
            
      
            pdf.set_font("Arial", size=10, style="B")
            pdf.cell(200, 10, txt=f"Solusi Penyakit", ln=True)
            pdf.set_font("Arial", size=10)
            
            # Loop untuk menampilkan dengan nomor urut
            
        
            solusi_penyakit = db.get_solusi_penyakit(penyakit)
            solusi_penyakit = solusi_penyakit.split(";")

        
            daftar_solusi = []
            
            for frasa in solusi_penyakit:
                daftar_solusi.append(frasa.strip())
            
            # Loop untuk menampilkan dengan nomor urut
            for i, frasa in enumerate(daftar_solusi, start=1):
                pdf.cell(200, 10, txt=f"{i}. {frasa}", ln=True)
               
    
        
            pdf.ln(10)
            
    else:
        pdf.set_font("Arial", size=10)
        pdf.cell(200, 10, txt=f"-", ln=True)
    
    return pdf.output(dest="S").encode("latin1")


    

if st.session_state.next == 9:

    st.subheader("Hasil Akhir")
   
    file_pdf = buat_laporan()
    
    base64_pdf = b64encode(buat_laporan()).decode("latin1")
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="400" type="application/pdf">'
    
    
    st.markdown(pdf_display, unsafe_allow_html=True)
    st.download_button(
        label="Download PDF",
        data=file_pdf,
        file_name = "Laporan Kesehatan_"+st.session_state.nama_lengkap+ "_"+str(st.session_state.tanggal_pemeriksaan)+".pdf",
        mime="application/pdf"
    )
    
    if st.button("Kembali ke Awal"):
        st.session_state.next = 0
        st.success("Anda Berhasil Kembali ke Awal!")
        time.sleep(1)
        st.rerun()
    
    
