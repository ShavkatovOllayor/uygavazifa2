import csv

with open("expenses.csv", "r") as fayl:
    oqish = csv.DictReader(fayl)

    jami = 0
    soni = 0
    eng_katta = None

    print("Barcha xarajatlar:")

    for xarajat in oqish:
        nom = xarajat["nom"]
        summa = int(xarajat["summa"])

        print(nom, "-", summa, "so'm")

        jami += summa
        soni += 1

        if eng_katta is None or summa > eng_katta["summa"]:
            eng_katta = {
                "nom": nom,
                "summa": summa
            }

    print("\nJami xarajat:", jami, "so'm")
    print("Eng katta xarajat:", eng_katta["nom"])
    print("Summasi:", eng_katta["summa"], "so'm")
    print("Xarajatlar soni:", soni)