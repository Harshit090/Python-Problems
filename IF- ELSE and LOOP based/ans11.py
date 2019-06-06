for i in range(7):
    for j in range(5):
        if i is 0 and j is 0:
            print(" ", end=' ')
        elif i is 0:
            print("*", end=' ')
        elif i is 1:
            if j is 0:
                print('*' , end=' ')
            else:
                print(' ' , end=' ')
        elif i is 2:
            if j is 0:
                print('*' , end=' ')
            else:
                print(' ' , end=' ')
        elif i is 3:
            if j is 0 or j is 4:
                print(' ' , end=' ')
            else:
                print('*' , end=' ')
        elif i is 4:
            if j is 4:
                print('*' , end=' ')
            else:
                print(' ' , end=' ')
        elif i is 5:
            if j is 4:
                print('*' , end=' ')
            else:
                print(' ' , end=' ')
        elif i is 6:
            if j is 4:
                print(' ' , end=' ')
            else:
                print('*' , end=' ')

    print("\n")
