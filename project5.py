# -*- coding: utf-8 -*-
"""Untitled18.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pT_Q7Cga3touEwAgBoCwqWL0M87a58Og
"""

#from google.colab import files
#a=files.upload()

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv("Project4.csv")
data.head(6)

x=data.iloc[:,1].values
y=data.iloc[:,2].values

x=x.reshape(-1,1)
y=y.reshape(-1,1)

reg=RandomForestRegressor(n_estimators=10000,random_state=0)
reg.fit(x,y)

pred_y=reg.predict(x)

x_grid=np.arange(min(x),max(x),0.01)
x_grid=x_grid.reshape(len(x_grid),1)
plt.scatter(x,y,color="blue")
plt.plot(x_grid,reg.predict(x_grid),color="red")
plt.xlabel("level")
plt.ylabel("salary")
plt.title("Salary prediction using Randomforest Algo")
plt.show()



