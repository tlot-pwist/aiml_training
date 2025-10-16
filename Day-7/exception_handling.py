try:
    num1=float(input('enter first number: '))
    num2=float(input('enter second number: '))
    total=num1/num2

    print(f'sum of {num1} and {num2} = {total}')

    except Exception as warning:
    print('error',warning)
finally:
    print('end of program')
