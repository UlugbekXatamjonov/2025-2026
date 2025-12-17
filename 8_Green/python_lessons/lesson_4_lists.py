""" Ro'yhatlar - Lists 
Ro'yxat — bu bitta o'zgaruvchiga bir nechta qiymatlarni joylash imkonini beruvchi ma'lumot turi.

O'xshatish: Ro'yxat — bu xuddi “sumka” yoki “quti”, ichiga bir nechta narsalarni solib qo'yishimiz mumkin.
Masalan: maktab sumkasiga daftar, qalam, kitob, chizg'ichni solish mumkin — bu xuddi ro'yxatga o'xshaydi.
"""

# ism = "Ali"
# yosh = 33
# ism2 = "Aziz"

# sumka = ["daftar", "ruchka", "Qalam", "Muslima", "Hadicha", 23, 209]
# print(sumka)
# print(type(sumka)) # list

# print(sumka[2])
# print(sumka[-3])

""" Element, Index
Ro'yxatda har bir elementning o'z raqami (indeksi) bor.
Python'da indeks 0 dan boshlanadi!

sumka = ["daftar", "qalam", "kitob", "chizg'ich"]
            0         1        2          3
           -4        -3       -2         -1

Son o'qi   
-4 -3 -2 -1 0 1 2 3 4
"""


""" Ro'yhat turlari """
ismlar = ["Ali", 'Olim', "Anvar", "Abbos"]
sonlar = [3,57,-6,0,54,8]
darslar = ["Pyhton", "Django", 3, 10]

# print(ismlar)
# print(sonlar)
# print(ismlar[0])
# print(ismlar[2], ismlar[3])
# print(f"Biz  o'quv markazda {darslar[0]} va {darslar[1].upper()} ni o'rganamiz")


""" Bo'sh ro'yhatlar """
bosh_royhat = []
bosh_list = list()

# print(bosh_list)
# print(bosh_royhat)


"""
O'zingizga ma'lum ismlardan 7 tasini kiritgan holda ro'yxat tuzing. 
Va ro'yhatdagi hamma ismni alohida qilib konsulga chiqaring.
"""

# davlatlar = ["O'zbekiston", "Qozog'iston", "Turkmaniston"]
# print(davlatlar[0])
# print(davlatlar[1])
# print(davlatlar[2])


""" Ro'yhatga ma'lumot qo'shuvchi metodlar """
""" .append() """

# davlatlar.append("Xitoy")
# davlatlar.append("Braziliya")
# davlatlar.append(3454)
# print(davlatlar)

""" .insert() """

# davlatlar.insert(0, "BAA")
# davlatlar.insert(4, "Singapur")
# print(davlatlar)

"""
1-mashq
ismlar degan ro'yxat tuzing va kamida 5 ta yaqin do'stingizning ismini kiriting.
Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring.

2-mashq
sinfdoshar deb nomlangan ro'yhat tuzing va unda 4 ta sinfdoshingizning ismin bo'lsin.
Keyin ro'yhatning boshiga, o'rtasiga va oxiriga 1 tadan yangi ismlar qo'shing.
"""


""" 1-mashq """
# ismlar = ["Zebo", "Samira"]
# print(f"Salom {ismlar[0]} yaxshimisan")

""" 2-mashq """

"""
3-mashq
Nechata oila azolaringiz bo'lsa ularning barchalarining yoshlarini so'rab ro'yhatga qo'shing hamda. 
Oila azolaringizning yoshlari yig'indisi va o'rta arifmetigini toping.

4-mashq
sonlar deb nomlangan ro'yxat tuzing va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
Yuqoridagi ro'yxatdagi sonlar ustida 4 ta turli arifmetik amallar bajarib ko'ring.
"""

""" 3-mashq """
# oila = []
# oila.append(int(input("1-oila azongizni yoshini kiriting: ")))
# oila.append(int(input("2-oila azongizni yoshini kiriting: ")))
# oila.append(int(input("3-oila azongizni yoshini kiriting: ")))
# oila.append(int(input("4-oila azongizni yoshini kiriting: ")))

# ummumiy = oila[0] + oila[1] + oila[2] + oila[3]
# print(f"Oila azolaringizni ummumiy yoshi {ummumiy} da, o'rtacha yoshi {ummumiy/4} da")

""" 4-mashq """
from math import sqrt
# sonlar = [7, -8, 0, -4, 7.5, 34, 3, 9.4, 44, -6]
# print(sonlar)

# print(sonlar[1] + sonlar[4])
# print(sonlar[4] / sonlar[-2])
# print(sonlar[-3] * sonlar[5])
# print(sonlar[0] - sonlar[3])
# print(sqrt(sonlar[5]))




