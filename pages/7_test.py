import streamlit as st
import PyPDF2
import io

def main():
    st.title("PDF Viewer & Downloader")
    
    # Input name
    name = st.text_input("Enter your name:")
    
    # File uploader
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    
    if uploaded_file is not None:
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")
        
        # Display PDF
        if st.button("View PDF"):
            with io.BytesIO(uploaded_file.read()) as pdf_bytes:
                pdf_reader = PyPDF2.PdfReader(pdf_bytes)
                text = "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
                st.text_area("PDF Content:", text, height=300)
        
        # Provide download button
        st.download_button(
            label="Download PDF",
            data=uploaded_file.getvalue(),
            file_name=uploaded_file.name,
            mime="application/pdf"
        )

if __name__ == "__main__":
    main()
