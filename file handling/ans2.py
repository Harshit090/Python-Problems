with open('data.txt','w') as f:
    a = "\nEntered some data again"
    f.write(a)
with open('data.txt','r') as f:
    b = f.read()
    print(b)
f.close()
