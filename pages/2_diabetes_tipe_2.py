import streamlit as st
from assets import database as db


col1, col2 = st.columns([8, 2])
with col1:
  st.title("Informasi Tentang Diabetes Tipe 2")
with col2:
  st.markdown(
        '<a href="https://bebas-diabetes.streamlit.app/login_pengguna" target="_self" style="font-size:20px;">Login Disini</a>',
        unsafe_allow_html=True
  )
kiri, tengah, kanan = st.columns(3)

with tengah:
  st.image("assets/Free From Diabetes Logo.png", width=300)

text = """
  <div style="text-align: justify;">
    Diabetes tipe 2 adalah penyakit yang membuat kadar gula darah meningkat akibat kelainan 
    pada kemampuan tubuh untuk menggunakan hormon insulin. Diabetes tipe 2 merupakan jenis diabetes yang paling sering terjadi. 
    Insulin adalah hormon yang membantu gula darah (glukosa) masuk ke dalam sel tubuh 
    untuk diubah menjadi energi. Hormon ini diproduksi oleh pankreas ketika seseorang makan. 
    Pada diabetes tipe 2, tingginya kadar gula darah terjadi akibat resistensi insulin, 
    yaitu kondisi sel ketika tubuh tidak dapat menggunakan hormon insulin dengan baik. Penyakit diabetes tipe 2 adalah penyakit yang paling umum di dunia dan ditimbulkan oleh berbagai macam sebab, 
    seperti faktor genetik, gaya hidup, dan lingkungan. Faktor terjadinya Diabetes Tipe 2 dapat dibagi menjadi dua yaitu:
  </div>
"""

st.markdown(text, unsafe_allow_html=True)
st.write(" ")
st.write("**Faktor Tidak Bisa Diubah**")

kiri, tengah, kanan = st.columns(3)

with tengah:
  st.image("https://p2ptm.kemkes.go.id/uploads//TmQwU05BQS9YYlJpanB5VnNtRldFUT09/WhatsApp_Image_2021_11_17_at_08_41_47.jpg", width=270, caption="Faktor Tidak Bisa Diubah")
url = "https://p2ptm.kemkes.go.id/infographic-p2ptm/penyakit-diabetes-melitus?page=13"
st.write("Sumber Gambar: [https://p2ptm.kemkes.go.id/infographic-p2ptm/penyakit-diabetes-melitus?page=13](%s)" % url)

st.write(
  """
  Faktor tidak bisa diubah merupakan faktor-faktor yang diluar kendali manusia seperti:
  - Usia : Orang dengan usia lebih dari 45 tahun lebih rentan terkena penyakit Diabetes Tipe 2 dan risiko semakin meningkat
      seiring bertambahnya usia.
  - Riwayat Keluarga : Terdapat anggota keluarga dekat (*first-degree relative* seperti orang tua dan saudara kandung) yang terkena diabetes
  - Riwayat Penyakit : Riwayat melahirkan bayi dengan Berat Badan Lahir (BBL) > 4 kg atau Diabetes Mellitus Gestasional.
  - Riwayat Lahir    : Lahir dengan Berat Badan Lahir (BBL) < 2,5 kg atau terlahir prematur.
  """
)




kiri, tengah, kanan = st.columns(3)

with tengah:
  st.image("https://p2ptm.kemkes.go.id//uploads/cEdQdm1WVXZuRXhad3FtVXduOW1WUT09/1720499682_4171081e51c1b700bf5c.png", width=270, caption="Faktor Bisa Diubah")
url = "https://p2ptm.kemkes.go.id/infographic-p2ptm/penyakit-diabetes-melitus/faktor-risiko-penyakit-diabetes-melitus-dm-faktor-risiko-yang-bisa-diubah"
st.write("Sumber Gambar: [https://p2ptm.kemkes.go.id/infographic-p2ptm/penyakit-diabetes-melitus/faktor-risiko-penyakit-diabetes-melitus-dm-faktor-risiko-yang-bisa-diubah](%s)" % url)




