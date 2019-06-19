b = input("Enter a string to be added to list by a comma sepration \n")
a = b.split(',')
c = []
n = int(input("Enter value of n"))
for i in a:
    if len(i) > n:
        c.append(i)
print(c)
