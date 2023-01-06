#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt


def bar_chart(cars):
    # length check (getting the number of cars using gas and disel)
    gas = len(cars[cars['fueltype'] == 'gas'])
    disel = len(cars[cars['fueltype'] == 'diesel'])
    # lists creation
    y = [gas, disel]
    x = ['gas', 'disel']
    f = ['lightcoral', 'lightskyblue']
    fig = plt.figure()
    plt.bar(x, y, label="fuel type", color=f, ec='black')  # plotting the graph
    plt.xlabel("fuel")  # create a label for x-axis
    plt.ylabel("count")  # create a label for y-axis
    plt.title("Number of cars by fuel")  # create a title for  graph
    #displaying a digital value above the bar charts
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha="center", va="bottom")
    plt.show()


def subplot(cars):
    # search for the 5 cheapest cars
    less_expensive_cars = cars.nsmallest(5, "price")
    less_expensive_cars
    df_less = less_expensive_cars
    # subplot creation:
    fig, ax = plt.subplots(figsize=(15, 12))
    plt.suptitle("horsepower 5 cheapest cars ", fontsize=22, y=0.95, color = "brown")
    # Get the hp and ca_name from the grouped dataframe and convert to list
    car_name = df_less['CarName'].to_list()
    hp = df_less['horsepower'].to_list()
    for i in range(len(df_less['CarName'])):
        # add a new subplot iteratively
        ax = plt.subplot(1, 5, i + 1)
        ax.bar(car_name[i], hp[i],color = 'lightblue')

        # chart formatting
        ax.set_ylim(40, 70)
    plt.show()


def pie_subplot(cars):
    #correct mistakes
    cars.replace('maxda rx3', 'mazda rx3', inplace=True)
    cars.replace('maxda glc deluxe', 'mazda glc deluxe', inplace=True)
    cars.replace('porcshce panamera', 'porsche panamera', inplace=True)
    cars.replace('toyouta tercel', 'toyota tercel', inplace=True)
    cars.replace('vokswagen rabbit', 'volkswagen rabbit', inplace=True)
    cars.replace('vw rabbit', 'volkswagen rabbit', inplace=True)
    cars.replace('vw dasher', 'volkswagen dasher', inplace=True)
    # creation a new data frame, which contains the 10 most frequent cars
    frequancy = cars["CarName"].value_counts().to_frame().reset_index().head(10)
    frequancy.columns = ["Cars", "frequancy"]
    from pandas.plotting import table
    plt.figure(figsize=(16, 8))
    ax1 = plt.subplot(121) # one row and two columns worth of figures. The last number means that  place the plot in the left most column
    frequancy.plot(kind='pie', y='frequancy', ax=ax1, autopct='%1.1f%%',
                   startangle=800, shadow=False,labels=frequancy['Cars'], legend=False, fontsize=10)
    ax2 = plt.subplot(122) # place the plot in the right most column.
    plt.axis('off')
    tbl = table(ax2, frequancy, loc='center')
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(16)
    tbl.scale(1, 2)
    plt.show()

