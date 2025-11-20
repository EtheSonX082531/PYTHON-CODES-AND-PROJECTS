class Account:
    def __init__(self, balance, accno):
        self.balance = balance
        self.accno = accno
        print("Created An Account Successfully..\n")

    def credit(self, amount):
        if amount <= 0:
            print("Invalid amount for credit!")
            return

        self.balance += amount
        print(f"Credited Taka {amount} in Account No: {self.accno} Successfully...")
        print(f"New Balance: {self.balance}")

    def debit(self, amount):
        if amount <= 0:
            print("Invalid amount for debit!")
        elif amount > self.balance:
            print("Sorry, you don't have enough balance!")
            print("Available Balance:", self.balance)
        else:
            self.balance -= amount
            print(f"Debited Taka {amount}.")
            print("New Balance:", self.balance)

    def showBalance(self):
        print(f"You have {self.balance} taka in your Account!")
        

acc1 = Account(1000, 5625)
acc2 = Account(200, 1024)

acc1.credit(500)
acc1.showBalance()
acc1.debit(600)

acc1.credit(700)
acc1.showBalance()
