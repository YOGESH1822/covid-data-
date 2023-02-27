#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


from sklearn.impute import SimpleImputer


# In[ ]:





# In[ ]:





# In[6]:


df=pd.read_csv('D:/CODING/PYTHON DATA SCIENCE/archive/country_wise_latest.csv')


# In[7]:


df.head()


# In[8]:


df.head(10)


# In[9]:


df.rename(columns={'Country/Region':'Country'})


# In[10]:


df.describe()


# In[11]:


df.info()


# In[12]:


df=df.fillna('NA')


# In[ ]:





# In[14]:


df.info()


# In[15]:


df.head(10)


# In[17]:


df2=df.groupby('Country/Region')[['Country/Region','Confirmed']].sum().reset_index()


# In[19]:


df2.head(10)


# In[20]:


import matplotlib.pyplot as plt


# In[21]:


x=np.linspace(0,10,1000)
y=np.sin(x)
plt.plot(x,y)


# In[22]:


plt.scatter(x,y)


# In[23]:


plt.scatter(x[:30],y[:30])


# In[25]:


plt.scatter(x[:30],y[:30],color='red')


# In[26]:


plt.plot(x,y,color='b')
plt.plot(x,np.cos(x),color='g')


# In[28]:


countries=df['Country/Region'].unique()
len(countries)


# In[29]:


for idx in range(0,len(countries)):    
    C = df[df['Country/Region']==countries[idx]].reset_index()        
    plt.scatter(np.arange(0,len(C)),C['Confirmed'],color='blue',label='Confirmed')
    plt.scatter(np.arange(0,len(C)),C['Recovered'],color='green',label='Recovered')
    plt.scatter(np.arange(0,len(C)),C['Deaths'],color='red',label='Deaths')
    plt.title(countries[idx])
    plt.xlabel('Days since the first suspect')
    plt.ylabel('Number of cases')
    plt.legend()
    plt.show()


# In[36]:


df4 = df.groupby(['Deaths'])[['Confirmed','Recovered']].sum().reset_index()


# 

# In[37]:


C = df4
plt.scatter(np.arange(0,len(C)),C['Confirmed'],color='blue',label='Confirmed')
plt.scatter(np.arange(0,len(C)),C['Recovered'],color='green',label='Recovered')
plt.scatter(np.arange(0,len(C)),C['Deaths'],color='red',label='Deaths')
plt.title('World')
plt.xlabel('Days since the first suspect')
plt.ylabel('Number of cases')
plt.legend()
plt.show()


# In[ ]:




