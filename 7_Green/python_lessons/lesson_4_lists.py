
ismlar = ['Umarbek', "Ali", "Alisher", "Abubakr", "Asror", "Mohlaroy", "Nigora"]
# print(ismlar)
# sonlar = [3, 0, -5, 7, 90, -45]

"""
list - Ro'yhat
element - Royhatni tashkil qiluvchi ma'lumot
index - elementning tartib raqami, manfiy(-) va musbat(+)
"""

# print(ismlar)
# print(type(ismlar)) # list - Ro'yhat


# print(ismlar[5])
# print(ismlar[-2])

""" Qo'shish """
""" 1-usul """
# ismlar.append("Oisha") # method - usul
# ismlar.append(input("Ism kiriting: ")) 
# print(ismlar)

""" 2-usul """
# ismlar.insert(0, "Isroil")
# ismlar.insert(4, input("Ism kiriting: "))
# print(ismlar)


""" Mashq """
""" sinfdoshar deb nomlangan ro'yhat yarating va unda 4 ta sinfdoshingizning ismini bo'lsin. 
Keyin ro'yhatning boshiga , o'rtasiga va oxiriga 1 tadan yangi ismlar qo'shing. 
"""
# sinfdoshlar = ["Jo'rabek", "Umarbek", "Nodirjon", "Sunnatali"]
# print(sinfdoshlar)

# sinfdoshlar.insert(0, "Mohina")
# sinfdoshlar.insert(3, "Dilshoda")
# # sinfdoshlar.insert(-1, "Umida")
# sinfdoshlar.append("Umida")
# print(sinfdoshlar)


""" Elementni o'chirish """
""" 1-usul """
# del sinfdoshlar[2] # index bo'yicha o'chiradi
# print(sinfdoshlar)

""" 2-usul """
# sinfdoshlar.remove("Umarbek") # qiymati bo'yicha o'chiradi
# print(sinfdoshlar)

""" 3-usul """
# sinfdoshlar.pop(1) # index bo'yicha o'chiradi
# print(sinfdoshlar)

""" 4-usul """
# sinfdoshlar.pop() # eng ohirginchisini o'chiradi
# print(sinfdoshlar)


""" clear() """
# sinfdoshlar.clear() # ro'yhatni tozalaydi
# print(sinfdoshlar)


""" ro'yhatni o'chirish """
# del sinfdoshlar # ro'yhatni butunlay o'chirib tashlaydi



"""
1) mevalar deb nomlangan ro'yhat yarating va unga eng kamida 5 meva nomini kiriting. 
    Ro'yhatning oxiriga yana 3 ta meva     nomini qo'shing keyin, 3 ta mevani indexsi bo'yicha o'chirib tashlang. 
    So'ngra yana 3 yangi mevani ro'yhatning  boshiga, o'rtasiga va oxiriga qo'shing. 
"""

# mevalar = ['olma', 'anor']
# print(mevalar)

# mevalar.append("Shaftoli")
# mevalar.append("Xurmo")
# mevalar.append("Anjir")
# print(mevalar)

# del mevalar[0]
# del mevalar[0]
# mevalar.pop(1)
# print(mevalar)

# mevalar.insert(0, "Uzum")
# mevalar.insert(4, "Nok")
# mevalar.insert(0, "Olxo'ri")
# print(mevalar)

"""
2) friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan 
    do'stlaringizni kiriting. Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi 
    yordamida o'chrib tashlang. Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
"""

# friends = []
# print(friends)

# friends.append("A1")
# friends.append("A2")
# friends.append("A3")
# friends.append("A4")
# friends.append("A5")
# friends.append("A6")
# print(friends)

# friends.remove("A2")
# friends.remove("A4")
# print(friends)

# friends.insert(0, "A7")
# friends.insert(4, "A8")
# friends.append("A9")
# print(friends)



""" 
3) Imtihon ballari deb nomlangan ro'yhat yarating va unga foydalanuvchidan so'rab so'ngi 4 ta imtihon natijalarini kiriting. 
So'ngra ro'yhatdagi barcha imtihon natijalarini qo'shib ummumiy ballar yig'indisini va o'rta arifmetik balni toping va konsulga chiqaring.

"""
# ballar = []

# ballar.append(float(input("1-fandan bahongizni kiriting: ")))
# ballar.append(float(input("2-fandan bahongizni kiriting: ")))
# ballar.append(float(input("3-fandan bahongizni kiriting: ")))
# ballar.append(float(input("4-fandan bahongizni kiriting: ")))
# print(ballar)

# yigindi = ballar[0] + ballar[1] + ballar[2] + ballar[3] 
# orta = yigindi/4

# print(f"Ballaringiz yig'indisi {yigindi} o'rtacha bahongiz {orta}")



"""
Mashinalar deb nomlangan ro'yhat yarating va unda o'zingiz bilgan 7 ta mashina nomi bo'lsin. 
Ro'yhatdan 2 ta mashina nomini del metodi yordamida o'chirib tashlang. 1 ta mashina nomini esa remove metodi yordamida o'chirib tashlang. 
Keyin esa pop metodi yordamida ham 2 hil usulda 1 tadan mashina nomini o'chirib tashlang va ro'yhatni konsulga chiqaring.
"""

""" Elementning qiymatini o'zgartirish """
# mashinalar = ["BMW M5", "CHevrolet Cobalt", "Porshe 911", "Nissan GTR", "Jentra"]
# print(mashinalar)

# mashinalar[0] = "BMW M8"
# mashinalar[2] = input("Yangi nomni kiriting:")
# print(mashinalar)

""" Ro'yhatdagi elementlar sonini o'lchash """
# print(len(ismlar)) # length - len
# print(f"Menda {len(mashinalar)} ta mashina bor")


"""
13-mashq
O'zingizga ma'lum 7 ta davlat nomini qo'shgan holatda davlatlar deb nomlangan ro'yhat tuzing. 
3 ta elementni 3 hil usulda o'chirib tashlang. Yangi 2 ta davlat nomini 2 xil usulda qo'shing. Va so'ngida ro'yhatni tozlab tashlang.
"""

# davlatlar = ['Ummon', "qatar", "Saudia arabistoni", "Quvaiyt", "Misr", "BAA", "Turkiya"]
# print(davlatlar)

# del davlatlar[0]
# davlatlar.pop()
# davlatlar.remove("BAA")
# print(davlatlar)

# davlatlar.append("Nigeriya")
# davlatlar.insert(2, "Gana")
# print(davlatlar)

# davlatlar.clear()
# print(davlatlar)


"""
14-mashq
Foydalanuvchidan 7 ta ism so'rang va ismlar deb nomlangan ro'yhatga qo'shing. Ro'yhatdagi 2 ta elementni qiymatini o'zgartiring. 
Yangi 2 ta ismni 2 xil usulda qo'shing. 3 ta elementni 3 hil usulda o'chirib tashlang. Va so'ngida ro'yhatni uzunligini o'lchang.
"""

# ismlar = []
# ismlar.append(input("1- ism kiriting: "))
# ismlar.append(input("2- ism kiriting: "))
# ismlar.append(input("3- ism kiriting: "))
# ismlar.append(input("4- ism kiriting: "))
# ismlar.append(input("5- ism kiriting: "))
# ismlar.append(input("6- ism kiriting: "))
# ismlar.append(input("7- ism kiriting: "))
# print(ismlar)

# ismlar[0] = "Lola"
# ismlar[-4] = "Laylo"
# print(ismlar)

# del ismlar[0]
# ismlar.pop()
# ismlar.remove("Lola")
# print(ismlar)

# ismlar.append("Abdulloh")
# ismlar.insert(2, "Nozima")
# print(ismlar)

# print(len(ismlar))


""" Matinni uzunligini o'lchash """
# ism = "Shohjahon"
# print(len(ism))



""" Sug'urib olib qo'shish """
# green = ["Komron", "Javohir", "Zilola", "Inomjon", "Bobur", "Mirziyo"]
# blue = ["Muhammadali", "Nigora", "Shohjahon", "Abubakir", "Azizbek", "Saidbek", "Kamron"]
# print(green)
# print(blue)

# green.append(blue.pop(0))
# green.insert(0, blue.pop(1))

# print(green)
# print(blue)


""" 24-mashq
sonlar deb nomlangan ro'yhat tuzing unda eng kamida 10 ta manfiy(-) va musbat(+) sonlar bo'lsin.
Keyin esa yangi musbat sonlar deb nomlangan yangi bo'sh ro'yhat yarting va unga sonlar ro'yhatidan faqat musbat sonlarni sug'urib olib qo'shing.
So'ngra har ikkala ro'yhatni konsulga chiqaring.
"""

