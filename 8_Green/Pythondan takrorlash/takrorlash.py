# """
# Thame: Ro'yhatlar(Lists)
# """  

# """ Element, Index"""

# """
mevalar = ["olma", 'gilos', "o'rik", "olcha"]
#               0       1        2        3
#              -4      -3       -2       -1
# """

ismlar = [ "Abduboqiyeva Fotimaxon", "Abduboqiyeva Mubinaxon", "Abduboqiyeva Zuxraxon"]
# print(ismlar)
# print(ismlar[2])
# print(ismlar[-1])


# family = ["Olim", "Anvar", "Gul"]
# print(f"Salom {family[0]}")
# print(f"Salom {family[1]}")
# print(f"Salom {family[2]}")


# """ Ro'yhat turlari """
# ismlar = ["Ali", 'Olim', "Anvar", "Abbos"]
# sonlar = [3,5.7,-6,0,54,8]
# darslar = ["Pyhton", "Django", 3, 10]
# bosh_royhat = []

# print(sonlar[3])


""" .append() --> Ro'yhatga element qo'shish """
# friends = [] # bo'sh ro'yhat
# print(friends)

# friends.append("Umarbek")
# friends.append("Asadbek")
# friends.append("Quvonchbek")
# print(friends)

# friends.append(input("1-Do'stingizning ismini kiriting: "))
# friends.append(input("2-Do'stingizning ismini kiriting: "))
# print(friends)

# """
# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni qo'shing(musbat, manfiy, butun, o'nlik).
# """
# sonlar = []
# """
# manfiy --> -3, -5.7, -54
# musbat --> 4, 8, 9.2
# """

# sonlar.append(int(input("Butun son kiriting: ")))
# sonlar.append(int(input("Butun son kiriting: ")))
# sonlar.append(float(input("Butun son kiriting: ")))
# sonlar.append(float(input("Butun son kiriting: ")))

# print(sonlar)


# ikkichilar = ["Malika", "Rayhona", "Sobirjonova"]
# # ikkichilar.append("Shahlo")
# ikkichilar.insert(0, "Shahlo")
# ikkichilar.insert(2, "Shohsanam")
# print(ikkichilar)

# """
# append --> Doim ro'yhat oxiriga element qo'shadi
# insert --> Ro'yhatning istalgan joyiga(index bo'yicha) element qo'shadi
# """


""" .extend() --> bir ro'yhatni boshqasiga qo'shib beradi """
ikkichilar = ["Malika", "Shohsanam", "S. Zilola"]
# alochilar = ["Sevara", "Zilola", "Iroda"]
# print(ikkichilar)
# print(alochilar)

# ikkichilar.extend(alochilar) # "alochilar" ni "ikkichilar" ro'yhatiga qo'shib beradi
# print(ikkichilar)
# print(alochilar)

""" Ro'yhatdan elementni o'chirish """
# del ikkichilar[3] # elementni index bo'yicha o'chiradi
# print(ikkichilar)

# ikkichilar.remove("S. Zilola") # elementni qiymati(nomi) bo'yicha o'chiradi
# print(ikkichilar)

# ikkichilar.pop() # ro'yhatdagi oxirgi elementni o'chiradi
# print(ikkichilar)

# ikkichilar.pop(2) # elementni index bo'yicha o'chiradi
# print(ikkichilar)

"""
1) friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan 
    do'stlaringizni kiriting. Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi 
    yordamida o'chrib tashlang. Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
    
2) aktyorlar va honandalar degan ro'yhatlaer yarating va ularga o'zingiz eng ko'p kuzatadigan
    aktyorlar va honandalar ni kiriting, ulardan ikkitadan aktyorni o'chirib tashalng, va yangi 3tadan qo'shing.
    song'ra har ikkala ro'yhatdagi elementlarni insonlar degan yangi ro'yhatga jamlang.
    
3) mevalar deb nomlangan ro’yhat yarating va unga eng kamida 5 meva nomini kiriting. 
    Ro’yhatning oxiriga yana 3 ta meva     nomini qo’shing keyin, 3 ta mevani indexsi bo’yicha o’chirib tashlang. 
    So’ngra yana 3 yangi mevani ro’yhatning  boshiga, o’rtasiga va oxiriga qo’shing. 
"""

