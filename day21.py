num=int(input("Enter a number : "))
reverse=0
n=abs(num)
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n//=10
if num<0:
    reverse=-reverse
print("Reverse of the number is :",reverse)