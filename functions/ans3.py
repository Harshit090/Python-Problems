def reverse_string(a):
    c = len(a)
    if c % 4 == 0:
        d = a[::-1]
        e = True
        return d,e
    else:
        d = a
        e = False
        return d,e

a = input("Enter a string\n")

b,c = reverse_string(a)
if c == True:
    print(b, "Reversed")
else:
    print(b, "not reversed")   