""" 3-MASHQ """
# mevalar = ["olma",  "nok", "uzum", "apelsin", "tarvuz", "anor"]
# print(mevalar)

""" 3 ta element append yordamida ro'yhatga o'shidi """
# mevalar.append("Kiwi")
# mevalar.append("ananas")
# mevalar.append("qovun")
# print(mevalar)

# del mevalar[0]
# del mevalar[3]
# mevalar.pop(-1)
# print(mevalar)

# mevalar.insert(0, "gilos")
# mevalar.insert(3, "Olcha")
# mevalar.append("Mango")
# print(mevalar)


# green = ["Malika", "Shahlo", "Zuhra"]
# blue = []
# print(green)
# print(blue)

# blue.append(green.pop(2))
# blue.append(green.pop(0))
# print(green)
# print(blue)

"""
4) friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan 
    do'stlaringizni kiriting. Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi 
    yordamida o'chrib tashlang. Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.

5) Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() 
    metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends 
    ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.

6) mevalar deb nomlangan ro'yhat yarating va unga eng kamida 5 meva nomini kiriting. Ro'yhatning oxiriga yana 3 ta meva nomini qo'shing keyin, 3 ta mevani indexsi bo'yicha o'chirib tashlang. So'ngra yana 3 yangi mevani ro'yhatning boshiga, o'rtasiga va oxiriga qo'shing.
    
7) Sonlar deb nomlangan bo'sh ro'yhat yarating. Foydalanuvchidan so'rab unga 5 ta turli sonlar qo'shing. Keyin ulardan 2 tasini index bo'yicha o'chirib tashlang, yana yangi 4 ta elementni ro'yhatning turli joylariga qo'shing. 2 ta elemetni indexi bo'yicha o'chiring.

8) Bozorlik deb nomlangan bo'sh ro'yhat yarating. Keyin unga bozorlik uchun 5 ta mahsulot nomini qo'shing.  Va ulardan 2 tasini indexi orqali o'chirib tashlang,  va ro'yhatning boshiga o'rtasiga va oxiriga 3 ta mahsulotni qo'shing. So'ngra elementlardan 2 tasini qiymati bo'yicha o'chirib tashlang. Va yana 3 ta mahsulot nomini ro'yhatning turli joylariga qo'shing. Eng so'ngida ro'yhatni konsulga chiqarib qo'ying.

"""

"""1 mashq"""
# friends = ["malika","madina","rano","fotima","zuhra"]

# friends.append("komila")
# friends.append("maryam")
# friends.append("diyora")
# friends.append("ziroat")
# friends.append("saida")

# print(friends)

# friends.remove("malika")
# friends.remove("rano")
# friends.remove("fotima")
# print(friends)

# friends.insert(0, "malika")
# friends.insert(1, "madina")
# friends.insert(2, "rano")
# print(friends)


"""2 mashq"""
# mehmonlar = []
# mehmonlar.append("zilola")
# mehmonlar.append("rayhona")
# mehmonlar.append("iroda")
# mehmonlar.append("sarvinos")
# mehmonlar.append("saida")

# mehmonlar.pop(0)
# mehmonlar.pop(3)
# mehmonlar.pop(2)
# mehmonlar.pop(1)

# print(mehmonlar)


# sonlar = list(range(2,100, 2))
# print(sonlar)


ismlar = ["Shahzodbek", "Abdulloh", "Ali", "Olim", "Hasan", "Husan", "Nodirbek"]
# print(ismlar)

# ismlar.sort() # Alifbo bo'yicha tartiblab beradi
# print(ismlar)

# ismlar.sort(reverse=True)# Alifboga teskari tartib  bo'yicha tartiblab beradi
# print(ismlar)


# print(sorted(ismlar)) # Alifbo bo'yicha bir marta tartiblab beradi
# print(sorted(ismlar, reverse=True)) # Alifboga teskari bir marta tartiblab beradi

# ismlar.reverse() # Ro'yhatni boshi va oirini aylantirib beradi
# print(ismlar)


"""
O'zingizga ma'lum ismlardan 10 tasini kiritgan holda ro'yxat tuzing  va ro'yxatni konsolga chiqaring.
-ro'yxatning uzunligini konsolga chiqaring;
-sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring;
-sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring;
-reverse() metodi yordamida ro'yxatni aylantirib chiqaring.
"""


sonlar  = [454, -4343, 0, 2, 53, 843, -74, 43.5, 8, -32]
# print(sonlar)

# sonlar.sort()
# print(sonlar)

# sonlar.sort(reverse=True)
# print(sonlar)


""" min() max()  sum() """
# print(min(sonlar))
# print(max(sonlar))
# print(sum(sonlar))



"""

7) 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing.
    -ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring;
    -ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring;
    -ro'yxatdagi elementlar sonini hisoblang;
"""

# sonlar = list(range(120, 1200, 2))
# print(sonlar)
# print(sum(sonlar))
# print(max(sonlar)-min(sonlar))
# print(len(sonlar))


"""
    1-mashq
    Foydalanuvchidan uning oila azolarining yoshlarini so’rab bir ro’yhatga qo’shing va:
    Ro’yhatdagi eng katta sonni;
    Ro’yhatdagi eng kichik sonni;
    Ro’yhatdagi barcha sonlar yig’indisini toping;
    Ro’yhatni o’sish tartibida tartiblang.

    2-Mashq 
    Foydalanuvchidan 3 ta son kiritishini so’rang va :
        ular ichidagi eng katta sonni toping
        ular ichidagi eng kichik sonni toping.
        barcha sonlar yig’indisini toping.

    3-Mashq 
    Ushbu ro’yhatni:     sonlar = [45, -96, 0, 63.2, 1257, -6752.2, 42, 3, 542] 
        - o’sish tartibida;
        - kamayish tartibida;
        - boshi va oxirini aylantirib konsulga chiqaring.

    4-mashq
    Quidagicha sonli ro’yhatlar yarating:
        200 dan 400 gacha toq sonli;
        301 dan 500 gacha juft sonli;
        10 dan 600 gacha 25 ga bo’linadigan sonlardan iborat;

    5-mashq
    Foydalanuvchidan uning ismini va u o’qigan kitoblaridan 5 tasini so’rab kitoblar deb nomlangan ro’yhatga qo’shing. 
    Keyin esa ro’yhatdan 1 ta kitobni o’chirib tashlang. So’ngra ro’yhatning 2- va 3- indexlarga yangi kitoblar 
    nomini qo’shing.
0.
    6-mashq
    Fanlar deb nomlangan ro’yhat yarating, 2 ta fan bo’lsin. Keyin esa:
    2 ta yangi qiymat qo’shing(2 xil usulda);
    2 ta qiymatni o’zgartiring;
    3 ta qiymatni o’chiring(3 xil usulda);
   
    8-Mashq
    O'zingizga ma'lum mashinalar ro'yxatini tuzing(eng kamida 10 ta) va ro'yxatni konsolga chiqaring.
    -ro'yxatning uzunligini konsolga chiqaring;
    - ro'yxatni doimy tartiblangan holda konsolga chiqaring;
    - ro'yxatni doimy teskari tartibda konsolga chiqaring;
    - ro'yxatni ortidan(aylantirib) boshlab konsolga chiqaring;


    """


# gullar = ["atirgul", "chinnigul", "moychechak"]
# gullar.sort()
# gullar.sort(reverse=True)
# gullar.reverse()


"""  .clear()  --> ro'yhatni tozalash """
# fruts = ["apple", "banana", "cherry", "olma"]
# print(fruts)

# fruts.clear()
# print(fruts)

# """ range() --> sonli oraliq hosil qiladi """
# sonlar = list(range(20, 80, 10))
# print(sonlar)

# """ .copy() --> ro'yhatdan nusxa olish """
# mevalar = fruts.copy()
# print(mevalar)

# fruts2 = ["apple", "banana", "cherry", "olma", "gilos", "anor", "behi"]
# print(fruts2)

# fruts3 = fruts2[:3] # eng bosidan 3-indexgacha nusxalash
# print(fruts3)

# fruts4 = fruts2[4:] # 4-indexdan eng oxirigacha nusxalash
# print(fruts4)

# fruts5 = fruts2[2:5] # 2-indexdan, 5-index gacha nesxalash 
# print(fruts5)

# fruts6 = fruts2[:] # ro'yhatni boshidan oxirigacha nusxalash
# print(fruts6)


"""
    4-mashq
    Quidagicha sonli ro’yhatlar yarating:
        200 dan 400 gacha toq sonli;
        301 dan 500 gacha juft sonli;
        10 dan 600 gacha 25 ga bo’linadigan sonlardan iborat;

    6-mashq
    Fanlar deb nomlangan ro’yhat yarating, 2 ta fan bo’lsin. Keyin esa:
    2 ta yangi qiymat qo’shing(2 xil usulda);
    2 ta qiymatni o’zgartiring;
    3 ta qiymatni o’chiring(3 xil usulda);
   
    7-Mashq
    O'zingizga ma'lum mashinalar ro'yxatini tuzing(eng kamida 10 ta) va ro'yxatni konsolga chiqaring.
    -ro'yxatning uzunligini konsolga chiqaring;
    - ro'yxatni doimy tartiblangan holda konsolga chiqaring;
    - ro'yxatni doimy teskari tartibda konsolga chiqaring;
    - ro'yxatni ortidan(aylantirib) boshlab konsolga chiqaring;
"""



""" for operatori """

""" for operatori """
# ismlar = ["Laylo", "Muslima", "Ma'rifat", "Odina", "Umida", "Dilshoda"]
# print(f"Salom {ismlar[0]}, ertaga qayerga borasan.")

# for ism in ismlar:
#     print(f"Salom {ism}, ertaga qayerga borasan.")
#     print("Agar ertaga vaqting bo'lsa hayvonot bog'iga borsak nima deysan ?")
    
# print("Bu habar hammaga yuborildi")


# sonlar = [1,2,3,4,5,]
# sonlar = list(range(1, 20)) # 1,2,3,4,5,6,7,8,9,10,, ...20
# for son in sonlar:
#     # print(f"{son} ning kvadrati {son**2}")
#     # print(f"{son} ning kubi {son**3}")
#     print(f"{son} dan 1 ta kichik son {son-1} va 3 ta katta son  {son+3}")


# for x in range(100):
#     print(f"I will not talk on English lesson({x+1} row)")


# son = int(input("Nechta oila azoingiz bor: "))
# ismlar = []
# for i in range(son):
#     ismlar.append(input(f"{i+1} - oila azoingizni ismini kiriting: "))
# print(ismlar)  


"""
1-mashq | Ushbu koddagi bir nechta hatoliklarni to’g’irlang va dasturni to’g’ri ishga tushuring.

son = input("Nechta meva nomini kiritmoqchisiz: ")
mevalar = []

for s in range(Son):
    meva = input(f"{x+3} - meva nomini kiriting: "
sabzavotlar.append(mava)  
print(mevala)

2-mashq | -322 dan -2 gacha bo’lgan barcha toq sonlarning:

1) 5 chi va 7 chi darajasini toping;
2) Ro’yhatdagi har bir sondan 4 taga kichik sonni konsulga chiqaring;
3) Ro’yhatdagi har bir sonning 4 -darajasini toping;
4) Ro’yhatning uzunligini o’lchang;
5) Ro’yhatni avval o’sish tartibida keyin esa kamayish tartibida tartiblab konsulga chiqaring;
"""

# son = int(input("Nechta meva nomini kiritmoqchisiz: "))
# mevalar = []

# for s in range(son):
#     meva = input(f"{s+1} - meva nomini kiriting: ")
#     mevalar.append(meva)  
# print(mevalar)


# sonlar  =list(range(-321, -2, 2))

# for son in sonlar:
#     print(f"{son} ning 5- darajasi {son**5}, 7-darajasi {son**7} ga teng.")
#     print(f"{son} dan 4 ta kichik son {son-4}")
#     print(f"{son} ning 4-darajasi {son**4}")


# print(len(sonlar))

# sonlar.sort()
# print(sonlar)

# sonlar.sort(reverse=True)
# print(sonlar)


