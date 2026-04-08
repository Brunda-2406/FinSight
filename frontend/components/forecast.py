import streamlit as st
import json
import pandas as pd
import plotly.express as px

def show_forecast():
    st.header("📈 Forecast")

    try:
        with open("outputs/forecast.json") as f:
            data = json.load(f)

        df = pd.DataFrame(data)

        fig = px.line(df, x="ds", y="yhat", title="Spending Forecast")
        st.plotly_chart(fig)

    except:
        st.warning("No forecast data available")