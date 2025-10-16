
# class Bird:
#     def fly(self):
#         print("Bird can fly")



# class Airplane(Bird):
#     def fly(self):
#         print("Airplane can fly")


# helang=Bird()
# print("Bird Implementation")
# helang.fly()

# print("Airplane Implementation")
# MAS=Airplane()
# MAS.fly()

# print("using for loop")
# for obj in [Bird(),Airplane()]:
#     obj.fly()


# class Employee:
#     def reg(self):
#         self.id=int(input("enter id: "))
#         self.name=input("enter name: ")

#     def display(self):
#         print(f"id: {self.id}")
#         print(f"name: {self.name}")

# #inheritance class
# class Developer(Employee):

#     def reg(self):
#         super().reg()
#         self.domain=input("enter domain: ")

#     def display(self):
#         super().display()
#         print(f"domain: {self.domain}")

# print("\nParent implementation(class Employee)")
# dev1=Employee()
# dev1.reg()
# dev1.display()

# print("\ninheritance implementation(class Developer)")
# dev1=Developer()
# dev1.reg()
# dev1.display()

class Employee:
    def __init__(self,id,name,qual):
        self.id=id
        self.name=name
        self.qual=qual

    def display(self):
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"qualification: {self.qual}")

#inheritance class
class Developer(Employee):
    def __init__(self,id,name,qual,domain,project):
        super().__init__(id,name,qual)
        self.domain=domain
        self.project=project

    def display(self):
        super().display()
        print(f"domain: {self.domain}")
        print(f"project: {self.project}")
        print("\n")

print("\nParent implementation(class Employee)")
dev1=Employee(3,"zaman","master")
dev1.display()

print("\ninheritance implementation(class Developer)")
dev1=Developer(1,"izam","bach degree","datalaju.com","side project")
dev1.display()