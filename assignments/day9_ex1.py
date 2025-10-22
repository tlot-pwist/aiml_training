# Write a program using functions to find greatest of three numbers entered by user
# Write the solution in Assignments folder with name
# day_9_ex1.py
# Push on GitHub
# Share GitHub link in chat once done

def biggest_of_three(a, b, c):
    if a>b and a>c:
        biggest=a
    elif b>a and b>c:
        biggest=b
    else:
        biggest=c
    return biggest

num1,num2,num3=map(int, input('enter 3 numbers with space between them: ').split())
print(f'the biggest number is: {biggest_of_three(num1,num2,num3)}')




    
