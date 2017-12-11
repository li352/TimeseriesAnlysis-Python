
# coding: utf-8

# In[5]:

import numpy as np
import pandas as pd
import os
os.getcwd()
os.chdir('Desktop')


# In[6]:

data=pd.read_csv('raw_data.csv')


# In[8]:

data.head()


# In[9]:

type(data.t)


# In[10]:

type(data.t[5])


# In[13]:

data1=pd.read_csv('raw_data.csv', parse_dates=["t"])


# In[14]:

data1.head()


# In[15]:

type(data.t[5])


# In[17]:

data1.index


# In[20]:

data2=pd.read_csv('raw_data.csv', parse_dates=["t"], index_col="t")


# In[22]:

data2.index


# In[25]:

data2["2011-01-01"].B.mean()


# In[29]:

data2["2011-01-01":"2011-02-01"].B.mean()


# In[30]:

data2["2011-01-01":"2011-02-01"].B.mean( )


# In[48]:

get_ipython().magic('matplotlib inline')
(data2.B.resample("B").mean()).plot()


# In[49]:

get_ipython().magic('matplotlib inline')
(data2.B.resample("W").mean()).plot()


# In[51]:

get_ipython().magic('matplotlib inline')
(data2.B.resample("M").mean()).plot()


# In[52]:

get_ipython().magic('matplotlib inline')
(data2.B.resample("Q").mean()).plot()


# In[55]:

get_ipython().magic('matplotlib inline')
(data2.B.resample("M").mean()).plot(kind="bar")


# In[ ]:



