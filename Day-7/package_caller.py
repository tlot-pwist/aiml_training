import sys
import os

# 1. Use a raw string for the Windows path (FIXED)
# package_parent_dir = r'C:\Users\DELL\Coding\AIML\Day-7'

# # 2. Add the directory to the system path
# if package_parent_dir not in sys.path:
#     sys.path.append(package_parent_dir)

try:
# 3. Import the module inside the package
# from package.student import Student
# from package.student import Student #can directly access classes e.g when initialize class instance stud1=Student(para1,para2)
    from package import student

except ImportError as err:
    print(f'error: could not find module/class.\nDeatils: {err}')
    sys.exit(1)
# import package.student #cara access stud1=package.student.Student(stud_id,stud_name)

# 4. Access the class/function from the imported module
# Note: student is the module, Student is the class inside it.
# print(student.Student(345, 'zaman'))

# s1=student.Student(345,'zaman')
# s1.show_details()

stud_name=input('enter student name: ')
try:
    stud_id=int(input('enter student id: '))
except ValueError:
    print('Error. student id must be in digits.')
    sys.exit(1)
stud1=package.student.Student(stud_id,stud_name) #bila guna from package.student
stud1=student.Student(stud_id,stud_name) #bila guna from package import student
stud1=Student(stud_id,stud_name) #bila guna from package.student import Student

stud1.show_details()