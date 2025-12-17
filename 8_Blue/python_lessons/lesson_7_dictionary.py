""" Dictionary - Lug'at """
"""
Dictionary — bu ma’lumotlarni “kalit: qiymat” (key: value) ko‘rinishida saqlaydigan ma'lumot turi.
"""

son = 6
onlik_son = 9.5
ism = "Muhammad"
ismlar = ["Olim", "Ahmad", "Abbos"]


lugat = {
    'ism':"Nodirbek",
    'yosh':34,
    "ball":234.5,
    'oila':["Asadbek", "Nozima", "Gulg'uncha"]
}
# print(lugat)
# print(type(lugat))


talaba = {
    "ism": "Ali",
    "yosh": 14,
    "sinfi": 7
}

"""
Kalit (key) - "ism", "yosh", "sinfi"
Qiymat (value) - "Ali", 14, 7
"""
# print(talaba)
# print(talaba["ism"])
# print(talaba["sinfi"])
# print(talaba["yosh"])
# print(f"Talabaning ismi {talaba['ism']} va u {talaba['yosh']} yoshda")


""" Qiymat qo'shish """
# """ 1-usul """
# talaba["maktab"] = "BM school"
# print(talaba)

# """ 2-usul """
# talaba.update({"baho":5})
# print(talaba)


""" Qiymatni o'zgartirish """
# """ 1-usul """
# talaba["maktab"] = "2-maktab"
# print(talaba)

# """ 2-usul """
# talaba.update({"yosh":20})
# print(talaba)

"""
1-mashq
otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta 
    m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida 
    konsolga chiqaring M: Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
    
2-mashq
Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. 
    Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
    
3-mashq
Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z(atamani) kiriting 
    (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
"""

ota = {
    "ism":"",
    "familya":""
}

# print(f"Mening otamning ismi {ota['ism']}")







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

""" Ro'yhatdan nusha olish """
# meals = taomlar.copy()
# print(meals)

# meals2 = dict(taomlar)
# print(meals2)



python = {
    'print':"Biror ma'lumotni koinsulga chiqaradi",
    "komment":"kommentga olish",
    "int":"Butun son"
}

# print(f"print - {python['print']}")


""" get() metodi """
# savol = input("Python dan biror atamani kiriting: ").lower()

# print(python[savol]) 
# print(python.get(savol, "Bu haqda bizda ma'lumot yo'q"))

"""    
4-mashq
Mashina haqida lug‘at tuzing: model, rang, yil kabi keylari bo'lsin.
    - “rang” ni boshqa rangga o‘zgartiring.
    - Yangi “tezlik” kaliti qo‘shing.
    - Mashina lug‘atidan biror elementni pop() bilan o‘chiring.
    - Va so'ngida lug'atni tozalab tashlang.
"""

"""
    
9-mashq
books deb nomlangan lug'at tuzing{“key”:”kitob nomi”}. Ichida 2 ta element bo'lsin. 
Yana  yangi  2 ta elementni 2 xil usulda qo'shing, 2 ta elementni 2 xil usulda yangilang, 
3 ta elementni 3 xil usulda o'chiring va so'ngra lug'atni tozalab tashlang.

10-mashq
Mevalar deb nomlangan lug'at tuzing, unda {“kalit”:”meva nomi”}  ko'rinishidagi 2 ta meva bo'lsin.   
Keyin esa:  2 ta yangi qiymat qo'shing,  2 ta qiymatni o'zgartiring, 2 ta qiymatni o'chiring. 
So'ngra mevalar lug'atini o'chirib tashlang;


11-mashq
Foydalanuvchidan 7 ta shahar nomini so'rang va shaharlar deb nomlangan lug'at tuzing. 
3 ta elementni 3 hil usulda o'chirib tashlang. Yangi 2 ta shahar nomini 2 xil usulda qo'shing.
Ro'yhatni tozalab yuboring, so'ngra uni o'chirib tashlang.

12-mashq
fruts deb nomlangan lug'at tuzing{“key”:”meva nomi”}. Ichida 2 ta element bo'lsin. 
Yana yangi 2 ta elementni 2 xil usulda qo'shing, 2 ta elementni 2 xil usulda yangilang, 
3 ta elementni 3 xil usulda o'chiring va so'ngra lug'atni tozalab tashlang.
    
13-mashq
Teachers deb nomlangan lug'at tuzing, unda {“fan nomi”:”O'qtuvchi ismi”}  ko'rinishidagi 2 ta ism bo'lsin.   
Keyin esa:  2 ta yangi qiymat qo'shing,  2 ta qiymatni o'zgartiring, 2 ta qiymatni o'chiring. So'ngra lug'atni o'chirib tashlang;

14-mashq
Shaharlar deb nomlangan lug'at tuzing, unda {“ixtiyoriy kalit”:” shahar nomi”} ko'rinishidagi 2 ta shahar bo'lsin. 
Keyin esa: 2 ta yangi qiymat qo'shing, 2 ta qiymatni o'zgartiring, 2 ta qiymatni o'chiring. 
So'ngra shaharlar lug'atini o'chirib tashlang;  
"""

"""
Restoran menusi lug'atini tuzing(kamida 7 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat
buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda 
bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
"""

# menu = {
#     "choy":5000,
#     "salat":12000,
#     'osh':35000
# }

# savol1 = input("1-taomni kiriting: ")
# savol2 = input("2-taomni kiriting: ")
# savol3 = input("3-taomni kiriting: ")


# print(menu.get(savol1, f"Bizda {savol1} yo'q"))
# print(menu.get(savol2, f"Bizda {savol2} yo'q"))
# print(menu.get(savol3, f"Bizda {savol3} yo'q"))


""" keys(), values() """
# print(menu)
# print(menu.keys())
# print(menu.values())

# for taom in menu.keys():
#     print(taom)

# for narx in menu.values():
#     print(narx)


""" items() """
# for taom, narx in menu.items():
#     print(f"{taom}ning narxi {narx} so'm")

""" 19-mashq
Ingliz-O'zbek lug'atini Tuzing. Key o'rnida ingliz tilidagi so'z, value o'rnida o'zbekcha so'z bo'lsin. Foydalanuvchidan biror so'z so'rang agar u lug'atda bor so'zni kiritsa unga u so'zning tarjimasini qaytaring, agar bo'lmasa “Bizda bu so'z haqida ma'lumot yo'q” degan javobni qaytaring.
"""

# eng_uzb = {
#     'apple':"olma",
#     'apricot':"o'rik",
#     'apple':"olma",
#     'apricot':"o'rik"
# }

# savol = input("So'z kiriting: ").lower()

# for eng, uz in eng_uzb.items():
#     if savol == eng:
#         print(f"{eng} - {uz}")
#     elif savol == uz:
#         print(f"{uz} - {eng}")

# if savol not in eng_uzb.keys() and savol not in eng_uzb.values():
#         print(f"{savol} haqida ma'lumot yo'q !")



mahsulotlar = {
    "olma":4_500,
    "nok":2_000,
    "non":3_000,
    "asal":15_000,
    "tuz":2_500,    
}


# bor = []
# yoq = []
# summa = 0


# print("Assalomu aleykum do'konimizga hush kelibsiz !")
# print("Bizning do'konda quidagi mahsulotlar bor: ")

# for mahsulot, narx in mahsulotlar.items():
#     print(f"{mahsulot} - {narx} so'm")

# xaridlar_soni=  int(input("Nechta mahsulot olmoqchisiz: "))

# for i in range(xaridlar_soni):
#     savol = input(f"{i+1}-mahsulot nomini kiriting: ") 
#     if savol in mahsulotlar:
#         bor.append(savol)
#     else:
#         yoq.append(savol)

# for mahsulot, narx in mahsulotlar.items():
#     if mahsulot in bor:
#         summa += narx

# print(f"Bizda siz aytgan quidagi {len(bor)} ta mahsulotlar bor {bor} va ularning umumiy narxi {summa} so'm")
# print(f"Bizda siz aytgan quidagi {len(yoq)} ta mahsulotlar yo'q {yoq}")





