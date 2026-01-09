import os
os.system("cls")

list = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
dict = {}
for k,v  in list:
    if k in dict:
        dict[k].append(v)
    else:
        dict[k] = [v]