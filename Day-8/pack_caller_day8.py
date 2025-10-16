from package_day8 import calc

while True:
    try:
        fnum=float(input('enter first number: '))
        snum=float(input('enter second number: '))
        opr=input('choose one punishment +, - , * , /: ')

        if(opr=='+'):
            print(f'{fnum} + {snum} = {calc.add(fnum,snum)}')

        elif(opr=='-'):
            print(f'{fnum} - {snum} = {calc.minus(fnum,snum)}')

        elif(opr=='*'):
            print(f'{fnum} x {snum} = {calc.times(fnum,snum)}')

        elif opr=='/':
            print(f'{fnum} / {snum} = {round(calc.divide(fnum,snum),4)}')

        else:
            raise ValueError

    except ZeroDivisionError as zerr:
        print('error',zerr)

    except ValueError as val_err:
        print('error: ',val_err)

    except Exception as err:
        print('error',err)
    #     print(f'result: {round(result,4)} after dividing 
            
    #           {fnum} by {snum}')
    #     print(f'result: {result:.4f} after dividing {fnum} by {snum}')
    # choice 
    # finally:
    #     print('good bye')
