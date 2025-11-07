
class BankAccount:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number
    
    def deposite(self,amount):
        self.balance += amount
    
    def withdraw(self,amount):
        if self.balance < 0 or amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount



choice = int(input("Enter 1 to deposite and 2 to withdraw: "))
obj = BankAccount(1000, "123456789")
if choice == 1:
    amount = float(input("Enter amount to deposite: "))
    obj.deposite(amount)
    print(f"New balance after deposite: {obj.balance}")
elif choice == 2:
    withdraw = float(input("Enter widthdraw amount: "))
    obj.withdraw(withdraw)
    print(f"New balance after withdraw: {obj.balance}")
