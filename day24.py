import random
print("guess the number")
n=None
r=random.randint(1,100)
while n!=r:
    n=int(input("enter the number"))
    if n>r:
        print("too high")
    elif n<r:
        print("too low")
    else:
        print("you win")