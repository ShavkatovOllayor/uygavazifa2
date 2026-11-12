import json

with open("product.json", "r") as fayl:
    malumot = json.load(fayl)

nom = malumot["nom"]
narx = malumot["narx"]
miqdor = malumot["miqdor"]

umumiy = narx * miqdor

print("Mahsulot:", nom)
print("Narxi:", narx)
print("Miqdori:", miqdor)
print("Umumiy qiymati:", umumiy, "so'm")