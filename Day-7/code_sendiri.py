

import sys # You need to import 'sys' if you plan to use sys.exit(1)

# Assume the necessary imports for your Student class are here
# For example:
# from package.student import Student 

stud_name = input('enter student name: ')

# --- Start of the while loop implementation ---
stud_id = None  # Initialize stud_id
valid_id = False # Flag variable to control the loop

while not valid_id:
    try:
        stud_id_input = input('enter student id: ')
        stud_id = int(stud_id_input)
        valid_id = True  # Set the flag to True to exit the loop
    except ValueError:
        # This block executes if int() fails
        print('Error. student id must be an integer (digits only). Please try again.')
# --- End of the while loop implementation ---

# Now, stud_id is guaranteed to be a valid integer

# Use the correct instantiation based on your import:
# Option 1: If you used 'import package.student'
# stud1 = package.student.Student(stud_id, stud_name) 

# Option 2: If you used 'from package import student'
# stud1 = student.Student(stud_id, stud_name) 

# Option 3: If you used 'from package.student import Student'
# stud1 = Student(stud_id, stud_name) 

# For this example, let's assume Option 3:
# NOTE: Replace the line below with the correct one for your actual package structure
try:
    stud1 = Student(stud_id, stud_name)
    stud1.show_details()
except NameError:
    print("\n⚠️ Class 'Student' not defined. Cannot execute the rest of the code.")
    print("Please ensure you have the correct 'from package.student import Student' line at the top.")