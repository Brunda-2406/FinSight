import pandas as pd
import json
from models.risk_model import calculate_risk

def run_risk(input_path: str):
    df = pd.read_parquet(input_path)

    result = calculate_risk(df)

    with open("outputs/risk_score.json", "w") as f:
        json.dump(result, f, indent=4)

    print("Risk score generated")
    return result