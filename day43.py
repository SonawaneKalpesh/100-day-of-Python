numbers = list(map(int, input("Enter numbers separated by space: ").split()))

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("List after removing duplicates:", unique)