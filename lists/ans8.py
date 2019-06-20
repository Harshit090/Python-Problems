n = int(input("Enter range \n"))
a = []
b = []
for i in range(n):
    b = []
    for j in range(1,6):
        c = i*5 + j
        b.append(c)
    a.append(b)
print(a)
