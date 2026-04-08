import pandas as pd

def calculate_risk(df: pd.DataFrame):
    total_spend = df['amount'].sum()
    avg_spend = df['amount'].mean()
    volatility = df['amount'].std()

    score = (
        (volatility / avg_spend) * 40 +
        (total_spend / (avg_spend * len(df))) * 30
    )

    score = min(100, max(0, score))

    return {
        "risk_score": round(score, 2),
        "volatility": float(volatility),
        "avg_spend": float(avg_spend)
    }