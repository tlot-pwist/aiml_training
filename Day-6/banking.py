class Account:
    def __init__(self,acc_holder,bal):
        self.acc_holder=acc_holder
        self.bal=bal

    def acc_bal(self):
        print(f"Your account balance is: {self.bal:,.2f}")

    def new_depo(self,amount):
        self.bal+=amount
        print(f"balance after new deposit: {self.bal:,.2f}")

    def withdraw(self,amount):
        if(self.bal>=amount):
            self.bal-=amount
            print(f"balance after withdraw: {self.bal:,.2f}\n")
        else:
            print("insufficient balance")
            print("Transaction aborted")

    def show(self):
        print(f"\naccount holder name: {self.acc_holder} \nAccount balance: {self.bal:,.2f}")

account1=Account("izam",9000)

account1.show()
# print(f"Account holder name: {account1.acc_holder}")
# print(f"current account balance: {account1.bal}")

while True:
    print("\nChoose a transaction . .")
    print("1. deposit money")
    print("2. withdraw money")
    print("3. check account balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("\nDeposit Money")
        depo_amount=float(input("enter your deposit: "))
        account1.new_depo(depo_amount)
    
    elif choice == "2":
        WD_amount=float(input("enter amount to withdraw: "))
        account1.withdraw(WD_amount)

    elif choice == "3":
        print(f"Your account balance is {account1.acc_bal()}")
        #print("You ordered a Sandwich 🥪")
    elif choice == "4":
        print("Thank you for visiting! Goodbye 👋\n")
        break
    else:
        print("Invalid choice. Please choose again.\n")
    


