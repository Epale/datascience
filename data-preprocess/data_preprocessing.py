
# Data Preprocessing Template

# Importing the libraries
import numpy as np  
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
# C:\Users\gfoxd\datascience\Data.csv
dataset = pd.read_csv('Data.csv')    
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
 
# print(X)
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

print(X_train)
print(y_train)
print(X_test) 
print(y_test)

