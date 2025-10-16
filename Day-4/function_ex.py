# # def welcome(name):
# #     print("welcome to funtion in python dear ",name)
# #     username=input("enter your name:\t")
# #     #function call
#     # welcome(username)

# def add(num1,num2):
#     return num1+num2

# # fnum=int(input("enter first number: "))
# # snum=int(input("enter second number: "))
# # print(f"result after adding {fnum} and {snum} is: ",add(fnum,snum))

# def X(num1,num2):
#     return num1*num2

# def divide(num1,num2):
#     return num1/num2

# def minus(num1,num2):
#     return num1-num2

# def remainder(num1,num2):
#     return num1%num2

# fnum=int(input("enter first number: "))
# snum=int(input("enter second number: "))
# print(f"result after adding {fnum} and {snum} is: ",add(fnum,snum))
# print(f"result after multiplying {fnum} and {snum} is: ",X(fnum,snum))
# print(f"result after division of {fnum} and {snum} is: ",divide(fnum,snum))
# print(f"result after substraction of {fnum} and {snum} is: ",minus(fnum,snum))
# print(f"remainder after division of {fnum} and {snum} is: ",remainder(fnum,snum))

#default parameter in functions

# def info(id,name,city='KL'):
#     print(f"details as follow\n ID:{id} name:{name} city:{city}")


# info(1,"izam","pandan")
# info(101,"man")
# info(103,"zaman")

# #create a function to calculate 5 parameter number.
# def add(n1,n2=0,n3=0,n4=0,n5=0):
#     return n1+n2+n3+n4+n5

# print("result : ",add(1,2))
# print("result : ",add(1,2,3))
# print("result : ",add(1,2,3,4,5))

# def add(*args):
#     return sum(args)

# print("sum of 2,4,6,8 is ",add(2,4,6,8))
# print("sum of 2,4,6,8,1,3,5,7 is ",add(2,4,6,8,1,3,5,7))
# print("sum of 2,4,6,8,1,99,83,28,33 is ",add(2,4,6,8,1,99,83,28,33))


print("max of 2,4,6,8 is ",max(2,4,6,8)) #function max() is a pre-defined function.
print("max of 2,4,6,8,1,3,5,7 is ",max(2,4,6,8,1,3,5,7))
print("max of 2,4,6,8,1,99,83,28,33 is ",max(2,4,6,8,1,99,83,28,33))

print("min of 2,4,6,8 is ",min(2,4,6,8)) #function min() is a pre-defined function.
print("min of 2,4,6,8,1,3,5,7 is ",min(1,4,6,8,1,3,5,7))
print("min of 2,4,6,8,1,99,83,28,33 is ",min(3,4,6,8,1,99,83,28,33))

print("min of 2,4,6,8 is ",statistics.mean(2,4,6,8)) #function min() is a pre-defined function.
print("min of 2,4,6,8,1,3,5,7 is ",min(1,4,6,8,1,3,5,7))
print("min of 2,4,6,8,1,99,83,28,33 is ",min(3,4,6,8,1,99,83,28,33))
