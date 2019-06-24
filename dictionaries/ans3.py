import operator
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
sorted_x = sorted(d.items(), key=operator.itemgetter(1))
sorted_x1 = sorted(d.items(), key=operator.itemgetter(1), reverse = True)
dict1 = dict(sorted_x1)
dict = dict(sorted_x)
print(dict)
print(dict1)
