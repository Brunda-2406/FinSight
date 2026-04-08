import pandas as pd
import os

def run_cleaning(input_path: str):
    df = pd.read_parquet(input_path)

    df = df.drop_duplicates()
    df = df.dropna()

    # IQR filtering
    Q1 = df['amount'].quantile(0.25)
    Q3 = df['amount'].quantile(0.75)
    IQR = Q3 - Q1

    df = df[(df['amount'] >= Q1 - 1.5 * IQR) &
            (df['amount'] <= Q3 + 1.5 * IQR)]

    output_path = "data/processed/clean_data.parquet"
    os.makedirs("data/processed", exist_ok=True)
    df.to_parquet(output_path, index=False)

    print("Cleaning done ->", output_path)
    return output_path