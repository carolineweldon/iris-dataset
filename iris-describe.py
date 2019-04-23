#Caroline Weldon 
#Iris Data Set



import pandas as pd
from pandas.plotting import scatter_matrix
import numpy as np
import matplotlib.pyplot as plt 
from numpy.random import randn


iris = pd.read_csv('iris_dataset.csv')


#description of the data set 
print(iris.describe())

#description of the data by species
setosa=iris[iris['species']=='setosa']
versicolor =iris[iris['species']=='versicolor']
virginica =iris[iris['species']=='virginica']

print("seretosa", setosa.describe())
print("versicolor", versicolor.describe())
print("virginica", virginica.describe())