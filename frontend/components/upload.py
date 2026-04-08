import streamlit as st
import os

def upload_file():
    st.sidebar.header("📂 Upload Data")

    uploaded_file = st.sidebar.file_uploader(
        "Upload CSV or PDF", 
        type=["csv", "pdf"]
    )

    if uploaded_file:
        file_path = os.path.join("data/raw", uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.sidebar.success("File uploaded successfully ✅")
        return file_path

    return None