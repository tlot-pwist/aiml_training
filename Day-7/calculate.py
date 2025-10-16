def add(num1,num2):
    return num1+num2

def X(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

def minus(num1,num2):
    return num1-num2

def average(num1,num2):
    return ((num1+num2)/2)

def remainder(num1,num2):
    return num1%num2

'''
print("welcome to simple calculator")
while True:
    print("select operation \n1.Add \n2.sub \n3.multi \n4.division \n5.average \n6.exit")
    choice=int(input("enter your operation choice(1-6): "))
    if(choice==6):
        print("good bye")
        break
    if(choice>=6) or (choice<=0):
        print("invalid option. choose again")
        #continue
    else:
        fnum=int(input("enter first number: "))
        snum=int(input("enter second number: "))

    if(choice==1):
        print(f"result after adding {fnum} and {snum} is: ",add(fnum,snum))
    elif(choice==2):
        print(f"result after substraction of {fnum} and {snum} is: ",minus(fnum,snum))
    elif(choice==3):
        print(f"result after multiplying {fnum} and {snum} is: ",X(fnum,snum))
    elif(choice==4):
        print(f"result after division of {fnum} and {snum} is: ",divide(fnum,snum))              
    elif(choice==5):
        print(f"average between {fnum} and {snum} is: ",average(fnum,snum))
        #print(f"remainder after division of {fnum} and {snum} is: ",remainder(fnum,snum))
    #break

'''


