n = int(input("enter no of items to added in a list\n"))
a = []
b = []
print("Enter list 1\n")
for i in range(n):
    c = input()
    a.append(c)
print("Enter list 2\n")
for i in range(n):
    c = input()
    b.append(c)
d = {}
for (i,j) in zip(a,b):
    d[i] = j

key = input("Enter the key to be checked\n")

if key in d.keys():
    print("present")
else:
    print("Not present")
