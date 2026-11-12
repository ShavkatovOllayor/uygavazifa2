import json

with open("student.json", "r") as fayl:
    malumot = json.load(fayl)

malumot["ball"] = 95

with open("student.json", "w") as fayl:
    json.dump(malumot, fayl)

print("O‘quvchining yangi balli:", malumot["ball"])
print("Ma'lumotlar faylga saqlandi!")