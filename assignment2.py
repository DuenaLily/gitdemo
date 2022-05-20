#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Disable the warnings
import warnings
warnings.filterwarnings('ignore')


# In[2]:


zomato_restaurants = pd.read_csv("D:/zomato_restaurants.csv")
zomato_restaurants


# In[4]:


##a.
zomato_restaurants['name'].value_counts()


# In[ ]:


##b.
plt.figure(figsize = (8,8))
plt.pie(zomato_restaurants['online_order'].value_counts(), labels = zomato_restaurants['online_order'].unique(), autopct='%1.2f%%', explode = [0,0,])
plt.legend()
plt.show()


# In[53]:


##c.
zomato_restaurants.rest_type.value_counts().plot(kind='barh',figsize= (16,10))


# In[3]:


##d.
plt.figure(figsize = (8,8))
plt.pie(zomato_restaurants['book_table'].value_counts(), labels = zomato_restaurants['book_table'].unique(), autopct='%1.2f%%', explode = [0,0,])
plt.legend()
plt.show()


# In[14]:


##e.
zomato_restaurants=zomato_restaurants.replace(',','',regex=True)
zomato_restaurants['approx_cost(for two people)'].hist(bins=15,figsize=(35,10),color='darkorchid')
plt.title("Historam Plot of cost", fontsize = 12)
plt.xlabel("approx_cost(for two people)")
plt.ylabel("Frquency (in Range)")
plt.show()


# In[5]:


##box plot
sns.boxplot(x='approx_cost(for two people)',y='votes' ,data=zomato_restaurants)


# In[4]:


##f.
zomato_restaurants=zomato_restaurants.replace(',','',regex=True)
zomato_restaurants['rate'].hist(bins=50,figsize=(35,10),color='darkorchid')
plt.title("rate", fontsize = 12)
plt.xlabel("Rate")
plt.ylabel("Frquency (in Range)")
plt.show()


# In[6]:


##boxplot
sns.boxplot(x='rate',y='votes', data=zomato_restaurants)


# In[23]:


##g.

plt.bar(x = zomato_restaurants['online_order'],height=zomato_restaurants['approx_cost(for two people)'],width=1.6,color='orangered')
plt.title("Bar plot", fontsize = 12)
plt.xlabel("online_order")
plt.ylabel("approx_cost(for two people)")
plt.legend()
plt.show()


# In[31]:


##h.
plt.figure(figsize=(11,8))
sns.distplot(zomato_restaurants['approx_cost(for two people)'], color = 'deeppink')


# In[33]:


##i.
plt.style.use('ggplot')
sns.lmplot(x = 'votes', y = 'votes', hue = 'online_order', height = 8, data = zomato_restaurants)


# In[35]:


##j
zomato_restaurants.rest_type.value_counts().plot(kind='barh',figsize= (12,8))
zomato_restaurants.head(20)


# In[36]:


##k.
zomato_restaurants.location.value_counts().plot(kind='barh',figsize= (12,8))
zomato_restaurants.head(20)


# In[ ]:




