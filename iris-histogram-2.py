#Caroline Weldon 
#Iris Data Set



import pandas as pd
from pandas.plotting import scatter_matrix
import numpy as np
import matplotlib.pyplot as plt 
from numpy.random import randn


iris = pd.read_csv('iris_dataset.csv')

groups = iris.groupby(by = 'species')
means, sds = groups.mean(), groups.std()
means.plot(yerr = sds, kind = 'bar', figsize = (15,20), table = True)

plt.show()