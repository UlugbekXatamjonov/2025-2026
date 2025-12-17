""" for operatori """
"""
for — bu takrorlash operatori, u bizga bir xil amalni takrorlash imkonini beradi.

mevalar = ["olma", "banan", "gilos"]
for meva in mevalar:
    print(meva)

🗣 Tushuntirish:
“for meva in mevalar” — degani, har safar mevalar ro‘yxatidagi navbatdagi elementni olib, uni meva nomli o‘zgaruvchiga joylashtir.
print(meva) — esa har safar shu qiymatni ekranga chiqaradi.

💡 Hayotiy misol:
Xuddi sen savatdagi har bir mevani navbat bilan olib, stol ustiga qo‘yayotgandek.
"""


# mevalar = ["olma", "banan", "gilos"]
# for meva in mevalar:
#     print(meva)

# print("Mevalar juda foydali")



# ismlar = ["Laylo", "Muslima", "Ma'rifat", "Odina", "Umida", "Dilshoda"]
# for ism in ismlar:
#     print(f"Salom {ism}, ertaga qayerga borasan.")
#     print("Agar ertaga vaqting bo'lsa hayvonot bog'iga borsak nima deysan ?")
    
# print("Bu habar hammaga yuborildi")


# for son in range(1, 577): # [0,1, ... 565]
#     print(f"read, library, sweat, fox, box, water({son}-row)")



"""
Foydalanuvchidan 7 ta ism so'rang va ismlar deb nomlangan ro'yhatga qo'shing. 
"""

# ismlar = []
# for i in range(7): # [0, 2, .. 6]
#     ismlar.append(input(f"{i+1}-ism kiriting: "))

# print(ismlar)


from math import sqrt

# sonlar1 = list(range(1, 100))
# for son in sonlar1:
#     print(f"{son} ning 5-darajasi {son**5} ga teng")
#     print(f"{son} ning ildizi {sqrt(son)} ga teng")



# oila = []
# oila_azolari_soni = int(input("Nechta oila azoingiz bor: "))

# for son in range(oila_azolari_soni):
#     oila.append(input(f"{son+1}-oila azongizni ismini kiriting: "))
# print(oila)


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





"""
1-mashq
13 dan 90 gacha bo'lgan juft sonli ro'yhat tuzing va ro'yhatdagi har bir sonning 5-darajasini chiqaring.

2-mashq
20 dan 75 gacha bo'lgan toq sonli ro'yhat tuzing va ro'yhatdagi har bir sonning ildizni chiqaring.

3-mashq
Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, 
va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga qo'shing. Ro'yxatni konsolga chiqaring.
"""



"""

4-mashq
4 dan 873 gacha bo'lgan toq sonli ro'yhat tuzing va ro'yhatdagi har bir sonning ildizini chiqaring.

5-mashq
-200 dan 200 gacha bo'lgan toq sonli ro'yhat tuzing va ro'yhatdagi har bir sonning o'zidan 10 taga katta sonni chiqaring.    
"""
from math import sqrt
# sonlar4 = list(range(5, 873, 2))
# for son in sonlar4:
#     print(f"{son} ning ildizi {sqrt(son)}")

# sonlar5 = list(range(-199, 200, 2))
# for son in sonlar5:
#     print(f"{son} dan 10 ta katta son {son + 10}")


"""
6-mashq
Foydalanuvchidan 5 ta eng sevimli multfilmini kiritshni so'rang, va multfilm degan ro'yxatga saqlab oling. 
Natijani konsolga chiqaring. 
 
7-mashq   
5 dan 100 gacha bo'lgan juft sonli ro'yhat tuzing va ro'yhatdagi har bir sonning 3-darajasini chiqaring.

8-mashq
10 dan 50 gacha bo'lgan toq sonli ro'yhat tuzing va ro'yhatdagi har bir sonning ildizni va 2-darajasini toping chiqaring.
"""

# cartoon = []
# for son in range(5):
#     cartoon.append(input(f"{son+1}-ultfilm nomini kiriting: "))
# print(cartoon)


# sonlar6 = list(range(6, 100, 2))
# for son in sonlar6:
#     print(f"{son} ning 3-darajasi {son**3}")

# sonlar7 = list(range(11, 50, 2))
# for son in sonlar7:
#     print(f"{son} ning ildiz {sqrt(son)} va 2-darajasi {son**2}")


"""

9-mashq
Foydalanuvchidan 6 ta, uning eng yaxshi do'stlari ismini so'rab, do'stlar deb nomlangan ro'yhatga qo'shing(for tsikli yordamida). 
Va ro'yhatdagi hamma ismlarni konsulga chiqaring.
Namuna: 1-do'stingizni ismini kiriting:
        2-do'stingizni ismini kiriting:

10-mashq
10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. 
    -ro'yxatning xar bir elementining kvadratini va kubini konsolga chiqaring.
    -ro'yhatdagi har bir elementdan 1 ga kichik va 3 ga katta bo'lgan sonni  konsulga chiqaring   
"""



# friends = []
# for son in range(6):
#     friends.append(input(f"{son+1}-do'stingizni ismini kiriting: "))
# print(friends)


# sonlar7 = list(range(11, 100, 2))
# for son in sonlar7:
#     print(f"{son} ning 2-darajasi {son**2}, 3-darajasi {son**3}")
#     print(f"{son} dan 1 ta kichik son {son-1} 3 ta kattasi {son+3}")






