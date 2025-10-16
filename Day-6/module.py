import math
import random
import inspect
import datetime
import os

listDirs=os.listdir()
for dir in listDirs:
    print(dir)

""" 
functions = inspect.getmembers(os, inspect.isbuiltin)
for n, func in functions:
    print(n)

# print("today is: ",datetime.date.today())
# print("sum of numbers 10,20 is ",math.sum(10,20))

# print(f"let's see a random number: {lambda(i:i in range(10))random.randint(1,100)}")

# print(math.sin(90))

# functions = inspect.getmembers(math, inspect.isbuiltin)
# for n, func in functions:
#     print(n)
"""

"""
dtclasses=inspect.getmembers(datetime, inspect.isclass)
print("all classes inside datetime module")
for n, func in dtclasses:
    print(n)

print("\nall functions inside datetime.date class")
functions=inspect.getmembers(datetime.date, inspect.isbuiltin)
for n, func in functions:
    print(n)

# print("sin 90 is ",math.sin(90))
# print("cos 90 is ",math.cos(90))
# print("tan 90 is ",math.tan(90))
"""