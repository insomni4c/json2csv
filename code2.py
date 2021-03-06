#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import requests
import urllib.parse
import pandas as pd
from pandas.io.json import json_normalize


# In[3]:


r = requests.get('https://ADDRESS',auth=('USERNAME','PASSWORD'))


# In[4]:


r.status_code


# In[5]:


r.json()


# In[19]:


# df = json_normalize(r.json())
# df.to_csv('test3.xlsx')


# In[15]:



with open('outputfile1.json', 'wb') as outf:
    outf.write(r.content)


# In[16]:


with open('outputfile1.json') as f:
    d = json.load(f)


# In[20]:


nrmliz = json_normalize(d['items'])
nrmliz.head(100)


# In[21]:


nrmliz.to_csv('newtest2.csv')


# In[ ]:




