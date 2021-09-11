import pandas as pd
import io
import os
import glob
import matplotlib.pyplot as plt



csv_files = glob.glob(os.path.join(f'../data', '*.csv'))

data = []

for f in csv_files:
  file = open(f, 'rb')
  decoder_wrapper = io.TextIOWrapper(file, errors='replace') 
  df = pd.read_csv(decoder_wrapper, skiprows=8)
  data.append(df)

data = pd.concat(data)
data.columns = [
  'timestamp','core0temp','core1temp','core2temp','core3temp','DROP',
  'DROP','core0low_temp','core0high_temp','core0load','core0mhz',
  'DROP','core1low_temp','core1high_temp','core1load','core1mhz',
  'DROP','core2low_temp','core2high_temp','core2load','core2mhz',
  'DROP','core3low_temp','core3high_temp','core3load','core3mhz',
  'power', 'DROP'
]
df = data.drop(['DROP'], axis=1)
df = df[~df.timestamp.str.contains('Session', na=False)]
df.timestamp = pd.to_datetime(df.timestamp, format='%H:%M:%S %m/%d/%y')
df.to_csv('../data/clean.csv')