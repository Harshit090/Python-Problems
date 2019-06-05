item = []
result = []
b = int(input("Enter no of binary no to be checked"))
for i in range(0,b):
    a = input("Input a binary no:\t")
    item.append(a)

for i in range(0,b):
    c = int(item[i], 2)
    d = c % 5
    if d is 0:
        result.append(item[i])
    else:
        continue
print(result)
