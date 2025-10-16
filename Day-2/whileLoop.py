# num1=1
# print("printing numbers from 1 to 100")
# while(num1<=100):
#     print(num1,end=" ")
#     num1+=1

#print the number that can be divided by 11
# num1=1
# print("printing numbers from 1 to 100 that are divisible by 11")
# while(num1<=100):
#     if(num1%11==0):
#         # break
#         print(num1,end=" ")
#     num1+=1

#print all numbers except the numbers that can be divided by 11
# num1=1
# print("printing numbers from 1 to 100 that are divisible by 11")
# while(num1<=100):
#     if(num1%11==0):
#         num1+=1
#         continue
#         # break
#     print(num1,end=" ")
    
#     num1+=1

# num1=1
# while True(num1%11==0) and (num1<=100)
#         print(num1,end=" ")



# correctPwd="cubatrytest"
# counter=1
# while True:
#        pwd=input("enter password to start the game: ")
#        if(pwd==correctPwd):
#                 print("welcome to the matrix")
#                 break
#        else:
#             print("wrong password, go away")
#             counter+=1
# print("game started")


correctPwd="cubatrytest"
counter=0
while True:
       pwd=input("enter password to start the game: ")
       if(pwd==correctPwd):
                print("welcome to the matrix")
                print("game started")
                break
       else:
        print("wrong password")
counter+=1
if(counter>=3):
                print("you have exceeded 3 attemps")
                print("blocked for 24 hours")
                break
