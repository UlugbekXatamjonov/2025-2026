""" Dictionary - Lug'atlar """
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

""" 
taomlar = {'ali':'osh'}
nomi    = {'key':'value'}
"""

# print(lugat)
# print(lugat["ism"])
# print(lugat["yosh"])

# print(f"{lugat['ism']} yaxshi bola, va yoshi {lugat['yosh']} yoshda")

# print(type(lugat)) # dict --> dictionary


""" Qiymat qo'shish """
""" 1-usul """
# lugat['kasb'] = 'Quruvchi'
# lugat['manzil'] = "Ipak yo'li ko'chasi, 67-uy"
# print(lugat)

""" 2-usul """
# print(lugat)
# lugat.update({"mashina":"Matiz"})


""" Qiymatni o'zgartirish """
# lugat.update({"yosh":12})
# lugat["ism"] = "Saidbek"

# print(lugat)

"""
1) otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta 
    m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida 
    konsolga chiqaring 
    M: Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
  
"""
otam = {
    'ism':"Suhrobjon",
    "t_yil":1981,
    "shahri":"Namangan",
    "kasb":"Shifokor",
}

# print(f"Otamning ismi {otam['ism']}, {otam['t_yil']}-yilda tug'ilgan, {otam['shahri']} shahrida tug'ilgan. Ularning kasbi {otam['kasb']}.")


"""
2) Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. 
    Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
"""

meals = {
    'father':"Osh",
    "mother":"Sho'rva",
    'brother':"Somsa",
    'sister':"Chuchvara"
}

# print(f"My father's favorite meal is {meals['father']}")

"""
3) Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 7 ta so'z(atamani) kiriting 
    (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
"""

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


""" keys, values """

davlatlar ={
    "o'zbekiston":"Toshkent",
    "turkiya":"Anqara",
    "aqsh":"Washington",
    'rossiya':"Moskva",
    "angilya":"London"
}

# print(davlatlar)
# print(davlatlar.keys())
# print(davlatlar.values())


# for davlat in davlatlar.keys():
#     print(davlat)

# for poytaxt in davlatlar.values():
#     print(poytaxt)


"""
mashq
Do’stlaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
"""

"""
mashq
Foydalanuvchidan uning yaqin do'sti haqidagi ma'lumotlarni so'ragan holda friend nomli lug'at tuzing. 
Lug'atda quidagi ma'lumotlar bo'lsin; ism, familiya, yosh, manzil, telefon raqam hamda kasb. 
Keyin lug'atdagi barcha ma'lumotlarni konsulga bir gap ko'rinishida chiqaring.
"""

# friend = {
#     'ism' : input("Ism kiriting: "), 
# }

# print(friend)


"""
15-mashq
Ingliz-O'zbek lug'atini Tuzing. Avval lug'atdagi faqat ingliz tilidasi so'zlarni keyin esa faqat o'zbek tilidagi so'zlarni konsulga chiqaring.
"""

eng_uzb = {
    'apple':"olma",
    "pear":"nok",
    "good":"yaxshi"
}

# 1-usul
# print(eng_uzb.keys())
# print(eng_uzb.values())

# 2-usul
# for key in eng_uzb.keys():
#     print(key)

# for value in eng_uzb.values():
#     print(value)




""" Qiymatni o'chirish """
""" 3 usul """
# del eng_uzb["apple"]
# print(eng_uzb)

# eng_uzb.pop("good")
# print(eng_uzb)

# eng_uzb.popitem() # lug'atni oxiridagi elementni olib tashlaydi
# print(eng_uzb)



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


"""
 
9-mashq
books deb nomlangan lug'at tuzing{“key”:”kitob nomi”}. Ichida 2 ta element bo'lsin. 
Yana  yangi  2 ta elementni 2 xil usulda qo'shing, 2 ta elementni 2 xil usulda yangilang, 
3 ta elementni 3 xil usulda o'chiring va so'ngra lug'atni tozalab tashlang.
"""



"""
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
  
"""

""" 10-mashq """

