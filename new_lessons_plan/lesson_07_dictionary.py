""" Dictionary - Lug'at """
"""
Dictionary — bu ma'lumotlarni “kalit: qiymat” (key: value) ko‘rinishida saqlaydigan ma'lumot turi.
"""

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

""" get() metodi """
# print(taomlar["abror"])
# print(taomlar.get("nodir","Bunday key yo'q"))



""" items() metodi """
# print(taomlar)
# print(taomlar.items())
# for key, value in taomlar.items():
#     print(f"{key.title()}ning sevimli taomi {value.title()}")
    
    
# davlatlar = {
#     'uzbekistan':"Tashkent",
#     'usa':"Vashington",
#     'russian':"Russian",
# }
# savol = input("Davlat nomini kiriting: ").lower()
# if savol in davlatlar:
#     print(f"Siz so'ragan {savol.upper()}ning poytaxti {davlatlar[savol].title()}")
# else:
#     print(f"Siz so'ragan {savol.title()} haqida bizda malumot yo'q")



""" keys() va values() metodlar """
# print(davlatlar.keys())
# print(davlatlar.values())

# for key in davlatlar.keys():
#     print(f"{key}")

# for value in davlatlar.values():
#     print(f"{value}")


# ismlar = {
#     '1':'Ali',
#     '2':'Hasan',
#     '3':'Husan',    
# }
# for kalit, qiymat in ismlar.items(): # items --> buyhum 
#     print(f"Salom do'stim {qiymat} sening tartib raqaming {kalit}")

# for key in ismlar.keys(): # key
#     print(f"Salom do'stim sening tartib raqaming {key}")

# for qiymat in ismlar.values(): # value   
#     print(f"Salom do'stoim {qiymat}")



""" Do'kon """
# mahsulotlar = {
#     "olma":4500,
#     "nok":2000,
#     "non":3000,
#     "asal":15000,
#     "tuz":2500,    
# }


# zakaz = []
# narx = 0
# yoq = []
# print("Assalomu aleykum do'konimizga hush kelibsiz !")
# son = int(input("\nNechta mahsulot sotib olishni hohlaysiz: "))# foydalanuvchi olmoqchi bo'lgan mahsulotlari soni

# print("Bizning do'konda quidagi mahsulotlar bor: ")
# for m in mahsulotlar:
#     print(f"{m.title()}", end=' ')# do'konimizdagi mahsulotlarni eslatib o'tamiz

# for n in range(son): #mahsulotlarni birma bir so'raymiz
#     xarid = input(f"\n{n+1}-mahsulot: ").lower()
#     zakaz.append(xarid)

# for k,v in mahsulotlar.items(): # sotib olingan mahsulotlar agar do'konimizda bo'lsa ularning narxini hisoblaymiz   
#         if k in zakaz:
#             narx += v 
            
# print("Siz sotib olmoqchi bo'lgan mahsulotlar quidagilar: ") #sotib olingan mahsulotlarni va ularning ummumiy narxini chiqaramiz
# for z in zakaz:
#     if z in mahsulotlar:
#         print(f"{z.title()}", end=" ")
#     else: 
#         yoq.append(z)


# print(f"va ularning ummumiy narxi: {narx} so'm") # do'konimizda yo'q mahsulotlarni eslatamiz
# print("Quidagi mahsulotlar esa bizning do'konda mavjud emas: ")
# for y in yoq:
#     print(f'{y.title()}', end=' ')





"""
1-mashq
otam (onam, akam, ukam, va hokazo) degan lug'at tuzing va lug'atga shu inson haqida kamida 3 ta 
    m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida 
    konsolga chiqaring M: Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
    
2-mashq
Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. 
    Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
    
3-mashq
Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z(atamani) kiriting 
    (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
    
4-mashq
Mashina haqida lug‘at tuzing: model, rang, yil kabi keylari bo'lsin.
    - “rang” ni boshqa rangga o‘zgartiring.
    - Yangi “tezlik” kaliti qo‘shing.
    - Mashina lug‘atidan biror elementni pop() bilan o‘chiring.
    - Va so'ngida lug'atni tozalab tashlang.
    
5-mashq
Do'stlar degan lug'at yasang unda key sifatida 5 ta do'stingizni ismi, value qismida esa uning sevimli mevasi nomi bo'lsin. 
Keyin barcha ma'lumotlarni na'munadagi kabi konsulga chiqaring.
Namuna: Naima almani yoqtiradi.
    
6-mashq
Oila deb nomlagan lug'at tuzing {“ota”:”Anvar”}. Keyin esa shu lug'atdan yangi family  deb nomlangan lug'atga nusxa oling. 
Va Har ikkala lug'atni konsulga chiqaring.


8-mashq
Foydalanuvchidan uning yaqin do'sti haqidagi ma'lumotlarni so'ragan holda friend nomli lug'at tuzing. 
Lug'atda quidagi ma'lumotlar bo'lsin; ism, familiya, yosh, manzil, telefon raqam hamda kasb. 
Keyin lug'atdagi barcha ma'lumotlarni konsulga bir gap ko'rinishida chiqaring.
    
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

15-mashq
Ingliz-O'zbek lug'atini Tuzing. Avval lug'atdagi faqat ingliz tilidasi so'zlarni keyin esa faqat o'zbek tilidagi so'zlarni konsulga chiqaring.

16-mashq
Mashina nomidan iborat lug'at Tuzing. {“Mashina nomi”:mashinaning narxi} bo'lsin. Foydalanuvchidan biror mashina nomini so'rang agar u sizning lug'atingizda bor mashina nomini aytsa, unga o'sha mashinaning  narxini ayting, agar bo'lmasa “Bizda bu mashina yo'q edi” degan habarni chiqaring.

17-mashq
Ism familiyalardan foydalanib eng kamida 5 ta familiya, ism juftligidan iborat lug'at shakillantiring(“familiya”:”ism”). 
Foydalanuvchidan biror o'quvchining ismi yoki familiyasini kiritishini so'rang. Agar ism kiritilsa familiyani, familiya kiritilsa ismni qaytaring. Agar foydalanuvchi kiritgan ism yoki familiya sizning lug'atingizda bo'masa “Bizda bu o'quvchi haqida ma'lumot yo'q” habarni chiqaring.

18-mashq
Davlatlar va ularning poytaxtlari lug'atini tuzing. Foydalanuvchidan istalgan davlatni kiritishni so'rang agar foydalanuvchi davlar kiritsa uning poytaxini, poytaxt kiritsa uning davlatini konsulga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.

19-mashq
Ingliz-O'zbek lug'atini Tuzing. Key o'rnida ingliz tilidagi so'z, value o'rnida o'zbekcha so'z bo'lsin. Foydalanuvchidan biror so'z so'rang agar u lug'atda bor so'zni kiritsa unga u so'zning tarjimasini qaytaring, agar bo'lmasa “Bizda bu so'z haqida ma'lumot yo'q” degan javobni qaytaring.

20-mashq
Restoran menusi lug'atini tuzing(kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat
buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda 
bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

"""









