# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 22:27:00 2019

@author: HP
"""

#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Scholarship Calculator
def result():
    a = input('Enter Name of Student: ')
    b = int(input('Enter Registration No. of Student :'))
    c = float(input('enter marks of 1 subject'))
    d = float(input('enter marks of 2 subject'))
    e = float(input('enter marks of 3 subject'))
    res=(c+d+e)/3.0
    print("Name of Student:",a)
    print("Registration No. of Student :",b)
    print("average is:",res)
    
result()
    
        
            
            

