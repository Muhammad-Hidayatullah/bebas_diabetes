import streamlit as st

st.title("Bantuan Penggunaan Aplikasi")


st.header("Cara Menggunakan Aplikasi")
st.write("""   
1. Melakukan registrasi dan login dengan memasukkan data Anda serta membuat username dan password.
   
2. Setelah melakukan login, anda akan masuk ke halaman akun Anda yang berisikan data profil, diagnosis, serta riwayat diagnosis.

3. Navigasi ke diagnosis dan pilih dan isi faktor risiko yang tersedia seperti riwayat penyakit, pola hidup, dan faktor risiko lainnya dan Anda akan mendapatkan tingkat risiko Anda.

4. Setelah itu Anda mengisi tes gula darah untuk mendapatkan diagnosis.

5. Jika gula darah tidak normal, maka dilanjutkan dengan mengisi gejala-gejala yang dialami dan mendapatkan penyakit berdasarkan gejala yang Anda alami serta penjelasan dan solusi.

6. Dan yang terakhir Anda dapat mengunduh hasil diagnosis Anda.

7. Anda juga dapat mengunduh riwayat diagnosis Anda atau menghapus riwayat diagnosis Anda pada halaman Riwayat.
""")

st.markdown("---")

st.title("Kirim Pesan Anda")
col1, col2= st.columns(2)
form_kontak = """
    <form action="https://formsubmit.co/admbebasdiabetes@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" required placeholder="Nama anda">
        <input type="email" name="email" required placeholder="Email anda">
        <textarea name="message" placeholder="Tulis pesan anda"></textarea>
        <button type="submit">Kirim</button>
</form>
"""

with col2:
    st.markdown(
    """
        📞 0819-0522-1487
        
        📧 admbebasdiabetes@gmail.com
      
    """
    )


with col1:
    st.markdown("Silahkan tinggalkan pesan pada kolom yang tersedia")
    st.markdown(form_kontak, unsafe_allow_html=True)

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
            
    local_css("./style/style.css")

