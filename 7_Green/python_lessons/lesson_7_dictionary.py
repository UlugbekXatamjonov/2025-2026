""" Dictionary - Lug'at """
"""
Dictionary — bu ma'lumotlarni “kalit: qiymat” (key: value) ko‘rinishida saqlaydigan ma'lumot turi.
"""

# talaba = {
#     "ism": "Ali",
#     "yosh": 14,
#     "sinfi": 7
# }

"""
Kalit (key) - "ism", "yosh", "sinfi"
Qiymat (value) - "Ali", 14, 7
"""

student = {
    "ism" :"Saida",
    "yosh": 8,
    "ball": 56.8,
    "friend" : ['Osiyo', "Oysha", 'Nigora']
}

# print(student)
# print(type(student)) # dict - dictionary - lug'at

# print(student["ism"])
# print(student["yosh"])
# print(student["ball"])
# print(student["friend"])

# print(f"Bizning eng aqilli o'quvchimiz {student['ism']} va u {student['yosh']} yoshda.")

""" Element qo'shish """
""" 1-usul """
# student["sinf"] = input("Sinf kiriting: ")
# print(student)

""" 2-usul """
# student.update({"maktab":"BM school"})
# print(student)


""" Elementni o'zgartirish """
""" 1-usul """
# student["sinf"] = '8 Green'
# print(student)

""" 2-usul """
# student.update({"maktab":"23- school"})
# print(student)


""" Elementni o'chirish"""
""" 1-usul """
# del student["ball"]
# print(student)

""" 2-usul """
# student.pop('ismm')
# print(student)

""" 3-usul """
# student.popitem() # oxiridan olib tashlaydi
# print(student)


""" Ro'yhatni tozalash """
# student.clear()
# print(student)

""" Ro'yhatdan nusxa olish """
# meals = student.copy()
# print(meals)

# meals2 = dict(student)
# print(meals2)

""" Ro'yhatni o'chirish """
# del student

"""
1-mashq
otam (onam, akam, ukam, va hokazo) degan lug'at tuzing va lug'atga shu inson haqida kamida 3 ta 
    m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida 
    konsolga chiqaring M: Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
    
2-mashq
Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. 
    Kamida uch kishining sevimli taomini konsolga chiqaring:
    N: Alining sevimli taomi osh
"""

# """ 1-mashq """
# otam = {
#     'ism':"Anvar",
#     'yil':1977,
#     'kasb':"Shifokor",
#     'manzil':""
# }
# print(f"Otamning ismi {otam['ism']}, {otam['yil']}-yilda, {otam['manzil']} tug'ilgan")

# """ 2-mashq """
# taomlar = {
#     'ali':"osh",
#     'muahammad':"manti"
# }

# print()


"""
4-mashq
Mashina haqida lug‘at tuzing: model, rang, yil kabi keylari bo'lsin.
    - “rang” ni boshqa rangga o‘zgartiring.
    - Yangi “tezlik” kaliti qo‘shing.
    - Mashina lug‘atidan biror elementni pop() bilan o‘chiring.
    - Va so'ngida lug'atni tozalab tashlang.
    
5-mashq
Do'stlar degan lug'at yasang unda key sifatida 5 ta do'stingizni ismi, value qismida esa uning sevimli mevasi nomi bo'lsin. 
Keyin barcha ma'lumotlarni na'munadagi kabi konsulga chiqaring.
Namuna: Naima Olmani yoqtiradi.
"""

""" 4-mashq """
mashina = {
    'model' : "Treker",
    'rang' : "qora",
    "yil" : 2024,
}
mashina["rang"] = 'oq'
mashina.update({'tezlik':'220'})
mashina.pop('yil')
mashina.clear()


""" 5-mashq """
friend = {
    'saida':"Anor",
    "oisha":"gilos",
    "nodira":"Qulpinay",
    "nigora":"Tarvuz",
    "sabina":"Malina",
    "ruxsora":"apelsin",
}

print(f"Saida {friend['saida']} ni yoqtiradi")
print(f"Sabina {friend['sabina']} ni yoqtiradi")
print(f"Ruxsora {friend['ruxsora']} ni yoqtiradi")


"""
8-mashq
Foydalanuvchidan uning yaqin do'sti haqidagi ma'lumotlarni so'ragan holda friend nomli lug'at tuzing. 
Lug'atda quidagi ma'lumotlar bo'lsin; ism, familiya, yosh, manzil, telefon raqam hamda kasb. 
Keyin lug'atdagi barcha ma'lumotlarni konsulga bir gap ko'rinishida chiqaring.
"""

frined = {
    'ismi' : input("Ismini kiriting: ")
}



"""
6-mashq
Oila deb nomlagan lug'at tuzing {“ota”:”Anvar”}. Keyin esa shu lug'atdan yangi family  deb nomlangan lug'atga nusxa oling. 
Va Har ikkala lug'atni konsulga chiqaring.

9-mashq
books deb nomlangan lug'at tuzing{“key”:”kitob nomi”}. Ichida 2 ta element bo'lsin. 
Yana  yangi  2 ta elementni 2 xil usulda qo'shing, 2 ta elementni 2 xil usulda yangilang, 
3 ta elementni 3 xil usulda o'chiring va so'ngra lug'atni tozalab tashlang.

10-mashq
Mevalar deb nomlangan lug'at tuzing, unda {“kalit”:”meva nomi”}  ko'rinishidagi 2 ta meva bo'lsin.   
Keyin esa:  2 ta yangi qiymat qo'shing,  2 ta qiymatni o'zgartiring, 2 ta qiymatni o'chiring. 
So'ngra mevalar lug'atini o'chirib tashlang;
"""



