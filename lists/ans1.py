b = input("Enter a string to be added to list by a comma sepration \n")
a = b.split(',')
counter = 0
for i in a:
    if len(i) >= 2:
        if i[0] == i[-1]:
             counter +=1
        else:
            continue
print(counter)
