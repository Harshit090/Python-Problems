a = input()
c = ' '
c = c + a[0]
for i in a[1:]:
    if i is a[0]:
        c = c + '$'
    else:
        c = c + i
print(a,c)
