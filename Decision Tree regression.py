#!/usr/bin/env python
# coding: utf-8

# In[16]:


#First reading the data
import numpy as np
import pandas as pd
data=pd.read_csv('Salary Data.csv')
x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values
print(data)


# In[17]:


#Second preprocessing on data: (Cleaning, Encoding, Normalizing, and feature engineering, and balancing 'in classification case')
# 1. Cleaning data 'handling the null values inside data' 
a=data['Salary'].unique()
b=data['Job Title'].nunique()
print(b)
#After checking the unique values inside each colum we found non 'Null' values to handle


# In[18]:


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


# In[49]:


# 3. Normalizing
from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
x[:,0]=np.ravel(ss.fit_transform(x[:,0].reshape(-1,1)))
x[:,4]=np.ravel(ss.fit_transform(x[:,4].reshape(-1,1)))
y=np.ravel(ss.fit_transform(y.reshape(-1,1)))
# 4. Balancing "we won't need it because we use 'regression' here"
# 5. Feature scalling for linear SVM


# In[ ]:





# In[52]:


#Start in applying model
#Split your data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.20,random_state=0)
#Start SVM regression model
#'SVR' it means support vector regression
from sklearn.tree import DecisionTreeRegressor
reg = DecisionTreeRegressor(random_state=10)
reg.fit(x_train,y_train)


# In[53]:


from sklearn.metrics import r2_score
pred=reg.predict(x_test)
p=r2_score(y_test,pred)
print(p)


# In[ ]:




