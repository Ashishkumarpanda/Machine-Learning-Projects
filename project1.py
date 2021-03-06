# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RO1sHrUkGABRcGD51RDCKbczYof0gWBI
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data=pd.read_csv("Project1.csv")
data

x=data.iloc[:,0].values

y=data.iloc[:,1].values

x=x.reshape(-1,1)
y=y.reshape(-1,1)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.25, random_state=42)

lin=LinearRegression()
lin.fit(x_train,y_train)

pred_y=lin.predict(x_test)

plt.scatter(x_train,y_train,color='green')
plt.plot(x_train,lin.predict(x_train),color='red')
plt.xlabel("Year Of experience")
plt.ylabel("Salary")
plt.title("Salary on basis of experience plot")
plt.show()