"""
1-mashq | Ushbu koddagi bir nechta hatoliklarni to'g'irlang va dasturni to'g'ri ishga tushuring.

son = input("Nechta meva nomini kiritmoqchisiz: ")
mevalar = []

for s in range(Son):
    meva = input(f"{x+3} - meva nomini kiriting: "
sabzavotlar.append(mava)  
print(mevala)

2-mashq | -322 dan -2 gacha bo'lgan barcha toq sonlarning:

1) 5 chi va 7 chi darajasini toping;
2) Ro'yhatdagi har bir sondan 4 taga kichik sonni konsulga chiqaring;
3) Ro'yhatdagi har bir sonning 4 -darajasini toping;


4) Ro'yhatning uzunligini o'lchang;
5) Ro'yhatni avval o'sish tartibida keyin esa kamayish tartibida tartiblab konsulga chiqaring;
"""





""" if-elif-else """


# ismlar  = ["Ali", "Olim", "Anvar", "Husan", "Jasur"]
# for ism in ismlar:
#     if ism == "Husan":
#         print(f"Salom {ism}. Hush kelibsan !")
#     elif ism == "Jasur":
#         print(f"Salom {ism}. Hush kelibsan !")
#     else:
#         print(f"Salom {ism}")



"""
    ==  -> teng bo'lsa
    !=  -> teng bo'lmasa
    >   -> katta bo'lsa
    <   -> kichik bo'lsa
    >=  -> katta yoki teng bo'lsa
    <=  -> kichik yoki teng bo'lsa
    or   -> yoki
    and  -> va 
"""

# parol1 = input("1-parolni kiriting: ")
# if len(parol1) >= 8:
#     parol2 = input("2-parolni kiriting: ")
#     if parol1 == parol2:
#         print("Parol muvaffaqiyatli o'rnatildi !")
#     else:
#         print("Parollar bir biriga mos emas !!!")
# else:
#     print("Parol eng kamida 8 ta belgidan iborat bo'lishi kerak !!!")
#     print("Qaytadan urinib ko'ring !")



""" Lug'at - Dictionary """
ismlar = {
    "malikova_naima":"olma", # element
    "sarvinoz":"ananas",
    "hadicha":'olcha',
    "mohlaroy":'gilos',
    'oydina':"banan"
}

# print(ismlar)
# print(ismlar["hadicha"])
# print(f"Hadichaning sevimli mevasi {ismlar['hadicha']}")

# print(type(ismlar)) # dict --> dictionary

# buyumlar = {
#     "ism":"Ali",
#     "yosh":12,
#     "student":True,
#     "oila":["ota","ona",'aka'],
#     "ball":{
#         'ict':50,
#         'math':23,
#         'eng':33
#     }
# }
# print(buyumlar)


""" Element qo'shish """
""" 1-usul """
# ismlar['rahima'] = "apelsin"
# print(ismlar)

# ismlar[input("Biror ism kiriting: ")] = input("Siz qaysi mevani yoqtirasiz: ")
# print(ismlar)

""" 2-usul """
# ismlar.update({'abror':"shaftoli"})
# print(ismlar)

# ismlar.update({input("Ism kiriting: "):input("Meva kiriting: ")})
# print(ismlar)

""" Elementni o'chirish """
# del ismlar["hadicha"]
# print(ismlar)

# ismlar.pop('sarvinoz')
# print(ismlar)

# ismlar.popitem() #  eng so'ngi elementni o'chirib tashlaydi
# print(ismlar)

""" Lug'atni o'chirib tashlash """
# del ismlar

""" Lug'atni tozalash """
# ismlar.clear()
# print(ismlar)

""" Nusxa olish """
# girls = ismlar.copy()
# print(girls)


