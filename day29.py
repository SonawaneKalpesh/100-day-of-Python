password = input("Enter password: ")

has_digit = False
has_letter = False

for char in password:
    if char.isdigit():
        has_digit = True
    if char.isalpha():
        has_letter = True

if len(password) >= 6 and has_digit and has_letter:
    print("Valid password ✅")
else:
    print("Invalid password ❌")