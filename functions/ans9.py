def add(a):
    def add1(b):
        c = 1 + b
        return c
    x = add1(a)
    return x
a = int(input("Enter a no\n"))
q = add(a)
print(q)
