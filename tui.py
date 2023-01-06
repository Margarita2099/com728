#!/usr/bin/env python
# coding: utf-8

# In[1]:


## TUI is short for Text-User Interface. This module is responsible for communicating with the user.
## The functions in this module will display information to the user and/or retrieve a response from the user.

LINE_WIDTH = 85
#Display Tittle
def welcome():
    welcome_msg = 'Car prices Data'
    print('-' * len(welcome_msg), welcome_msg, '-' * len(welcome_msg), sep='\n')

# display information, that operation is started
def started(msg=""):
    output = f"Operation started: {msg}..."
    dashes = "-" * LINE_WIDTH
    print(f"{dashes}\n{output}\n")

# display information, that operation is finished
def completed():
    dashes = "-" * LINE_WIDTH
    print(f"\nOperation completed.\n{dashes}\n")

#Display an error message:
def error(msg):
    print(f"Error! {msg}\n")

# Main menu
def menu(variant=0):
    if variant == 0:
        print('[1] Process Data\n'
              '[2] Data in tables\n'
              '[3] Visualise Data\n'
              '[4] Exit\n')
    #pricess in list module
    elif variant == 1:
        print('[1] Record for an individual car by id \n'
              '[2] Records all cars for a specified cylinder number \n'
              '[3] Records all cars in the specified car body\n'
              '[4] Retrieve a specific number of columns  related to an individual car by id\n')
    # process in tables module
    elif variant == 2:
        print('[1] Retrieve the car names alphabetically \n'
              '[2] Retrieve summary of sales (total car price) for each car body\n'
              '[3] Retrieve the top 5 car sale by price (the most expensive) and per car body\n'
              '[4] Retrieve total price by brands')
    # process in plot module
    elif variant == 3:
        print('[1]  Number of cars per fuel system bar chart\n'
              '[2] The horsepower of the  cheapest 5 car sale by price  subplot \n'
              '[3]  top 10 cars by frequency')
    #Getting input from the user
    choice = input('Select one of the possible options, e.g. 1 ')
    # Checking input on errors
    if choice.isdigit():
        choice = int(choice)
        if variant == 0 or variant == 1 or variant == 2:
            if 1 <= choice <= 4:
                return choice
            return print("ERROR. There is no such item")

        elif variant == 3:
            if 1 <= choice <= 3:
                return choice
            return print("ERROR. There is no such item")
        return print("ERROR. Variant is invalid")
    else:
        print('ERROR. Try to write an integer !')
        return None


# In[ ]:




