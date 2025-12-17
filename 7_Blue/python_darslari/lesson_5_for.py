""" for operatori """
"""
for — bu takrorlash operatori, u bizga bir xil amalni takrorlash imkonini beradi.

mevalar = ["olma", "banan", "gilos"]
for meva in mevalar:
    print(meva)

🗣 Tushuntirish:
“for meva in mevalar” — degani, har safar mevalar ro'yxatidagi navbatdagi elementni olib, uni meva nomli o'zgaruvchiga joylashtir.
print(meva) — esa har safar shu qiymatni ekranga chiqaradi.

💡 Hayotiy misol:
Xuddi sen savatdagi har bir mevani navbat bilan olib, stol ustiga qo'yayotgandek.
"""

# mevalar = ["olma", "banan", "gilos"]
# for meva in mevalar: # meva ="olma"
#     print(f"Men {meva}ni yaxshi ko'raman")
#     print(f"Chunki {meva} juda mazzali")
#     print("Siz ham ko'proq meva istemolo qiling !")

""" Matn uchun """
# ism = "Shavkat"
# for i in ism:
#     print(i)

""" range() """
# for raqam in range(1, 101): # [0,1 .... 99]
#     print(f"Men tannafusdan unumli foydalanaman !({raqam})")

# sonlar = [1,2,3,4,5,]
# sonlar = list(range(1, 20)) # 1,2,3,4,5,6,7,8,9,10,, ...20
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2}")
#     print(f"{son} ning kubi {son**3}")
#     print("----------------------------")
   
   

"""
Foydalanuvchidan 7 ta ism so'rang va ismlar deb nomlangan ro'yhatga qo'shing. 
"""
# ismlar = []

# for i in range(7): # 0, 1 ... 6
#     ismlar.append(input(f"{i+1}-ismni kiriting: "))

# print(ismlar)


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

""" 1-mashq """
# son = int(input("Nechta meva nomini kiritmoqchisiz: "))
# mevalar = []

# for s in range(son):
#     meva = input(f"{s+1} - meva nomini kiriting: ")
#     mevalar.append(meva)  
# print(mevalar)

# sonlar  =list(range(-321, -2, 2))

""" 2-mashq """
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
3-mashq
13 dan 90 gacha bo'lgan juft sonli ro'yhat tuzing va ro'yhatdagi har bir sonning 5-darajasini chiqaring.

4-mashq
20 dan 75 gacha bo'lgan toq sonli ro'yhat tuzing va ro'yhatdagi har bir sonning ildizni chiqaring.

5-mashq
Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, 
va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga qo'shing. Ro'yxatni konsolga chiqaring.

"""
from math import sqrt

""" 3-mashq """
# sonlar3 = list(range(14, 90, 2))
# for son in sonlar3:
    # print(f"{son} ning 5- darajasi {son**5} ga teng.")

""" 4-mashq """
# sonlar4 = list(range(21, 75, 2))
# for son in sonlar4:
#     print(f"{son} ning ildizi  {sqrt(son)} ga teng.")

""" 5-mashq """

# odamlar_soni = int(input("Bugun necha kishi bilan ko'rishdingiz: "))
# odamlar = []
# for son in range(odamlar_soni): # [0, 1, 2,3,4]
#     odamlar.append(input(f"{son+1}-ko'rishgan insoningizning ismini kiriting: "))

# print(odamlar)

"""
6-mashq
4 dan 873 gacha bo'lgan toq sonli ro'yhat tuzing va ro'yhatdagi har bir sonning ildizini chiqaring.

7-mashq
-200 dan 200 gacha bo'lgan toq sonli ro'yhat tuzing va ro'yhatdagi har bir sonning o'zidan 10 taga katta sonni chiqaring.    

8-mashq
Foydalanuvchidan 5 ta eng sevimli multfilmini kiritshni so'rang, va multfilm degan ro'yxatga saqlab oling. 
Natijani konsolga chiqaring. 
"""