# sonlar = [0, -6, 7, -34, 99, 6, -4, 91, 55]
# print(sonlar)

# musbat_sonlar = []
# musbat_sonlar.append(sonlar.pop(0))
# musbat_sonlar.append(sonlar.pop(1))
# musbat_sonlar.append(sonlar.pop(2))
# musbat_sonlar.append(sonlar.pop(2))
# musbat_sonlar.append(sonlar.pop(3))
# musbat_sonlar.append(sonlar.pop(3))

# print(sonlar)
# print(musbat_sonlar)



""" Ro'yhatdan nusxa olish -->  copy() """
# ismlar = ["Xasanov", "Husanboy", "Olimov", "Ahmadjon", "Jo'rabek", 'Shamsiddin' ]
# ismlar2 = ismlar.copy()

# print(ismlar)
# print(ismlar2)

# ismlar2.append("Abubakr")
# print(ismlar2)


""" sum(), max(), min() funksiyalari """
# sonlar = [32,-323, 4.3, 54,27,3,90, 8.1, 0, -54, 433]

# print(max(sonlar)) # eng katta sonni topib beradi
# print(min(sonlar)) # eng kichik sonni topib beradi
# print(sum(sonlar)) # Ro'yhatdagi sonlar yig'indisini topib beradi

# print(f"Ro'yhatda jami {len(sonlar)} ta son bor. Kattasi {max(sonlar)}, kichigi {min(sonlar)} va yig'indisi {sum(sonlar)} ga teng.")


"""
1-mashq
sonlar = [2, 6, -9, 0, 8.5, 21, 65, -34, 43.6, -44, 847, 0, 32, -4]
Ushbu ro'yhatdagi:
-sonlarning yig'indisini toping;
-ro'yhatning uzunligini toping;
-eng katta va eng kichik sonni toping.
"""
# sonlar = [2, 6, -9, 0, 8.5, 21, 65, -34, 43.6, -44, 847, 0, 32, -4]
# print(sum(sonlar))
# print(len(sonlar))
# print(max(sonlar))
# print(min(sonlar))



"""
2-mashq
Foydalanuvchidan uning oila azolarining yoshlarini so'rab bir ro'yhatga qo'shing va:
-Ro'yhatdagi eng katta sonni;
-Ro'yhatdagi eng kichik sonni;
-Ro'yhatdagi barcha sonlar yig'indisini toping;
-O'rta arifmetigini;
-Ro'yhatni uzunligini;
"""

# family_age = []
# family_age.append(int(input("1-oila azoingizni yoshini kiriting: ")))
# family_age.append(int(input("1-oila azoingizni yoshini kiriting: ")))
# family_age.append(int(input("1-oila azoingizni yoshini kiriting: ")))
# family_age.append(int(input("1-oila azoingizni yoshini kiriting: ")))
# family_age.append(int(input("1-oila azoingizni yoshini kiriting: ")))

# print(max(family_age))
# print(min(family_age))
# print(sum(family_age))
# print(sum(family_age) / len(family_age))
# print(len(family_age))



""" range() - sonli oraliq hosil qilib beradi """
# sonlar1 = list(range(12, 100))
# print(sonlar1)

# juft = list(range(0, 100, 2))
# print(juft)

# toq = list(range(1, 100, 2))
# print(toq)

# beshga = list(range(5, 100, 5))
# print(beshga)


"""
20-mashq
200 dan 430 gacha bo'lgan toq sonlar ro'yxatini tuzing.
-101 dan 2020 gacha bo'lgan juft sonlardan iborat ro'yhat tuzing.
-322 dan -2 gacha bo'lgan toq sonlardan iborat ro'yhat tuzing va ro'yhatning uzunligini toping.

21-mashq
3 dan 100 gacha juft sonli ro'yhat tuzing;
-ro'yhatdagi sonlar yig'indisini toping;
-eng kichkina son va eng katta son yig'indisini toping.

"""

""" 20-mashq """
# list1 = list(range(201, 430, 2))
# print(list1)

# list2 = list(range(-100, 2020, 2))
# print(list2)

# list3 = list(range(-321, -2, 2))
# print(list3)
# print(len(list3))

""" 20-mashq """
# list4 = list(range(4, 100, 2))
# print(list4)

