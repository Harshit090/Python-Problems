b = input("Enter a string to be added to list by a space sepration \n")
a = b.split(' ')
c = []
n = int(input("enter the increment value"))

for i in range(n):
    c.append(a[i::n])
print(c)