"""
4-mashq
taomlar = {
    'ali':'osh',
    'vali':'shashlik',
    'hasan':"lag'mon",
    'husan':"mastava",
    'olim':"somsa",
    'nodir':"kabob",
}
Ushbu lug'atdagi:
2 ta elementning qiymatini o'zgartiting(o'zingiz);
2 ta yangi element qo'shing(o'zingiz)
1 ta elementning qiymatini foydalanuvchidan so'rab o'zgartiting;
2 ta yangi elementni foydalanuvchidan so'rab  qo'shing;


5-mashq
Fanlar deb nomlangan lug'at yarating, unda {“kalit”:”fan nomi”}  ko'rinishidagi
2 ta fan bo'lsin.  Keyin esa:
    2 ta yangi qiymat qo'shing(2 xil usulda);
    2 ta qiymatni o'zgartiring(2 xil usulda);
    3 ta qiymatni o'chiring(3 xil usulda);
    yangi lug'at yaratib unga Fanlar lug'atidan nusxa oling;
    So'ngra Fanlar ro'yhatini tozalab tashlang;


6-mashq
books deb nomlangan lug'at yarating{“key”:”kitob nomi”}. Ichida 2 ta element bo'lsin. 
Yana  yangi  2 ta elementni 2 xil usulda qo'shing, 2 ta elementni 2 xil usulda yangilang, 
3 ta elementni 3 xil usulda o'chiring va so'ngra lug'atni tozalab tashlang.

"""



taomlar = {
    'ali':'osh',
    'vali':'shashlik',
    'hasan':"lag'mon",
    'husan':"mastava",
    'olim':"somsa",
    'nodir':"kabob",
}

""" .get() --> metodi - xatolikni oldini olish uchun ishlatiladi """

# print(taomlar["ali5"])
# print(taomlar.get('ali5', "Bunday ism yo'q"))

# print(taomlar.get(input("Biror ism kiriting: ").lower(), "Bunday ism yo'q"))

# print(taomlar["vali"])
# print(taomlar["hasan"])


davlatlar = {
    'uzbekistan':"Tashkent",
    'usa':"Washington",
    'russian':"Moscow",
}

""" .keys() va .values() metodlari  """

# print(davlatlar.keys())
# print(davlatlar.values())

# for davlat in davlatlar.keys():
#     print(davlat)

# for poytaht in davlatlar.values():
#     print(poytaht)

  
""" .items() - metodi """

# for key, value in davlatlar.items():
#     # print(f"{key} - {value}")
#     print(f"{value} is the capital city of {key.title()}")


davlatlar = {
    'uzbkistan':"tashkent",
    'turkey':"ankhara",
    "south korea":"seul",
    "china":"pekin"
}

# savol = input("Davlat yoki poytaht nomini kiriting: ").lower()

# for davlat, poytaht in davlatlar.items():
#     if savol == davlat:
#         print(f"{davlat.title()} ning poytahti {poytaht.title()} shahri")
#     elif savol == poytaht:
#         print(f"{poytaht.title()} shahri {davlat.title()}ning poytahti")
    
# if savol not in davlatlar.keys() and savol not in davlatlar.values():
#     print(f"{savol} haqida bizda ma'lumot yo'q")


""" 
Foydalanuvchidan tug'ilgan yilini so'rab uning yoshini topib beradigan dastur tuzing. 
dastur faqat "stop" so'zini yozganda to'xtasin
"""

# while True:
#     yil = input("Tug'ilgan yilingizni kiriting: ").lower()

#     if yil == 'stop' or yil == "exit":
#         print("The end")
#         break
    
#     elif yil.isdigit():
#         yil  = int(yil)
#         print(f"Sizning yoshingiz {2025 - yil} yosh da")


""" Funksiya """


def daraja(son:int, daraja:int) ->int:
    """ Docstring 
    Sonning darajasini topib beruvchi funksiya
    """
    
    return son**daraja
    
# print(daraja(5, 2))
# print(daraja(7, 4))


""" *args - arguments """
def our_max(*sonlar:list) -> int:
    """ Berilgan sonlarning eng kattasini topib beruvchi funksiya """
    
    sonlar = sorted(sonlar)
    
    return sonlar[-1]

# a = our_max(4, -6, 0, -434, 23, 64, -334)
# print(a)


""" **kwargs --> key word arguments"""

def full_name(name:str, surname:str, **kwargs) ->str:
    """ Inson haqida ma'lumot beruvchi funksiya """
    
    return f"{name} {surname} {kwargs['yosh']} yoshda va {kwargs['maktab']}da o'qiydi"
    
# print(full_name("Hilola", "Bahodirova", yosh=9, maktab="BM"))


def juft(son:int, )->list:
    """  """
    
    return list(range(0, son, 2))

# print(juft(10))
# print(juft(30))


