a = input("enter a string\n")
b = {}
'''
    for i in a:
        b[i] = 0
        for j in a:
            if i == j:
                b[i] = b[i] + 1
            else:
                continue
    print(b)
'''
for i in a:
    if i in b:
        pass
    else:
        x = a.count(i)
        b[i] = x
print(b)
