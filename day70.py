def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


number = int(input("Enter number of terms: "))

print("Fibonacci sequence:")

for i in range(number):
    print(fibonacci(i), end=" ")