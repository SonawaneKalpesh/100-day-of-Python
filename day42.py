numbers = list(map(int, input("Enter numbers separated by space: ").split()))

total = 0

for num in numbers:
    total += num

print("Sum of all elements:", total)