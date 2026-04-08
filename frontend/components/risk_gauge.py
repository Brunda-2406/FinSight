import streamlit as st
import json

def show_risk_gauge():
    st.header("⚠️ Risk Score")

    try:
        with open("outputs/risk_score.json") as f:
            data = json.load(f)

        score = data.get("risk_score", 0)

        st.metric("Risk Score", f"{score}/100")

    except:
        st.warning("No risk data available")