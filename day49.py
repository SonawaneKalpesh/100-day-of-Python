numbers = list(map(int, input("Enter numbers separated by space: ").split()))
chunk_size = int(input("Enter chunk size: "))

for i in range(0, len(numbers), chunk_size):
    print(numbers[i:i + chunk_size])