# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 16:31:37 2020

@author: Selman
"""

""" Libraries """
#Installing Libraries
import pandas as pd
""" Libraries End"""

""" Code Section """
#Data Preprocessing

#Data Upload
data = pd.read_csv('file_name.csv') #if the file is in the same directory (Windows - Mac - Linux)
data = pd.read_csv('Users/username/.../file_name.csv') #if the file is in the a different directory (Mac)
data = pd.read_csv('C:\\Users\...\file_name.csv') #if the file is in the a different directory (Windows)
data = pd.read_csv('home/users/.../file_name.csv') #if the file is in the a different directory (Linux)
print(file_name)

#Accessing data in DataFrame format
var_name = data[['column_name']]
print(var_name)
# || 
var_name_2 = data.iloc[ :, starting_column_index : end_column_index].values
print(var_name_2)

#Divide by Training and Test Data
from sklearn.model_selection import train_test_split
x_train, x_test, y_tarin, y_test = train_test_split(independent_var, dependent_var, test_size = 0.33, random_state = 0)

# Attribute Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)

Y_train = sc.fit_transform(y_train)
Y_test = sc.fit_transform(y_test) 

""" Code Sectio End"""
