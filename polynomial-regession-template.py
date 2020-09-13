# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 00:30:57 2020

@author: Selman
"""

""" Libraries """
#Installing Libraries
import pandas as pd
import matplotlib.pyplot as plt
""" Libraries End"""

""" Code Section """
#Data Upload
data = pd.read_csv('file_name.csv')

#DataFrame Slicing
x = data.iloc[:, 1:2]
y = data.iloc[:, 2:]

#NumPy Transform
X = x.values
Y = y.values

#Linear Regression
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X, Y)

#Polynomial Regression - Degree = 2
from sklearn.preprocessing import PolynomialFeatures
pr = PolynomialFeatures(degree = 2)
x_p = pr.fit_transform(X)
lr_2 = LinearRegression()
lr_2.fit(x_p, y)

#Polynomial Regression - Degree = 4
from sklearn.preprocessing import PolynomialFeatures
pr_2 = PolynomialFeatures(degree = 4)
x_p_2 = pr_2.fit_transform(X)
lr_3 = LinearRegression()
lr_3.fit(x_p_2, y)

#Visualization
    #Linear Reg.
plt.scatter(X, Y, color = 'brown')
plt.plot(x, lr.predict(X), color = 'blue')
plt.show()
    
    #Polynomial Reg.
plt.scatter(X, Y, color = 'brown')
plt.plot(x, lr_2.predict(pr.fit_transform(X)), color = 'blue')
plt.show()

plt.scatter(X, Y, color = 'brown')
plt.plot(x, lr_3.predict(pr_2.fit_transform(X)), color = 'blue')
plt.show()