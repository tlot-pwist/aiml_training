def display():
    print("welcome to the recap of functions")

def welcome(name):
    print("welcome to functions dear",name)

def cube(num):
    cube=num**3
    print(f"cube of given number {num} is {cube}")

def square(num):
    return num*num

# welcome("izam")
# display()

# cube_num=int(input("enter a number to calculate the cube: "))
# cube(cube_num)

username=input("enter user name: ")
welcome(username)
my_num=int(input("enter number to find out cube and square: "))
cube(my_num)
print(f"the square of the number {my_num} is {square(my_num)}")
