def sorting_string(b):
    a = []
    a = b.split('-')
    a.sort()
    return a

def sortng_print(x):
    c = ''
    for i in x:
        if i < x[-1]:
            c = c + i + '-'
        else:
            c = c + i
    return c

b = input("Entre a list with hyphen seprated words\n")
x = sorting_string(b)
y = sortng_print(x)
print(y)
