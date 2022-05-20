#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# 1. Combine four series to form and create a Dataframe with name series_data. Use the Dataframe and perform following operations.

# In[3]:


s1={'ID':pd.Series([1,2,3,4,5,6,7,8,9,10]),
'name':pd.Series(['jack','peter','john','jim','manual','rose','nik','sam','rim','don']),
'city':pd.Series(['dubai','bangalore','chennai','kochi','pune','paris','kolkata','jaipur','delhi','mumbai']),
'age':pd.Series([23,54,56,32,46,19,32,76,30,58])}
df=pd.DataFrame(s1)
df


# a. Display first five rows and last five rows using pandas method

# In[28]:


df.head()


# In[4]:


df.tail()


#  b.Convert the index of a series into a column of a dataframe.

# In[30]:


df['index']=df.index
df


#  c.Drop the index column of the dataframe.

# In[33]:


df.drop('index', axis = 1)


# d.Display the frequency counts of unique items of a series data.

# In[34]:


df.value_counts()


# 2. How to stack two random series vertically and horizontally?

# In[46]:


s1 = pd.Series(np.random.randint(100,700, 7))
s2 = pd.Series(np.random.randint(10,70, 7))
print(s1)
print(s2)
df=pd.concat([s1,s2],axis=1)               
print(df)


# 3. How to convert a numpy array to a Dataframe of given shape?

# In[47]:


series = {'Column1' : pd.Series(np.random.randint(50,70, 7)),
               'Column2' : pd.Series(np.random.randint(20,40, 7))}
df = pd.DataFrame(series)
df


# 4. Find the index positions of items of series A in another series B using numpy.where() and pd.Index() methods?
# 

# In[2]:


##using numpy.where()
A= [2,6,8,1,4,0,3,8,3,9]
B= [1,6,6,0,4,3,9,8,2,9]
np.where(pd.Series(A)==pd.Series(B))


# In[4]:


##using pd.index()
A= [2,6,8,1,4,0,3,8,3,9]
B= [1,6,6,0,4,3,9,8,2,9]
pd.Index(pd.Series(A)==pd.Series(B))


# 5. How to convert the first character of each Categorical value in a series to uppercase keeping rest of values to lowercase?
# 

# In[49]:


series= pd.Series(['apple','banana','orange','grape']).str.capitalize()
print(series)


# 6. How to filter valid emails from a series data using following pattern to be matched?

# In[5]:


emails = pd.Series(['books at amazom.com', 'james@egypt.com', 'jones@yahoo.in', 'bigdata@gmail.com'])
pattern ='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'
result= emails.str.findall(pattern)
print([i for i in result if len(i)>0])


# 7. Analysing earthquake data using url: https://raw.githubusercontent.com/ammishra08/MachineLearning/master/Datasets/earthquakes_2014.csv
# 

# In[22]:


## a. Create a Datafrme using URL

earth_df = pd.read_csv("https://raw.githubusercontent.com/ammishra08/MachineLearning/master/Datasets/earthquakes_2014.csv", sep=',', 
                        header = 0)
df = pd.DataFrame(earth_df)
df


# In[33]:


## b. Display Info of the Dataframe

df.info()


# In[34]:


## c. Convert time column from object to datetime format [Hint: Use pd.to_datetime()]

df['time'] = pd.to_datetime(df['time'])
df.info()


# In[35]:


## d. Rename columns latitude, longitude, depth, mag to  ‘Lat’, ‘Long’, ‘D, M’ column names.

earth_df=earth_df.rename(columns={'latitude':'Lat','longitude':'Long','depth':'D','mag':'M'})
earth_df


# In[36]:


## e. Find out invalid data (the nan values from missing points)

df.isnull()


# In[37]:


## f. Drop all nan values from the existing data.

df.dropna()


# In[24]:


## g. Replace the invalid data with central tendencies.

earth_df=earth_df[['nst','gap','dmin']]=earth_df[['nst','gap','dmin']].apply(lambda x:x.fillna(x.median()))
earth_df


# 8. Analysing data using url:
# https://raw.githubusercontent.com/ammishra08/MachineLearning/master/Datasets/house_sales_data.csv
# 

# In[11]:


## a. Load the data file
sales_df= pd.read_csv("https://raw.githubusercontent.com/ammishra08/MachineLearning/master/Datasets/house_sales_data.csv")
sales_df


# In[42]:


## b. Sorting the Rows Data using Column ‘price’ and reset index & update the dataframe.

df=sales_df['price'].sort_values()
df.reset_index()


# In[43]:


##c. Slice the rows and columns using iloc row positions 100 to 300 , columns 2 to 9 positions.

sales_df.iloc[100:300,2:9]


# In[44]:


## d. Filter all columns with letter ‘a’ in it.

sales_df.filter(like = 'a')


# In[13]:


## e. Filter the columns with Price > 250000 and the view column is True.

sales_df['price'] > 250000


# In[27]:


## f. Compute the average price of a house with sqft_living  > 25000 and the view column  is True.

df=sales_df.groupby('price')['sqft_living'].mean()> 25000
df


# In[ ]:




