c = []
with open('data1.txt','r') as f:
    b = f.read()
    c = b.split('\n')
    print(c)
f.close()
