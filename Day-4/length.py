# def inch_to_cm(num):
#     cm=num*2.54
#     return cm

# inch=float(input("insert length in inch: "))

# print(f"{inch} inch in cm is: {inch_to_cm(inch)} cm")

#write a function to find out the table of given number
def gen_table(num):
    for i in range(1,11):
        print(f"{num}*{i}=\t{num*i}")

number=int(input("enter number to find out table: "))
gen_table(number)
