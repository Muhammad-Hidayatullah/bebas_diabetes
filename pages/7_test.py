import streamlit
from streamlit_pdf_viewer import pdf_viewer


# Declare variable.
if 'pdf_ref' not in st.session_state:
    st.session_state.pdf_ref = None


# Access the uploaded ref via a key.
st.file_uploader("Upload PDF file", type=('pdf'), key='pdf')

if st.session_state.pdf:
    st.session_state.pdf_ref = st.session_state.pdf  # backup

# Now you can access "pdf_ref" anywhere in your app.
if st.session_state.pdf_ref:
    binary_data = st.session_state.pdf_ref.getvalue()
    pdf_viewer(input=binary_data, width=700)
