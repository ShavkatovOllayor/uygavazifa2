import csv

with open("sportchilar.csv", "r") as fayl:
    oqish = csv.DictReader(fayl)

    eng_yuqori = None

    print("Barcha sportchilar:")
    print("-------------------")

    for sportchi in oqish:
        ism = sportchi["ism"]
        sport = sportchi["sport"]
        ball = int(sportchi["ball"])

        print("Ism:", ism)
        print("Sport:", sport)
        print("Ball:", ball)
        print("-------------------")

        
        if ball > 80:
            print("80 balldan yuqori:", ism, ball)

        
        if eng_yuqori is None or ball > eng_yuqori["ball"]:
            eng_yuqori = {
                "ism": ism,
                "sport": sport,
                "ball": ball
            }

    print("\nEng yuqori ball olgan sportchi:")
    print("Ism:", eng_yuqori["ism"])
    print("Sport:", eng_yuqori["sport"])
    print("Ball:", eng_yuqori["ball"])