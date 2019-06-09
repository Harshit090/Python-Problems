l = [] ; n = []
x = int(input("Enter no of words to be added to list"))
for i in range(x):
    a = input("Enter a string\n")
    l.append(a)

for i in range(x):
    n.append(len(l[i]))

b = len(l[0])

for i in range(x):
    if b < len(l[i]):
        b = len(l[i])
    else:
        continue
print(b,"is the length of the longest string in the list")
