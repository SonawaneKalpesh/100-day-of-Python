class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")

    def display_account(self):
        print("\n===== ACCOUNT DETAILS =====")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Balance: ₹{self.balance}")


account_number = input("Enter account number: ")
name = input("Enter account holder name: ")

account = BankAccount(account_number, name)

while True:
    print("\n===== BANK ACCOUNT SYSTEM =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Display Account")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        account.display_account()

    elif choice == "5":
        print("Thank you for using the Bank Account System!")
        break

    else:
        print("Invalid choice. Please try again.")