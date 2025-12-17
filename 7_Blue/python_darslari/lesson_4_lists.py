""" Lists - Ro'yhatlar """  
ismlar = ["Abbos", "Azizbek", "Oisha", "Dilmurod", "Anvar", "Husnida", "Muhlisa"]
# print(ismlar)

"""
List - Ro'yhat, O'zgaruvchi turi
element - Ro'yhatni tashkil qiluvchi ma'lumot
index - elemetning tartib raqami, har bir elementda 2 ta index bo'ladi, manfiy(-) va musbat(+)
""" 

# print(ismlar[2])
# print(ismlar[-5], ismlar[-4])
#
# print(type(ismlar)) # list


""" Qo'shish """
""" 1-usul """
# ismlar.append("Azizbek") # method  - uslub
# ismlar.append(input("Ism kiriting: "))
# print(ismlar)

""" 2-usul """
# ismlar.insert(0, "Shavkat")
# ismlar.insert(4, input("Ism kiriting: "))
# print(ismlar)
#


""" Mashq """
""" sinfdoshar deb nomlangan ro'yhat yarating va unda 4 ta sinfdoshingizning ismini bo'lsin. 
Keyin ro'yhatning boshiga , o'rtasiga va oxiriga 1 tadan yangi ismlar qo'shing. """


# sinfdoshlar = ["Asadbek", "Murodjon", "Olimjon", "Javohir"]
# print(sinfdoshlar)
#
# sinfdoshlar.insert(0, "Hojiakbar")
# sinfdoshlar.insert(30, "Ilg'orjon")
# sinfdoshlar.append("Iymona")
# print(sinfdoshlar)


""" O'chirish """
""" 1-usul """
# del ismlar[0] # del --> index bo'yicha o'chiradi
# del ismlar[-3]
# print(ismlar)

""" 2-usul """
# ismlar.remove("Dilmurod") # .remove(nomi) --> qiymati bo'yicha o'chiradi
# print(ismlar)

""" 3-usul """
# ismlar.pop(-3) # .pop(index) --> index bo'yicha o'chiradi
# print(ismlar)

""" 4-usul """
# ismlar.pop()    # .pop() --> oxirgi elementni o'chiradi
# ismlar.pop()
# print(ismlar)

""" Ro'yhatni o'chirish """
# del ismlar

""" Bo'sh ro'yhat """
# friends = []
# dostlar = list()

"""
1) friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan 
    do'stlaringizni kiriting. Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi 
    yordamida o'chrib tashlang. Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
    
2) mevalar deb nomlangan ro'yhat yarating va unga eng kamida 5 meva nomini kiriting. 
Ro'yhatning oxiriga yana 3 ta meva nomini qo'shing keyin, 3 ta mevani indexsi bo'yicha o'chirib tashlang. 
So'ngra yana 3 yangi mevani ro'yhatning boshiga, o'rtasiga va oxiriga qo'shing. 
    
3) Sonlar deb nomlangan bo'sh ro'yhat yarating. Foydalanuvchidan so'rab unga 5 ta turli manfiy, 
musbat va o'nlik sonlar qo'shing. Keyin ulardan 2 tasini qiymati bo'yicha o'chirib tashlang, 
yana yangi 4 ta elementni ro'yhatning turli joylariga qo'shing. 2 ta elemetni indexi bo'yicha o'chiring.
"""



"""
4) Bozorlik deb nomlangan bo'sh ro'yhat yarating. Keyin unga bozorlik uchun 5 ta mahsulot nomini qo'shing.  
Va ulardan 2 tasini indexi orqali o'chirib tashlang,  va ro'yhatning boshiga o'rtasiga va oxiriga 3 ta mahsulotni qo'shing. So'ngra elementlardan 2 tasini qiymati bo'yicha o'chirib tashlang. Va yana 3 ta mahsulot nomini ro'yhatning turli joylariga qo'shing. Eng so'ngida ro'yhatni konsulga chiqarib qo'ying.
"""


"""
5) Foydalanuvchidan uning ismini va u o'qigan kitoblaridan 5 tasini so'rab kitoblar deb nomlangan ro'yhatga qo'shing. 
Keyin esa ro'yhatdan 1 ta kitobni o'chirib tashlang. So'ngra ro'yhatning 2- va 3- indexlarga yangi kitoblar nomini qo'shing.

6) Fanlar deb nomlangan ro'yhat yarating, 5 ta fan bo'lsin. Keyin esa:
    2 ta yangi qiymat qo'shing(2 xil usulda);
    4 ta qiymatni o'chiring(4 xil usulda);


7) sinfdoshar deb nomlangan ro'yhat yarating va unga 4 ta sinfdoshingizning ismini so'rab qo'shing. 
Keyin ro'yhatdan 2 ta ismni o'chiring. Keyin esa ro'yhatni tozalab tashlang va keyin ro'yhatni o'chiring.

8) sonlar = [-34, 45, 0, -65.3, 3.6, 2, 62]  ushbu ro'yhatdagi:
    birinchi va to'rtinchi elementlar ayirmasini toping.
    minus birinchi elementni minus uchinchi elementga ko'paytiring.
    uchinchi element ildizini toping.
    birinchi elementga uchinchi elementni qo'shib chiqqan natijani, -ikkinchi elementga bo'ling
"""
sonlar = [-2, -1, 0, 1, 2, 3, 4, 5] 
# print(sonlar[1] - sonlar[4])

