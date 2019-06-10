a = input("Enter a sentence\n")
b = a.split(" ")
counter = []
for i in range(len(b)):
    c = 0
    for j in range(len(b)):
        if b[i] == b[j]:
            c = c + 1
        else:
            continue
    counter.append(c)
print(a,"\n",b,"\n",counter)
