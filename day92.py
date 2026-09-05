class InsufficientBalanceError(Exception):
    pass


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(
                "Insufficient balance!"
            )

        self.balance -= amount
        print(f"₹{amount} withdrawn successfully.")
        print(f"Remaining balance: ₹{self.balance}")


account = BankAccount("Rahul", 5000)

print("===== BANK ACCOUNT =====")
print("Account Holder:", account.name)
print("Balance: ₹", account.balance)

try:
    amount = float(input("Enter withdrawal amount: "))
    account.withdraw(amount)

except InsufficientBalanceError as error:
    print("Error:", error)

except ValueError:
    print("Error: Please enter a valid amount.")

finally:
    print("Transaction completed.")