""" Ro'yhatni tozlash """
# print(sonlar)

# sonlar.clear() 
# print(sonlar)


""" max(), min(), sum() """
# print(max(sonlar)) # Eng katta son
# print(min(sonlar)) # Eng kichik son
# print(sum(sonlar)) # Sonlar yig'indisi

""" 
9-mashq
Foydalanuvchidan 5 ta u o'qigan kitoblari nomani so'rang va “books” deb nomlangan ro'yhatga qo'shing. 
So'ngra ro'yhatdagi kitoblar nomini konsulga chiqaring.
Siz o'qigan kitoblar: 1- "O'tgan kunlar", 2- ""...""
"""

# books = []
# books.append(input("1-kitob nomini kiriting: "))
# books.append(input("2-kitob nomini kiriting: "))
# books.append(input("3-kitob nomini kiriting: "))
# books.append(input("4-kitob nomini kiriting: "))
# books.append(input("5-kitob nomini kiriting: "))

# print(f"Siz o'qigan kitoblar: 1-{books[0]} 2-{books[1]}, 3-{books[2]}, 4-{books[3]}, 5-{books[4]}.")



"""
10)
Imtihon ballari deb nomlangan ro'yhat yarating va unga foydalanuvchidan so'rab so'ngi 5 ta imtihon natijalarini kiriting.
So'ngra ro'yhatdagi barcha imtihon natijalarini qo''shib ummumiy ballar yig'indisini toping va konsulga chiqaring.
"""

# ballar = []

# ballar.append(float(input("1-haftalik imtihon balingizni kiriting: ")))
# ballar.append(float(input("2-haftalik imtihon balingizni kiriting: ")))
# ballar.append(float(input("3-haftalik imtihon balingizni kiriting: ")))
# ballar.append(float(input("4-haftalik imtihon balingizni kiriting: ")))
# ballar.append(float(input("5-haftalik imtihon balingizni kiriting: ")))

# # total = (ballar[0] + ballar[1] + ballar[2] + ballar[3] + ballar[4] ) / 5
# total = sum(ballar)
# middle = round(total / 5, 2)
# print(total)
# print(middle)


"""
11-mashq

Foydalanuvchidan uning sevimli taomlari nomini kiritishini so'rang va taomlar deb nomlangan ro'yhatga qo'shing. 
Keyin esa ro'yhatning turli joylariga o'zingizning ham yaxshi ko'rgan taomlaringizni index bo'yicha qo'shing va ro'yhatni konsulga chiqaring.

12-mashq 
Mashinalar deb nomlangan ro'yhat yarating va unda o'zingiz bilgan 5 ta mashina nomi bo'lsin. 
Ro'yhatdan 1 ta mashina nomini del metodi yordamida o'chirib tashlang. 1 ta mashina nomini esa remove metodi yordamida o'chirib tashlang. 
Keyin esa pop metodi yordamida ham 2 hil usulda 1 tadan mashina nomini o'chirib tashlang va ro'yhatni konsulga chiqaring.
"""

""" Elementning qiymatini o'zgartirish """
# mashinalar = ["BMW M5", "CHevrolet Cobalt", "Porshe 911", "Nissan GTR"]
# print(mashinalar)

# mashinalar[0] = "BMW M8"
# mashinalar[2] = input("Yangi nomni kiriting:")
# print(mashinalar)

""" Ro'yhatning uzunligini o'lchash """
# print(len(mashinalar)) # len() - length

# print(f"Sizda {len(mashinalar)} ta mashina bor.")

"""
13-mashq
O'zingizga ma'lum 7 ta davlat nomini qo'shgan holatda davlatlar deb nomlangan ro'yhat tuzing. 
3 ta elementni 3 hil usulda o'chirib tashlang. Yangi 2 ta davlat nomini 2 xil usulda qo'shing. Va so'ngida ro'yhatni tozlab tashlang.

14-mashq
Foydalanuvchidan 7 ta ism so'rang va ismlar deb nomlangan ro'yhatga qo'shing. Ro'yhatdagi 2 ta elementni qiymatini o'zgartiring. 
Yangi 2 ta ismni 2 xil usulda qo'shing. 3 ta elementni 3 hil usulda o'chirib tashlang.
"""


"""
15-mashq
Foydalanuvchidan 3 ta son kiritishini so'rang va uni sonlar deb nomlangan ro'yhatga qo'shing so'ngra:
    -ro'yhatdagi eng katta sonni toping.
    -ro'yhatdagi eng kichik sonni toping.
    -barcha sonlar yig'indisini toping.
"""


"""
sonlar = [2, 6, -9, 0, 8.5, 21, 65, -34, 43.6, -44, 847, 0, 32, -4]
Ushbu ro'yhatdagi:
-sonlarning yig'indisini toping;
-ro'yhatning uzunligini toping;
-eng katta va eng kichik sonni toping.
"""


""" Sug'urib olib qo'shish """
# green = ["Komron", "Javohir", "Zilola", "Inomjon", "Bobur", "Mirziyo"]
# blue = ["Muhammadali", "Nigora", "Shohjahon", "Abubakir", "Azizbek", "Saidbek", "Kamron"]
# print(green)
# print(blue)

# green.append(blue.pop(0))
# green.insert(0, blue.pop(1))

# print(green)
# print(blue)

"""
17-mashq
sonlar deb nomlangan ro'yhat tuzing unda eng kamida 10 ta manfiy(-) va musbat(+) sonlar bo'lsin.
Keyin esa musbat sonlar deb nomlangan yangi bo'sh ro'yhat tuzing va 
unga sonlar ro'yhatidan faqat musbat sonlarni sug'urib olib qo'shing. So'ngra har ikkala ro'yhatni konsulga chiqaring.


18-mashq
Taomlar degan ro'yxat tuzing va ichiga istalgan 5ta taomning nomini kiriting.
Yangi nonushta ro'yxati tuzing va unga faqat nonushtaga yeyiladigan taomlarni sug'urib olib qo'shing, 
va qo'shimcha 2 ta taom ham qo'shing. ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring.

19-mashq 
Mehmonlar deb nomlangan  ro'yxat tuzing. .pop() va .append() 
metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends degan boshqa 
ro'yxatga sug'urib olib qo'shing.
"""


""" Ro'yhatdan nusxa olish -->  copy() """
# ismlar = ["Xasanov", "Husanboy", "Olimov", "Ahmadjon", "Jo'rabek", 'Shamsiddin' ]
# ismlar2 = ismlar[3:4]

# print(ismlar)
# print(ismlar2)


""" Ro'yhatning uzunligini o'lchash --> len() """ # len --> length --> uzunlik
# print(len(ismlar))
# print(f"Bizning oilada {len(ismlar)} ta inson yashaydi")

# sonlar = [1,2,3,4,5,6,7,45435,54,5,34,]
# print(len(sonlar))


""" Matinni uzunligini o'lchash """
# ism = "Saidbek "
# print(len(ism))


""" range() - sonli oraliq hosil qilib beradi """

# sonlar = list(range(1, 100)) # 1 dan 100 gacha bo'lgan sonlar
# print(sonlar)

# juft = list(range(0, 100, 2)) # juft sonlar
# print(juft)

# toq = list(range(1, 100, 2)) # toq sonlar
# print(toq)

# beshga = list(range(5, 100, 5)) # 5  ga bo'linuvchi sonlar
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

"""22-mashq"""
# juft_sonlar = list(range(120, 1201, 2))
# yigindi = sum(juft_sonlar)
# ayirma = max(juft_sonlar) - min(juft_sonlar)
# qancha = len(juft_sonlar)
# print("Ro'yxatdagi sonlar yig'indisi:", yigindi)
# print("Eng katta va eng kichik sonlar ayirmasi:", ayirma)
# print("Ro'yxatdagi elementlar soni:", qancha)

"""23-mashq"""

# juft_sonlar2 = list(range(100, 1001, 2))
# print("Juft sonlar ro'yxati:", juft_sonlar2)

# toq_sonlar2 = list(range(21, 201, 2))
# print("Toq sonlar ro'yxati:", toq_sonlar2)

# beshga_bolinadigonlar = list(range(100, 501, 5))
# print("5 ga bo'linuvchi sonlar:", beshga_bolinadigonlar)


"""
24-mashq
45 dan 120 gacha bo'lgan juft sonli ro'yxat;
30 dan 90 gacha bo'lgan toq sonli ro'yxat
980 dan 1560 gacha 3 ga qoldiqsiz bo'linadigan sonlardan iborat ro'yhat
-10 dan 32 gacha 9 ga qoldiqsiz bo'linadigan sonlardan iborat ro'yhat
50 dan 100 gacha 3 ga qoldiqsiz bo'linadigan sonlardan iborat ro'yhat tuzing.
"""
# juft_sonlar = list(range(46, 120, 2))
# print(juft_sonlar)

# toq_sonlar = list(range(31, 90, 2))
# print(toq_sonlar)

# uchga_bolinuvchi = list(range(981, 1560, 3))
# print(uchga_bolinuvchi)

# toqga_bolinuvchi = list(range(-9, 32, 9))
# print(toqga_bolinuvchi)

# uchga_bolinuvchi = list(range(51, 100, 3))
# print(uchga_bolinuvchi)


""" Ro'yhat elementlarini tartiblash """
# ismlar = ["Xasanov", "Husanboy", "Olimov", "Ahmadjon", "Jo'rabek", 'Shamsiddin', "Abdulaziz", "Abdulloh"]
# print(ismlar)
# ismlar.sort() # A-Z | Alifbo bo'yicha tartiblaydi
# print(ismlar)

# ismlar.sort(reverse=True) # Z-A | Alifboga teskari tartiblaydi
# print(ismlar)

# ismlar.reverse()# Ro'yhatni boshi va oxirini aylantirib chiqaradi
# print(ismlar)



# sonlar = [90, -4, 0, 87, -34, 56, 2, 9, 12, -5, 81]
# print(sonlar)

# sonlar.sort() # - > + tartiblaydi
# print(sonlar)

# sonlar.sort(reverse=True) #  + > - tartiblaydi
# print(sonlar)

# sonlar.reverse()# Ro'yhatni boshi va oxirini aylantirib chiqaradi
# print(sonlar)


"""
25-mashq
O'zingizga ma'lum davlatlarning ro'yxatini tuzing (eng kamida 7 ta) va ro'yxatni konsolga chiqaring.
-ro'yxatning uzunligini konsolga chiqaring;
-sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
-reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring;

26-mashq
O'zingizga ma'lum mashinalar ro'yxatini tuzing (eng kamida 7 ta) va ro'yxatni konsolga chiqaring.
ro'yxatning uzunligini konsolga chiqaring;
sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
So'ngra ro'yhatni tozlab tashlang.

27-mashq
10 dan 100 gacha toq sonli ro'yhat tuzing:
-ro'yhatni o'sish va kamayish tartibida tartiblang.


28-mashq
Foydalanuvchidan ikkita son qabul qilib olib ular oralig'ida joylashgan sonlardan iborat sonli ro'yhat shakillantiring.
Ro'yhatning uzunligini konsulga chiqaring.
Ro'yhatni avval o'sish tartibida so'ngra kamayish tartibida tartiblang va konsulga chiqaring.


"""


""" 25-mashq """

# davlatlar = ["O'zbekiston", "Qozog'iston", "Rossiya", "Xitoy", "Turkiya", "AQSH", "Germaniya"]
# print(davlatlar)
# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)
# print(len(davlatlar))
# davlatlar.reverse()
# print(davlatlar)

""" 26-mashq """
# mashinalar = ["BMW", "Mercedes", "Audi", "Lexus", "Toyota", "Kia", "Hyundai"]
# print(mashinalar)
# print(len(mashinalar))
# mashinalar.sort()
# print(mashinalar)
# mashinalar.sort(reverse=True)
# print(mashinalar)
# mashinalar.clear()
# print(mashinalar)



""" 27-mashq """
# toq_sonlar = list(range(11, 100, 2))
# print(toq_sonlar)
# toq_sonlar.sort()
# print(toq_sonlar)
# toq_sonlar.sort(reverse=True)
# print(toq_sonlar)



""" 28-mashq """
# son1 = int(input("Birinchi sonni kiriting: "))
# son2 = int(input("Ikkinchi sonni kiriting: "))
# sonlar = list(range(son1, son2))
# print(sonlar)
# print(len(sonlar))
# sonlar.sort()
# print(sonlar)
# sonlar.sort(reverse=True)
# print(sonlar)



""" Uyga vaqzifa """
"""
29-mashq
Quidagicha sonli ro'yhatlar yarating:
200 dan 400 gacha toq sonli;
301 dan 500 gacha juft sonli;
10 dan 600 gacha 25 ga bo'linadigan sonlardan iborat;


30-mashq
-2024 dan 2024 gacha bo'lgan juft sonli ro'yhat shakillantiring va ro'yhatdagi eng katta sonni toping;
123 dan 87384 gacha bo'lgan toq sonli ro'yhat shakillantiring va ro'yhatdagi eng kichik sonni toping;
352 dan 20010118 gacha bo'lgan faqat 11 ga bo'linadigan sonli ro'yhat shakillantiring va ro'yhatdagi barcha sonlarning yig'indisini toping.

"""




