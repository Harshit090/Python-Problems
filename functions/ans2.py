def insrt_string_middle(a,b):
    c = ''
    d = b

    for j in range(1,len(a)):
        if j <= len(a)/2:
            c = c + a[j-1]
        else:
            continue
    c = c + d
    for j in range(1,len(a)):
        if j >=len(a)/2:
            c = c + a[j]
        else:
            continue
    return c

a = input("Enter a string\n")
b = input("enter the string between wich string is to be inserted\n")

x = insrt_string_middle(b,a)
print(x)
