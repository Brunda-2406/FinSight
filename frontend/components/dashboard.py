import streamlit as st
import pandas as pd

def show_dashboard():
    st.header("📊 Dashboard")

    try:
        df = pd.read_parquet("data/processed/clean_data.parquet")

        st.subheader("Category Summary")
        summary = df.groupby("category")["amount"].sum().reset_index()
        st.dataframe(summary)

    except:
        st.warning("No data available yet")