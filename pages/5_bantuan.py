import streamlit as st

st.title("Bantuan dan Panduan Penggunaan Aplikasi")

st.header("Selamat Datang di Aplikasi Diagnosis Penyakit Diabetes Mellitus Tipe 2")
st.write("""
Aplikasi ini dirancang untuk membantu Anda dalam mendiagnosis dan memantau kesehatan terkait diabetes mellitus tipe 2. 
Silakan ikuti panduan di bawah ini untuk memanfaatkan semua fitur yang tersedia.
""")

st.markdown("---")

st.header("Fitur Aplikasi")
st.subheader("1. Registrasi dan Login")
st.write("""
Pada bagian ini, Anda dapat melakukan registrasi dengan cara memasukkan username yang belum terdaftar, password, 
nama lengkap, jenis kelamin, tanggal lahir, pekerjaan, email, dan alamat tempat tinggal. Setelah registrasi, Anda 
dapat login menggunakan username dan password yang telah Anda buat.
""")


st.subheader("2. Check Up")
st.write("""
Pada bagian ini Anda harus mengisi pemeriksaan kesehatan Anda. Yang pertama adalah memasukkan Faktor Tidak Diubah
seperti usia di atas 45 tahun, riwayat keluarga diabetes, riwayat penyakit kardiovaskular, dan riwayat lahir <2,5 kg atau prematur.
Lalu Anda mengisi Faktor Risiko Bisa Diubah yang terdiri dari Pemeriksaan Gaya Hidup, Pemeriksaan Fisik, dan Pemeriksaan Tekanan dan Kolestrol Darah.
Setelah mengisi semuanya Anda akan mendapatkan total Faktor Risiko Anda dan tingkt risiko terkena Diabetes Mellitus Tipe 2 berdasarkan Faktor Risiko. 
Setelah itu mengisi pemeriksaan gula untuk mengetahui apa level gula darah Anda berdasarkan Gula Darah Sewaktu (GDS), Gula Darah Puasa (GDP), dan 
Gula Darah 2 Jam Setelah Makan (GD2PP). Dari pemeriksaan darah ini ditambah dengan total Faktor Risiko Anda akan mendapatkan diagnosa apakah Anda berisiko terkena Diabetes
Mellitus Tipe 2 atau tidak.

""")

st.subheader("3. Pemeriksaan Komplikasi")
st.write("""
Di bagian ini, Anda dapat memilih gejala-gejala yang dialami pasien dari daftar yang tersedia. 
Cukup centang gejala yang relevan dan klik tombol "Submit" untuk menyimpan pilihan Anda. Setelah itu Anda 
akan mendapatkan gejala-gejala yang Anda pilih, komplikasi penyakit, gejala penyakit yang cocok (intersect) dengan 
yang Anda piilih, gejala penyakitnya secara penuh, dan solusi 
""")

st.markdown("---")

st.header("Cara Menggunakan Aplikasi")
st.write("""   
1. **Pilih Menu Diagnosis**: Pada bagian ini Anda dapat melakukan Login dan Registrasi. Apabila Anda belum memiliki akun
Anda dapat melakukan registrasi dengan cara memasukkan username yang belum terdaftar, password, nama lengkap, jenis kelamin, tanggal lahir, pekerjaan, email, dan alamat tempat tinggal Anda.
Setelah itu Anda akan diarahkan ke halaman login. Anda dapat login menggunakan username dan password yang telah Anda buat.
   
2. **Tampilan Data Pasien**: Setelah Anda berhasil login, Anda akan diarahkan ke halaman tampilan data pasien. Disini Anda dapat data Anda dan diberikan pilihan untuk Update Data Anda, Lanjut Pemeriksaan, dan Logout. 

3. **Pemeriksaan Kesehatan**: Setelah Anda memilih Lanjut Pemeriksaan, Anda akan diarahkan untuk mengisi data pemeriksaan kesehatan Anda dan Anda akan mendapatkan total Faktor Risiko Anda dan tingkt risiko terkena Diabetes Mellitus Tipe 2 Anda.
Untuk memastikan akurasi, Anda akan diminta untuk mengisi test gula darah Anda. Dari pemeriksaan darah ini ditambah dengan total Faktor Risiko Anda maka akan diperoleh hasil akhir diagnosa tingkat risiko Anda terkena Diabetes Mellitus Tipe 2.

4. **Gejala-Gejala**: Setelah mendapatkan hasil tingkat risiko Anda, Anda akan mengisi gejala-gejala yang dialami. Dengan metode Forward Chaining maka komplikasi penyakit akan dipilih berdasarkan gejala-gejala terbanyak dan cocok sesuai dengan yang Anda pilih. 
Anda akan mendapatkan nama jenis penyakit, gejala yang cocok, gejala komplikasi penyakit, dan solusi atau pengobatan komplikasi penyakit tersebut.

5. **Laporan Hasil**: Setelah semuanya selesai, Anda akan mendapatkan hasil laporan Anda dalam bentuk PDF yang dapat Anda unduh.

""")

st.markdown("---")

st.header("Kontak Bantuan")
st.write("""
Jika Anda memerlukan bantuan lebih lanjut atau memiliki pertanyaan, silakan hubungi tim dukungan kami di:
- Email: support@diabetesapp.com
- Telepon: +62 123 456 7890
""")

st.write("Terima kasih telah menggunakan aplikasi kami! Semoga aplikasi ini bermanfaat untuk Anda.")
