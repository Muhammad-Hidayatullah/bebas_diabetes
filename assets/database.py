import streamlit as st
import mysql.connector
import pandas as pd
from fpdf import FPDF
import io
import re


# Accessing secrets using the 'mysql' key
db_credentials = st.secrets["mysql"]

# Connecting to the database
def connect_to_db():
    
    db_credentials = {
        "host": st.secrets["mysql"]["host"],
        "user": st.secrets["mysql"]["username"],
        "password": st.secrets["mysql"]["password"],
        "database": st.secrets["mysql"]["database"],
        "port": st.secrets["mysql"]["port"]
    }
    
    return mysql.connector.connect(
        host=db_credentials["host"],
        user=db_credentials["user"],
        password=db_credentials["password"],
        database=db_credentials["database"],
        port=db_credentials["port"]
    )


def forward_chaining(fakta, aturan):
    # Penyakit yang mungkin didiagnosis
    kemungkinan_penyakit = {}
    
    for penyakit, gejala_penyakit in aturan.items():
        # Hitung jumlah gejala yang cocok
        gejala_cocok = fakta.intersection(gejala_penyakit)
        kemungkinan_penyakit[penyakit] = len(gejala_cocok) / len(gejala_penyakit)
    
    # Filter penyakit dengan tingkat kecocokan tinggi (contoh: > 70%)
    hasil = {penyakit: kecocokan for penyakit, kecocokan in kemungkinan_penyakit.items() if kecocokan > 0.5}
    
    return hasil



def get_name(username, password):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()

        # SQL query to check user credentials
        query = "SELECT name FROM pengguna WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))

        # Fetch one result
        name = cursor.fetchone()

        return name[0] if name else None
       

    except mysql.connector.Error as err:
        st.error(f"Database error: {err}")  # Show the error
        return False  # Indicate failure

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def get_tanggal_lahir_pengguna(username, password):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()

        # SQL query to check user credentials
        query = "SELECT tanggal_lahir FROM pengguna WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))

        # Fetch one result
        name = cursor.fetchone()

        return name[0] if name else None
       

    except mysql.connector.Error as err:
        st.error(f"Database error: {err}")  # Show the error
        return False  # Indicate failure

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def get_data_pengguna(username):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT * FROM pengguna WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    conn.close()
    return result if result else None
    
    
     
def fetch_faktor_risiko():
    conn = connect_to_db()
    query = "SELECT nama_risiko, deskripsi FROM faktor_risiko;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

#UNTUK PENYAKIT
def fetch_penyakit():
    conn = connect_to_db()
    query = "SELECT * FROM komplikasi_penyakit;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df


def add_komplikasi_penyakit(id_komplikasi_penyakit, nama_penyakit, penjelasan, solusi):
    conn = connect_to_db()
    cursor = conn.cursor()
    
    query = "INSERT INTO komplikasi_penyakit (id_komplikasi_penyakit, nama_penyakit, penjelasan, solusi) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (id_komplikasi_penyakit, nama_penyakit, penjelasan, solusi))
    conn.commit()
    st.success("Komplikasi Penyakit Berhasil Ditambahkan")
    conn.close()
    
    
def update_komplikasi_penyakit(id_komplikasi_penyakit, nama_penyakit, penjelasan, solusi):
    conn = connect_to_db()
    cursor = conn.cursor()
    
    query = "UPDATE komplikasi_penyakit SET nama_penyakit = %s, penjelasan = %s, solusi = %s WHERE id_komplikasi_penyakit = %s"
    
    cursor.execute(query, (nama_penyakit, penjelasan, solusi, id_komplikasi_penyakit))
    conn.commit()
    st.success("Penyakit Berhasil Diupdate")
    conn.close()
    
    
    
def hapus_komplikasi_penyakit(id_komplikasi_penyakit):
    conn = connect_to_db()
    cursor = conn.cursor()
    
    query = "DELETE FROM komplikasi_penyakit WHERE id_komplikasi_penyakit =  %s"
    
    cursor.execute(query, (id_komplikasi_penyakit,)) #harus ditambah koma ,
    conn.commit()
    st.success("Penyakit Berhasil Dihapus")
    conn.close()
    

    
    
#UNTUK GEJALA

def fetch_gejala():
    conn = connect_to_db()
    query = "SELECT * FROM `gejala` ORDER BY `id_gejala` ASC;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df


def add_gejala(id_gejala, nama_gejala):
    conn = connect_to_db()
    cursor = conn.cursor()
    
    query = "INSERT INTO gejala (id_gejala, nama_gejala) VALUES (%s, %s)"
    cursor.execute(query, (id_gejala, nama_gejala))
    conn.commit()
    
    st.success("Gejala Berhasil Ditambahkan")
    conn.close()
    
    
def update_gejala(id_gejala, nama_gejala):
    conn = connect_to_db()
    cursor = conn.cursor()
    
    query = "UPDATE gejala SET nama_gejala = %s WHERE id_gejala = %s"
    
    cursor.execute(query, (nama_gejala, id_gejala))
    conn.commit()
    st.success("Gejala Berhasil Diupdate")
    conn.close()
    

