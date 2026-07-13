numbers = list(map(int, input("Enter numbers separated by space: ").split()))
k = int(input("Enter number of rotations: "))

k = k % len(numbers)

rotated = numbers[-k:] + numbers[:-k]

print("Rotated list:", rotated)