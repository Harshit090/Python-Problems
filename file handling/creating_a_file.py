with open('data.txt','w') as f:
    a = "Entered some data in file. looooooooool (-_>)"
    f.write(a)
with open('data.txt','r') as f:
    b = f.read()
    print(b)
f.close()
