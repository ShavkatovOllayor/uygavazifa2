import json

with open("user.json", "r") as fayl:
    malumot = json.load(fayl)

print("Ismi:", malumot["ism"])
print("Yoshi:", malumot["yosh"])
print("Shahri:", malumot["shahar"])