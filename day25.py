def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero"

print("=== Simple Calculator ===")
print("Operations: +  -  *  /")

expression = input("Enter expression (e.g., 5 + 3): ")

try:
    parts = expression.split()
    if len(parts) == 3:
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])
        
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            result = "Invalid operator"
        
        print(f"Result: {result}")
    else:
        print("Invalid format. Use: number operator number")
except ValueError:
    print("Invalid input. Please enter numbers correctly.")