import streamlit as st

file_pdf = st.file_uploader("Upload a PDF", type="pdf")

if file_pdf is not None:
    pdf_display = f'<embed src="data:application/pdf;base64,{file_pdf}" width="700" height="400" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)
