print("===== EXCEPTION HANDLING SYSTEM =====")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

else:
    print("Division successful.")
    print("Result:", result)

finally:
    print("Program execution completed.")