class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


account = BankAccount("Rahul", 5000)

print("Name:", account.name)
print("Balance:", account.get_balance())

account.deposit(2000)
print("Balance:", account.get_balance())

account.withdraw(1000)
print("Balance:", account.get_balance())