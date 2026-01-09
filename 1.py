import os
os.system("cls")

students = {
    "Samandar": 18,
    "Muzaffar": 19,
    "Xojiakbar": 16,
    "Islom": 20,
    "Asomiddin": 14,
    "Sobitjon": 17,
    "Shoxruh": 20
}
for i in students:
    if students[i]>=18:
        print(i)