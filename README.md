**Analysis of Fisher's Iris Data Set – Caroline Weldon** 

**GMIT Ireland - Higher Diploma in Data Analytics: Programming & Scripting**


[Project 2019.pdf](https://github.com/carolineweldon/iris-dataset/files/3120707/Project.2019.pdf)


Download repository at  https://github.com/carolineweldon/iris-dataset 

**Run Code**-You will need to install Python, Visual Studio Code and Cmder.
Install Python libraries Pandas, Matplotlib and NumPy.


**Background**

*Iris Flower* 


![iris_flower](https://user-images.githubusercontent.com/47527906/56797984-d8a3fc80-680d-11e9-9090-764aed565f00.jpg)

The objective of this project is to research and explore Fisher's Iris Dataset. The Iris flower data set is a multivariate data set 
introduced by the British statistician and biologist Ronald Fisher in his 1936 paper. This dataset is by far one of the best known and
commonly used datasets in the Data Science. The dataset consists of 50 samples from each of three species of Iris (Setosa, Versicolor 
and Virginica).Four features were measured from each sample: the length and the width of the Sepals and Petals, in centimetres. The 
fifth column is the species names of the flower observed. Based on the combination of these four features, Fisher developed a linear 
discriminant model to distinguish the species from each other, and based on Fisher's linear discriminant model, this data set became a 
typical test case for many statistical classification techniques in machine learning. (Wikipedia)  

**CSV File**

I downloaded the Iris dataset from github: https://gist.github.com/curran/a08a1080b88344b0c8a7#file-iris-csv 
I saved the file under filename iris_dataset.csv


**Analysis** 

**iris-data.png**


![iris-data](https://user-images.githubusercontent.com/47527906/56681090-78537480-66c0-11e9-8668-d0b12069c1c7.PNG)

The code iris-data.py gives us a snapshot of the data and the format of the csv file, with column headings and rows numbered from 0 on.

**iris-data-2.png**

![iris-data2](https://user-images.githubusercontent.com/47527906/56681485-47c00a80-66c1-11e9-83b0-02999394eaae.PNG)

The code iris-data.py shows us there are 150 rows with 5 columns; 3 species with 50 samples of each.

**iris-describe.png**


![iris-describe](https://user-images.githubusercontent.com/47527906/56682540-a7b7b080-66c3-11e9-9e29-19078387669f.PNG)


The program iris-describe.py outputs a summary of each attribute. This includes mean, standard deviation, min values and max values for
all species and for each species separately. 

**iris-scatter.png** 

![iris-scatter](https://user-images.githubusercontent.com/47527906/56682788-33c9d800-66c4-11e9-942f-558ae0ea60ee.png)

iris-scatter.py looks at the interactions between all pairs of attributes. The diagonal grouping of some pairs of attributes suggest a high correlation and  predicable relationship

**iris-scatter-2.png**

![iris-scatter-2](https://user-images.githubusercontent.com/47527906/56683271-11848a00-66c5-11e9-9344-d7170ef05581.png)

iris-scatter-2.py suggest a high correlation between petal length and petal width. Clearly these two values increase together otherwise we would have very long but rather thin petals or very short but rather wide petals.

**iris-scatter-3.png**


![iris-scatter-3](https://user-images.githubusercontent.com/47527906/56683494-92dc1c80-66c5-11e9-970e-ee392320297a.png)

iris-scatter-3.py splits iris flower into each species. The scatter plot of petal length and petal width shows a distinct difference 
between Setosa compared to the other species. Setosa is very distinct fom the other two species in term of sepal length and sepal width, but versicolor and virginica seem to mix into each other.

**iris-histogram.png**

![iris-histogram](https://user-images.githubusercontent.com/47527906/56798208-43553800-680e-11e9-9b85-045bf684e28a.png)

**iris-histogram-2.png** *(note error of my scale in python script - could not figure out how to rescale correctly)*

![iris-histogram-2](https://user-images.githubusercontent.com/47527906/56798706-3a189b00-680f-11e9-99ea-48340e7fb3e2.png)



**iris-correlation.png**


![iris-correlation](https://user-images.githubusercontent.com/47527906/56798576-ec039780-680e-11e9-8fbc-1e8265ec1025.PNG)

**iris-correlation-2.png** *(Error in my scale of graph)*


![iris-correlation-2](https://user-images.githubusercontent.com/47527906/56798788-68967600-680f-11e9-835c-526f9744791c.png)

**iris-boxplot.png**

![iris-boxplot](https://user-images.githubusercontent.com/47527906/56798882-a398a980-680f-11e9-8553-cab0d95a2854.png)

**iris-boxplot-2.png**


![iris-boxplot-2](https://user-images.githubusercontent.com/47527906/56798999-e2c6fa80-680f-11e9-8897-9dc326a0a88b.png)













**Results** 

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

 