st.write(
  """
  
  
  Faktor bisa diubah merupakan faktor-faktor yang dapat diubah oleh manusia seperti:
  - Merokok : Perokok aktif
  - Pola Makan Buruk : Sering mengonsumsi makanan/minuman yang mengandung gula, garam, dan lemak tinggi serta rendah serat atau kurang konsumsi buah-buahan dan sayuran.
  - Konsumsi Alkohol : Konsumsi alkohol yang berlebihan > 28 gram atau > 4 botol bir dalam sehari.
  - Kurang Tidur : Kurang tidur atau mengalami gangguan tidur sehingga tidur tidak berkualitas dengan waktu tidur hanya < 6 jam dalam sehari.
  - Aktivitas Fisik : Kurang beraktivitas fisik atau berolahraga dengan waktu < 150 menit dalam seminggu.
  - Berat Badan : Berat badan yang berlebihan atau obesitas dengan Indeks Massa Tubuh > 23 kg/m2 untuk untuk ras dan etnis tertentu seperti Asia, Afro-Amerika, Hispanik/Amerika Latin, Indian Amerika, dan Kepulauan Pasifik.
  - Lingkar Perut : Lingkaran perut mengalami obesitas sentral dengan lingkar perut ≥ 90 cm untuk pria dan lingkar perut ≥ 80 cm untuk wanita.
  - Hipertensi : Hipertensi dengan tekanan darah sistolik ≥ 140 mmHg dan/atau tekanan darah diastolik ≥ 90 mmHg.
  - Disiplidemia : Memiliki tingkat kolestrol yang tidak seimbang dengan kolestrol baik High Density Lipoprotein (HDL) ≤ 35 mg/dL dan/atau kolestrol jahat Low Density Lipoprotein (LDL) ≥  100 mg/dL dan/atau trigliseria ≥  250 mg/dL.
  - Kolestrol Tinggi : Memiliki kadar kolesterol total > 240 mg/dL dan dapat digunakan Rumus Friedwal yaitu Kolestrol LDL = Kolestrol Total - HDL  - Trigliserida/5
  - Gula Darah
    
    Terdapat 3 macam pemeriksaan gula darah yang akan digunakan yaitu:
    
    - Gula Darah Sewaktu (GDS)
        - Normal:  70 – 139 mg/dL
        - Prediabetes: 140 – 199 mg/dL
        - Gula Dara Tinggi: ≥ 200 mg/dL
    - Gula Darah Puasa (GDP)
        - Normal:  70 – 99 mg/dL
        - Prediabetes: 100 – 125 mg/dL
        - Gula Darah Tinggi: ≥126 mg/dL
    - Gula Darah 2 Jam Setelah Makan (GD2PP)
        - Normal: 70 - 139 mg/dL
        - Prediabetes: 140 - 199 mg/dL
        - Gula Darah Tinggi: ≥ 200 mg/dL
        
  
  """
)

st.write(
  """
    **Pengobatan dan Pencegahan**
    
    Penanganan Diabetes Mellitus Tipe 2 adalah dengan cara mengatur pola makan, olahraga, dan pengobatan medis seperti pemberian insulin atau obat. 
    Pasien harus rutin melakukan pemeriksaan kesehatan dan tes gula darah secara rutin sambil mengikuti pengobatan.
    
    Pencegahan penyakit Diabetes Mellitus Tipe 2 dapat dilakukan dengan cara seperti berikut ini:
    - Aktif bergerak, beraktivitas, atau berolahraga secara rutin minimal 150 menit dalam seminggu.
    - Menjaga Indeks Massa Tubuh ideal sebesar 18,5 - 22,9 k/m2.
    - Menghindari makanan yang mengandung gula, garam, dan lemak tinggi.
    - Perbanyak makan sayur-sayuran, buah-buahan, makanan tinggi serat, dan rendah kalori.
    - Kurangi atau jauhi merokok dan minum alkohol
    - Kurangi begadang dan tidur yang secukupnya sekitar 7-8 jam per hari.
  """
)

st.write(
  """
    **Komplikasi Penyakit Diabetes Mellitus Tipe 2**
  
    - Hiperglikemia : Kelebihan gula dalam darah.
    - Hipoglikemia : Kekurangan gula dalam darah.
    - Ketoasidosis Diabetik : Kadar keton yang tinggi dalam tubuh akibat tubuh tidak dapat mengubah glukosa menjadi energi.
    - Neuropati Diabetik : Gangguan saraf akibat penyakit diabetes.
    - Nefropati Diabetik : Penurunan fungsi ginjal akibat penyakit diabetes.
    - Retinopati Diabetik	: Kerusakan pada mata akibat penyakit diabetes.
    - Penyakit Kardiovaskular	: Penyakit yang menyerang pembuluh darh dan jantung seperti penyakit jantung koroner, stroke, aritmia, serangan jantung, gagal jantung, dan lain-lain.
  
  """
)

st.write("")
st.write("")
st.write("")
st.write("")

st.markdown(
  """
      **Sumber referensi:**
      
      [1] https://www.alodokter.com/diabetes-tipe-2
      
      [2] https://ayosehat.kemkes.go.id/topik-penyakit/diabetes--penyakit-ginjal/diabetes-melitus-tipe-2
      
      [3] https://www.nhs.uk/conditions/type-2-diabetes/
      
  """
)
