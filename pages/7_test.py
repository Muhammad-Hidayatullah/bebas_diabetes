import streamlit as st
from fpdf import FPDF
import io
from streamlit_pdf_viewer import pdf_viewer

# Declare variable to store the generated PDF
if 'pdf_ref' not in st.session_state:
    st.session_state.pdf_ref = None

# Take input text from the user
input_text = st.text_area("Enter text for the PDF:")

if input_text:
    # Create a PDF in memory using FPDF
    pdf = FPDF()
    pdf.add_page()
    
    # Set font
    pdf.set_font("Arial", size=12)
    
    # Add text to PDF
    pdf.multi_cell(200, 10, txt=input_text)
    
    # Save PDF to a byte stream
    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    
    # Move cursor to the beginning of the PDF file
    pdf_output.seek(0)
    
    # Store the generated PDF in session state
    st.session_state.pdf_ref = pdf_output.read()  # Save the binary content of the generated PDF

# Display the generated PDF
if st.session_state.pdf_ref:
    pdf_viewer(input=st.session_state.pdf_ref, width=700)
