#Caroline Weldon 
#Iris Data Set

import pandas as pd
from pandas.plotting import scatter_matrix
import numpy as np
import matplotlib.pyplot as plt 
from numpy.random import randn


iris = pd.read_csv('iris_dataset.csv')

#correlation
dt = iris[iris.columns]
corr = dt.corr(method="pearson")
print(corr)