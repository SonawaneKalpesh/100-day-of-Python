num=int(input("Enter a number : "))

total=0
n= abs(num)

while n > 0 :
    digit =n % 10
    total =digit
    n//=10

print("sum of digit ",total)