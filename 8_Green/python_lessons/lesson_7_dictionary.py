""" Dictionary - Lug'at """
"""
Dictionary — bu ma'lumotlarni “kalit: qiymat” (key: value) ko‘rinishida saqlaydigan ma'lumot turi.
"""

talaba = {
    "ism": "Ali",
    "yosh": 14,
    "sinfi": 7,
    'dostlar':["Olim", "Anvar", "Iroda"]
}

"""
Kalit (key) - "ism", "yosh", "sinfi"
Qiymat (value) - "Ali", 14, 7
"""


# print(talaba)
# print(talaba["ism"])
# print(talaba["yosh"])
# print(f"Talabaning ismi {talaba['ism']} va u {talaba['yosh']} yoshda")


""" Qiymat qo'shish """
""" 1-usul """
# talaba["maktab"] = "BM school"
# print(talaba)

""" 2-usul """
# talaba.update({"baho":5})
# print(talaba)


""" Qiymatni o'zgartirish """
""" 1-usul """
# talaba["maktab"] = "2-maktab"
# print(talaba)

""" 2-usul """
# talaba.update({"yosh":20})
# print(talaba)

""" Qiymatni o'chirish """
""" 3 usul """
# del talaba["ism"]
# print(talaba)

# talaba.pop("yosh")
# print(talaba)

# talaba.popitem() # ro'yhatning oxiridagi elementni olib tashlaydi
# print(talaba)


taomlar = {
    'ali':'osh',
    'vali':'shashlik',
    'hasan':"lag'mon",
    'husan':"mastava",
    'olim':"somsa",
    'nodir':"kabob",
}

""" Ro'yhatni tozalash """
# taomlar.clear()
# print(taomlar)

""" Ro'yhatdan nusxa olish """
# meals = taomlar.copy()
# print(meals)

# meals2 = dict(taomlar)
# print(meals2)




""" keys() va values() metodlar """
davlatlar = {
    'uzbekistan':"Tashkent",
    'usa':"Vashington",
    'russian':"Moscow",
}
print(davlatlar.keys())
print(davlatlar.values())

for key in davlatlar.keys():
    print(f"{key}")

for value in davlatlar.values():
    print(f"{value}")

""" items() """
print(davlatlar)
print(davlatlar.items())
for davlat, shahar in davlatlar.items():
    print(f"{davlat.title()}ning poytaxti  {shahar.title()} shahri")

davlatlar = {
    'aqsh':"vashington",
    'xitoy':"pekin",
    "turkiya":"anqara",
    'fransiya':"parij"
}

savol = input("Davlat yoki poytaxt nomini kiriting: ").lower()
for davlat, shahar in davlatlar.items():
    if savol == davlat:
        print(f"{davlat.title()} ning poytaxti {shahar} shahri")
    elif savol == shahar:
        print(f"{shahar.title()} {davlat.title()}ning poytahti.")
        
if savol not in davlatlar.keys() and savol not in davlatlar.values():
    print(f"Bizda {savol} haqida ma'lumot yo'q")