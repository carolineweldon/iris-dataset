Analysis of Fisher's Iris Data Set – Caroline Weldon 
GMIT Ireland - Higher Diploma in Data Analytics: Programming & Scripting


Download repository at  https://github.com/carolineweldon/iris-dataset 
Run Code-You will need to install Python, Visual Studio Code and Cmder.
Install Python libraries Pandas, Matplotlib and NumPy.


Background

The objective of this project is to research and explore Fisher's Iris Dataset. The Iris flower data set is a multivariate data set 
introduced by the British statistician and biologist Ronald Fisher in his 1936 paper. This dataset is by far one of the best known and
commonly used datasets in the Data Science. The dataset consists of 50 samples from each of three species of Iris (Setosa, Versicolor 
and Virginica).Four features were measured from each sample: the length and the width of the Sepals and Petals, in centimetres. The 
fifth column is the species names of the flower observed. Based on the combination of these four features, Fisher developed a linear 
discriminant model to distinguish the species from each other, and based on Fisher's linear discriminant model, this data set became a 
typical test case for many statistical classification techniques in machine learning. (Wikipedia)  

CSV File

I downloaded the Iris dataset from github: https://gist.github.com/curran/a08a1080b88344b0c8a7#file-iris-csv 
I saved the file under filename iris_dataset.csv


Analysis 

iris-data.png


![iris-data](https://user-images.githubusercontent.com/47527906/56681090-78537480-66c0-11e9-8668-d0b12069c1c7.PNG)

The code iris-data.py gives us a snapshot of the data and the format of the csv file, with column headings and rows numbered from 0 on.

iris-data-2.png

![iris-data2](https://user-images.githubusercontent.com/47527906/56681485-47c00a80-66c1-11e9-83b0-02999394eaae.PNG)

The code iris-data.py shows us there are 150 rows with 5 columns; 3 species with 50 samples of each.






Results 

The Setosa species has low petal lengths when compared to the other species. This low petal length explains why there was a negative
skew when looking at petal length on boxplot graph. The Setosa flowers also tend to have larger sepal widths when compared to the other 
flowers. On the other hand, Versicolor and Virginica tend to have similar measurements when compared to each other. However, the 
Versicolor flowers tend to have smaller petal lengths and widths than the Virginica flowers. Overall, the measurement that seems to be 
most unique amongth the flowers are their petal lengths. 

References 
https://matplotlib.org/
https://www.kaggle.com/uciml/iris
https://docs.scipy.org/doc/numpy/index.html
https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html

 

