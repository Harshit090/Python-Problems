a = input("Enter a string \n")
b = input("Enter a string \n")
c = ' '
d = ' '
c = c + b[0:1]
d = d + a[0:1]
c = c + a[1:]
d = d + b[1:]
e = c + " " + d
print(e)
