import pandas as pd
import numpy as np
from operator import eq

df1=pd.read_csv('/home/amulya/Downloads/accident_2015.csv')
df2=pd.read_csv('/home/amulya/Downloads/accident_2016.csv')
desred_decimals = 3    
df1['LATITUDE']=df1['LATITUDE'].apply(lambda x: round(x,desred_decimals))
df1['LONGITUD']=df1['LONGITUD'].apply(lambda x: round(x,desred_decimals))
df2['LATITUDE']=df2['LATITUDE'].apply(lambda x: round(x,desred_decimals))
df2['LONGITUD']=df2['LONGITUD'].apply(lambda x: round(x,desred_decimals))
roads=pd.read_csv('/home/amulya/Downloads/road_data - Sheet1.csv')
k=list(roads['Road'])
print(df1['TWAY_ID'])
#print(k)
c=0
c1=0
for s in range(0,df1['TWAY_ID'].count()):  
  if df1['TWAY_ID'][s] in k  :   
      c+=1
  else :
      df1.drop(s,inplace=True)

         
    
    
    
    
df1.to_csv('/home/amulya/Downloads/accident-2015-cleaned.csv', sep=',', encoding='utf-8')
# Dropping elements from the second column
for s1 in range(0,df2['TWAY_ID'].count()): 
  #print(df1['TWAY_ID'][s])  
  if df2['TWAY_ID'][s1] in k  :
      c+=1
  else :
   df2.drop(s1,inplace=True)
df2.to_csv('/home/amulya/Downloads/accident-2016-cleaned.csv', sep=',', encoding='utf-8')
 