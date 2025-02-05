import streamlit as st
from fpdf import FPDF
import io
from streamlit_pdf_viewer import pdf_viewer

# Input for name
name = st.text_input("Enter your name:")

if name:
    # Create a PDF in memory using FPDF
    pdf = FPDF()
    pdf.add_page()
    
    # Set font
    pdf.set_font("Arial", size=12)
    
    # Add text to PDF
    pdf.cell(200, 10, txt=f"Hello {name}!", ln=True, align='C')
    
    # Save PDF to a byte stream
    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    
    # Move cursor to the beginning of the PDF file
    pdf_output.seek(0)
    
    # Display the generated PDF
    pdf_viewer(pdf_output)
    
    # Create a download button for the PDF
    st.download_button(
        label="Download PDF",
        data=pdf_output,
        file_name=f"hello_{name}.pdf",
        mime="application/pdf"
    )
