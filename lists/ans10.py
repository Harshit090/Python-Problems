b = input("Enter a string to be added to list by a space sepration \n")
a = b.split(' ')
c = input("Enter a string to be added to list by a space sepration \n")
d = c.split(' ')
e = []
for i in a:
    for j in d:
        if i == j:
            e.append(i)
        else:
            continue
print(a)
print(d)
print(e)
