"""
price=float(input("enter product price:"))
discount=price*0.10
discPrice=price-discount
print(f"Price: {price} \n Discounted Price: {discPrice}")
"""

"""
salary=50000.50
tds=salary*0.10
bonus = 5000.60
salary+=bonus

print("salary with bonus",salary)

print(f"salary {salary} and tds is {tds}")
salary-=tds
print("salary after tds",salary)
"""

"""
age=int(input("enter your age: "))
if(age>=18):
    print("you are eligible to cast your vote")
else:
    print("you have not come to age yet \nbye bye")
"""
"""
marks=int(input("enter marks without '%' sign: "))
if(marks<30):
    print("Loserrr")
else:
    print("you shall pass the gate")
"""

"""
#xsCode="Lot237A"
xsCode=input("enter access code: ")
#if (xsCode!="Lot237A"):

if(xsCode=="Lot237A"):
    print("welcome to the matrix . . .")
    
else:
    print("you shall not pass!!!")
    input("enter new access code if you still want to pass: ")
"""

"""
mathMarks=int(input("enter your marks in mathematics: "))
cheMarks=int(input("insert your chemistry marks: "))
BmMarks=int(input("insert you bahasa melayu marks: "))

if((mathMarks>=55) and (cheMarks>=50) and (BmMarks>=60)):
    print("You are awesome!")

else:
    print("better luck next time")
    """

"""
  idProof=input("enter your id: ")

if((idProof=="passport") or (idProof=="d1") or (idProof=="voter id")):
    print(f"Valid ID {idProof}. It is accepted here")
else:
    print("Only passport or d1 or voter id is accepted")
    print(f"{idProof} is not valid ID")
      """

mathMarks=int(input("enter your marks in mathematics: "))
gapYear=int(input("enter gap year. if none, enter 0: "))

if((mathMarks>=55) and  (gapYear!=0)):
    print("You are awesome!")

else:
   print("not bad")

   