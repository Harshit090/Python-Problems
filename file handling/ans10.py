c = []
a = input("ENter a list with space seperation\n")
b = a.split(' ')
with open('test1.txt','w') as f:
    for i in b:
        f.write(i + '\n')
    f.close()
with open('test1.txt','r') as f:
    d = f.read()
    for i in d:
        if i == '\n':
            continue
        else:
            c.append(i)
    print(c)
    f.close()
