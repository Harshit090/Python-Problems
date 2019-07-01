def add_tags(a,b):
    c = "<"+a+">"+b+"<"+a+">"
    return c
x = input("enter tag\n")
y = input("enter data\n")

d = add_tags(x,y)
print(d)    
