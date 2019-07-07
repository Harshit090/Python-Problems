c = []
x = 0
with open('data.txt','r') as f:
    b = f.read()
    c = b.split(' ')
    for i in c:
        if x < len(i):
            x = len(i)
            y = i
        else:
            continue
print(x , y)
f.close()
