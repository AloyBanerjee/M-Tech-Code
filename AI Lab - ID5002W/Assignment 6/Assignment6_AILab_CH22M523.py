#!/usr/bin/env python
# coding: utf-8

# In[139]:


import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import GridSearchCV


# In[127]:


#Change the working directory 
os.chdir('C://Users//kunta//Desktop//M.Tech//Trimester 2//AI Lab//Assignmnt//4//Datasets_assgnmnt4//Datasets//Datasets')
#Load the data
my_file = pd.read_csv('ch22m5 (23).csv')


# In[128]:


#Display the data
display(my_file.describe())


# In[129]:


#Check if any null value present
my_file.isnull().isna().values.any()


# In[130]:


#Take the input and label data in the x, y variable
y = my_file[['y']]
x = my_file.drop('y', axis=1) 


# In[131]:


# unique vaues present in y
np.unique(y)


# In[132]:


#Standardize the input data
stadardize_x=StandardScaler().fit_transform(x)


# In[133]:


#Split the data into train and test
X_train, X_test, Y_train, Y_test= train_test_split(stadardize_x, y, test_size=0.2, random_state=22)


# In[134]:


print("Shape of X_train: ",X_train.shape[0])
print("Shape of X_test: ",X_test.shape[0])
print("Shape of Y_train: ",Y_train.size)
print("Shape of Y_test: ",len(Y_test))


# In[142]:


#Check the best parameter for C and gamma
params = {
    'C': [0.1, 1, 10, 100, 1000],
    'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
    'kernel': ['rbf']
}

clf = GridSearchCV(
    estimator=SVC(),
    param_grid=params,
    cv=5,
    n_jobs=5,
    verbose=1
)

clf.fit(X_train, np.ravel(Y_train))
print(clf.best_params_)


# In[146]:


svm_rbf = svm.SVC(kernel="rbf", C=10, gamma = 0.01, probability=True)
svm_rbf.fit(X_train, np.ravel(Y_train))


# In[147]:


y_pred_svm_rbf = svm_rbf.predict(X_test)


# In[149]:


acc_svm_rbf = accuracy_score(Y_test, y_pred_svm_rbf)
roc_auc_svm_rbf = roc_auc_score(Y_test, y_pred_svm_rbf,multi_class='ovr')
print(f"Accuracy (RBF Kernel): {acc_svm_rbf:.4f}")
print(f"ROC-AUC (RBF Kernel): {roc_auc_svm_rbf:.4f}")


# In[ ]:




