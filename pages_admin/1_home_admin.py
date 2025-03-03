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


import streamlit as st

# Example data
user_total = 10

# Custom CSS for the card
st.markdown(
    f"""
    <div style="
        width: 150px;
        padding: 3px;
        border-radius: 2px;
        background-color: #f0f2f6;
        text-align: center;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    ">
        <h3 style="color: #333;">User Total</h3>
        <p style="font-size: 24px; font-weight: bold; color: #007BFF;">{user_total}</p>
    </div>
    """,
    unsafe_allow_html=True
)


st.title("DASBOR ADMIN")
st.subheader("Jumlah Pengguna")


st.image("./assets/admin.png", width=300)

st.write("Silahkan pilih menu-menu berikut dan atur sesuai kebutuhan")


