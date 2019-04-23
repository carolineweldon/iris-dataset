#Caroline Weldon 
#Iris Data Set



import pandas as pd
from pandas.plotting import scatter_matrix
import numpy as np
import matplotlib.pyplot as plt 
from numpy.random import randn



iris = pd.read_csv('iris_dataset.csv')



#petal width/petal length scatter plot and sepal/sepal length scatter 

plt.figure()
fig,ax=plt.subplots(1,2,figsize=(17, 9))
iris.plot(x="sepal_length",y="sepal_width",kind="scatter",ax=ax[0],sharex=False,sharey=False,label="sepal",color='r')
iris.plot(x="petal_length",y="petal_width",kind="scatter",ax=ax[1],sharex=False,sharey=False,label="petal",color='b')
ax[0].set(title='Sepal comparasion ', ylabel='sepal_width')
ax[1].set(title='Petal Comparasion',  ylabel='petal_width')
ax[0].legend()
ax[1].legend()

plt.show()



