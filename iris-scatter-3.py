#Caroline Weldon 
#Iris Data Set



import pandas as pd
from pandas.plotting import scatter_matrix
import numpy as np
import matplotlib.pyplot as plt 
from numpy.random import randn

iris = pd.read_csv('iris_dataset.csv')


#description of the data by species
setosa=iris[iris['species']=='setosa']
versicolor =iris[iris['species']=='versicolor']
virginica =iris[iris['species']=='virginica']
#petal width/petal length scatter plot and sepal/sepal length scatter 

#scatter for each Species petal width/petal length scatter plot and sepal/sepal length scatter 

plt.figure()
fig,ax=plt.subplots(1,2,figsize=(21, 10))

setosa.plot(x="sepal_length", y="sepal_width", kind="scatter",ax=ax[0],label='setosa',color='r')
versicolor.plot(x="sepal_length",y="sepal_width",kind="scatter",ax=ax[0],label='versicolor',color='b')
virginica.plot(x="sepal_length", y="sepal_width", kind="scatter", ax=ax[0], label='virginica', color='g')

setosa.plot(x="petal_length", y="petal_width", kind="scatter",ax=ax[1],label='setosa',color='r')
versicolor.plot(x="petal_length",y="petal_width",kind="scatter",ax=ax[1],label='versicolor',color='b')
virginica.plot(x="petal_length", y="petal_width", kind="scatter", ax=ax[1], label='virginica', color='g')

ax[0].set(title='Sepal comparasion ', ylabel='sepal_width')
ax[1].set(title='Petal Comparasion',  ylabel='petal_width')
ax[0].legend()
ax[1].legend()
plt.show()