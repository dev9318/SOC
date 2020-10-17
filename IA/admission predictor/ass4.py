import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset = pd.read_csv('/Users/Dev/Desktop/IA/Admission_Predict.csv')
X = dataset[['GRE Score'    ,'TOEFL Score'	,'University Rating'	,'SOP'	,'LOR' ,'CGPA'	,'Research']].values
Y = dataset['Chance of Admit'].values
regressor = LinearRegression()  
regressor.fit(X, Y)
  
print(regressor.coef_)
