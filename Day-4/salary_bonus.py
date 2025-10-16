def func_bonus(gaji):
    bonus=0.1*gaji
    return bonus

def output_bonus():
    print("your bonus is 10% from salary : ",func_bonus(gaji))
    print(f"salary is {gaji} \nbonus 10% is ",func_bonus(gaji))

gaji=float(input("your salary per month: "))
output_bonus()
#bonus=0.1*gaji
# print("your bonus is 10% from salary : ",func_bonus(gaji))
# print(f"salary is {gaji} \nbonus 10% is ",func_bonus(gaji))