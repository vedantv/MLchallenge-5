import pandas as pd
import math

df = pd.read_csv('train.csv')
print(len(df))
df['avg_T']=(df['T1']+df['T2']+df['T3']+df['T4']+df['T5']+df['T6']+df['T7']+df['T8']+df['T9'])/9
df['avg_T']=df['avg_T']-df['T_out']
df['avg_RH']=0
for i in range(1,10):
    h='RH_'+str(i)
    df['avg_RH']+=df[h]
print(df.head())
