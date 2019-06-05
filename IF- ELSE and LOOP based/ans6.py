for i in range(7):
    for j in range(5):
        if i is 0 and j is 0:
            print(" ", end=' ')
        elif i is 0 and j is 4:
            print(" ", end=' ')
        elif i is 0:
            print("*", end=' ')
        elif i is 3:
            print('*' , end=' ')
        else:
            if j is 0 or j is 4:
                print('*', end=' ')
            else:
                print(' ', end=' ')
    print("\n")
