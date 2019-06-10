a = input("enter a string \n")
b = ''

for i in range(len(a)):
    if i%2 is 0:
        b = b + a[i]
    else:
        continue

print(a,b)
