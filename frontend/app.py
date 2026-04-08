import streamlit as st
from components.upload import upload_file
from components.dashboard import show_dashboard
from components.charts import show_charts
from services.pipeline_runner import run_pipeline

# NEW IMPORTS
from components.risk_gauge import show_risk_gauge
from components.forecast import show_forecast
from components.insights import show_insights

st.set_page_config(layout="wide")

st.title("💸 FinSight Autopilot")

# Upload
file_path = upload_file()

# Run pipeline
if file_path:
    if st.button("Run Analysis"):
        run_pipeline(file_path)

# Show results
show_dashboard()
show_charts()

# NEW FEATURES
show_risk_gauge()
show_forecast()
show_insights()