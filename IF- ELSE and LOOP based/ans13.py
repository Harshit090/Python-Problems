for i in range(15):
    for j in range(17):
        if i < 3:
            print("0", end=" ")
        if i >= 3 and i < 6:
            if j < 4:
                print("0", end=" ")
        if i >= 6 and i < 9:
            print("0", end=" ")
        if i >= 9 and i < 12:
            if j < 13:
                print(" ", end=" ")
            else:
                print("0", end=" ")
        if i >= 12:
            print("0", end=" ")
    print("\n")
