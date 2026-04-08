import subprocess
import streamlit as st
import os
import sys

def run_pipeline(file_path):
    st.write("⚙️ Running pipeline...")

    progress = st.progress(0)

    steps = [
        ("Ingestion", 20),
        ("Cleaning", 40),
        ("EDA", 60),
        ("Risk", 80),
        ("Forecast", 100)
    ]

    for step, value in steps:
        st.write(f"Running {step}...")
        progress.progress(value)

    # ✅ FIX: Ensure correct root path
    project_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../..")
    )

    # ✅ FIX: Use same Python (venv) + correct working directory
    result = subprocess.run(
        [sys.executable, "-m", "pipelines.run_pipeline", file_path],
        capture_output=True,
        text=True,
        cwd=project_root
    )

    # ✅ Show logs in UI (VERY IMPORTANT for debugging)
    st.text(result.stdout)
    st.text(result.stderr)

    if result.returncode != 0:
        st.error("Pipeline failed")
        return False

    st.success("Pipeline completed!")
    return True