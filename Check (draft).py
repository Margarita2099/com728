#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
cars = pd.read_csv('CarPrice.csv')
print(cars.CarName.unique())
print("___________________________________________________________________________________")
print(cars.cylindernumber.unique())
print("___________________________________________________________________________________")
print(cars.carbody.unique())
print("___________________________________________________________________________________")
Brand = cars['CarName'].apply(lambda x : x.split(' ')[0])
cars.insert(3,"Brand",Brand)
cars.drop(['CarName'],axis=1,inplace=True)
print(cars.Brand.unique())


# In[ ]:




