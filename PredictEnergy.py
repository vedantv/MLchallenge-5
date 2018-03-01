import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
###data visualisation
df = pd.read_csv('train.csv')
df['avg_T']=(df['T1']+df['T2']+df['T3']+df['T4']+df['T5']+df['T6']+df['T7']+df['T8']+df['T9'])/9
df['avg_T']
df['avg_RH']=0
for i in range(1,10):
    h='RH_'+str(i)
    df['avg_RH']+=df[h]
df['avg_RH']/=9
print(df.head())

x=np.array(df['avg_T'])
y=np.array(df['avg_RH'])
z=np.array(df['Energy'])
w=np.array(df['Tdewpoint'])
plt.scatter(z,y,label='rh', color='k', s=10, marker="o")
plt.scatter(z,x,label='temp', color='r', s=10, marker="x")
plt.scatter(x,y,label='th', color='g', s=10, marker=".")
plt.scatter(z,w,label='temp', color='y', s=10, marker=".")
plt.show()