# mevalar = {
#     "meva1":"banan",
#     "meva2":"olma",
#     "meva3":"behi"
# }
# print(mevalar)

# mevalar["meva4"] = "shaftoli"
# mevalar["meva5"] = "kiwi"
# print(mevalar)

# mevalar["meva2"] = "mango"
# mevalar["meva3"] = "ananas"
# print(mevalar)

# del mevalar["meva1"]
# del mevalar["meva4"]
# print(mevalar)

# del mevalar

""" 11-mashq """


# shaharlar = {
#     "shahar1":input("1-shaharni kiriting: "),
#     "shahar2":input("2-shaharni kiriting: "),
#     "shahar3":input("3-shaharni kiriting: "),
#     "shahar4":input("4-shaharni kiriting: "),
#     "shahar5":input("5-shaharni kiriting: "),
#     "shahar6":input("6-shaharni kiriting: "),
#     "shahar7":input("7-shaharni kiriting: ")
# }
# print(shaharlar)

# del shaharlar["shahar2"]
# shaharlar.pop("shahar3")
# shaharlar.popitem()
# print(shaharlar)

# shaharlar.update({"shahar8":"purtugaliya"})
# shaharlar ["shahar9"] = "italiya"


# print(shaharlar)

# shaharlar.clear()
# print(shaharlar)

# del shaharlar



""" 12-mashq """
# fruits = {
#     "meva1":"olma",
#     "meva2":"banan"
# }
# print(fruits)

# fruits["meva3"] = "ananas"
# fruits.update({"meva4":"apilsin"})
# print(fruits)

# fruits["meva3"] = "apelsin"
# fruits.update({"meva4":"mandarin"})
# print(fruits)

# del fruits["meva1"]
# fruits.popitem()
# fruits.pop("meva2")
# print(fruits)

# fruits.clear()
# print(fruits)


"""
16-mashq
Mashina nomidan iborat lug'at Tuzing. {“Mashina nomi”:mashinaning narxi} bo'lsin. Foydalanuvchidan biror mashina nomini so'rang agar u sizning lug'atingizda bor mashina nomini aytsa, unga o'sha mashinaning  narxini ayting, agar bo'lmasa “Bizda bu mashina yo'q edi” degan habarni chiqaring.
# """

# cars = {
#     'bmw':222000,
#     'matiz':5000,
# }

# savol = input("Mashina nomini kiriting: ").lower()
# print(cars.get(savol, "Bizda bu mashina yo'q"))


# if savol in cars:
#     print(f"{savol.title()} ning narxi {cars[savol]} $")
# else:
#     print(f"Bizda {savol.title()} nomli mashina yo'q")



""" .items() """

# print(cars.keys())
# print(cars.values())


# for key, value in cars.items():
#     print(f"{key} ning narxi {value} $")



""" Do'kon """
# mahsulotlar = {
#     "olma":4_500,
#     "nok":2_000,
#     "non":3_000,
#     "asal":15_000,
#     "tuz":2_500,    
# }
# bor = []
# yoq = []
# summa = 0

# print("Assalomu aleykum ! \nDo'konimizga xush kelibsiz !")
# print("Bizning do'konda quidagi mahsulotlar bor: ")

# for mahsulot, narx in mahsulotlar.items():
#     print(f"{mahsulot} - {narx} so'm")

# soni = int(input("Nechta mahsulot sotib olmoqchisiz: "))
# for s in range(soni):
#     savol = input(f"{s+1}-mahsulot nomini kiriting: ")

#     if savol in mahsulotlar:
#         bor.append(savol)
#     else:
#         yoq.append(savol)


# for mahsulot, narx in mahsulotlar.items():
#     if mahsulot in bor:
#         summa = summa + narx # summa += narx


# print(f"Siz sotib olmoqchi bo'lgan {len(bor)} ta mahsuloit bizda bor, va ularning ummuniy narxi {summa} so'm")
# print(f"Lekin bizda quidagi {len(yoq)} ta mahsulotlar yo'q: {yoq}")

