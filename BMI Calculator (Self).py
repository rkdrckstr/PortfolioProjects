#!/usr/bin/env python
# coding: utf-8

# In[17]:


name = input("Enter your name: ")

weight = int(input("Enter your weight in kg: "))

height = int(input("Enter your height in cm: "))

height_in_m = height/100

BMI = weight / (height_in_m * height_in_m)

print("BMI Score: " + str(BMI))

if BMI>0:
    if(BMI<18.5):
        print(name +", you are underwight.")
    elif (BMI<=24.9):
        print(name +", you are normal weight.")
    elif (BMI<29.9):
        print(name +", you are overweight.")
    elif (BMI<34.9):
        print(name +", you are obese.")
    elif (BMI<39.9):
        print(name +", you are severely obese.")
    else:
        print(name +", you are morbidly obese.")
else:
    print("Enter valid input")


# In[ ]:





# In[ ]:




