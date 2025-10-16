class InvalidAge(Exception):
    pass
def check_age(age):
    if(age<=0):
        raise InvalidAge('age is just numero uno')
    elif age<18:
        raise InvalidAge('under 18 should study smart')
    elif(age>=150):
        raise InvalidAge("that's ancient!")
    else:
        print(f'{age} is within range')
try:
    user_age=int(input('enter age: '))
    check_age(user_age)
except Exception as err:
    print('error: ',err)
