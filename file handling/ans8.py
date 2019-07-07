import os
a = os.stat('data.txt')
print(a.st_size)
