from prophet import Prophet
import pandas as pd

def run_prophet(df):
    data = df[['date', 'amount']].rename(columns={
        'date': 'ds',
        'amount': 'y'
    })

    model = Prophet()
    model.fit(data)

    future = model.make_future_dataframe(periods=30)
    
    forecast = model.predict(future)  

    forecast = forecast[['ds', 'yhat']].tail(30)

    # Fix negative values
    forecast['yhat'] = forecast['yhat'].apply(lambda x: max(50, x))

    return forecast