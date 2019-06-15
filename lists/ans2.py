b = int(input("Enter a no of no to be added in a list \n"))
a = []
for i in range(b):
    n = int(input("enter no : \t"))
    a.append(n)
c = 0
d = 1
for i in a:
    c = c + i
    d = d*i
print(c,"\n",d)
