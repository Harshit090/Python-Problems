a = []
b = []
with open('data.txt','r') as f:
    a = f.readlines()
    f.close()
with open('data1.txt','r') as f:
    b = f.readlines()
    f.close()
with open('data1.txt','w') as f:
    for i in range(len(a)):
        c = a[i][:-1] + " " + b[i]
        f.write(c)
    f.close()
with open('data1.txt','r') as f:
    b = f.readlines()
    print(b)
    f.close()

print(len(a))
