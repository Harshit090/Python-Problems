a = input("Enter a string \n")
b = input("Enter a string \n")
c = ''
d = ''
c = c + a[:2]
d = d + b[-2:]
e = c + d

if len(a) > 2 and len(b) > 2:
    print(e, c ,d)
if len(e) >2:
    print(e, c ,d)
