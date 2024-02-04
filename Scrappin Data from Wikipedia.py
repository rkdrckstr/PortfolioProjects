#!/usr/bin/env python
# coding: utf-8

# Scrappin Data from a Real Website + Pandas

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[3]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[4]:


print(soup)


# In[54]:


soup.find('table')


# In[9]:


soup.find_all('table')[0]


# In[12]:


soup.find('table', class_ = 'wikitable sortable')


# In[30]:


table = soup.find_all('table')[0]


# In[31]:


print(table)


# In[98]:


world_titles = table.find_all('th')[0:7]


# In[99]:


world_titles


# In[100]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[101]:


import pandas as pd


# In[109]:


df = pd.DataFrame(columns = world_table_titles)

df


# In[103]:


column_data = table.find_all('tr')


# In[112]:


for row in column_data[2:]:
    row_data = row.find_all('th')
    indv_row_data = [data.text.strip() for data in row_data]
    row_data2 = row.find_all('td')[0:6]
    indv_row_data2 = [data.text.strip() for data in row_data2]
    final_data = indv_row_data + indv_row_data2
    
    
    length = len(df)
    df.loc[length] = final_data


# In[113]:


df


# In[116]:


df.to_csv(r'C:\Users\rohiwpan\Documents\Python Tut\Companies.csv', index = False)


# In[ ]:




