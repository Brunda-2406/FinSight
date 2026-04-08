from agents.ingestion_agent import run_ingestion
from agents.cleaning_agent import run_cleaning
from agents.eda_agent import run_eda
from agents.risk_agent import run_risk
from agents.forecast_agent import run_forecast
import sys

def run_pipeline(input_file):
    step1 = run_ingestion(input_file)
    step2 = run_cleaning(step1)

    run_eda(step2)
    run_risk(step2)
    run_forecast(step2)

    print("Pipeline completed!")

if __name__ == "__main__":
    input_file = sys.argv[1]
    run_pipeline(input_file)