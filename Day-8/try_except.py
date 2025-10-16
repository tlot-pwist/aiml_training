
try:
    fnum=float(input('enter first number: '))
    snum=float(input('enter second number: '))
    result=fnum/snum
    print(f'result: {round(result,4)} after dividing {fnum} by {snum}')
    print(f'result: {result:.4f} after dividing {fnum} by {snum}')
except Exception as err:
    print('error',err)
finally:
    print('good bye')
