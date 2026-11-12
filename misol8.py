import csv

ism = input("Ismingizni kiriting: ")
yosh = input("Yoshingizni kiriting: ")
kurs = input("Kursingizni kiriting: ")

with open("students.csv", "a") as fayl:
    yozish = csv.writer(fayl)
    yozish.writerow([ism, yosh, kurs])

print("\nYangi o'quvchi qo'shildi!")

with open("students.csv", "r") as fayl:
    oqish = csv.reader(fayl)

    print("\nBarcha o'quvchilar:")
    for qator in oqish:
        print(qator)