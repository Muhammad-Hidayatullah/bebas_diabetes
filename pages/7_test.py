import streamlit as st
import base64

# Upload the PDF file
file_pdf = st.file_uploader("Upload a PDF", type="pdf")

if file_pdf is not None:
    # Read the file content
    file_bytes = file_pdf.read()
    
    # Base64 encode the PDF content
    base64_pdf = base64.b64encode(file_bytes).decode("utf-8")
    
    # Embed the PDF in HTML using base64 data
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="400" type="application/pdf">'
    
    # Display the embedded PDF
    st.markdown(pdf_display, unsafe_allow_html=True)
