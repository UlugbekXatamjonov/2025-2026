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


print(talaba)
print(talaba["ism"])
print(talaba["yosh"])
print(f"Talabaning ismi {talaba['ism']} va u {talaba['yosh']} yoshda")


""" Qiymat qo'shish """
""" 1-usul """
talaba["maktab"] = "BM school"
print(talaba)

""" 2-usul """
talaba.update({"baho":5})
print(talaba)


""" Qiymatni o'zgartirish """
""" 1-usul """
talaba["maktab"] = "2-maktab"
print(talaba)

""" 2-usul """
talaba.update({"yosh":20})
print(talaba)

""" Qiymatni o'chirish """
""" 3 usul """
del talaba["ism"]
print(talaba)

talaba.pop("yosh")
print(talaba)

talaba.popitem() # ro'yhatning oxiridagi elementni olib tashlaydi
print(talaba)






