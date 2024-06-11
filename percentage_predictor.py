#!/usr/bin/python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model as lm

# Importing and Reading the file
data = pd.read_csv('https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv')

# Plotting the data points
plt.scatter(data.Hours, data.Scores)
plt.xlabel("Hours")
plt.ylabel("Scores")

# Defining coordinates
x = data['Hours'].values.reshape(-1, 1)  # Reshape x to a 2D array
y = data['Scores'].values

# Creating Linear Regression object 
reg = lm.LinearRegression()

# Fitting the data
reg.fit(x, y)

# Plotting the regression line
plt.plot(x, reg.predict(x), color='red', label='Regression Line')
plt.legend()

# Show plot
plt.show()

#Predicting the values
x_new = np.array([9.25]).reshape(-1,1)
y_pred = reg.predict(x_new)

#Plotting Predicted values
plt.scatter(x_new,y_pred , color='green',label ='predicted value')
plt.xlabel("Hours")
plt.ylabel("Scores")
plt.show()

#Printing the value
print("Predicted value",y_pred)