# print(sum(list4))
# print(list4[0] + list4[-1])
# print(min(list4) + max(list4))

"""
22-mashq
120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing.
-ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring;
-eng katta va eng kichik son o'rtasidagi ayirmani hisoblang;
-ro'yxatdagi elementlar sonini hisoblang;

23-mashq
100 dan 1000 gacha bo'lgan juft sonlardan iborat ro'yhat tuzing.
20 dan 200 gacha bo'lgan toq sonlardan iborat ro'yhat tuzing.
100 dan 500 gacha barcha 5 ga bo'linuvchi sonlardan iborat ro'yhat tuzing.

"""



""" Ro'yhat elementlarini tartiblash """
# ismlar = ["Xasanov", "Husanboy", "Olimov", "Ahmadjon", "Jo'rabek", 'Shamsiddin', "Abdulaziz", "Abdulloh"]
# print(ismlar)

# """ .sort() --> Ro'yhatni alifbo bo'yicha tartiblaydigan metod """
# ismlar.sort() # Ro'yhatni alifbo bo'yicha tartiblaydi
# print(ismlar)

# ismlar.sort(reverse=True) # Ro'yhatni alifboga teskari tartibda tartiblaydi
# print(ismlar)

# """ .reverse() --> Ro'yhatni aylantirib beradigan metod """
# ismlar.reverse() # Ro'yhatni aylantirib beradi
# print(ismlar)


# sonlar = [32,-323, 4.3, 54,27,3,90, 8.1, 0, -54, 433]
# print(sonlar)

# """ .sort() --> Ro'yhatni alifbo bo'yicha tartiblaydigan metod """
# sonlar.sort() # Ro'yhatni alifbo bo'yicha tartiblaydi
# print(sonlar)

# sonlar.sort(reverse=True) # Ro'yhatni alifboga teskari tartibda tartiblaydi
# print(sonlar)

# """ .reverse() --> Ro'yhatni aylantirib beradigan metod """
# sonlar.reverse() # Ro'yhatni aylantirib beradi
# print(sonlar)


"""
19-mashq
O'zingizga ma'lum davlatlarning ro'yxatini tuzing (eng kamida 7 ta) va ro'yxatni konsolga chiqaring.
-ro'yxatning uzunligini konsolga chiqaring;
-sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
-reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring;

21-mashq
10 dan 100 gacha toq sonli ro'yhat tuzing:
-ro'yhatni o'sish va kamayish tartibida tartiblang.

"""


""" 19-mashq """

# davlatlar = ["O'zbekiston", "Qozog'iston", "Rossiya", "Xitoy", "Turkiya", "AQSH", "Germaniya"]
# print(davlatlar)

# davlatlar.sort()
# print(davlatlar)

# davlatlar.sort(reverse=True)
# print(davlatlar)

# print(len(davlatlar))

# davlatlar.reverse()
# print(davlatlar)


""" 21-mashq """
# toq_sonlar = list(range(11, 100, 2))
# print(toq_sonlar)

# toq_sonlar.sort()
# print(toq_sonlar)

# toq_sonlar.sort(reverse=True)
# print(toq_sonlar)


"""
22-mashq
Foydalanuvchidan ikkita son qabul qilib olib ular oralig'ida joylashgan sonlardan iborat sonli ro'yhat shakillantiring.
Ro'yhatning uzunligini konsulga chiqaring.
Ro'yhatni avval o'sish tartibida so'ngra kamayish tartibida tartiblang va konsulga chiqaring.
"""

# son1 = int(input("1-sonni kiriting: "))
# son2 = int(input("2-sonni kiriting: "))

# sonlar3 = list(range(son1, son2))
# print(sonlar3)

# print(len(sonlar3))

# sonlar3.sort()
# print(sonlar3)

# sonlar3.sort(reverse=True)
# print(sonlar3)



"""
23-mashq
-2024 dan 2024 gacha bo'lgan juft sonli ro'yhat shakillantiring va ro'yhatdagi eng katta sonni toping;
123 dan 87384 gacha bo'lgan toq sonli ro'yhat shakillantiring va ro'yhatdagi eng kichik sonni toping;
352 dan 20010118 gacha bo'lgan faqat 11 ga bo'linadigan sonli ro'yhat shakillantiring va ro'yhatdagi barcha sonlarning yig'indisini toping.
"""

