
#take user marks from user 0-50 
##if user enter outside [0-50] raise error InvalidMark using custom exception
#give chance to the user until he/she entered valid marks.
import sys #to use sys.exit()

class InvalidMark(Exception):
    pass

def check_mark(mark):
    if(mark<=0):
        raise InvalidMark('no marks for you today')
    elif mark>50:
        raise InvalidMark('because you are too smart')
    else:
        print(f'{mark} is within range')
        print('keep come and carry on')
        sys.exit()

# def finally():
    

# try:
#     mark=int(input('enter marks: '))
#     check_mark(mark)
# except Exception as err:
#     print('error:',err)
# finally:
#     print('keep calm and carry on')

while True:
    try:
        mark=int(input('\nenter marks: '))
        check_mark(mark)
    except Exception as err:
        print('\nerror:',err)
        
    choice=input('\nPress y to reenter marks or press other keys to exit: ')
    if (choice=='y' or choice=='Y'):
        continue
    else:
        print('\nsee you when we see you!')
    break
