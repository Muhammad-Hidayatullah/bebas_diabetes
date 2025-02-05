import streamlit
from streamlit_pdf_viewer import pdf_viewer


# Declare variable.
if 'pdf_ref' not in ss:
    ss.pdf_ref = None


# Access the uploaded ref via a key.
st.file_uploader("Upload PDF file", type=('pdf'), key='pdf')

if ss.pdf:
    ss.pdf_ref = ss.pdf  # backup

# Now you can access "pdf_ref" anywhere in your app.
if ss.pdf_ref:
    binary_data = ss.pdf_ref.getvalue()
    pdf_viewer(input=binary_data, width=700)
