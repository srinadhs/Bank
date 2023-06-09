class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into account {self.account_number}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")
        else:
            print(f"Insufficient funds in account {self.account_number}.")

    def check_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")


# Example usage:

# Create a new account
account1 = BankAccount("1234567890", "John Doe")

# Deposit money
account1.deposit(1000)

# Withdraw money
account1.withdraw(500)

# Check account balance
account1.check_balance()
