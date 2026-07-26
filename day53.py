numbers = [10, 20, 30, 40, 50]

index = int(input("Enter index to remove: "))

if 0 <= index < len(numbers):
    removed = numbers.pop(index)
    print("Removed element:", removed)
    print("Updated list:", numbers)
else:
    print("Invalid index")