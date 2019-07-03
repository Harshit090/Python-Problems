def perfect_no(a):
    d = []
    for i in range(1,a+1):
        if a%i == 0:
            d.append(i)
        else:
            continue
    c = 0
    for i in d:
        c = c + i
    if c/2 == a:
        x = True
    else:
        x = False
    return x

a = int(input("Enter a no\n"))
b = perfect_no(a)
if b == True:
    print("it is a perfect no")
else:
    print("it is not a perfect no")
