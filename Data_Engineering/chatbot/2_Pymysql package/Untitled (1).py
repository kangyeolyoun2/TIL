#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pickle

file = open("/Users/kangyeolyoun/Desktop/pickle file/aws_mysql_db", "rb")
data = pickle.load(file)


# In[16]:


import sys
import requests
import base64
import json
import logging
import pymysql



host = data[0]
port = int(data[1])
database = data[2]
password = data[3]

def main():
    
    conn = pymysql.connet(host, user=username, passwd=password, db=database,                         port=port, use_unicode=True, charset="utf8")
    cursor = conn.cursor()
    print("success")
    sys.exit(0)


# In[ ]:




