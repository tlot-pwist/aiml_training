class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def show_details(self):
        print('student id: ',self.id)
        print('student name: ',self.name)

    # This method defines the "informal" string representation 
    # (used by print(), str(), etc.)
    # def __str__(self):
    #     return f"Student ID: {self.id}, Name: {self.name}"

    # (Optional, but good practice)
    # This method defines the "official" string representation (used by repr())
    # def __repr__(self):
    #     return f"Student({self.id!r}, {self.name!r})"

stud1=Student(123,'izam')