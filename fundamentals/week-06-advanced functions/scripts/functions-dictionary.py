#!/usr/bin/env python3
"""Week 06 — Functions and Dictonaries
Run this script to recap variables, control loops and functions. Then learn about dictionaries
    python scripts/functions-dictonary.py
"""


# ── Recap variables─────────────────────────────────────────
# There are different types of variables
# you can look at these as temporary memory. And if you would put them in a bag you can put
# them together and manipulate them
# Good practice is to use logical naming to show purpose
# You can print these on the program output
from datetime import datetime
from os import name


print("Good day")

string_welcome = "good day"
int_noon = 12
float_amount = 123.56
bool_choice = True

my_shoppingbag = ["Carrots", "2", "3.5", True]
print(my_shoppingbag[1]) # prints the string 2

yourname = input("What is your name?")

print(f"Hello, {yourname}! {string_welcome}")


# ── Recap control-flow and functions─────────────────────────────────────────
# With a control you can have certain code executed based on a condition
# If <condition> then <do something> Else <do another thing>
# While <condition> do <repeat something> and For <condition> <do something>
# Functions are defined by the keyword def <name> (input)
# Use functions for clean code and reusability. There also build-in functions
# functions can also be part of a class, like datetime.

time = 10 
int_afternoon = 18
# Source - https://stackoverflow.com/a/22022021
# Posted by dawg, modified by community. See post 'Timeline' for change history
# Retrieved 2026-05-11, License - CC BY-SA 3.0

currenthour = datetime.today().hour

def setclock (mytime=currenthour):
      mytime = mytime+1
      return(mytime)

while time > 0 and time <24 :
    time = setclock(time)
    if time < int_noon: 
        print(f"good morning, time:{time}")
    elif time <int_afternoon:
        print(f"good afternoontime:{time}")      
    else:
        print(f"good night:{time}")
for i in my_shoppingbag:
    print(i)
    print(type(i))	
print("good day")

# ── Build-in functions ───────────────────────────────────────────────────────────
# Several useful functions are print(), sum(),type(),len(), max()/,min(),abs(),map()
# 
int_list = [1,2,3,5,7,11]

# print the type of objects in the variable int_list with separator
print(type(int_list)," - ")
# sum the numbers
my_sum = sum(int_list)
print(my_sum)
my_tuple = (1,2,3,5,7,11)
print(my_tuple, " _ ")
my_set = {1,2,3,5,7,11}
print(my_set, " ~ ")

#print the type
print(type(my_sum))
print(type(int_list))
print(type(my_tuple))
print(type(my_set))

#return the list lenght, max, min and abs value
print(len(int_list))
print(max(int_list))
print(min(int_list))
print(abs(my_sum))

# map executes a function for given list and returns the outcome as a list
def squaredNum (x):
    return x*x

def toUpper(s):
    return s.upper()

squared_Numbers = map(squaredNum, int_list)
print(list(squared_Numbers))
My_Upper_bag = map(toUpper, my_shoppingbag)
print(list(My_Upper_bag))

# ── Filters ────────────────────────────────────────────────────────
# Filters are used for on-the fly (in-memory) filtering of lists
def is_even(x):
    return x % 2 == 0
even_numbers = list(filter(is_even, int_list))
print(even_numbers)

# ── Methods ───────────────────────────────────────────────────────────────────
# A METHOD is a function that belongs to a specific type of object
# You call it with a dot:  list_name.method_name()
# Depending on the type of the Python object you're dealing with, you'll be able to use different methods and they behave differently.​
# A method may also be used for different types of python objects.

print("\n=== Methods ===")
fruits = ["banana", "apple", "cherry"]
print(f"Start           : {fruits}")
fruits.append("mango")
print(f"append('mango') : {fruits}")
currentTime = datetime.now()
print(f"Current time:  {currentTime}")
print(f"uppercase fruit:  {list(fruits[0].upper())}")


# ── Dictionary ───────────────────────────────────────────────────────────────────
# A dictionary is an unordered collection of items that store data in key-value pairs.​
# Unordered: Items do not have a defined order; access is based on keys.​
# Mutable: You can change, add, or remove key-value pairs after the dictionary is created.​
# Key-Value pairs: Each key must be unique and immutable (e.g., strings, numbers, tuples),​
# while values can be of any data type.​
# Created with {}​, items separated by ,
# Specific value can be accessed with [key]

#create an dictionary object
teacher = {
    "name": "Marijn",
    "age": 48,
    "city": "Eindhoven"
}

print(teacher["name"])
teacher["job"] ="Engineer"
teacher["age"] = 48.5
del teacher["city"]
# iterating through values
for tid,tvalue in teacher.items():
    print(f"tid: {tid} tvalue: {tvalue}")

#checking if item exists
if "name" in teacher:
    print("name is found")

# ── Lamdba ───────────────────────────────────────────────────────────────────
# Lambda function
#A lambda function is a small, anonymous function defined using the lambda keyword.​
#Syntax:​
#
#lambda arguments: expression​
#Can Take Multiple Arguments:​
#
#Example: add = lambda x, y: x + y

square = lambda x: x ** 2
squared_Numbers = map(square, int_list)
print("Squared Numbers with Lamdba ", list(squared_Numbers))
squared_Numbers = map(lambda x:x**2, int_list)
print("Squared Numbers with inline Lamdba ", list(squared_Numbers))
