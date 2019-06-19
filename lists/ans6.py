b = input("Enter a string to be added to list by a space sepration \n")
a = b.split(' ')
c = []
for i in a:
    if i in c:
        continue
    else:
        c.append(i)
print(a)
print(c)
