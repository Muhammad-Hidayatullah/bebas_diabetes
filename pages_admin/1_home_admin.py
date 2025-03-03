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
        background-color: #f9f9f9; /* Light gray for alternating rows */
    }
</style>
"""

st.title("DASBOR ADMIN")
st.subtitle("Jumlah Pengguna")

st.image("./assets/admin.png", width=300)

st.write("Silahkan pilih menu-menu berikut dan atur sesuai kebutuhan")