def aniqla(harf:str)-> str:
    """  """
    unlilar = ["i", "o", "u", "a", "e"]
    
    if harf in unlilar:
        return f"{harf} - unli"
    elif harf == "o'":
        return f"{harf} - unli"
    else:
        return f"{harf} - undosh"

# print(aniqla("a"))
# print(aniqla("o'"))
# print(aniqla("sh"))
# print(aniqla("d"))
    
    
 
"""
link -> https://docs.python.org/3/howto/regex.html
link -> https://docs.python.org/3/library/re.html
link -> https://www.w3schools.com/python/python_regex.asp

RegEx funksiyalari
match()     -   Solishtirish uchun  
findall()   -   Barcha mosliklarni o'z ichiga olgan ro'yxatni qaytaradi
search()    -   Agar matnning istalgan joyida moslik mavjud bo'lsa, Match ob'ektini qaytaradi

\w - So'z belgilari -->  a-z / A-Z 
\d - Raqam  --> 0-9
\b - So'z chegarasi --> $
\s - bo'shliq 
^  - boshlanish
"""

from re import match, findall, search
 
# tel = "+7 921 014-96-13"
# phone_pattern = r"^[+][0-9][\s][0-9]{3} [0-9]{3}[-][0-9]{2}[-]$"

# print(match(phone_pattern, tel))
 
 
phone_pattern1 = r"[+][0-9][\s][0-9]{3} [0-9]{3}[-][0-9]{2}[-][0-9]{2}"
matn1 = """
    Bugun kun quyoshli va issiq +7 921 014-96-13 bo'lyapdi. 30-01-2001 Mahzuna dadasining mashinasida maktabga keldi. 
    Mashinaning raqami 50 A327CB ed. Uning dugonasi Oydina esa 40 V456AA +9 921 014-96-13 raqamli mashinada keldi.
    Maftuna yangi  +8 921 014-96-13 telefon raqami oldi u +998(90) 545-50-75 edi.  Uning oldingi raqami esa 
    +998(95) 963-12-81 edi. Oyisiniki esa +998(55) 325-65-95 bo'lgan. 02-06-2022
"""

# print(findall(phone_pattern1, matn1))
# print(search(phone_pattern1, matn1))

# pattern1 = r"^[A-Z]{2} [0-9]{7}$"
# pattern2 = r"^[A-Z]{2} [0-9]{3}[-][0-9]{2} [A-Z]"
# pattern3 = r"[A-Za-z]{7}"
# pattern4 = r"[#][A-Za-z0-9]{,12}"
# pattern5 = r"[0-9]{,5}"
# pattern6 = r"[S][a-z]{,10}[a]"

# print(match(pattern1, matn1))
  
# pattern7 = r"^[a-z0-9]{4,12}$"
# pattern7 = r"^[@][a-z]{4,12}$"
  

""" Datetime """
""" datetime - moduli """

from datetime import date, datetime, timedelta

"""
date - > sana bilan ishlash
datetime -> sana va vaqt bilan ishlash
timedelta -> sana va vaqtga + sana qo'shib beradi
""" 



"""
max min sum len
datetime timedelta
while
"""

def maxx(*sonlar:int)->int:

    sonlar = sorted(sonlar)
    return sonlar[-1]

# print(maxx(2,7,-8, 54, 43,2))


def minn(*sonlar:int)->int:

    sonlar = sorted(sonlar)
    return sonlar[0]

# print(minn(2,7,-8, 54, 43,2))


def summ(*sonlar:int)-> int:
    """  """
    summa = 0
    for son in sonlar:
        summa = summa + son
    return summa

# print(summ(2,7,-8, 54, 43,2))


def lenn(*sonlar:int)-> int:
    """  """
    uzunlik = 0
    for son in sonlar:
        uzunlik = uzunlik + 1
    return uzunlik

# print(lenn(2,7,-8, 54, 43,2))




from datetime import date
bugun = date.today()

while True:
    t_yil = input("Tug'ilgan yilingizni kiriting(chiqish uchun 'chiqish' deb yozing): ").lower()
    
    if t_yil == 'chiqish':
        print("Dastur to'xtadi !")
        break
    
    elif t_yil.isdigit():
        t_yil = int(t_yil)
        
        yosh = bugun.year- t_yil
                
        print(yosh)



    
















