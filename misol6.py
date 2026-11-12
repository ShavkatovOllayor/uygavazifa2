import csv

with open("students.csv", "r") as fayl:
    oqish = csv.DictReader(fayl)

    print("Barcha o'quvchilar:")
    print("20 yoshdan kattalar:")

    for talaba in oqish:
        print(talaba["ism"])

        if int(talaba["yosh"]) > 20:
            print("20 yoshdan katta:", talaba["ism"], talaba["yosh"])