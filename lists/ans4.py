a = []
c = []
for i in range(1,31):
    b = i*i
    a.append(b)
    if i < 6:
        c.append(b)
    elif i > 25:
        c.append(b)
    else:
        continue
print(a)
print(c)
