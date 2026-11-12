import json

talaba = {
    "ism": "Sardor",
    "yosh": 20,
    "kurs": 2
}
json_matn = json.dumps(talaba)
print("JSON matn:")
print(json_matn)
yangi_talaba = json.loads(json_matn)

print("Talabaning ismi:", yangi_talaba["ism"])