
# class Player:
#     def __init__(self) -> None:
#         print("welcome to player class")

#     def reg(self,id,name,team) -> int|str:
#         self.id=id
#         self.name=name
#         self.team=team

#     def display(self) -> None:
#         print(f"Id: {self.id} \nName: {self.name} \nTeam: {self.team}\n")

# #object creation
# playa1=Player()
# playa2=Player()
# playa3=Player()
# playa4=Player()

# playa1.reg(1,"MSD", "India")
# playa2.reg(2,"man", "Malaysia")
# playa3.reg(3,"izam", "COlombia")

# playa1.display()
# playa2.display()
# playa3.display()


class Player:
    def __init__(self,id,name,team) -> None:
        self.id=id
        self.name=name
        self.team=team
        print("welcome to player class")

    # def reg(self,id,name,team) -> int|str:
    #     self.id=id
    #     self.name=name
    #     self.team=team

    def display(self) -> None:
        print(f"Id: {self.id} \nName: {self.name} \nTeam: {self.team}\n")

    def __str__(self) -> str:
        return f"\n{self.id} {self.name} {self.team}\n"

#object creation
playa1=Player(1,"MSD", "India")
playa2=Player(2,"man", "Malaysia")
playa3=Player(3,"izam", "COlombia")
playa4=Player(4,"zaman", "Palestine")

# playa1.reg(1,"MSD", "India")
# playa2.reg(2,"man", "Malaysia")
# playa3.reg(3,"izam", "COlombia")

# playa1.display()
# playa2.display()
# playa3.display()
# playa4.display()

print(playa1)
