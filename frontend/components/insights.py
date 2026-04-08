import streamlit as st
from services.llm_service import generate_insights

def show_insights():
    st.header("🧠 AI Insights")

    if st.button("Generate Insights"):
        try:
            with st.spinner("Analyzing your finances..."):
                insights = generate_insights(
                    "outputs/risk_score.json",
                    "outputs/forecast.json"
                )

            st.success("Insights Generated ✅")
            st.write(insights)

        except Exception as e:
            st.error(f"Error: {e}")