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
result = []
for (i,j) in zip(a,b):
    d = {}
    d['colour name'] = i
    d['colour code'] = j
    result.append(d)
print(result)
