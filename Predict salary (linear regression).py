#!/usr/bin/env python
# coding: utf-8

# In[111]:


#First reading the data
import numpy as np
import pandas as pd
data=pd.read_csv('Salary Data.csv')
x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values
print(data)


# In[112]:


#Second preprocessing on data: (Cleaning, Encoding, Normalizing, and feature engineering, and balancing 'in classification case')
# 1. Cleaning data 'handling the null values inside data' 
a=data['Salary'].unique()
b=data['Job Title'].nunique()
print(b)
#After checking the unique values inside each colum we found non 'Null' values to handle


# In[113]:


# 2. Encoding
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#Frist applying 'label encoder' for binary encoding
x[:,1]=LabelEncoder().fit_transform(x[:,1])
x[:,3]=LabelEncoder().fit_transform(x[:,3])
#Second applying 'OneHotencoder' for multi categorical classification
from sklearn.compose import ColumnTransformer
hotencoder=ColumnTransformer([('encoder',OneHotEncoder(),[2])],remainder="passthrough")
x=np.array(hotencoder.fit_transform(x))

print(x)


# In[114]:


# 3. Normalizing
from sklearn.preprocessing import MinMaxScaler
x[[0]]=MinMaxScaler().fit_transform(x[[0]])
x[[4]]=MinMaxScaler().fit_transform(x[[4]])
# 4. Balancing "we won't need it because we use 'regression' here"


# In[115]:


#Start in applying model
#Split your data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.20,random_state=0)
#First applying the 'Single Linear Regression'
from sklearn.metrics import r2_score
def eval_model(model, x, y):
    model.fit(x, y)
    y_pred = model.predict(x)
    r2 = r2_score(y, y_pred)
    return r2

from sklearn.linear_model import LinearRegression
linear_reg = LinearRegression()
#in the next statement we pass our model that we want to apply with the dataset to the 'eval_model' function the printing the accuracy 
tryy=eval_model(linear_reg, x_train, y_train)
print(tryy)
y_r2=eval_model(linear_reg,x_test,y_test)
print(y_r2)


# In[118]:


#Second applying the 'multi linear regression'

from sklearn.preprocessing import PolynomialFeatures
pf = PolynomialFeatures(degree=2)
X_train_poly = pf.fit_transform(x_train)
X_test_poly = pf.fit_transform(x_test)
nonlinear_reg = LinearRegression()

R_squ=eval_model(nonlinear_reg, X_train_poly, y_train)
print(R_squ)
y_pred_test =nonlinear_reg.predict(X_test_poly)
y_r2=r2_score(y_test, y_pred_test)
print(y_r2)


import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
plt.scatter(y_test, y_pred_test, alpha=0.4)
plt.plot([0, 50000], [0, 50000], c='red')
plt.xlabel('y_true')
plt.ylabel('y_pred')
plt.grid(axis='both')
plt.show()


# In[ ]:




