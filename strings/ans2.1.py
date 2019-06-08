a = input()
b = ' '
for i in a:
    if i is '$':
        b = b + a[0]
    else:
        b = b + i
print(a,b,)
