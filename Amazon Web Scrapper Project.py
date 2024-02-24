#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries

from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime


# In[45]:


# connect to website

URL = 'https://www.amazon.in/DUDEME-Offline-Programmer-Developer-T-Shirt/dp/B08SKLCF53/ref=sr_1_6?crid=2IFLT11NYU5CQ&dib=eyJ2IjoiMSJ9.zDLdWYIiIDI_vYH9tdcgJKFoiXbTNZnqn8TQtJYkheTD7qynDAq8C4SistMjbSsB_k6MapaGCzgZHOCcVkpptWMzRCFwfjV2fjv376cKU2DhbIOYfuQk9BnfY5VsSbac._D7F8Frogdvi19XvuP8Z_pixZtWvJiMgf20S8Pd0Flo&dib_tag=se&keywords=data+analyst+tshirt&qid=1708783507&sprefix=data+analyst+tshi%2Caps%2C235&sr=8-6'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

    
page = requests.get(URL, headers=headers)

Soup1 = BeautifulSoup(page.content, "html.parser")

Soup2 = BeautifulSoup(Soup1.prettify(), "html.parser")

title = Soup2.find(id='productTitle').get_text()

price = Soup2.find(class_="a-price-whole").get_text()


print(title)
print(price)




# In[47]:


title = title.strip()
price = price.strip()
print(title)
print(price)
type(title)
type(price)


# In[52]:


import datetime

today = datetime.date.today()

print(today)


# In[54]:


import csv

header = ['Title','Price', 'Date']
data = [title, price, today]

with open('AmazonWebScrapperDataSet.csv', 'w', newline = '', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
    


# In[63]:


import pandas as pd

df = pd.read_csv(r"C:\Users\rohiwpan\AmazonWebScrapperDataSet.csv")

print(df)


# In[62]:


#Appending Data to CSV

with open('AmazonWebScrapperDataSet.csv', 'a+', newline = '', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)
    


# In[64]:


def check_price():
    URL = 'https://www.amazon.in/DUDEME-Offline-Programmer-Developer-T-Shirt/dp/B08SKLCF53/ref=sr_1_6?crid=2IFLT11NYU5CQ&dib=eyJ2IjoiMSJ9.zDLdWYIiIDI_vYH9tdcgJKFoiXbTNZnqn8TQtJYkheTD7qynDAq8C4SistMjbSsB_k6MapaGCzgZHOCcVkpptWMzRCFwfjV2fjv376cKU2DhbIOYfuQk9BnfY5VsSbac._D7F8Frogdvi19XvuP8Z_pixZtWvJiMgf20S8Pd0Flo&dib_tag=se&keywords=data+analyst+tshirt&qid=1708783507&sprefix=data+analyst+tshi%2Caps%2C235&sr=8-6'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

    page = requests.get(URL, headers=headers)

    Soup1 = BeautifulSoup(page.content, "html.parser")

    Soup2 = BeautifulSoup(Soup1.prettify(), "html.parser")

    title = Soup2.find(id='productTitle').get_text()

    price = Soup2.find(class_="a-price-whole").get_text()
    
    title = title.strip()
    price = price.strip()
    
    import datetime

    today = datetime.date.today()
    
    import csv

    header = ['Title','Price', 'Date']
    data = [title, price, today]
    
    with open('AmazonWebScrapperDataSet.csv', 'a+', newline = '', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


# In[ ]:


while(True):
    check_price()
    time.sleep(86400)


# In[66]:


import pandas as pd

df = pd.read_csv(r"C:\Users\rohiwpan\AmazonWebScrapperDataSet.csv")

print(df)


# In[ ]:




