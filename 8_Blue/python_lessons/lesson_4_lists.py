""" Lists - Ro'yhatlar """

ismlar = ['ALi', "Olim", "Azizbek", "Abduhalil", "Rashidbek", 34, 9.6, 34]
# print(ismlar)
# print(type(ismlar)) # list - ro'yhat


# print(ismlar[2])
# print(ismlar[-5])

"""
List - Ro'yhat, O'zgaruvchi turi
element - Ro'yhatni tashkil qiluvchi ma'lumot
index - elemetning tartib raqami, har bir elementda 2 ta index bo'ladi, manfiy(-) va musbat(+)
""" 


""" Qo'shish """
""" 1-usul """
# ismlar.append("Zilola") # method - usul
# ismlar.append("Samandar")
# print(ismlar)

""" 1-usul """
# ismlar.insert(3, "Elbek")
# ismlar.insert(0, "Abdulaziz")
# print(ismlar)
# print(ismlar)

  
""" O'chirish """
""" 1-usul """
# del ismlar[3]
# print(ismlar)

""" 2-usul """
# ismlar.pop(-1)
# print(ismlar)

""" 3-usul """
# ismlar.pop()
# print(ismlar)

""" 4-usul """
# ismlar.remove("Olim")
# ismlar.remove(34)
# print(ismlar)


""" Ro'yhatni o'chirish """
# del ismlar
# print(ismlar)

""" Ro'yhatni tozalash """
# ismlar.clear()
# print(ismlar)


"""
1) friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan 
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
# print(friends)


# friends.remove("A2")
# friends.remove("A3")
# friends.remove("A5")
# print(friends)


# friends.insert(0, "A6")
# friends.insert(3, "A7")
# friends.append("A8")
# print(friends)



# sonlar = [-34, 45, 0, -65.3, 3.6, 2, 62] 
# print(sonlar[2] + sonlar[4])

"""
4-mashq
sonlar deb nomlangan ro'yxat tuzing va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring.
Ro'yxatdagi 2 ta sonning qiymatini o'zgartiring, yana 2 tasini esa o'chirib tashlang.

5-mashq
mevalar deb nomlangan ro'yhat tuzing va unga eng kamida 5 meva nomini kiriting.
Ro'yhatning oxiriga yana 3 ta meva nomini qo'shing keyin, 3 ta mevani indexsi bo'yicha o'chirib tashlang.
So'ngra yana 3 yangi mevani ro'yhatning boshiga qo'shing. Ro'yhatdagi 2 ta element qiymatini o'zgartiring.

6-mashq
Fanlar deb nomlangan ro'yhat tuzing, 5 ta fan bo'lsin. Keyin esa:
2 ta yangi qiymat qo'shing (2 xil usulda);
4 ta qiymatni o'chiring (4 xil usulda).

7-mashq
Bozorlik deb nomlangan bo'sh ro'yhat tuzing. Keyin unga bozorlik uchun 5 ta mahsulot nomini qo'shing.
Va ulardan 2 tasini indexi bo'yicha o'chirib tashlang, va ro'yhatning boshiga o'rtasiga va oxiriga 3 ta mahsulotni qo'shing.
So'ngra elementlardan 2 tasini qiymati bo'yicha o'chirib tashlang. Va yana 3 ta mahsulot nomini ro'yhatning turli joylariga qo'shing.
Eng so'ngida ro'yhatni konsulga chiqarib qo'ying.

"""



""" Elementning qiymatini o'zgartirish """
# family = ["Xasanov Husanboy", "Olimov Ahmadjon", "Jo'rabek", 'Shamsiddin', 55, 90 ]
# print(family)

# family[0] = "Mirziyo"
# family[-2] = 49
# print(family)

"""
9-mashq
friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chirib tashlang.
Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.

10-mashq
sonlar = [-34, 45, 0, -65.3, 3.6, 2, 62]  ushbu ro'yhatdagi:
birinchi va to'rtinchi elementlar ayirmasini toping.
minus birinchi elementni minus uchinchi elementga ko'paytiring.
ikkinchi element ildizini toping.
birinchi elementga uchinchi elementni qo'shib chiqqan natijani, -ikkinchi elementga bo'ling.

11-mashq
Foydalanuvchidan uning ismini va u o'qigan kitoblaridan 5 tasini so'rab kitoblar deb nomlangan ro'yhatga qo'shing.
Keyin esa ro'yhatdan 1 ta kitobni o'chirib tashlang.
So'ngra ro'yhatning 2- va 3-indexlariga yangi kitoblar nomini qo'shing.

12-mashq
Bozorlik deb nomlangan bo'sh ro'yhat tuzing.
Unga 5 ta mahsulot qo'shing, 2 tasini indexi orqali, 2 tasini qiymati orqali o'chiring,
so'ngra boshiga, o'rtasiga va oxiriga yangi elementlar qo'shing.
Natijani konsolga chiqaring.
"""
# sonlar = [-34, 45, 0, -65.3, 3.6, 2, 62]
# print(sonlar[1] - sonlar[4])


""" Sug'irib olib qo'shish --> append() va pop()"""
# guruh1 = ["Nurziyo", "Jahongir", "Ziyovuddin", "Abdullo"]
# guruh2 = ["Azizbek", "Abduhalil", "I.Abdullo", "Elbek", "Mirziyo"]

# guruh1.append(guruh2.pop(1))
# guruh1.insert(1, guruh2.pop(0))

# print(guruh1)
# print(guruh2)


""" Ro'yhatdan nusxa olish -->  copy() """
# guruh3 = guruh1.copy()
# print(guruh3)

""" 24-mashq
sonlar deb nomlangan ro'yhat tuzing unda eng kamida 10 ta manfiy(-) va musbat(+) sonlar bo'lsin.
Keyin esa yangi musbat sonlar deb nomlangan yangi bo'sh ro'yhat yarting va unga sonlar ro'yhatidan 
faqat musbat sonlarni sug'urib olib qo'shing.
So'ngra har ikkala ro'yhatni konsulga chiqaring.
"""

# sonlar = [-34, 45, 0, -65.3, 3.6, 2, 62]
# musbat_sonlar = []

# musbat_sonlar.append(sonlar.pop(6))
# musbat_sonlar.append(sonlar.pop(5))
# musbat_sonlar.append(sonlar.pop(4))
# musbat_sonlar.append(sonlar.pop(2))
# musbat_sonlar.append(sonlar.pop(1))


# print(musbat_sonlar)
# print(sonlar)

"""
Taomlar degan ro'yxat tuzing va ichiga istalgan 5ta taomning nomini kiriting.
-nonushta degan yangi ro'yxatga taomlardan nusxa oling;
-yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing;
-ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring.
"""
# taomlar = ["Palov", "Non", "Qaymoq", "Norin", "Sho'rva"]
# nonushta = taomlar.copy()
# print(taomlar)
# print(nonushta)

# nonushta.pop(4)
# nonushta.pop(3)
# nonushta.pop(0)
# print(nonushta)

# nonushta.append("Sut")
# nonushta.append("Sumalak")
# print(nonushta)
# print(taomlar)

"""
Shaxarlar deb nomlangan ro'yhat tuzing va unda 6 ta o'zingiz bilgan shaxar nomi bo'lsin.
Foydalanuvchidan 3 ta shahar kiritishini so'rang va ularni turli joylarga qo'shing.
Uzb degan bo'sh ro'yhat tuzing va unga yuqoridagi ro'yhatdan O'zbekiston shaharlarini sug'urib olib qo'shing.
"""

shaharlar = ["Andijon", "Venetsiya", "Berlin", "London", "Samarqand", "Parij"]
# shaharlar.insert(0, input("Shahar nomi ni kiriting: "))
# shaharlar.insert(3, input("Shahar nomi ni kiriting: "))
# shaharlar.append(input("Shahar nomi ni kiriting: "))

# uzb =[]
# uzb.append(shaharlar.pop(6))
# uzb.append(shaharlar.pop(1))

# print(shaharlar)
# print(uzb)


""" Ro'yhatning uzunligini o'lchash --> len() """ # len --> length --> uzunlik
# print(len(shaharlar))
# print(f"Bizning oilada {len(shaharlar)} ta inson yashaydi")

# sonlar = [1,2,3,4,5,6,7,45435,54,5,34,]
# print(len(sonlar))


""" Matinni uzunligini o'lchash """
# ism = "Abdulhamid '"
# print(len(ism))



""" sum(), max(), min() funksiyalari """
# sonlar = [32,-323, 4.3, 54,27,3,90, 8.1, 0, -54, 433]

# print(max(sonlar)) # eng katta sonni topib beradi
# print(min(sonlar)) # eng kichik sonni topib beradi
# print(sum(sonlar)) # Ro'yhatdagi sonlar yig'indisini topib beradi

# print(f"Ro'yhatda jami {len(sonlar)} ta son bor. Kattasi {max(sonlar)}, kichigi {min(sonlar)} va yig'indisi {sum(sonlar)} ga teng.")



""" range() - sonli oraliq hosil qilib beradi """
# sonlar = list(range(-100, 100))
# print(sonlar)

# juft = list(range(2, 100, 2))
# print(juft)

# toq = list(range(1, 100, 2))
# print(toq)

# beshga = list(range(5 , 50, 5))
# print(beshga)

# onikkiga = list(range(12, 100, 12))
# print(onikkiga)


"""

14-mashq
sonlar = [2, 6, -9, 0, 8.5, 21, 65, -34, 43.6, -44, 847, 0, 32, -4]
Ushbu ro'yhatdagi:
-sonlarning yig'indisini toping;
-ro'yhatning uzunligini toping;
-eng katta va eng kichik sonni toping.

15-mashq
3 dan 100 gacha juft sonli ro'yhat tuzing;
-ro'yhatdagi sonlar yig'indisini toping;
-eng kichkina son va eng katta son yig'indisini toping.

16-mashq
200 dan 430 gacha bo'lgan toq sonlar ro'yxatini tuzing.
-101 dan 2020 gacha bo'lgan juft sonlardan iborat ro'yhat tuzing.
-322 dan -2 gacha bo'lgan toq sonlardan iborat ro'yhat tuzing va ro'yhatning uzunligini toping.


17-mashq
120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing.
-ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring;
-eng katta va eng kichik son o'rtasidagi ayirmani hisoblang;
-ro'yxatdagi elementlar sonini hisoblang;

18-mashq
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
23-mashq
-2024 dan 2024 gacha bo'lgan juft sonli ro'yhat shakillantiring va ro'yhatdagi eng katta sonni toping;
123 dan 87384 gacha bo'lgan toq sonli ro'yhat shakillantiring va ro'yhatdagi eng kichik sonni toping;
352 dan 20010118 gacha bo'lgan faqat 11 ga bo'linadigan sonli ro'yhat shakillantiring va ro'yhatdagi barcha sonlarning yig'indisini toping.
"""

"""
22-mashq
Foydalanuvchidan ikkita son qabul qilib olib ular oralig'ida joylashgan sonlardan iborat sonli ro'yhat shakillantiring.
Ro'yhatning uzunligini konsulga chiqaring.
Ro'yhatni avval o'sish tartibida so'ngra kamayish tartibida tartiblang va konsulga chiqaring.
"""

"""
24-mashq
45 dan 120 gacha bo'lgan juft sonli ro'yxat;
30 dan 90 gacha bo'lgan toq sonli ro'yxat;
980 dan 1560 gacha 3 ga qoldiqsiz bo'linadigan sonlardan iborat ro'yhat;
-10 dan 32 gacha 9 ga qoldiqsiz bo'linadigan sonlardan iborat ro'yhat;
50 dan 100 gacha 3 ga qoldiqsiz bo'linadigan sonlardan iborat ro'yhat tuzing.

25-mashq
O'zingizga ma'lum gullar ro'yxatini tuzing(eng kamida 6 ta) va ro'yxatni konsolga chiqaring.
-ro'yxatning uzunligini konsolga chiqaring
- ro'yxatni doimy tartiblangan holda konsolga chiqaring;
- ro'yxatni doimy teskari tartibda konsolga chiqaring;
- ro'yxatni ortidan(aylantirib) boshlab konsolga chiqaring;
"""






