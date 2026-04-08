import pandas as pd
import json
from models.prophet_model import run_prophet

def run_forecast(input_path: str):
    df = pd.read_parquet(input_path)

    forecast = run_prophet(df)

    result = forecast.to_dict(orient="records")

    with open("outputs/forecast.json", "w") as f:
        json.dump(result, f, indent=4, default=str)

    print("Forecast generated")
    return result