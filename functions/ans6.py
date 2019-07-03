def panagram_fun(a):
    b = a.lower()
    d = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    c = {}
    e = []
    for i in d:
        if i in b:
            x = True
            continue
        else:
            x = False
            break
    return x

a = input("Enter a string\n")
b = panagram_fun(a)
if b == True:
    print("It is a panagram")
else:
    print("It is not a panagram")
