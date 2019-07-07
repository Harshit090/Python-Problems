a = []
c = []
words = []
avg = []
d = {}
with open('data.txt', 'r') as f:
    b = f.read()
    a = b.split('\n')
    f.close()
for i in range(len(a)):
    x = len(a[i])
    c.append(x)
for i in a:
    y = i.split(' ')
    words.append(len(y))
print(a)
print(c)
print(words)
for i in range(len(c)):
    n = c[i]/words[i]
    avg.append(n)
print(avg)

for i in range(len(avg)):
    d['line no' + ' ' + str(i)] = avg[i]
print(d)
