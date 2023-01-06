#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import tui
from IPython.display import display #I utilise this import to obtain a pretty good view of the table (otherwise, the output window of Jupiter Notebook would not accommodate all the data).
#Retrieving the car names alphabetically
def alphabet(cars):
    tui.started("Retrieving the car names alphabetically")
    #To accurately display the translation of all letters in Lowercase letters
    cars.CarName = cars.CarName.str.lower()
    # sorting from a to z
    alphabet_order = cars.sort_values('CarName', ascending=True)
    alphabet_order = alphabet_order.reset_index(drop=True)
    # setting parameters for display
    pd.set_option('display.max_rows', 206)
    pd.set_option('display.colheader_justify', 'center')
    display(alphabet_order)
    tui.completed()

#Retrieving summary of sales (total car price) for each car body
def price_for_car_body(cars):
    tui.started("Retrieving summary of sales  for each car body")
    # access a group columns by label using loc, find specific car body and sum the price
    total_convertible = cars.loc[cars['carbody'] == 'convertible', 'price'].sum()
    total_hatchback = cars.loc[cars['carbody'] == 'hatchback', 'price'].sum()
    total_sedan = cars.loc[cars['carbody'] == 'sedan', 'price'].sum()
    total_wagon = cars.loc[cars['carbody'] == 'wagon', 'price'].sum()
    total_hardtop = cars.loc[cars['carbody'] == 'hardtop', 'price'].sum()
    # Creation a data frame to  achieve greater visibility
    df_price_body = pd.DataFrame({'Car body': ['convertible', 'hatchback', 'sedan', 'wagon', 'hardtop'],
                       'Total price': [total_convertible, total_hatchback, total_sedan, total_wagon, total_hardtop]})
    pd.set_option('display.max_rows', 5)
    pd.set_option('display.max_columns', 3)
    pd.set_option('display.colheader_justify', 'center')
    print(df_price_body)
    tui.completed()


#Retrieving the top 5 car sale by price (the most expensive) and per car body
def most_expensive_by_carbody(cars):
    tui.started("Retrieve the top 5 car sale by price and per car body")
    # Search a specific car body
    most_expensive_convertible = cars.query(" `carbody` == 'convertible'")
    # getting the 5 most expensive
    most_expensive_convertible = most_expensive_convertible.loc[most_expensive_convertible['price'].nlargest(5).index]
    most_expensive_convertible = most_expensive_convertible.reset_index(drop=True)
    print("\033[1m top 5 convertible car sale by price: \033[0m ")
    print()
    pd.set_option('display.max_rows', 5)
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.width', 1000)
    pd.set_option('display.colheader_justify', 'center')
    display(most_expensive_convertible)
    most_expensive_hatchback = cars.query(" `carbody` == 'hatchback'")
    most_expensive_hatchback = most_expensive_hatchback.loc[most_expensive_hatchback['price'].nlargest(5).index]
    most_expensive_hatchback = most_expensive_hatchback.reset_index(drop=True)
    print()
    print("\033[1m top 5 hatchback  car  sale by price: \033[0m ")
    display(most_expensive_hatchback)
    most_expensive_sedan = cars.query(" `carbody` == 'sedan'")
    most_expensive_sedan = most_expensive_sedan.loc[most_expensive_sedan['price'].nlargest(5).index]
    most_expensive_sedan = most_expensive_sedan.reset_index(drop=True)
    print()
    print("\033[1m top 5 sedan  car  sale by price: \033[0m")
    display(most_expensive_sedan)
    print()
    most_expensive_wagon = cars.query(" `carbody` == 'wagon'")
    most_expensive_wagon = most_expensive_wagon.loc[most_expensive_wagon['price'].nlargest(5).index]
    most_expensive_wagon = most_expensive_wagon.reset_index(drop=True)
    print("\033[1m top 5 wagon  car  sale by price: \033[0m")
    display(most_expensive_wagon)
    print()
    most_expensive_hardtop = cars.query(" `carbody` == 'hardtop'")
    most_expensive_hardtop = most_expensive_hardtop.loc[most_expensive_hardtop['price'].nlargest(5).index]
    most_expensive_hardtop = most_expensive_hardtop.reset_index(drop=True)
    print("\033[1m top 5 hardtop  car  sale by price: \033[0m")
    display(most_expensive_hardtop)
    tui.completed()

# Retrieving the price by brands
def brands(cars):
    tui.started("Retrieve the total price by brands")
    # add a new  column, which is obtained by taking the first values in the column CarName
    cars['brand'] = cars.CarName.str.split(' ').str.get(0)
    # Check on errors and correction
    cars.brand = cars.brand.str.lower()
    cars.brand.replace('maxda', 'mazda', inplace=True)
    cars.brand.replace('porcshce', 'porsche', inplace=True)
    cars.brand.replace('toyouta', 'toyota', inplace=True)
    cars.brand.replace('vokswagen', 'volkswagen', inplace=True)
    cars.brand.replace('vw', 'volkswagen', inplace=True)
    # sum of price for each brand
    brands_price = cars[['brand', 'price']].groupby('brand', as_index=False).sum().rename(
        columns={'price': 'total_price'})
    pd.set_option('display.max_rows', 22)
    pd.set_option('display.max_columns', 3)
    pd.set_option('display.width', 500)
    pd.set_option('display.colheader_justify', 'center')
    print(brands_price)
    tui.completed()

