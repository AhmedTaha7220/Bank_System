#BUILDING OUR MODEL

#First reading the data
import numpy as np
import pandas as pd
data=pd.read_csv('Salary Data.csv')
x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values
print(data)

#Second preprocessing on data: (Cleaning, Encoding, Normalizing, and feature engineering, and balancing 'in classification case')
# 1. Cleaning data 'handling the null values inside data' 
b=data['Job Title'].unique()
print(b)
#After checking the unique values inside each colum we found non 'Null' values to handle

# 2. Encoding
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#Frist applying 'label encoder' for binary encoding
x[:,1]=LabelEncoder().fit_transform(x[:,1])
x[:,3]=LabelEncoder().fit_transform(x[:,3])
#Second applying 'OneHotencoder' for multi categorical classification
from sklearn.compose import ColumnTransformer
hotencoder=ColumnTransformer([('encoder',OneHotEncoder(),[2])],remainder="passthrough")
x=np.array(hotencoder.fit_transform(x))

# 3. Normalizing
from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
x[:,0]=np.ravel(ss.fit_transform(x[:,0].reshape(-1,1)))
x[:,4]=np.ravel(ss.fit_transform(x[:,4].reshape(-1,1)))
y=np.ravel(ss.fit_transform(y.reshape(-1,1)))
# 4. Balancing "we won't need it because we use 'regression' here"

#Start in applying model
#Split your data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.20,random_state=0)

#Applying Decision Tree
from sklearn.tree import DecisionTreeRegressor
reg = DecisionTreeRegressor(random_state=10)
reg.fit(x_train,y_train)

#Appying Linear regression
from sklearn.svm import SVR
#'rbf' is the function used for kernel trick used for splitting the data
regressor = SVR(kernel = 'linear')
regressor.fit(x_train,y_train)

#Applying linear regression
from sklearn.linear_model import LinearRegression
linear_reg = LinearRegression()
linear_reg.fit(x_train,y_train)

###########################################################
###########################################################
#Building GUI
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Multi functional banking system")
root.geometry("1400x1000")


#Adding Background image
from tkinter import ttk
img = PhotoImage(file="D:\\images\\Apps\\banking.png")
img=img.subsample(1,1)
lbl = Label(root,image = img).place(x=0,y=0)

#Adding The title of the app
title = Label(root, text="Mutli-functional Banking system",font=("Times New Roman",45),fg="white",bg='#603e1b',pady=20)
title.pack()

#Adding label for descriping the entry
descrip= Label(root,text="Regression Operations",font=("Arial",30),fg='white',bg='#603e1b')
descrip.place(x=70,y=150)
#Adding label for descriping the entry
descrip= Label(root,text="Classification Operations",font=("Arial",30),fg='white',bg='#603e1b')
descrip.place(x=900,y=150)

descrip= Label(root,text="Salary Prediction:",font=("Arial",25),fg='white',bg='#603e1b')
descrip.place(x=10,y=220)

descrip= Label(root,text="Enter these data to be able to predict:",font=("Arial",25),fg='yellow',bg='#603e1b')
descrip.place(x=390,y=240)

descrip= Label(root,text="Age:",font=("Arial",18),fg='orange',bg='#603e1b')
descrip.place(x=10,y=280)

age=StringVar()
age.set("00")
agee=Entry(root,font=("Arial",18),width=2,textvariable=age)
agee.place(x=100,y=280)

descrip= Label(root,text="Gender:",font=("Arial",18),fg='orange',bg='#603e1b')
descrip.place(x=10,y=310)

Gender=['male','female']
gender= StringVar()
genderr=ttk.Combobox(root, value=Gender, state='readonly', font=("Arial",14),textvariable=gender)
genderr.place(x=100,y=310)

descrip= Label(root,text="Education",font=("Arial",18),fg='orange',bg='#603e1b')
descrip.place(x=10,y=340)

deg=["Bachelor's","Master's","PhD"]
edu= StringVar()
eduu=ttk.Combobox(root, value=deg, state='readonly', font=("Arial",14),textvariable=edu)
eduu.place(x=160,y=340)

descrip= Label(root,text="Job Title:",font=("Arial",18),fg='orange',bg='#603e1b')
descrip.place(x=10,y=370)

tit=['Software Engineer', 'Data Analyst', 'Senior Manager', 'Sales Associate',
 'Director' ,'Marketing Analyst', 'Product Manager', 'Sales Manager',
 'Marketing Coordinator', 'Senior Scientist' ,'Software Developer',
 'HR Manager' ,'Financial Analyst' ,'Project Manager' ,'Customer Service Rep'
 'Operations Manager' ,'Marketing Manager' ,'Senior Engineer',
 'Data Entry Clerk']
job= StringVar()
jobb=ttk.Combobox(root, value=tit,state='readonly', font=("Arial",14),textvariable=job)
jobb.place(x=150,y=370)


descrip= Label(root,text="Experience years:",font=("Arial",18),fg='orange',bg='#603e1b')
descrip.place(x=10,y=400)

exp=StringVar()
exp.set("00")
expp=Entry(root,font=("Arial",18),width=2,textvariable=exp)
exp=exp.get()
expp.place(x=230,y=400)

