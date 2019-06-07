a = int(input("Enter a no \n"))
b = int(input("Enter a no \n "))

for i in range(1,a+1):
    for j in range(1,b+1):
        print(i*j, end=' ')
    print("\n")
