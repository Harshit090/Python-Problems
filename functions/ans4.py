def palandrome(a):
    b = a[::-1]
    if b == a:
        return True
    else:
        return False


a = input("Enter a string to be checked for palandrome\n")
c = palandrome(a)

if c == True:
    print("Its a palandrome")
else:
    print("Its not a palandrome")
