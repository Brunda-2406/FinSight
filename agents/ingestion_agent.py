import pandas as pd
import os

def run_ingestion(input_path: str):
    if input_path.endswith(".csv"):
        df = pd.read_csv(input_path)

    elif input_path.endswith(".json"):
        df = pd.read_json(input_path)

    else:
        raise ValueError("Unsupported file format")

    # Normalize
    df.columns = [col.lower() for col in df.columns]

    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])

    if 'amount' in df.columns:
        df['amount'] = df['amount'].astype(float)

    output_path = "data/interim/transactions.parquet"
    os.makedirs("data/interim", exist_ok=True)
    df.to_parquet(output_path, index=False)

    print("Ingestion done ->", output_path)
    return output_path