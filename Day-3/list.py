# print("List Example 1")

# my_list = [10, 20, 30, "python",None,True,12.45,"izam"]

# #print("number of items in list are: ",my_list.count)
# print("number of items in list are: ",len(my_list))
# for item in my_list:
#     print(item)

# print("second example of list")
# employee_list=["nirman","izam","bin","zahid","zam","zaman"]
# print("number of employees",len(employee_list))
# print("all employees")
# for emp_name in employee_list:
#     print(emp_name,end=" ")


    #sort example

# print("sort list example")
# employee_list=["nirman","izam","bin","zahid","zam","zaman"]
# print("number of employees: ",len(employee_list))
# print("\n all employees before sort")
# for emp_name in employee_list:
#     print(emp_name)

# employee_list.sort()
# print("\nall employees after sort")
# for emp_sort in employee_list:
#     print(emp_sort)

# employee_list.reverse()
# print("\nsort in descending order")
# for emp_sort in employee_list:
#     print(emp_sort)


#append, remove, pop, insert method


#new_emp=input("ENter new employee name: ")
#employee_list.append(new_emp) #append : add a new item at the end of a list
#new_emp_index=int(input("enter the index position to add the new employee: "))
#employee_list.insert(new_emp_index,new_emp)#insert: add a new item at a given index.
#print("\nAfter adding new employee: \nNumber of employees are: ",len(employee_list))print("\nAfter adding new employee: \nNumber of employees are: ",len(employee_list))

#remove from a list example
"""
print("sort list example")
employee_list=["nirman","izam","bin","zahid","zam","zaman"]
print("number of employees: ",len(employee_list))
print("\n all employees before sort")
for emp_name in employee_list:
    print(emp_name)
el_emp=input("ENter employee name to delete: ")
if del_emp in employee_list:
    employee_list.remove(del_emp)
print("\nNumber of employees after deletion: ",len(employee_list))
for emp_name in employee_list:
    print(emp_name)
else:
    print(f"{del_emp} is not in the list.")
print("\nNumber of employees after deletion: ",len(employee_list))
for emp_name in employee_list:
    print(emp_name)
else:
    print(f"{del_emp} is not in the list.")
"""


#pop example => remove index and element in it. the updated number of index will be reduced.
employee_list=["nirman","izam","bin","zahid","zam","zaman"]
print("number of employees: ",len(employee_list))
print("List of employee names before pop:")
for emp_name in employee_list:
    print(emp_name)

del_index=int(input("enter index of the employee to be removed: "))
print(f"the name deleted at index {del_index} is {employee_list.pop(del_index)}")

print("the new number of employees: ",len(employee_list))
print("the updated employee list after pop() is:")
for emp_name in employee_list:
    print(emp_name)

# senarai_nombor = [28, 83, 19, 2, 33, 5, 9, 44]
# for i in range(3,8):
#  print(i)

