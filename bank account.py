class BankAccount:
    bank_name = "67 Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}. New balance: {self.balance}")
        else:
            print(f"Insufficient funds for {self.owner}. Withdrawal failed.")
        
    def show_balance(self):
        print(f"{self.owner}'s current balance: {self.balance}")


account1 = BankAccount("Yuzuha", 100)
account2 = BankAccount("Alice", 50)

account1.show_balance()
account2.show_balance()

account1.deposit(50)
account1.withdraw(30)
account1.show_balance()

account2.deposit(100)
account2.withdraw(200)
account2.show_balance()