def hapus_gejala(id_gejala):
    conn = connect_to_db()
    cursor = conn.cursor()
    
    query = "DELETE FROM gejala WHERE id_gejala =  %s"
    
    cursor.execute(query, (id_gejala,)) #harus ditambah koma ,
    conn.commit()
    st.success("Gejala Berhasil Dihapus")
    conn.close()
    
def nama_gejala(id_gejala):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT nama_gejala FROM gejala WHERE id_gejala = %s"
    cursor.execute(query, (id_gejala,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None
    
    
#UNTUK GEJALA
def fetch_relasi_penyakit_dan_gejala_full():
    conn = connect_to_db()
    query = "SELECT relasi_penyakit_gejala.id_komplikasi_penyakit, komplikasi_penyakit.nama_penyakit, relasi_penyakit_gejala.id_gejala, gejala.nama_gejala FROM relasi_penyakit_gejala JOIN komplikasi_penyakit ON relasi_penyakit_gejala.id_komplikasi_penyakit = komplikasi_penyakit.id_komplikasi_penyakit JOIN gejala ON relasi_penyakit_gejala.id_gejala = gejala.id_gejala;;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def fetch_relasi_penyakit_dan_gejala():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT id_komplikasi_penyakit, id_gejala FROM relasi_penyakit_gejala;"
    cursor.execute(query)
    data_relasi_penyakit_dan_gejala = cursor.fetchall()
    conn.close()
    return data_relasi_penyakit_dan_gejala



def fetch_relasi_nama_penyakit_dan_nama_gejala():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT komplikasi_penyakit.nama_penyakit, gejala.nama_gejala FROM relasi_penyakit_gejala JOIN komplikasi_penyakit ON relasi_penyakit_gejala.id_komplikasi_penyakit = komplikasi_penyakit.id_komplikasi_penyakit JOIN gejala ON relasi_penyakit_gejala.id_gejala = gejala.id_gejala;"

    cursor.execute(query)
    relasi_nama_penyakit_dan_nama_gejala = cursor.fetchall()
    conn.close()
    return relasi_nama_penyakit_dan_nama_gejala
    

def get_solusi_penyakit(nama_penyakit):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT solusi FROM komplikasi_penyakit WHERE nama_penyakit = %s"
    cursor.execute(query, (nama_penyakit,))
    solusi = cursor.fetchone()
    conn.close()
    return solusi[0] if solusi else None
    

def add_relasi_penyakit_dan_gejala(id_komplikasi_penyakit, id_gejala):
    conn = connect_to_db()
    cursor = conn.cursor()
    
    query = "INSERT INTO relasi_penyakit_gejala (id_komplikasi_penyakit, id_gejala) VALUES (%s, %s)"
    cursor.execute(query, (id_komplikasi_penyakit, id_gejala))
    conn.commit()
    
    st.success("Relasi Penyakit dan Gejala Berhasil Ditambahkan")
    conn.close()
    
    
def update_relasi_penyakit_dan_gejala(id_komplikasi_penyakit, id_gejala, id_gejala_baru):
    conn = connect_to_db()
    cursor = conn.cursor()
    
    query = "UPDATE relasi_penyakit_gejala SET id_gejala = %s WHERE id_komplikasi_penyakit = %s AND id_gejala = %s"

    cursor.execute(query, (id_gejala_baru, id_komplikasi_penyakit, id_gejala))
    
    conn.commit()
    st.success("Relasi Penyakit dan Gejala Berhasil Diupdate")
    conn.close()


def hapus_relasi_penyakit_dan_gejala(id_komplikasi_penyakit, id_gejala):
    conn = connect_to_db()
    cursor = conn.cursor()
    
    query = "DELETE FROM relasi_penyakit_gejala WHERE id_komplikasi_penyakit = %s AND id_gejala = %s"
    
    cursor.execute(query, (id_komplikasi_penyakit, id_gejala)) #harus ditambah koma ,
    conn.commit()
    st.success("Relasi Penyakit dan Gejala Berhasil Dihapus")
    conn.close()



def fetch_artikel():
    conn = connect_to_db()
    query = "SELECT * FROM artikel;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df



def add_artikel(nama_website, link_gambar, judul_artikel, nama_penulis, tanggal_artikel, link_artikel):
    conn = connect_to_db()
    cursor = conn.cursor()
    
    query = "INSERT INTO artikel (nama_website, link_gambar, judul_artikel, nama_penulis, tanggal_artikel, link_artikel) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (nama_website, link_gambar, judul_artikel, nama_penulis, tanggal_artikel, link_artikel))
    conn.commit()
    conn.close()
    

def update_artikel(nama_website, link_gambar, judul_artikel, nama_penulis, tanggal_artikel, link_artikel, id_artikel):
    conn = connect_to_db()
    cursor = conn.cursor()
    
    query = "UPDATE artikel SET nama_website = %s, link_gambar = %s, judul_artikel = %s, nama_penulis = %s, tanggal_artikel = %s, link_artikel = %s WHERE id_artikel= %s"

    cursor.execute(query, (nama_website, link_gambar, judul_artikel, nama_penulis, tanggal_artikel, link_artikel, id_artikel))
    conn.commit()
    st.success("Artikel Berhasil Diupdate")
    conn.close()

def hapus_artikel(id_artikel):
    conn = connect_to_db()
    cursor = conn.cursor()
    
    query = "DELETE FROM artikel WHERE id_artikel = %s"
    
    cursor.execute(query, (id_artikel,)) #harus ditambah koma ,
    conn.commit()
    st.success("Artikel Berhasil Dihapus")
    conn.close()


def fetch_admin():
    conn = connect_to_db()
    query = "SELECT * FROM admin;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def fetch_pengguna():
    conn = connect_to_db()
    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT * FROM pengguna;
    """ 
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    if not result:
        return None

    # Convert result to Pandas DataFrame
    df = pd.DataFrame(result)

    # Column renaming dictionary
    ganti_header = {
        "id_pengguna": "ID Pengguna",
        "username": "Username",
        "password": "Password",
        "nama_pengguna": "Nama Pengguna",
        "jenis_kelamin": "Jenis Kelamin",
        "alamat": "Alamat",
        "email": "Email",
        "pekerjaan": "Pekerjaan",
        "tanggal_lahir": "Tanggal Lahir"
    }

    # Rename columns
    df.rename(columns=ganti_header, inplace=True)

    return df 





def update_pengguna(username, password, nama_pengguna, jenis_kelamin, alamat, email, pekerjaan, tanggal_lahir, username_lama):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "UPDATE pengguna SET username = %s, password = %s, nama_pengguna = %s, jenis_kelamin = %s, alamat = %s, email = %s, pekerjaan = %s, tanggal_lahir = %s WHERE username = %s"
    cursor.execute(query, (username, password, nama_pengguna, jenis_kelamin, alamat, email, pekerjaan, tanggal_lahir, username_lama))
    conn.commit()
    conn.close()
    
def hapus_data_pengguna(id_pengguna):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "DELETE FROM pengguna WHERE id_pengguna = %s"
    cursor.execute(query, (id_pengguna,))
    conn.commit()
    conn.close()
    
def forward_chaining(gejala_gejala):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT id_komplikasi_penyakit FROM relasi_penyakit_gejala WHERE id_gejala = %s"
    penyakit_yang_mungkin = set()
    for gejala in gejala_gejala:
        cursor.execute(query, (gejala,))
        penyakit_penyakit = cursor.fetchall()
        for penyakit in penyakit_penyakit:
            penyakit_yang_mungkin.add(penyakit[0])
    return penyakit_yang_mungkin
        
        

def menambah_id_pengguna_default():
    
    conn = connect_to_db()
    cursor = conn.cursor()
    
    # Ambil ID terakhir dari database (misalnya A0001, A0002, dst)
    cursor.execute("SELECT id_pengguna FROM pengguna ORDER BY id_pengguna DESC LIMIT 1")
    last_id = cursor.fetchone()
    
    if last_id:
        # Ambil nomor dari ID terakhir dan increment 1
        last_number = int(last_id[0][2:])  # Mengambil angka setelah 'A'
        new_id = f"PS{last_number + 1:03d}"  # Formatkan ID seperti A0001, A0002, dst
    else:
        # Jika tidak ada data sebelumnya, mulai dengan A0001
        new_id = "PS001"
    
    conn.close()
    return new_id

def menambah_id_komplikasi_penyakit_default():
    
    conn = connect_to_db()
    cursor = conn.cursor()
    
    # Ambil ID terakhir dari database (misalnya A0001, A0002, dst)
    cursor.execute("SELECT id_komplikasi_penyakit FROM komplikasi_penyakit ORDER BY id_komplikasi_penyakit DESC LIMIT 1")
    last_id = cursor.fetchone()
    
    if last_id:
        # Ambil nomor dari ID terakhir dan increment 1
        last_number = int(last_id[0][1:])  # Mengambil angka setelah 'A'
        new_id = f"P{last_number + 1:04d}"  # Formatkan ID seperti PS001, PS002, dst
    else:
        # Jika tidak ada data sebelumnya, mulai dengan A0001
        new_id = "P0001"
    
    conn.close()
    return new_id

def menambah_id_gejala_default():
    
    conn = connect_to_db()
    cursor = conn.cursor()
    

    cursor.execute("SELECT id_gejala FROM gejala ORDER BY id_gejala DESC LIMIT 1")
    last_id = cursor.fetchone()
    
    if last_id:
        # Ambil nomor dari ID terakhir dan increment 1
        last_number = int(last_id[0][1:])  # Mengambil angka setelah 'G'
        new_id = f"G{last_number + 1:04d}"  # Formatkan ID seperti G01, G02, dst
    else:
        # Jika tidak ada data sebelumnya, mulai dengan A0001
        new_id = "G0001"
    
    conn.close()
    return new_id

def menambah_id_pemeriksaan_kesehatan_default():
    conn = connect_to_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id_pemeriksaan FROM pemeriksaan_kesehatan ORDER BY id_pemeriksaan DESC LIMIT 1")
    last_id = cursor.fetchone()
    
    if last_id:
        last_number = int(last_id[0][1:])
        new_id = f"K{last_number + 1:04}"
    else:
        new_id = "K0001"
    
    conn.close()
    return new_id
    

    

def add_pengguna(id_pengguna, username, password, nama_pengguna, jenis_kelamin, alamat, email, pekerjaan, tanggal_lahir):
    conn = connect_to_db()
    cursor = conn.cursor()
    
    query = "INSERT INTO pengguna (id_pengguna, username, password, nama_pengguna, jenis_kelamin, alamat, email, pekerjaan, tanggal_lahir) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(query, (id_pengguna, username, password, nama_pengguna, jenis_kelamin, alamat, email, pekerjaan, tanggal_lahir))
    conn.commit()
    
    st.success("pengguna Berhasil Didaftarkan")
    conn.close()
    
    
def get_id_pengguna(username):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()

        # SQL query to check user credentials
        query = "SELECT id_pengguna FROM pengguna WHERE username = %s"
        cursor.execute(query, (username,))

        # Fetch one result
        name = cursor.fetchone()

        return name[0] if name else None
       

    except mysql.connector.Error as err:
        st.error(f"Database error: {err}")  # Show the error
        return False  # Indicate failure

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    
    
    
def get_id_penyakit(nama_penyakit):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT id_komplikasi_penyakit FROM komplikasi_penyakit WHERE nama_penyakit = %s"
    cursor.execute(query, (nama_penyakit,))
    id_penyakit = cursor.fetchone()
    conn.close()
    return id_penyakit[0] if id_penyakit else None
    
    
def get_jenis_kelamin(username):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT jenis_kelamin FROM pengguna WHERE username = %s"
    cursor.execute(query, (username,))
    jenis_kelamin = cursor.fetchone()
    conn.close()
    return jenis_kelamin[0] if jenis_kelamin else None
    
def add_pemeriksaan_kesehatan(id_pemeriksaan, id_pengguna, risiko_diabetes, tanggal_pemeriksaan):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "INSERT INTO pemeriksaan_kesehatan (id_pemeriksaan, id_pengguna, risiko_diabetes, tanggal_pemeriksaan) VALUES (%s, %s, %s, %s);"
    cursor.execute(query, (id_pemeriksaan, id_pengguna, risiko_diabetes, tanggal_pemeriksaan))
    conn.commit()
    conn.close()
    
    
def add_pemeriksaan_faktor_permanen(id_pemeriksaan, usia_di_atas_45_tahun, riwayat_keluarga_diabetes, riwayat_diabetes_gestasional, riwayat_penyakit_berat_badan_rendah):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "INSERT INTO pemeriksaan_faktor_permanen (id_pemeriksaan, usia_di_atas_45_tahun, riwayat_keluarga_diabetes, riwayat_diabetes_gestasional, riwayat_lahir_berat_badan_lahir_rendah) VALUES (%s, %s, %s, %s, %s);"
    cursor.execute(query, (id_pemeriksaan, usia_di_atas_45_tahun, riwayat_keluarga_diabetes, riwayat_diabetes_gestasional, riwayat_penyakit_berat_badan_rendah))
    conn.commit()
    conn.close()
    
    
def add_kebiasaan_hidup(id_pemeriksaan, konsumsi_alkohol, kurang_aktivitas, merokok, pola_makan_buruk, kurang_tidur):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "INSERT INTO kebiasaan_hidup(id_pemeriksaan, konsumsi_alkohol, kurang_aktivitas, merokok, pola_makan_buruk, kurang_tidur) VALUES (%s, %s, %s, %s, %s, %s);"
    cursor.execute(query, (id_pemeriksaan, konsumsi_alkohol, kurang_aktivitas, merokok, pola_makan_buruk, kurang_tidur))
    conn.commit()
    conn.close()
    
    
def add_pemeriksaan_fisik(id_pemeriksaan, berat_badan, tinggi_badan, lingkar_perut, indeks_massa_tubuh):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "INSERT INTO pemeriksaan_fisik(id_pemeriksaan, tinggi_badan, berat_badan, lingkar_perut, indeks_massa_tubuh) VALUES (%s, %s, %s, %s, %s);"
    cursor.execute(query, (id_pemeriksaan, berat_badan, tinggi_badan, lingkar_perut, indeks_massa_tubuh))
    conn.commit()
    conn.close()

def add_pemeriksaan_laboratorium(id_pemeriksaan, gula_darah_sewaktu, gula_darah_puasa, gula_darah_2_jam_setelah_makan, tekanan_darah, HDL, LDL, trigliserida, total_kolestrol):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "INSERT INTO pemeriksaan_laboratorium(id_pemeriksaan, gula_darah_sewaktu, gula_darah_puasa, gula_darah_2_jam_setelah_makan, tekanan_darah, HDL, LDL, trigliserida, total_kolestrol) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(query, (id_pemeriksaan, gula_darah_sewaktu, gula_darah_puasa, gula_darah_2_jam_setelah_makan, tekanan_darah, HDL, LDL, trigliserida, total_kolestrol))
    conn.commit()
    conn.close()

def get_tanggal_terkini(id_pengguna):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT MAX(tanggal_diagnosis) FROM diagnosis_penyakit WHERE diagnosis_penyakit.id_pengguna = %s;"
    cursor.execute(query, (id_pengguna,))
    tanggal_terkini = cursor.fetchone()
    conn.close()
    return tanggal_terkini[0]
    
    
def menambah_id_diagnosis_default():
    
    conn = connect_to_db()
    cursor = conn.cursor()
    

    cursor.execute("SELECT id_diagnosis FROM diagnosis_penyakit ORDER BY id_diagnosis DESC LIMIT 1")
    last_id = cursor.fetchone()
    
    if last_id:
        # Ambil nomor dari ID terakhir dan increment 1
        last_number = int(last_id[0][1:])  # Mengambil angka setelah 'D'
        new_id = f"D{last_number + 1:04d}" 
    else:
        # Jika tidak ada data sebelumnya, mulai dengan D0001
        new_id = "D0001"
    
    conn.close()
    return new_id

def fetch_diagnosis_penyakit_admin():
    conn = connect_to_db()
    
    query = """
    SELECT diagnosis_penyakit.tanggal_diagnosis, diagnosis_penyakit.id_diagnosis, diagnosis_penyakit.id_pengguna, pengguna.nama_pengguna, diagnosis_penyakit.gejala_terpilih, komplikasi_penyakit.nama_penyakit, diagnosis_penyakit.gejala_cocok, diagnosis_penyakit.persentase_kecocokan
    FROM diagnosis_penyakit
    LEFT JOIN pengguna ON diagnosis_penyakit.id_pengguna = pengguna.id_pengguna
    LEFT JOIN komplikasi_penyakit ON diagnosis_penyakit.id_komplikasi_penyakit = komplikasi_penyakit.id_komplikasi_penyakit;
    """
    
    df = pd.read_sql(query, conn)
    ganti_header = {
        "id_diagnosis": "ID Diagnosis",
        "id_pengguna": "ID Pengguna",
        "nama_pengguna": "Nama Pengguna",
        "gejala_terpilih": "Gejala Terpilih",
        "nama_penyakit": "Nama Penyakit",
        "gejala_cocok": "Gejala Cocok",
        "persentase_kecocokan": "Persentase Kecocokan",
        "tanggal_diagnosis": "Tanggal Diagnosis"
    }
    df.rename(columns=ganti_header, inplace=True)
    return df

def insert_diagnosis_penyakit(id_diagnosis, id_pengguna, id_komplikasi_penyakit, gejala_terpilih, gejala_cocok, persentase_kecocokan, tanggal_diagnosis):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "INSERT INTO diagnosis_penyakit(id_diagnosis, id_pengguna, id_komplikasi_penyakit, gejala_terpilih, gejala_cocok, persentase_kecocokan, tanggal_diagnosis) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(query, (id_diagnosis, id_pengguna, id_komplikasi_penyakit, gejala_terpilih, gejala_cocok, persentase_kecocokan, tanggal_diagnosis))
    conn.commit()
    conn.close()
    
def get_last_id_pengguna():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT id_pengguna FROM pengguna ORDER BY id_pengguna DESC LIMIT 1"
    cursor.execute(query)
    result = cursor.fetchone()    
    conn.close()
    
    return result[0]

def get_jumlah_pengguna():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT COUNT(*) FROM pengguna;"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result[0]

def get_jumlah_penyakit():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT COUNT(*) FROM komplikasi_penyakit;"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result[0]
    
def get_jumlah_gejala():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT COUNT(*) FROM gejala;"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result[0]

def get_penjelasan_penyakit(nama_penyakit):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT penjelasan FROM komplikasi_penyakit WHERE nama_penyakit = %s"
    cursor.execute(query, (nama_penyakit,))
    result = cursor.fetchone()
    conn.close()
    return result[0]
    

def validasi_password(password):
        return len(password) >= 7

def validasi_email_regex(email):
    regex = r'^[a-zA-Z0-9_.+-]+@gmail\.com$'
    return re.match(regex, email) is not None

def check_data_registrasi_pengguna(username_pengguna, email, password_pengguna, nama, alamat):
    
    validation_errors = []
                
    if cek_username(username_pengguna) == True:
        validation_errors.append("Username sudah terdaftar")

        
    if cek_email(email) == True and email != None:
        validation_errors.append("Email Sudah Terdaftar")
    # Check if username is provided
    if not username_pengguna:
        validation_errors.append("Username tidak boleh kosong.")

    # Check if password is provided and meets the length requirement
    if not password_pengguna or not validasi_password(password_pengguna):
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
        return False
    else:
        return True

def check_update_data_pengguna(username_pengguna, email, password_pengguna, nama, alamat):
    validation_errors = []
                
    if cek_username(username_pengguna) == True and username_pengguna != username_pengguna:
        validation_errors.append("Username sudah terdaftar")

        
    if cek_email(email) == True and email != email:
        validation_errors.append("Email Sudah Terdaftar")
    # Check if username is provided
    if not username_pengguna:
        validation_errors.append("Username tidak boleh kosong.")

    # Check if password is provided and meets the length requirement
    if not password_pengguna or not validasi_password(password_pengguna):
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
        return False
    else:
        return True


def check_admin(username, password):
    
    try:
        connection = connect_to_db()
        cursor = connection.cursor()

        # SQL query to check user credentials
        query = "SELECT * FROM admin WHERE username_admin = %s AND password = %s"
        cursor.execute(query, (username, password))

        # Fetch one result
        result = cursor.fetchone()
        if result:
            if result[0] == username and result[2] == password:
                return True # User is found
        else:
            return False  # User not found

    except mysql.connector.Error as err:
        st.error(f"Database error: {err}")  # Show the error
        return False  # Indicate failure

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            

def check_pengguna(username, password):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()

        # SQL query to check user credential
        query = "SELECT * FROM pengguna WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))

        # Fetch one result
        result = cursor.fetchone()
        if result:
            if result[1] == username and result[2] == password:
                return True # User is found
        else:
            return False  # User not found

    except mysql.connector.Error as err:
        st.error(f"Database error: {err}")  # Show the error
        return False  # Indicate failure

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            
def cek_username(username):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()

        # SQL query to check user credential
        query = "SELECT * FROM pengguna WHERE username = %s"
        cursor.execute(query, (username,))

        # Fetch one result
        result = cursor.fetchone()

        if result:
            
            return True # User is found
        else:
            return False  # User not found

    except mysql.connector.Error as err:
        st.error(f"Database error: {err}")  # Show the error
        return False  # Indicate failure

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def cek_email(email):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()

        # SQL query to check user credential
        query = "SELECT * FROM pengguna WHERE email = %s"
        cursor.execute(query, (email,))

        # Fetch one result
        result = cursor.fetchone()

        if result is not None and result[6] == email:
            
            return True # Email sudah ada
        else:
            return False  # Email belum ada

    except mysql.connector.Error as err:
        st.error(f"Database error: {err}")  # Show the error
        return False  # Indicate failure

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


        
    
# Function to insert data into the database
def insert_admin(username, name, password):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()

    
        # SQL query to insert data
        query = "INSERT INTO admin (username_admin, nama_admin, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, name, password))

        # Commit the transaction
        connection.commit()
        
        
        st.success("Admin Berhasil Ditambahkan!")
        return True



    except mysql.connector.Error as err:
        err = "Username yang anda masukkan salah atau sudah terdaftar! Gunakan yang lain"
        st.error(f"Database error: {err}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            
    

def hapus_admin(username_admin):
    conn = connect_to_db()
    cursor = conn.cursor()
    
    query = "DELETE FROM admin WHERE username_admin = %s"
    
    cursor.execute(query, (username_admin,)) #harus ditambah koma ,
    conn.commit()
    st.success("Admin Berhasil Dihapus")
    conn.close()


def hapus_pemeriksaan_kesehatan_dan_diagnosis(tanggal_pemeriksaan):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "DELETE FROM pemeriksaan_kesehatan WHERE tanggal_pemeriksaan = %s"
    cursor.execute(query, (tanggal_pemeriksaan,))
    conn.commit()
    query = "DELETE FROM diagnosis_penyakit WHERE tanggal_diagnosis = %s"
    cursor.execute(query, (tanggal_pemeriksaan,))
    conn.commit()
    conn.close()
    
    

def fetch_pemeriksaan_kesehatan():
    conn = connect_to_db()
    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT pemeriksaan_kesehatan.tanggal_pemeriksaan, pemeriksaan_kesehatan.id_pemeriksaan, pemeriksaan_kesehatan.id_pengguna, pengguna.nama_pengguna, pemeriksaan_kesehatan.risiko_diabetes, pemeriksaan_faktor_permanen.usia_di_atas_45_tahun, pemeriksaan_faktor_permanen.riwayat_keluarga_diabetes, pemeriksaan_faktor_permanen.riwayat_diabetes_gestasional, pemeriksaan_faktor_permanen.riwayat_lahir_berat_badan_lahir_rendah, kebiasaan_hidup.konsumsi_alkohol, kebiasaan_hidup.kurang_aktivitas, kebiasaan_hidup.merokok, kebiasaan_hidup.pola_makan_buruk, kebiasaan_hidup.kurang_tidur, pemeriksaan_fisik.berat_badan, pemeriksaan_fisik.tinggi_badan, pemeriksaan_fisik.lingkar_perut, pemeriksaan_fisik.indeks_massa_tubuh, pemeriksaan_laboratorium.gula_darah_sewaktu, pemeriksaan_laboratorium.gula_darah_puasa, pemeriksaan_laboratorium.gula_darah_2_jam_setelah_makan, pemeriksaan_laboratorium.tekanan_darah, pemeriksaan_laboratorium.HDL, pemeriksaan_laboratorium.LDL, pemeriksaan_laboratorium.trigliserida, pemeriksaan_laboratorium.total_kolestrol
    FROM pemeriksaan_kesehatan
    JOIN pemeriksaan_faktor_permanen ON pemeriksaan_kesehatan.id_pemeriksaan = pemeriksaan_faktor_permanen.id_pemeriksaan
    JOIN pengguna ON pemeriksaan_kesehatan.id_pengguna = pengguna.id_pengguna
    JOIN kebiasaan_hidup ON kebiasaan_hidup.id_pemeriksaan = pemeriksaan_kesehatan.id_pemeriksaan
    JOIN pemeriksaan_fisik ON pemeriksaan_kesehatan.id_pemeriksaan = pemeriksaan_fisik.id_pemeriksaan
    JOIN pemeriksaan_laboratorium ON pemeriksaan_laboratorium.id_pemeriksaan = pemeriksaan_kesehatan.id_pemeriksaan;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    if not result:
        return None

    # Convert result to Pandas DataFrame
    df = pd.DataFrame(result)
    
    ganti_header = {
        "tanggal_pemeriksaan": "Tanggal Pemeriksaan",
        "id_pemeriksaan": "ID Pemeriksaan",
        "id_pengguna": "ID Pengguna",
        "nama_pengguna": "Nama Pengguna",
        "risiko_diabetes": "Risiko Diabetes",
        "usia_di_atas_45_tahun": "Usia di Atas 45 Tahun",
        "riwayat_keluarga_diabetes": "Riwayat Keluarga Diabetes",
        "riwayat_diabetes_gestasional": "Riwayat Diabetes Gestasional",
        "riwayat_lahir_berat_badan_lahir_rendah": "Riwayat Lahir Berat Badan Lahir Rendah",
        "konsumsi_alkohol": "Konsumsi Alkohol",
        "kurang_aktivitas": "Kurang Aktivitas",
        "merokok": "Merokok",
        "pola_makan_buruk": "Pola Makan Buruk",
        "kurang_tidur": "Kurang Tidur",
        "berat_badan": "Berat Badan",
        "tinggi_badan": "Tinggi Badan",
        "lingkar_perut": "Lingkar Perut",
        "indeks_massa_tubuh": "Indeks Massa Tubuh",
        "gula_darah_sewaktu": "Gula Darah Sewaktu",
        "gula_darah_puasa": "Gula Darah Puasa",
        "gula_darah_2_jam_setelah_makan": "Gula Darah 2 Jam Setelah Makan",
        "tekanan_darah": "Tekanan Darah",
        "HDL": "HDL",
        "LDL": "LDL",
        "trigliserida": "Trigliserida",
        "total_kolestrol": "Total Kolestrol"
    }
    
    df.rename(columns=ganti_header, inplace=True)
    
    # Convert DataFrame back to a list of dictionaries
    return df  # Returns as a list of dictio



def fetch_pemeriksaan_kesehatan_pengguna(id_pengguna):
    conn = connect_to_db()
    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT pemeriksaan_kesehatan.tanggal_pemeriksaan, pemeriksaan_kesehatan.id_pemeriksaan, pemeriksaan_kesehatan.id_pengguna, pengguna.nama_pengguna, pemeriksaan_kesehatan.risiko_diabetes, pemeriksaan_faktor_permanen.usia_di_atas_45_tahun, pemeriksaan_faktor_permanen.riwayat_keluarga_diabetes, pemeriksaan_faktor_permanen.riwayat_diabetes_gestasional, pemeriksaan_faktor_permanen.riwayat_lahir_berat_badan_lahir_rendah, kebiasaan_hidup.konsumsi_alkohol, kebiasaan_hidup.kurang_aktivitas, kebiasaan_hidup.merokok, kebiasaan_hidup.pola_makan_buruk, kebiasaan_hidup.kurang_tidur, pemeriksaan_fisik.berat_badan, pemeriksaan_fisik.tinggi_badan, pemeriksaan_fisik.lingkar_perut, pemeriksaan_fisik.indeks_massa_tubuh, pemeriksaan_laboratorium.gula_darah_sewaktu, pemeriksaan_laboratorium.gula_darah_puasa, pemeriksaan_laboratorium.gula_darah_2_jam_setelah_makan, pemeriksaan_laboratorium.tekanan_darah, pemeriksaan_laboratorium.HDL, pemeriksaan_laboratorium.LDL, pemeriksaan_laboratorium.trigliserida, pemeriksaan_laboratorium.total_kolestrol
    FROM pemeriksaan_kesehatan
    JOIN pemeriksaan_faktor_permanen ON pemeriksaan_kesehatan.id_pemeriksaan = pemeriksaan_faktor_permanen.id_pemeriksaan
    JOIN pengguna ON pemeriksaan_kesehatan.id_pengguna = pengguna.id_pengguna
    JOIN kebiasaan_hidup ON kebiasaan_hidup.id_pemeriksaan = pemeriksaan_kesehatan.id_pemeriksaan
    JOIN pemeriksaan_fisik ON pemeriksaan_kesehatan.id_pemeriksaan = pemeriksaan_fisik.id_pemeriksaan
    JOIN pemeriksaan_laboratorium ON pemeriksaan_laboratorium.id_pemeriksaan = pemeriksaan_kesehatan.id_pemeriksaan
    WHERE pemeriksaan_kesehatan.id_pengguna = %s;
    """
    cursor.execute(query, (id_pengguna,))
    result = cursor.fetchall()
    conn.close()
    if not result:
        return None

    # Convert result to Pandas DataFrame
    df = pd.DataFrame(result)

    # Column renaming dictionary
    ganti_header = {
        "id_pemeriksaan": "ID Pemeriksaan",
        "id_pengguna": "ID Pengguna",
        "nama_pengguna": "Nama Pengguna",
        "risiko_diabetes": "Risiko Diabetes",
        "tanggal_pemeriksaan": "Tanggal Pemeriksaan",
        "usia_di_atas_45_tahun": "Usia Di Atas 45 Tahun",
        "riwayat_keluarga_diabetes": "Riwayat Keluarga Diabetes",
        "riwayat_diabetes_gestasional": "Riwayat Diabetes Gestasional",
        "riwayat_lahir_berat_badan_lahir_rendah": "Riwayat Berat Badan Lahir Rendah",
        "konsumsi_alkohol": "Konsumsi Alkohol",
        "kurang_aktivitas": "Kurang Aktivitas",
        "merokok": "Merokok",
        "pola_makan_buruk": "Pola Makan Buruk",
        "kurang_tidur" : "Kurang Tidur",
        "tinggi_badan": "Tinggi Badan",
        "berat_badan": "Berat Badan",
        "lingkar_perut": "Lingkar Perut",
        "indeks_massa_tubuh": "Indeks Massa Tubuh",
        "gula_darah_sewaktu": "Gula Darah Sewaktu",
        "gula_darah_puasa": "Gula Darah Puasa",
        "gula_darah_2_jam_setelah_makan": "Gula Darah 2 Jam Setelah Makan",
        "tekanan_darah": "Tekanan Darah",
        "HDL": "HDL",
        "LDL": "LDL",
        "trigliserida": "Trigliserida",
        "total_kolestrol": "Total Kolesterol",
    }

    # Rename columns
    df.rename(columns=ganti_header, inplace=True)

    # Convert DataFrame back to a list of dictionaries
    return df  # Returns as a list of dictio
    
    
    




def fetch_pemeriksaan_fisik():
    
    
    conn = connect_to_db()
    query = "SELECT * FROM pemeriksaan_fisik"
    df = pd.read_sql(query, conn)
    return df

def fetch_pemeriksaan_faktor_permanen():
    conn = connect_to_db()
    query = "SELECT * FROM pemeriksaan_faktor_permanen"
    df = pd.read_sql(query, conn)
    return df


def fetch_pemeriksaan_laboratorium():

    conn = connect_to_db()
    query = "SELECT * FROM pemeriksaan_laboratorium;"
    df = pd.read_sql(query, conn)
    return df

def fetch_kebiasaan_hidup():
    conn = connect_to_db()
    query = "SELECT * FROM kebiasaan_hidup"
    df = pd.read_sql(query, conn)
    return df



def get_diagnosis_penyakit(id_pengguna):
    
    conn = connect_to_db()
    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT diagnosis_penyakit.tanggal_diagnosis, diagnosis_penyakit.id_diagnosis, diagnosis_penyakit.id_pengguna, pengguna.nama_pengguna, komplikasi_penyakit.nama_penyakit, diagnosis_penyakit.gejala_terpilih, diagnosis_penyakit.gejala_cocok, diagnosis_penyakit.persentase_kecocokan
    FROM diagnosis_penyakit
    LEFT JOIN pengguna ON diagnosis_penyakit.id_pengguna = pengguna.id_pengguna
    LEFT JOIN komplikasi_penyakit ON diagnosis_penyakit.id_komplikasi_penyakit = komplikasi_penyakit.id_komplikasi_penyakit
    WHERE diagnosis_penyakit.id_pengguna = %s;
    """ 
    cursor.execute(query, (id_pengguna,))
    result = cursor.fetchall()
    conn.close()
    if not result:
        return None

    # Convert result to Pandas DataFrame
    df = pd.DataFrame(result)

    # Column renaming dictionary
    ganti_header = {
        "id_diagnosis": "ID Diagnosis",
        "id_pengguna": "ID Pengguna",
        "nama_pengguna": "Nama Pengguna",
        "nama_penyakit": "Nama Penyakit",
        "gejala_terpilih": "Gejala Terpilih",
        "gejala_cocok": "Gejala Cocok",
        "persentase_kecocokan": "Persentase Kecocokan",
        "tanggal_diagnosis": "Tanggal Diagnosis"
    }

    # Rename columns
    df.rename(columns=ganti_header, inplace=True)

    return df 



def hapus_hasil_pemeriksaan_dan_diagnosis_penyakit_admin(id_pengguna, tanggal):
    conn = connect_to_db()
    query = "DELETE FROM pemeriksaan_kesehatan WHERE id_pengguna = %s AND tanggal_pemeriksaan = %s"
    cursor = conn.cursor()
    cursor.execute(query, (id_pengguna, tanggal))
    conn.commit()
    query = "DELETE FROM diagnosis_penyakit WHERE id_pengguna = %s AND tanggal_diagnosis = %s"
    cursor.execute(query, (id_pengguna, tanggal))
    conn.commit()
    conn.close()

