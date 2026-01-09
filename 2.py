import os
os.system("cls")

login = {
    "jeymsBond": "agent007",
    "tony_stark": "ironman101",
    "piterParker": "spider.12.12",
    "sherlok": "sher.104"
}

username = input("Username kiriting: ")
parol = input("Parol kiriting: ")

if username in login:
    if parol==login[username]:
        print("Hisobga kirdingiz!")
    else:
        print("Parol noto'g'ri!")
else:
    print("Bunday foydalanuvchi mavjud emas!")
