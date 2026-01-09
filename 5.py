import os
os.system("cls")

dict = {
    'Math': [88, 89, 90],
    "Physics": [92, 94, 89],
    "Chemistry": [90, 87, 93]
}

change = int(input("Change: "))
for key in dict:
    for i in range(len(dict[key])):
        dict[key][i] += change

print(dict)    
