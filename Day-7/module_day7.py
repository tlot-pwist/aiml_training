import math
import inspect


# num=int(input("enter number to find squre root: "))
# print(f"square root of {num} is ",math.sqrt(num))

# functions = inspect.getmembers(math, inspect.isbuiltin)

# print("All Function in math module")
# for n, func in functions:
#     print(func)

""" 
import random
name=input("enter your name: ")

rand_num=random.randint(1,10)
print(f"coupon holder: {name} \ncoupon number: {rand_num}")
if rand_num==1:
    print("you get a piece of paper")

elif rand_num==9:
    print("you get it or not?" )  

else:
    print("no mercy!!!")  

"""

import datetime
"""
dtclasses=inspect.getmembers(datetime, inspect.isclass)

# print("All Function in datetime module")
# for n, func in dtclasses:
#     print(n,func)

print("\n---Today---")
print(datetime.date.today())

print("\ncurrent date time")
print(datetime.datetime.now())

print("\ncurrent time")
print(f"{datetime.datetime.now().time()}\n")

cttime=datetime.datetime.now().time()
formatedtime=datetime.datetime.now().strftime("%I:%M:%S %p")

print("current time",cttime)
print(f"formated time {formatedtime}\n")


# print("time zone: ")
# print(datetime.timezone(Malaysia))

"""

# import os

# print("current directory: ",os.getcwd())
# print("login name: ",os.getlogin())

# functions=inspect.getmembers(os, inspect.isbuiltin)

# print("all function is os module")
# for n,func in functions:
#     print(n)

"""create a folder inside current directory using python"""

import os

cdir=os.getcwd()
print('current folder(s) in the current directory:') #aku tambah sendiri
files = os.listdir(cdir) #aku tambah sendiri
print(f'{files}\n') #aku tambah sendiri. output: tunjuk folder dan file yang ada dalam directory.

folder_name=input('enter folder name to create: ')
folder_path=os.path.join(cdir,folder_name)

if os.path.exists(folder_path):
    print('folder already exist')
    rename_folder=input('rename the folder: ')
    os.rename(folder_name,rename_folder)
    print(f'folder name {folder_name} has been changed to {rename_folder}')

else:
    os.makedirs(folder_path,exist_ok=True)
    print(f'{folder_name} created at {folder_path}')

""" rename a folder """
#os.rename(folder_name,'rename_folder')
#take folder name from user
#if it is exist, ask new name then rename it

""" remove a folder """