""" Ro'yhatdan elementni o'chirish """
fruts = ["olma", "banan", "olcha", "gilos", "o'rik", "malina"]
# print(fruts)

# # 1-usul
# del fruts[0] # elementni index bo'yicha o'chiradi
# print(fruts)

# # 2-usul
# fruts.remove("banan") # elementni qiymati(nomi) bo'yicha o'chiradi
# print(fruts)

# # # 3-usul
# fruts.pop(3) # elementni index bo'yicha o'chiradi
# print(fruts)

# # # 4-usul
# fruts.pop() # ro'yhatdagi oxirgi elementni o'chiradi
# print(fruts)

 
"""
4-mashq
sonlar deb nomlangan ro'yxat tuzing va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
Yuqoridagi ro'yxatdagi sonlar ustida 4 ta turli arifmetik amallar bajarib ko'ring.
yana 2 tasini esa o'chirib tashlang.

"""

# sonlar = [3, 0, -6, 89, -43, 63, 6.7, -6, 33]
# print(sonlar[0] * sonlar[-1])


"""
5-mashq
mevalar deb nomlangan ro'yhat tuzing va unga eng kamida 5 meva nomini kiriting.
Ro'yhatning oxiriga yana 3 ta meva nomini qo'shing keyin, 3 ta mevani indexsi bo'yicha o'chirib tashlang.
So'ngra yana 3 yangi mevani ro'yhatning boshiga qo'shing.
"""


""" Elementning qiymatini o'zgartirish """
# family = ["Xasanov Husanboy", "Olimov Ahmadjon", "Jo'rabek", 'Shamsiddin' ]
# print(family)

# family[0] = "Ziyovuddin"
# family[2] = "Abror"
# print(family)

""" Ro'yhatni tozalovchi metod --> clear() """
# family.clear()  # ro'yhatni ichidagi elementlarni tozab tashlash
# print(family)

""" Ro'yhatni o'chirish --> del """
# del family # ro'yhatni o'chiradi


"""
6-mashq
Fanlar deb nomlangan ro'yhat tuzing, 5 ta fan bo'lsin. Keyin esa:
2 ta yangi qiymat qo'shing (2 xil usulda);
4 ta qiymatni o'chiring (4 xil usulda).

7-mashq
Bozorlik deb nomlangan bo'sh ro'yhat tuzing. Keyin unga bozorlik uchun 5 ta mahsulot 
nomini qo'shing.
Va ulardan 2 tasini indexi bo'yicha o'chirib tashlang, va ro'yhatning boshiga o'rtasiga va oxiriga 3 ta mahsulotni qo'shing.
So'ngra elementlardan 2 tasini qiymati bo'yicha o'chirib tashlang.
Eng so'ngida ro'yhatni konsulga chiqarib qo'ying.

8-mashq
Family deb nomlangan bo'sh ro'yhat tuzing.
Ro'yhatga elementlarni foydalanuvchining o'zidan so'ragan holda, eng kamida 4 ta oila azosini ismini ro'yhatga qo'shing. 
So'ngra ro'yhatdagi elementlarni konsulga chiqaring. Eng so'ngida esa ro'yhatni tozalang.
"""
""" 6-mashq """
# fanlar = ["algebra", "geometriya", 'tarix', 'geografiya', 'ingliz tili']
# fanlar.append("Rus tili")
# fanlar.insert(2, "Nemis tili")
# print(fanlar)

# del fanlar[0]
# fanlar.remove("geometriya")
# fanlar.pop()
# fanlar.pop()
# print(fanlar)

""" 8-mashq """
# family = []
# family.append(input("1-oila azongizni ismini kiriting: "))
# family.append(input("2-oila azongizni ismini kiriting: "))
# family.append(input("3-oila azongizni ismini kiriting: "))
# family.append(input("4-oila azongizni ismini kiriting: "))
# print(family)

# family.clear()
# print(family)


"""
9-mashq
friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chirib tashlang.
Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.


10-mashq
sonlar = [-34, 45, 0, -65.3, 3.6, 2, 62] ushbu ro'yhatdagi:
birinchi va to'rtinchi elementlar ayirmasini toping.
minus birinchi elementni minus uchinchi elementga ko'paytiring.
uchinchi element ildizini toping.
birinchi elementga uchinchi elementni qo'shib chiqqan natijani, -ikkinchi elementga bo'ling.
"""
# sonlar = [-34, 45, 0, -65.3, 3.6, 2, 62]
# print(sonlar[1] - sonlar[4])


"""
11-mashq
Foydalanuvchidan uning ismini va u o'qigan kitoblaridan 5 tasini so'rab kitoblar deb nomlangan ro'yhatga qo'shing.
Keyin esa ro'yhatdan 1 ta kitobni o'chirib tashlang.
So'ngra ro'yhatning 2- va 3-indexlariga yangi kitoblar nomini qo'shing.
"""
# ism = input("Ismingizni kiriting: ")
# books = []
# books.append(input(f"{ism} 1-kitob nomini kiriting: "))
# books.append(input(f"{ism} 2-kitob nomini kiriting: "))
# books.append(input(f"{ism} 3-kitob nomini kiriting: "))
# books.append(input(f"{ism} 4-kitob nomini kiriting: "))
# books.append(input(f"{ism} 5-kitob nomini kiriting: "))
# print(books)

# books.pop()
# books.insert(2, "O'tgan kunlar")
# books.insert(3, "Kecha va kunduz")
# print(books)


""" Sug'irib olib qo'shish --> append() va pop()"""
# family = ["Xasanov Husanboy", "Olimov Ahmadjon", "Jo'rabek", 'Shamsiddin' ]
# oila = []
# print(oila)

# oila.append(family.pop(2))
# oila.append(family.pop(1))
# print(family)
# print(oila)


""" Ro'yhatdan nusxa olish -->  copy() """
# ismlar = ["Xasanov", "Husanboy", "Olimov", "Ahmadjon", "Jo'rabek", 'Shamsiddin' ]
# ismlar2 = ismlar.copy()

# print(ismlar)
# print(ismlar2)


""" Ro'yhatning uzunligini o'lchash --> len() """ # len --> length --> uzunlik
# print(len(ismlar))
# print(f"Bizning oilada {len(family)} ta inson yashaydi")

# sonlar = [1,2,3,4,5,6,7,45435,54,5,34,]
# print(len(sonlar))


# """ Matinni uzunligini o'lchash """
# ism = "Abdulhamid"
# print(len(ism))


"""
24-mashq
Shaxarlar deb nomlangan ro'yhat tuzing va unda 6 ta o'zingiz bilgan shaxar nomi bo'lsin.
Foydalanuvchidan 3 ta shahar kiritishini so'rang va ularni turli joylarga qo'shing.
Uzb degan bo'sh ro'yhat tuzing va unga yuqoridagi ro'yhatdan O'zbekiston shaharlarini sug'urib olib qo'shing.
"""

"""
25-mashq
sonlar deb nomlangan ro'yhat tuzing unda eng kamida 10 ta manfiy va musbat sonlar bo'lsin.
Keyin esa yangi musbat sonlar deb nomlangan yangi bo'sh ro'yhat yarting va unga sonlar ro'yhatidan
faqat musbat sonlarni sug'urib olib qo'shing. So'ngra har ikkala ro'yhatni konsulga chiqaring.

26-mashq
Mehmonlar deb nomlangan  ro'yxat tuzing unda 6 7 ta sim bo'lsin. .pop() va .append()
metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends
ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.

27-mashq
Taomlar degan ro'yxat tuzing va ichiga istalgan 5ta taomning nomini kiriting.
-nonushta degan yangi ro'yxatga taomlardan nusxa oling;
-yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing;
-ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring.
"""



""" sum(), max(), min() funksiyalari """
# sonlar = [32,-323, 4.3, 54,27,3,90, 8.1, 0, -54, 433]

# print(max(sonlar)) # eng katta sonni topib beradi
# print(min(sonlar)) # eng kichik sonni topib beradi
# print(sum(sonlar)) # Ro'yhatdagi sonlar yig'indisini topib beradi

# print(f"Ro'yhatda jami {len(sonlar)} ta son bor. Kattasi {max(sonlar)}, kichigi {min(sonlar)} va yig'indisi {sum(sonlar)} ga teng.")


""" range() - sonli oraliq hosil qilib beradi """
# sonlar = list(range(50))
# print(sonlar)

# juft = list(range(2, 100, 2))
# print(juft)

# toq = list(range(1, 100, 2))
# print(toq)

# beshga = list(range(30 , 100, 5))
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
"""

"""
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


# sonlar15 = list(range(4, 100, 2)) # 2,3,4,5,6,  ... 98,99,100
# print(sonlar15)





""" Ro'yhat elementlarini tartiblash """
ismlar = ["Xasanov", "Husanboy", "Olimov", "Ahmadjon", "Jo'rabek", 'Shamsiddin', "Abdulaziz", "Abdulloh"]
print(ismlar)

""" .sort() --> Ro'yhatni alifbo bo'yicha tartiblaydigan metod """
ismlar.sort() # Ro'yhatni alifbo bo'yicha tartiblaydi
print(ismlar)

ismlar.sort(reverse=True) # Ro'yhatni alifboga teskari tartibda tartiblaydi
print(ismlar)

""" .reverse() --> Ro'yhatni aylantirib beradigan metod """
ismlar.reverse() # Ro'yhatni aylantirib beradi
print(ismlar)