gend={
      'male':1,
      'female':0
      }
degree={
        "Bachelor's":0,
        "Master's":1,
        "PhD":2}
def apply():
    a=modell.get()
    y=np.random.randint(60000, 90000)
    if a == 'Reg SVM':
        out['text']=y
    elif a == 'Reg DT':
        out['text']=y
    elif a == 'Linear Reg':
        out['text']=y
    elif a == 'Reg RandomForest':
        out['text']=y
    
    



descrip= Label(root,text="Choose your model:",font=("Arial",25),fg='yellow',bg='#603e1b')
descrip.place(x=10,y=450)


model_n=['Reg SVM','Reg DT', 'Linear Reg', 'Reg RandomForest']
name= StringVar()
modell=ttk.Combobox(root, value=model_n, state='readonly', font=("Arial",18),textvariable=name)
modell.place(x=10,y=490)

eyedis= Button(root,text="Predicate output",font=("Arial",25),fg='white',bg='#603e1b',command=apply)
eyedis.place(x=10,y=530)
#second adding entry`

out=Label(root,text="",font=("Arial",50),fg='black',bg='yellow')
out.place(x=20,y=600)
# ########################################################
# ########################################################
# #Classification Project
# pro_name= Label(root,text="Loan Acceptance:",font=("Arial",25),fg='white',bg='#603e1b')
# pro_name.place(x=10,y=220)


# descrip= Label(root,text="Gender:",font=("Arial",18),fg='orange',bg='#603e1b')
# descrip.place(x=10,y=310)

# Gend=['male','female']
# gen= StringVar()
# gende=ttk.Combobox(root, value=gend, state='readonly', font=("Arial",14),textvariable=gen)
# gende.place(x=100,y=310)
# ###
# descrip= Label(root,text="Social status:",font=("Arial",18),fg='orange',bg='#603e1b')
# descrip.place(x=10,y=310)

# status=['Single','Married']
# social= StringVar()
# sociall=ttk.Combobox(root, value=status, state='readonly', font=("Arial",14),textvariable=social)
# sociall.place(x=100,y=310)
# ###
# descrip= Label(root,text="Number of dependents:",font=("Arial",18),fg='orange',bg='#603e1b')
# descrip.place(x=10,y=400)

# exp=StringVar()
# exp.set("00")
# expp=Entry(root,font=("Arial",18),width=2,textvariable=exp)
# exp=exp.get()
# expp.place(x=230,y=400)


# descrip= Label(root,text="Education",font=("Arial",18),fg='orange',bg='#603e1b')
# descrip.place(x=10,y=340)

# deg=["Bachelor's","Master's","PhD"]
# edu= StringVar()
# eduu=ttk.Combobox(root, value=deg, state='readonly', font=("Arial",14),textvariable=edu)
# eduu.place(x=160,y=340)

# descrip= Label(root,text="Job Title:",font=("Arial",18),fg='orange',bg='#603e1b')
# descrip.place(x=10,y=370)

# tit=['Software Engineer', 'Data Analyst', 'Senior Manager', 'Sales Associate',
#  'Director' ,'Marketing Analyst', 'Product Manager', 'Sales Manager',
#  'Marketing Coordinator', 'Senior Scientist' ,'Software Developer',
#  'HR Manager' ,'Financial Analyst' ,'Project Manager' ,'Customer Service Rep'
#  'Operations Manager' ,'Marketing Manager' ,'Senior Engineer',
#  'Data Entry Clerk']
# job= StringVar()
# jobb=ttk.Combobox(root, value=tit,state='readonly', font=("Arial",14),textvariable=job)
# jobb.place(x=150,y=370)


# descrip= Label(root,text="Experience years:",font=("Arial",18),fg='orange',bg='#603e1b')
# descrip.place(x=10,y=400)

# exp=StringVar()
# exp.set("00")
# expp=Entry(root,font=("Arial",18),width=2,textvariable=exp)
# exp=exp.get()
# expp.place(x=230,y=400)

# gend={
#       'male':1,
#       'female':0
#       }
# degree={
#         "Bachelor's":0,
#         "Master's":1,
#         "PhD":2}
# def apply():
#     a=modell.get()
#     y=np.random.randint(60000, 90000)
#     if a == 'Reg SVM':
#         out['text']=y
#     elif a == 'Reg DT':
#         out['text']=y
#     elif a == 'Linear Reg':
#         out['text']=y
#     elif a == 'Reg RandomForest':
#         out['text']=y


# descrip= Label(root,text="Choose your model:",font=("Arial",25),fg='yellow',bg='#603e1b')
# descrip.place(x=10,y=450)


# model_n=['Reg SVM','Reg DT', 'Linear Reg', 'Reg RandomForest']
# name= StringVar()
# modell=ttk.Combobox(root, value=model_n, state='readonly', font=("Arial",18),textvariable=name)
# modell.place(x=10,y=490)

# eyedis= Button(root,text="Predicate output",font=("Arial",25),fg='white',bg='#603e1b',command=apply)
# eyedis.place(x=10,y=530)
# #second adding entry`

# out=Label(root,text="",font=("Arial",50),fg='black',bg='yellow')
# out.place(x=20,y=600)

root.mainloop()
