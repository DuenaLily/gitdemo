#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[7]:


##1.
arr_1=np.arange(1,10).reshape(3,3)
arr_2=np.arange(11,20).reshape(3,3)
arr_1
arr_2
np.concatenate((arr_1,arr_2),axis=1)


# In[11]:


##2.
a = np.random.randint(100, size = (5))
print(a)


# In[16]:


##3.
a = np.random.randint(5, 10, size = (5,3,2))
a


# In[8]:


##4.
import random
def random_array(n):
    a=random.sample(range(1,50),n)
    print(a)
random_array(random.randint(1,10))


# In[11]:


##5.
#using python
import statistics
arr=[10, 60, 50, 30, 70, 20]
print("arr:",arr)
print("median of arr: %s" %(statistics.median(arr)))


#using numpy
arr=[10, 60, 50, 30, 70, 20]
print("arr:",arr)
print("median of arr:",np.median(arr))


# In[36]:


##6.
import statistics
arr_1=[10, 60, 50, 30, 70, 20]
result=statistics.variance(arr_1)
print("variance of arr: %s" %(result))
result1=statistics.mean(arr_1)
print("mean of arr: %s" %(result1))


# In[41]:


##7.
arr=np.arange(0,10)
print(arr)
arr_1=np.reshape(arr,(2,5))
print(arr_1)


# In[45]:


##8.
##vstack() is used to stack arrays in sequence vertically
arr1=np.arange(0,9).reshape(3,3)
arr2=np.arange(10,19).reshape(3,3)
result=np.vstack((arr1,arr2))
print(result)


# In[48]:


##9.
arr_3=np.arange(0,5)
arr_4=np.arange(2,7)
print("coomon values between arr_3 and arr_4:")
print(np.intersect1d(arr_3,arr_4))


# In[125]:


##10.
arr_1=np.array([2,6,8,1,4,0,3,8,3,9])
arr_2=np.array([1,6,6,0,4,3,9,8,2,9])
np.where(arr_1==arr_2)


# In[85]:


##11.
a=np.random.uniform(5,10,4).reshape(2,2)
a
               


# In[51]:


##12.
iris_df=pd.read_csv("https://raw.githubusercontent.com/ammishra08/MachineLearning/master/Datasets/iris.csv")
display(iris_df)

np.genfromtxt(iris_df['species'])


# In[103]:


##13.
iris_df.iloc[1:,:4]


# In[106]:


##14.
iris_df.agg(['mean', 'median','std'])


# In[108]:


##15
admission_df=pd.read_csv("https://raw.githubusercontent.com/ammishra08/MachineLearning/master/Datasets/Admission.csv")
display(admission_df)


# In[111]:


def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))
scaled_x = NormalizeData(admission_df)
print(scaled_x)


# In[131]:


##16.
iris_df['sepal_length'].isnull()


# In[126]:


##17.
x=np.genfromtxt('https://raw.githubusercontent.com/ammishra08/MachineLearning/master/Datasets/iris.csv',delimiter='')
print(x)


# In[127]:


##18.
admission_df['TOEFL Score'].sort_values()


# In[128]:


admission_df['GRE Score'].sort_values()


# In[2]:


##19.


# In[141]:


##20
arr_1=np.array([2,6,7,8,6,2,1,5,8])
def duplicates(arr_1):
    return[element in arr_1[:i] for i, element in enumerate(arr_1)]
result= duplicates(arr_1)
print(result)


# In[148]:


##21
df=pd.DataFrame(admission_df)
df=df.replace(np.nan,0)
df


# In[149]:


df=pd.DataFrame(iris_df)
df=df.replace(np.nan,0)
df


# In[ ]:




