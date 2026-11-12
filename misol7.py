import csv

with open("products.csv", "r") as fayl:
    oqish = csv.DictReader(fayl)

    eng_qimmat = None

    print("Barcha mahsulotlar:")

    for mahsulot in oqish:
        nom = mahsulot["nom"]
        narx = int(mahsulot["narx"])
        miqdor = int(mahsulot["miqdor"])

        umumiy = narx * miqdor

        print("Nomi:", nom)
        print("Narxi:", narx)
        print("Miqdori:", miqdor)
        print("Umumiy qiymati:", umumiy)
        print("-------------------")

        if eng_qimmat is None or narx > eng_qimmat["narx"]:
            eng_qimmat = {
                "nom": nom,
                "narx": narx
            }

    print("Eng qimmat mahsulot:")
    print(eng_qimmat["nom"])
    print("Narxi:", eng_qimmat["narx"])