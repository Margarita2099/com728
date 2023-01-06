#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import tui

#Retrieving a record for an individual car by id
def ret_by_id(records, headings):
    id = int(input(' Enter ID of car (from 1 to 205) e.g. 1:    '))
    # Creating a list with possible IDs
    possible_id = list(range(1, 206))
    # check input on error
    while id not in possible_id:
        print(f"Error! ID {id} doesn't exist, please try again")
        id = int(input(' Enter ID of car (from 1 to 205) e.g. 1:    '))
    # if no errors:
    tui.started(f" Retrieving a record for an individual car by id {id}: ")
    # enumerate returns a tuple with the counter and value:
    for index, line in enumerate(records):
        if index == id - 1:
            df = pd.DataFrame(line, headings)
    pd.set_option('display.max_rows', 20)
    print(df)        
    tui.completed()

#Retrieving all cars for a specified cylinder number
def cylinder_number(records):
    cylinder_user = int(input(" Please choose one of the cylinder number, (e.g. 2): [2] , [3], [4], [5], [6], [8], [12]:  "))
    # make a list with possible variants
    possible_cylinder_number = [2, 3, 4, 5, 6, 8, 12]
    # check on errors
    while cylinder_user not in possible_cylinder_number:
        print("Error! You entered the wrong number. Please choose one of the available options")
        cylinder_user = int(
            input(" Please choose one of the cylinder number, (e.g. 2): [2] , [3], [4], [5], [6], [8], [12]:  "))
    tui.started(f"Retrieving all cars for a  cylinder number {cylinder_user} ")
    for record in records:
        car_name = record[1]
        if cylinder_user == 4:
            cylindernumber = int(record[13])
            if cylindernumber == cylinder_user:
                print(car_name)
        elif cylinder_user == 6:
            cylindernumber = int(record[13])
            if cylindernumber == cylinder_user:
                print(car_name)
        elif cylinder_user == 3:
            cylindernumber = int(record[13])
            if cylindernumber == cylinder_user:
                print(car_name)
        elif cylinder_user == 5:
            cylindernumber = int(record[13])
            if cylindernumber == cylinder_user:
                print(car_name)
        elif cylinder_user == 12:
            cylindernumber = int(record[13])
            if cylindernumber == cylinder_user:
                print(car_name)
        elif cylinder_user == 2:
            cylindernumber = int(record[13])
            if cylindernumber == cylinder_user:
                print(car_name)
        elif cylinder_user == 8:
            cylindernumber = int(record[13])
            if cylindernumber == cylinder_user:
                print(car_name)
    tui.completed()

#Retrieving all cars in the specified car body
def car_body(records):
    car_body_user = input("Please choose one of the car body type, (e.g. sedan): [convertible], [hatchback], [sedan], [wagon], [hardtop]:  ")
    #make a list with possible values:
    possible_car_body = ["convertible", "hatchback", "sedan", "wagon", "hardtop"]
    #cheking error:
    while car_body_user not in possible_car_body:
        print("Error! You entered the wrong value. Please choose one of the available options. ")
        car_body_user = input(
            "Please choose one of the car body type, (e.g. sedan): [convertible], [hatchback], [sedan], [wagon], [hardtop]:  ")
    tui.started(f"Retrieving all cars in the {car_body_user} car body ")
    for record in records:
        car_name = record[1]
        #Check car_body:
        if car_body_user == 'convertible':
            carbody = record[4]
            if carbody == car_body_user:
                print(car_name)
        elif car_body_user == 'hatchback':
            carbody = record[4]
            if carbody == car_body_user:
                print(car_name)
        elif car_body_user == 'sedan':
            carbody = record[4]
            if carbody == car_body_user:
                print(car_name)
        elif car_body_user == 'wagon':
            carbody = record[4]
            if carbody == car_body_user:
                print(car_name)
        elif car_body_user == 'hardtop':
            carbody = record[4]
            if carbody == car_body_user:
                print(car_name)
    tui.completed()

# Retrieving Car name, fuel type, car body, horse power and price by ID
def info_by_id(records):
    id_user = int(input(' Enter ID of car (from 1 to 205) e.g. 1:    '))
    # make a list which contain possible id for input
    possible_id_user = list(range(1,206))
    # check input on error
    while id_user not in possible_id_user:
        print(f"Error! ID {id_user} doesn't exist, please try again")
        id_user = int(input(' Enter ID of car (from 1 to 205) e.g. 1:    '))
    tui.started(f"Retrieving Car name, fuel type, car body, horse power and price by ID {id_user}: \n")
    for index, line in enumerate(records):
        if index == id_user - 1:
            print(
                f" Car Name: {line[1]};\n Fuel type: {line[2]};\n Car body: {line[4]};\n Horse power: {line[16]};\n Price: {line[19]}")
    tui.completed()

