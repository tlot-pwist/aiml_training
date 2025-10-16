class Employee:
    def reg(self,id,name):
        self.id=id
        self.name=name

    def display(self):
        print(f"id: {self.id}")
        print(f"name: {self.name}")

#inheritance class
class Developer(Employee):
    def welcome(self):
        print("welcome to developer")


dev1=Developer()
dev1.welcome()
dev1.reg(1,"izam")
dev1.display()

dev1=Employee()
dev1.reg(2,"man")
dev1.display()