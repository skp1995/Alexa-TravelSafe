import pandas as pd
from operator import eq
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

df1=pd.read_csv('/home/amulya/Downloads/accident-2015-cleaned.csv')
df2=pd.read_csv('/home/amulya/Downloads/accident-2016-cleaned.csv')
roads=pd.read_csv('/home/amulya/Downloads/road_data - Sheet1.csv')
lis=[]

for index, row in df1.iterrows():
  for k in range(0,roads['Road'].count()):  
   if eq(row['TWAY_ID'],roads['Road'][k]) :
      k=roads['Normalized Value'][k]*100+row['FATALS']*2+row['DRUNK_DR']
      lis.append([row['ST_CASE'],k])
     
for index, row in df2.iterrows():
  for k in range(0,roads['Road'].count()):  
   if eq(row['TWAY_ID'],roads['Road'][k]) :
      k=roads['Normalized Value'][k]*100+row['FATALS']*2+row['DRUNK_DR']
      lis.append([row['ST_CASE'],k])
      
df=pd.DataFrame(lis)
df.to_csv('/home/amulya/Downloads/fianl-val.csv', sep=',', encoding='utf-8')      