import streamlit as st

st.session_state.style_tabel = """
<style>
    table {
        width: 100%;
        border-collapse: collapse;
        font-family: Arial, sans-serif;
        font-size: 12px;
    }
    th {
        background-color: green;
        color: white;
        padding: 10px;
        text-align: left;
    }
    td {
        background-color: white;
        padding: 10px;
        border: 1px solid #ddd;
        text-align: left;
    }
    tr:nth-child(even) td {
        background-color: #f9f9f9;
    }
</style>
"""




# Example data
total_pengguna = 10

def kartu(total_apa, nilai):
    style_kartu = f"""
    <div style="
        width: 150px;
        padding: 5px;
        border-radius: 3px;
        background-color: #f0f2f6;
        text-align: center;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    ">
        <p style="color: #333; font-weight: bold; font-size: 18px; margin: 5px 0;">{total_apa}</p>
        <p style="font-size: 20px; font-weight: bold; color: #007BFF; margin: 5px 0;">{nilai}</p>
    </div>
    """
    st.markdown(style_kartu, unsafe_allow_html=True)

# Contoh penggunaan
kartu("User Total", 10)


st.markdown(
    f"""
    <div style="
        width: 150px;
        padding: 5px;
        border-radius: 3px;
        background-color: #f0f2f6;
        text-align: center;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    ">
        <p style="color: #333; font-weight: bold; font-size: 20px;">Total Pengguna</p>
        <p style="font-size: 20px; font-weight: bold; color: #007BFF;">{total_pengguna}</p>
    </div>
    """,
    unsafe_allow_html=True
)




st.title("DASBOR ADMIN")
st.subheader("Jumlah Pengguna")


st.image("./assets/admin.png", width=300)

st.write("Silahkan pilih menu-menu berikut dan atur sesuai kebutuhan")


