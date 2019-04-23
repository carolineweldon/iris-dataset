#Caroline Weldon 
#Iris Data Set



import pandas as pd
from pandas.plotting import scatter_matrix
import numpy as np
import matplotlib.pyplot as plt 
from numpy.random import randn


iris = pd.read_csv('iris_dataset.csv')

#corelation visual 
dt = iris[iris.columns]
plt.style.use('ggplot')

plt.imshow(dt.corr(), cmap=plt.cm.Reds, interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(dt.columns))]
plt.xticks(tick_marks, dt.columns, rotation='vertical')
plt.yticks(tick_marks, dt.columns)




plt.show()