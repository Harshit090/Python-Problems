a = int(input("Enter a no to be checked"))
b = a % 7
c = a % 5

if a >= 1500 and a <= 2700:
    if b is 0 and c is 0:
        print(a, "is divisible by 7 and multipe of 5 ")
    elif b is 0 and c != 0:
        print(a, "is divisible by 7 but not a multipe of 5 ")
    elif c is 0 and b != 0:
        print(a, "is not divisible by 7 but a multipe of 5 ")
    else:
        print(a, "is not divisible by 7 and not a multipe of 5")
else:
    print("Enter a correct no")
