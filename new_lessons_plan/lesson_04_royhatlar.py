""" Ro'yhatlar - Lists 
Ro'yxat — bu bitta o'zgaruvchiga bir nechta qiymatlarni joylash imkonini beruvchi ma'lumot turi.

O'xshatish: Ro'yxat — bu xuddi “sumka” yoki “quti”, ichiga bir nechta narsalarni solib qo'yishimiz mumkin.
Masalan: maktab sumkasiga daftar, qalam, kitob, chizg'ichni solish mumkin — bu xuddi ro'yxatga o'xshaydi.
"""  

sumka = ["daftar", "qalam", "kitob", "chizg'ich"]
# print(sumka)

""" Element, Index
Ro'yxatda har bir elementning o'z raqami (indeksi) bor.
Python'da indeks 0 dan boshlanadi!

sumka = ["daftar", "qalam", "kitob", "chizg'ich"]
            0         1        2          3
           -4        -3       -2         -1

Son o'qi
-4 -3 -2 -1 0 1 2 3 4
"""

""" Ro'yhatdagi elementni chiqarish """
# print(sumka)
# print(sumka[0])
# print(sumka[-2])

""" Ro'yhat turlari """
# ismlar = ["Ali", 'Olim', "Anvar", "Abbos"]
# sonlar = [3,57,-6,0,54,8]
# darslar = ["Pyhton", "Django", 3, 10]

# print(ismlar)
# print(sonlar)
# print(ismlar[0])
# print(ismlar[2], ismlar[3])
# print(f"Biz  o'quv markazda {darslar[0].lower()} va {darslar[1].upper()} ni o'rganamiz")
# 

""" Bo'sh ro'yhatlar """
# bosh_royhat = []
# bosh_list = list()

# print(bosh_list)
# print(bosh_royhat)


""" Ro'yhatga ma'lumot qo'shuvchi metodlar """
# """ .append() """
# friends = []
# friends.append("Olim")
# friends.append(5465)
# friends.append(input("Ismingizni kiriting: "))
# print(friends)

# print(friends[0])
# print(friends[-2])
# print(f"Mening do'stimning ismi {friends[-2]}")

# """ .insert() """
# friends.insert(0, "Asadbek")
# friends.insert(1, input("Ism kiriting: "))
# print(friends)


""" Ro'yhatdan elementni o'chirish """
fruts = ["olma", "banan", "olcha", "gilos", "o'rik", "malina"]

# # 1-usul
# del fruts[0] # elementni index bo'yicha o'chiradi
# print(fruts)

# # 2-usul
# fruts.remove("banana") # elementni qiymati(nomi) bo'yicha o'chiradi
# print(fruts)

# # 3-usul
# fruts.pop(0) # elementni index bo'yicha o'chiradi
# print(fruts)

# # 4-usul
# fruts.pop() # ro'yhatdagi oxirgi elementni o'chiradi
# print(fruts)


""" Ro'yhatni tozalovchi metod --> clear() """
# fruts.clear()  # ro'yhatni ichidagi elementlarni tozab tashlash
# print(fruts)


""" Ro'yhatni o'chirish --> del """
# del fruts # ro'yhatni o'chiradi


""" Elementning qiymatini o'zgartirish """
family = ["Xasanov Husanboy", "Olimov Ahmadjon", "Jo'rabek", 'Shamsiddin' ]
# print(family)

# family[0] = "Ziyovuddin"
# family[2] = "Abror"

# print(family[0])
# print(family)

""" Sug'irib olib qo'shish --> append() va pop()"""
# oila = []
# print(oila)

# oila.append(family.pop(2))
# oila.append(family.pop(1))
# print(oila)


""" Ro'yhatdan nusxa olish -->  copy() """
# ismlar = ["Xasanov", "Husanboy", "Olimov", "Ahmadjon", "Jo'rabek", 'Shamsiddin' ]
# ismlar2 = ismlar.copy()

# print(ismlar)
# print(ismlar2)


""" Ro'yhatning uzunligini o'lchash --> len() """ # len --> length --> uzunlik
# print(len(family))
# print(f"Bizning oilada {len(family)} ta inson yashaydi")

# sonlar = [1,2,3,4,5,6,7,45435,54,5,34,]
# print(len(sonlar))


""" Matinni uzunligini o'lchash """
# ism = "Abdulhamid"
# print(len(ism))


""" sum(), max(), min() funksiyalari """
# sonlar = [32,-323, 4.3, 54,27,3,90, 8.1, 0, -54, 433]

# print(max(sonlar)) # eng katta sonni topib beradi
# print(min(sonlar)) # eng kichik sonni topib beradi
# print(sum(sonlar)) # Ro'yhatdagi sonlar yig'indisini topib beradi

# print(f"Ro'yhatda jami {len(sonlar)} ta son bor. Kattasi {max(sonlar)}, kichigi {min(sonlar)} va yig'indisi {sum(sonlar)} ga teng.")


""" range() - sonli oraliq hosil qilib beradi """
# sonlar = list(range(10, 50))
# print(sonlar)

# juft = list(range(2, 100, 2))
# print(juft)

# toq = list(range(1, 100, 2))
# print(toq)

# beshga = list(range(5 , 50, 5))
# print(beshga)

# onikkiga = list(range(24, 100, 12))
# print(onikkiga)



""" Ro'yhat elementlarini tartiblash """
# ismlar = ["Xasanov", "Husanboy", "Olimov", "Ahmadjon", "Jo'rabek", 'Shamsiddin', "Abdulaziz", "Abdulloh"]
# print(ismlar)

""" .sort() --> Ro'yhatni alifbo bo'yicha tartiblaydigan metod """
# ismlar.sort() # Ro'yhatni alifbo bo'yicha tartiblaydi
# print(ismlar)

# ismlar.sort(reverse=True) # Ro'yhatni alifboga teskari tartibda tartiblaydi
# print(ismlar)

""" .reverse() --> Ro'yhatni aylantirib beradigan metod """
# ismlar.reverse() # Ro'yhatni aylantirib beradi
# print(ismlar)


""" Mashqlar """
"""
--------------------------------------------
qo'shish, o'chirish, o'zgartirish
--------------------------------------------

1-mashq
ismlar degan ro'yxat tuzing va kamida 5 ta yaqin do'stingizning ismini kiriting.
Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring.

2-mashq
sinfdoshar deb nomlangan ro'yhat tuzing va unda 4 ta sinfdoshingizning ismin bo'lsin.
Keyin ro'yhatning boshiga, o'rtasiga va oxiriga 1 tadan yangi ismlar qo'shing.

3-mashq
Nechata oila azolaringiz bo'lsa ularning barchalarining yoshlarini so'rab ro'yhatga qo'shing hamda. 
Oila azolaringizning yoshlari yig'indisi va o'rta arifmetigini toping.

4-mashq
sonlar deb nomlangan ro'yxat tuzing va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
Yuqoridagi ro'yxatdagi sonlar ustida 4 ta turli arifmetik amallar bajarib ko'ring.
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

8-mashq
Family deb nomlangan bo'sh ro'yhat tuzing.
Ro'yhatga elementlarni foydalanuvchining o'zidan so'ragan holda, eng kamida 4 ta oila azosini ismini ro'yhatga qo'shing. 
So'ngra ro'yhatdagi elementlarni konsulga chiqaring. Eng so'ngida esa ro'yhatni tozalang.

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

11-mashq
Foydalanuvchidan uning ismini va u o'qigan kitoblaridan 5 tasini so'rab kitoblar deb nomlangan ro'yhatga qo'shing.
Keyin esa ro'yhatdan 1 ta kitobni o'chirib tashlang.
So'ngra ro'yhatning 2- va 3-indexlariga yangi kitoblar nomini qo'shing.

12-mashq
Bozorlik deb nomlangan bo'sh ro'yhat tuzing.
Unga 5 ta mahsulot qo'shing, 2 tasini indexi orqali, 2 tasini qiymati orqali o'chiring,
so'ngra boshiga, o'rtasiga va oxiriga yangi elementlar qo'shing.
Natijani konsolga chiqaring.

13-mashq
Sonlar deb nomlangan bo'sh ro'yhat tuzing.
Foydalanuvchidan so'rab unga 5 ta turli manfiy, musbat va o'nlik sonlar qo'shing.
Keyin ulardan 2 tasini qiymati bo'yicha o'chirib tashlang, yana yangi 4 ta elementni ro'yhatning turli joylariga qo'shing.
2 ta elementni indexi bo'yicha o'chiring.

--------------------------------------------
max(), min(), sum(), len(), range()
--------------------------------------------

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

--------------------------------------------
tartiblashga doir mashqlar
--------------------------------------------

19-mashq
O'zingizga ma'lum davlatlarning ro'yxatini tuzing (eng kamida 7 ta) va ro'yxatni konsolga chiqaring.
-ro'yxatning uzunligini konsolga chiqaring;
-sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
-reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring;

20-mashq
O'zingizga ma'lum mashinalar ro'yxatini tuzing (eng kamida 7 ta) va ro'yxatni konsolga chiqaring.
ro'yxatning uzunligini konsolga chiqaring;
sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
So'ngra ro'yhatni tozlab tashlang.

21-mashq
10 dan 100 gacha toq sonli ro'yhat tuzing:
-ro'yhatni o'sish va kamayish tartibida tartiblang.

22-mashq
Foydalanuvchidan ikkita son qabul qilib olib ular oralig'ida joylashgan sonlardan iborat sonli ro'yhat shakillantiring.
Ro'yhatning uzunligini konsulga chiqaring.
Ro'yhatni avval o'sish tartibida so'ngra kamayish tartibida tartiblang va konsulga chiqaring.

23-mashq
-2024 dan 2024 gacha bo'lgan juft sonli ro'yhat shakillantiring va ro'yhatdagi eng katta sonni toping;
123 dan 87384 gacha bo'lgan toq sonli ro'yhat shakillantiring va ro'yhatdagi eng kichik sonni toping;
352 dan 20010118 gacha bo'lgan faqat 11 ga bo'linadigan sonli ro'yhat shakillantiring va ro'yhatdagi barcha sonlarning yig'indisini toping.

--------------------------------------------
sug'urib olib qo'shishga doir mashqlar
--------------------------------------------

24-mashq
Shaxarlar deb nomlangan ro'yhat tuzing va unda 6 ta o'zingiz bilgan shaxar nomi bo'lsin.
Ro'yhatni avval alifbo bo'yicha, so'ngra alifboga teskari tartibda tartiblang.
Foydalanuvchidan 3 ta shahar kiritishini so'rang va ularni turli joylarga qo'shing.
Uzb degan bo'sh ro'yhat tuzing va unga yuqoridagi ro'yhatdan O'zbekiston shaharlarini sug'urib olib qo'shing.

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


