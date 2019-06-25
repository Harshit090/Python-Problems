d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}
x = 0
for i in d1.keys():
    for j in d2.keys():
        if i == j:
            x = d1[i] + d2[j]
            print(x,d1[i],d2[j])
            d3[i] = x
    if i in d3:
        continue
    else:
        d3[i] = d1[i]
for i in d2.keys():
    if i in d3:
        continue
    else:
        d3[i] = d2[i]
print(d3)
