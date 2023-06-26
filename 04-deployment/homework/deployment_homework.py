import sys

import numpy as np
import pandas as pd
import pickle

with open('model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)

categorical = ['PULocationID', 'DOLocationID']

def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df

year = int(sys.argv[1])
month = int(sys.argv[2])

df = read_data(f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-0{month}.parquet')

dicts = df[categorical].to_dict(orient='records')
X_val = dv.transform(dicts)
y_pred = model.predict(X_val)

# Calculate the standard deviation
std_dev = np.std(y_pred)

# Print the result
print("Standard Deviation:", std_dev)

mean = np.mean(y_pred)

# Print the mean
print("Mean:", mean)

df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')

df['predictions'] = y_pred

df_result = df[['ride_id','predictions']].copy()

output_file = 'data/df_result.parquet'

df_result.to_parquet(
    output_file,
    engine='pyarrow',
    compression=None,
    index=False
)


