import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn import preprocessing,svm,cross_validation
from sklearn.linear_model import LinearRegression
style.use('ggplot')
#data visualisation
df = pd.read_csv('train.csv')
df['avg_T']=(df['T1']+df['T2']+df['T3']+df['T4']+df['T7']+df['T8']+df['T9'])/7
df['avg_RH']=0
for i in range(1,10):
    if(i==5 or i==6):
        continue
    h='RH_'+str(i)
    df['avg_RH']+=df[h]
df['avg_RH']/=7
print(df.head())

x=np.array(df['avg_T'])
a=np.array(df['avg_RH'])
z=np.array(df['Energy'])

w=np.array(df['Tdewpoint'])
df['avg']=(df['avg_T']+df['avg_RH'])/2
v=np.array(df['avg'])

plt.scatter(z,a,label='rh', color='k', s=10, marker=".")
plt.scatter(z,x,label='temp', color='r', s=10, marker=".")
plt.scatter(z,v,label='th', color='g', s=10, marker=".")
plt.scatter(z,w,label='temp', color='y', s=10, marker=".")
#drop the columns Tdewpoint,T6,
X=np.array(df.drop(['Energy','T6','Tdempoint','Observation'],1))
X=preprocessing.scale(X)
y=np.array(df['Energy'])
forecast_out=int(math.ceil(0.01*len(df)))
clf=LinearRegression(n_jobs=-1)
clf.fit(X,y)

df1 = pd.read_csv('test.csv')
X_lately = np.array(df1.drop(['Observation'],1))
forecast_set = clf.predict(X_lately)


plt.show()