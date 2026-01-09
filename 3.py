import os
os.system("cls")

id = ['S001', 'S002', 'S003', 'S004']
street = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
number = [85, 98, 89, 92]
list = []
for i in range(len(id)):
    list.append({id[i]: {street[i]: number[i]}})
print(list)    

