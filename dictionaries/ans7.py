n = int(input("enter no of items to added in a list\n"))
a = []
b = []
print("Enter list 1\n")
for i in range(n):
    c = input()
    a.append(c)
print("Enter integer values in list 2\n")
for i in range(n):
    c = input()
    b.append(c)
d = {}
for (i,j) in zip(a,b):
    d[i] = j
x = 0
for i in d.values():
    x = x + int(i)
print(x)
