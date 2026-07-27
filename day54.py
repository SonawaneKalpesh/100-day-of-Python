numbers = list(map(int, input("Enter numbers separated by space: ").split()))

if numbers == numbers[::-1]:
    print("Palindrome list")
else:
    print("Not a palindrome list")