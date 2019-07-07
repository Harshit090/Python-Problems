a = input("ENter a list with space seperation\n")
b = a.split(' ')
with open('test.txt','w') as f:
    for i in b:
        f.write(i + '\n')
    f.close()
with open('test.txt','r') as f:
    b = f.read()
    print(b)
    f.close()
