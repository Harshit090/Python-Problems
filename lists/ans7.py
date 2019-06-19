b = input("Enter a string to be added to list by a space sepration \n")
a = b.split(' ')
d = []
n = int(input("enter range"))
for i in range(1,n+1):
    for j in a:
        d.append(j + str(i))
print(d)
