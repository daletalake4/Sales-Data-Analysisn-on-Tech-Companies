#!/usr/bin/env python
# coding: utf-8

# In[38]:



import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import os


# In[39]:


dataset=pd.read_csv("/storage/emulated/0/bluetooth/all_data.csv")


# In[44]:


all_data=dataset


# In[46]:


all_data.head()


# In[47]:


all_data.isnull().sum()


# In[48]:


all_data=all_data.dropna(how='all') 
all_data.shape


# In[49]:


'04/19/19 08:46'.split('/')[0]


# In[50]:


def month(x):
    return x.split('/')[0]


# In[51]:


all_data['month']=all_data['Order Date'].apply(month)


# In[52]:


all_data.head()


# In[53]:


all_data.dtypes


# In[54]:


all_data['month'].unique()


# In[55]:


filter=all_data['month']=='Order Date' 
all_data=all_data[~filter] 
all_data.head()


# In[70]:


all_data['month']=all_data['month'].astype(int) 
all_data.dtypes


# In[71]:


all_data['Quantity Ordered']=all_data['Quantity Ordered'].astype(int)
         
all_data['Price Each']=all_data['Price Each'].astype(float)


# In[72]:


all_data.dtypes


# In[80]:


all_data['sales']=all_data['Quantity Ordered']* all_data['Price Each']


# In[81]:


all_data.head()


# In[82]:


all_data.groupby('month')['sales'].sum()


# In[91]:


months=range(1,13)
plt.bar(months,all_data.groupby('month')['sales'].sum())
plt.xticks(months)
plt.xlabel('Month')
plt.ylabel('Sales in USD')

WHAT PRODUCTS ARE SOLD TOGETHER AND WHY
# In[93]:


all_data.head()


# In[94]:


df=all_data['Order ID'].duplicated(keep=False) 
df2=all_data[df] 
df2.head()


# In[96]:


df2['Grouped']=df2.groupby('Order ID')['Product'].transform(lambda x:','.join(x))


# In[97]:


df2.head()


# In[98]:


df2=df2.drop_duplicates(subset=['Order ID'])
df2.head()


# In[99]:


df2['Grouped'].value_counts()[0:5]. plot.pie()

