#BUILDING THE MODEL
import numpy as np
import pandas as pd 
import pickle
from statsmodels.tsa.holtwinters import ExponentialSmoothing



df = pd.read_csv('static\AirPassengers.csv')
df.rename(columns = {'#Passengers':'Passengers'}, inplace = True)
df_subset = df[(df['Month'] > '1949-01') & (df['Month'] < '1955-12')]
df_subset['Month'] = pd.to_datetime(df_subset['Month'],infer_datetime_format=True)
df_subset = df_subset.set_index(['Month'])

train=df_subset[:24] 
test=df_subset[24:] 

hwmodel=ExponentialSmoothing(df_subset.Passengers,trend='add', seasonal='mul', seasonal_periods=4).fit()
pickle.dump(hwmodel,open('model.pkl','wb'))