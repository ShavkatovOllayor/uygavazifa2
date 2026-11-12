import json
with open("phone.json", "r") as fayl:
    malumot = json.load(fayl)
print("Telefon modeli:", malumot["model"])
print("Brendi:", malumot["brend"])
print("Eski narxi:", malumot["narx"])


yangi_narx = int(input("Yangi narxni kiriting: "))

malumot["narx"] = yangi_narx

with open("phone.json", "w") as fayl:
    json.dump(malumot, fayl, indent=4)

print("Yangi narx:", malumot["narx"])
print("Ma'lumotlar saqlandi!")