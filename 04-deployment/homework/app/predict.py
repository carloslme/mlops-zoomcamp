import pickle

import numpy as np
import pandas as pd
from fastapi import FastAPI, HTTPException, status

app = FastAPI(title='Yellow Taxi Trip Records Prediction')

with open('model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)
categorical = ['PULocationID', 'DOLocationID']

def read_data(year:str, month:str):
    df = pd.read_parquet(f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-0{month}.parquet')
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60
    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()
    print(df.columns)
    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df


@app.get("/", status_code=200)
async def healthcheck():
    return "NYC classifier is all ready to go!"


@app.post("/predict", tags=["time"], status_code=status.HTTP_200_OK)
def predict(year:str, month: str):
    if (len(year) != 4) or (len(month) != 1):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="The arguments are invalid, please use this format year=2022 month=01" )
    df = read_data(year, month)
    
    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_pred = model.predict(X_val)
    return (f"Mean predict value for the year {year} and month {month} is {np.mean(y_pred):.1f}")
