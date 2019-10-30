#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import pickle
import requests
import json
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score


# In[6]:


def send_slack(msg, channel='#data-science', username="jaja_bot"):
    webhook_URL = "https://hooks.slack.com/services/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"
    payload = {
        "channel": channel,
        "username": username,
        "icon_emoji": ":provision",
        "text": msg,
    }
    response = requests.post(
        webhook_URL,
        data = json.dumps(payload),
    )
    return response


# In[12]:


def find_accuracy(alpha):
    
    article_df = pd.read_csv("{}/article.csv".format(os.path.dirname(os.path.realpath("__file__"))))
    
    X_train, X_test, y_train, y_test = train_test_split(article_df.content, article_df.category, test_size=0.1, random_state=1)
    
    clf = Pipeline([
        ('vect', TfidfVectorizer()),
        ('clf', MultinomialNB(alpha=float(alpha)))
    ])
    
    # 모델 생성
    model = clf.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    
    result = accuracy_score(y_test, y_pred)
    send_slack("alpha:{}, accuracy:{}".format(alpha, result))
    return result


# In[13]:


# alphas = [0.1, 0.01, 0.001]
# for alpha in alphas:
#     print(alpha, find_accuracy(alpha))


# In[ ]:


result = find_accuracy(sys.argv[1])
print(result)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




