import pandas as pd
import matplotlib.pyplot as plt
import os

def run_eda(input_path: str):
    df = pd.read_parquet(input_path)

    os.makedirs("outputs/charts", exist_ok=True)

    # Monthly spend
    df['month'] = df['date'].dt.to_period('M')
    monthly = df.groupby('month')['amount'].sum()

    plt.figure()
    monthly.plot()
    plt.title("Monthly Spending")
    plt.savefig("outputs/charts/monthly_spend.png")

    # Category spend
    category = df.groupby('category')['amount'].sum()

    plt.figure()
    category.plot(kind='bar')
    plt.title("Category Spending")
    plt.savefig("outputs/charts/category_spend.png")
    
    # Detect anomalies
    threshold = df['amount'].mean() + 2 * df['amount'].std()
    anomalies = df[df['amount'] > threshold]
    anomalies.to_csv("outputs/anomalies.csv", index=False)
    print(f" {len(anomalies)} anomalies detected")

    print(" EDA charts generated")