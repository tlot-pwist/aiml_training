# def add(a,b):
#     total=a+b
#     return total


# add=lambda a,b: a+b
# multi=lambda a,b:a*b
# div=lambda a,b:a/b
# avg=lambda a,b:(a+b)/2
# sub=lambda a,b:(a-b)

# num1=int(input("enter first number: "))
# num2=int(input("enter second number: "))

# print(f"multipication result of {num1} and {num2} is {multi(num1,num2)}")
# print(f"division result of {num1} and {num2} is {div(num1,num2)}")
# print(f"addition result of {num1} and {num2} is {add(num1,num2)}")
# print(f"substraction result of {num1} and {num2} is {sub(num1,num2)}")

check_odd=lambda n: "odd number" if n%2==1   else "even number"
num1=int(input("enter a number to check oddity: "))
print(check_odd(num1))

