import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
from streamlit_pdf_viewer import st_pdf

# Input for name
name = st.text_input("Enter your name:")

if name:
    # Create a PDF in memory
    pdf_buffer = io.BytesIO()
    c = canvas.Canvas(pdf_buffer, pagesize=letter)
    
    # Add text to PDF
    c.drawString(100, 750, f"Hello {name}!")
    
    # Save the PDF
    c.save()
    
    # Move buffer cursor to the beginning of the PDF
    pdf_buffer.seek(0)
    
    # Display the generated PDF
    st_pdf(pdf_buffer)
    
    # Create a download button for the PDF
    st.download_button(
        label="Download PDF",
        data=pdf_buffer,
        file_name=f"hello_{name}.pdf",
        mime="application/pdf"
    )
