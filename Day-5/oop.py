
# class Employee:
#     def display(self):
#         print("display of Employee Class")


# emp_001=Employee()
# emp_001.display()

class Employee:
    def reg(self,emp_id,emp_name):
        self.emp_id=emp_id
        self.emp_name=emp_name

    def display(self):
        print("Employee Details as follow:")
        print("Employee ID:",self.emp_id)
        print("Employee Name: ",self.emp_name)

emp_001 = Employee()
emp_002 = Employee()
emp_003 = Employee()

emp_001.reg("001","izam")
emp_002.reg("002","zaman")
emp_003.reg("003","man")

print("first employee details:")
emp_001.display()

print("\nsecond employee details:")
emp_002.display()

print("\nthird employee details:")
emp_003.display()