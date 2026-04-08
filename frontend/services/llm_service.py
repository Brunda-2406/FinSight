import json
import os
from dotenv import load_dotenv
from groq import Groq

# Load env
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_insights(risk_path, forecast_path):
    try:
        with open(risk_path, "r") as f:
            risk = json.load(f)

        with open(forecast_path, "r") as f:
            forecast = json.load(f)

        prompt = f"""
You are a financial advisor AI.

User Financial Data:
Risk Score:
{risk}

Forecast (next days):
{forecast[:10]}

Tasks:
1. Explain financial health
2. Identify risks
3. Highlight spending patterns
4. Give 3 actionable recommendations

Keep it simple and clear.
"""

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",   # 🔥 best free model
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"