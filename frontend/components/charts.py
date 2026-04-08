import streamlit as st
import plotly.express as px
import pandas as pd

def show_charts():
    st.subheader("📈 Spending Trends")

    try:
        df = pd.read_parquet("data/processed/clean_data.parquet")

        df["date"] = pd.to_datetime(df["date"])
        monthly = df.groupby(df["date"].dt.to_period("M"))["amount"].sum().reset_index()
        monthly["date"] = monthly["date"].astype(str)

        fig = px.line(monthly, x="date", y="amount", title="Monthly Spending")
        st.plotly_chart(fig)

    except:
        st.warning("Charts not available yet")