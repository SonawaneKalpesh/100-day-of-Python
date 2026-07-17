numbers = list(map(int, input("Enter numbers separated by space: ").split()))

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Element Occurrences:")
for key, value in frequency.items():
    print(f"{key}: {value}")