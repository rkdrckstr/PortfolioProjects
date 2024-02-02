#!/usr/bin/env python
# coding: utf-8

# In[23]:


import os, shutil


# In[24]:


path = input("File Path: ")


# In[25]:


file_name = os.listdir(path)


# In[26]:


folder_names = ['CSV Files', 'Image Files', 'Text Files']

for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs(path + folder_names[loop])
        
for file in file_name:
    if ".csv" in file and not os.path.exists(path + "CSV Files/" + file):
        shutil.move(path + file,path + "CSV Files/" + file)
    elif ".png" in file and not os.path.exists(path + "Image Files/" + file):
        shutil.move(path + file,path + "Image Files/" + file)
    elif ".txt" in file and not os.path.exists(path + "Text Files/" + file):
        shutil.move(path + file,path + "Text Files/" + file)
print('New folder have been created')
print('Respective files have been moved')
print('Thank you for using this program')


# In[ ]:




