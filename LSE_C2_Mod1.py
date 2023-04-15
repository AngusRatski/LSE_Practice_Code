#!/usr/bin/env python
# coding: utf-8

# In[1]:


#this is the first line of code
print("My name is Angus")
print("The date is Thursday 13th April 2023")


# In[2]:


#write a program to analyse real estate data
#create variables
a = 45000
b = 23400
c = 67000
d = 34600
e = 12900


# In[4]:


#find total sales value
total_sales = a + b + c + d + e
print(total_sales)


# In[5]:


#calculate average sales price for the month
average_sales = total_sales/5
print(average_sales)


# In[1]:


#find the missing property price value
print(c-6500)


# In[13]:


def new_member(name):
    return f"Hello and welcome to the program, {name}!"

print(new_member('Sarah'))


# In[21]:


def workout_time(*reported):
    total_minutes = sum(reported)
    if total_minutes < 60:
        return f"Your total workout time this week is {total_minutes} minutes"
    else:
        return f"Your total workout time this week is {total_minutes/60:.2f} hours"
    
print(workout_time(10, 10, 20, 30))


# In[23]:


list1 = (1, 2, 3, 4, 5, 6)

list1[5]


# In[29]:


dict_1={'name': 'John', '2': 'Age', 'Amount': 200}
dict_1['Amount']


# In[31]:


# Print the price.
sales_price = 24500

print(sales_price)


# In[33]:


# Print a text string verbatim.
print("My name is James Bond")


# In[34]:


# Determine whether x is greater than 10.
x = 11 

if x > 10:
    print('X is greater than 10')
else: 
    print('x is not greater than 10')


# In[35]:


# Create the variable list_a.
list_a = [1,2,3,4,'Ayaan', 'Hirsi']

list_a[5]


# Practising with Tuples

# In[2]:


tup1 = (4, 7, 13, 17.5)
print(tup1)
len(tup1)


# In[4]:


print(max(tup1))
print(min(tup1))


# In[7]:


print(tup1[0])
print(tup1[2])


# In[16]:





# In[19]:


#practising with sets
fruit = {'apple', 'pear', 'watermelon', 'tomato'}
vegetable = {'carrot', 'tomato', 'parsnip', 'leak'}
print(fruit.intersection(vegetable))


# In[ ]:


#add 'beatroot' to vegetable set
vegetable.add('beatroot')
print(vegetable)


# In[21]:


#use union to join sets of fruit and vegetables
edible_foods = fruit.union(vegetable)
print(edible_foods)


# In[23]:


print(edible_foods.difference(fruit))


# In[2]:


i = 0
a = 'aeroplane'

# The len function returns the length of an object.
while i < len(a): 
    print("Current Letter :", a[i])
    i += 1


# In[23]:


#function to print the fibonacci sequence
def fib(n):
    if n <= 0:
        return [0]
    else:
        sequence = [0, 1]
        while len(sequence) <= n:
            sequence.append(sequence[-1]+sequence[-2])
        return sequence

print(fib(7))


# In[18]:


#creating a class to describe the weather
class Weather:
    def __init__(weath, temperature, wind_speed, wind_direction):
        weath.temp = temperature
        weath.wspeed = wind_speed
        weath.wdirec = wind_direction
    def introduce(weath):
        print(f"The weather today is {weath.temp} degrees Celsius, the wind speed is {weath.wspeed}mph and the wind direction is {weath.wdirec}.")
        
weather_object = Weather('10', '7', 'SSE')
weather_object.introduce()


# In[25]:


#print today's date
from datetime import date
print(date.today())


# In[27]:


# Import modules and classes.
import datetime 
from datetime import datetime, date 
import pytz

local = datetime.now()
print("Local:", local.strftime ("%d/%m/%Y, %H:%M:%S"))

# Here, datetime_NY and datetime_London are datetime objects containing the 
# current date and time of their respective time zones.
tz_NY = pytz.timezone ('America/New_York')
datetime_NY = datetime.now(tz_NY)

print("NY:", datetime_NY.strftime("%d/%m/%Y, %H:%M:%S"))

tz_London = pytz.timezone ('Europe/London') 
datetime_London = datetime.now(tz_London)

print("London:", datetime_London.strftime ("%d/%m/%Y, %H:%M:%S"))


# In[36]:


#activity 1.3.5
#question 1
from datetime import time
t = time(14, 42, 5, 566)
print("Hour", t.hour)
print("Minute", t.minute)
print("Second", t.second)
print("Microsecond", t.microsecond)


# In[47]:


#question 2
from datetime import datetime
import calendar
dt = datetime(2019, 1, 28, 23, 55, 59, 1023)
print("Year:", dt.year)
print("Month:", calendar.month_name[dt.month])
print("Day:", dt.day)
print("Hour:", dt.hour)
print("Minute:", dt.minute)
print("Second:", dt.second)


# In[69]:


#question 3
from datetime import datetime, date
today = datetime.now()
print("Today's date is", today.strftime ("%d/%m/%Y, %H:%M:%S"))


# In[78]:


#question 4
from datetime import datetime

dt = datetime(2017, 1, 28)
# This is the code to return the full day name
dt.strftime('%A')


# In[ ]:




