import pandas as pd
import numpy as np

def rank(lat,lon,path):

    prev_data= pd.read_csv(path)
    lat=round(lat,2)
    lon=round(lon,2)
    lis=[]
    for index,row in prev_data.iterrows():
     if lat in row['LATITUDE'] and lon in row['LONGITUD'] :
       lis.append(row['Rank'])
       
    if round(np.mean(lis))>3:
       return 3
    else :
       return  round(np.mean(lis))