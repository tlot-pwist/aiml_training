def factorial(num):
    if((num==0) or (num==1)):
        return 1
    else:
        return num*factorial(num-1)
    
num=int(input("enter a number to find factorial: "))
print(f"factorial of {num} is: ",factorial(num))
