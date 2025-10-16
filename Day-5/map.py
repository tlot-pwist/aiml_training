
numbers=[10,25,30,40,1,2] #original list
print("original list")
for number in numbers:
    print(number,end=" ")

double_numbers=list(map(lambda x: 2*x, numbers))
print("\n\nthis is updated doubled number list:")
for double_number in double_numbers:
    print(double_number,end=" ")

even_numbers=list(map(lambda x: x%2==0, numbers))
# print("\n\nthis is updated even number list:")
# for number in numbers and even_number in even_numbers:
#     print(f"{number} -> {even_number}",end=" ")

