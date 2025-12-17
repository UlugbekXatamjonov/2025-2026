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

# ismlar = ["Laylo", "Muslima", "Ma'rifat", "Odina", "Umida", "Dilshoda"]
# print(f"Salom {ismlar[0]}, ertaga qayerga borasan.")

# for ism in ismlar:
#     print(f"Salom {ism}, ertaga qayerga borasan.")
#     print("Agar ertaga vaqting bo'lsa hayvonot bog'iga borsak nima deysan ?")
    
# print("Bu habar hammaga yuborildi")

""" range() """
# for son in range(5):
#     print(son)

sonlar = [1,2,3,4,5,]
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

1-mashq
13 dan 90 gacha bo'lgan juft sonli ro'yhat tuzing va ro'yhatdagi har bir sonning 5-darajasini chiqaring.

2-mashq
20 dan 75 gacha bo'lgan toq sonli ro'yhat tuzing va ro'yhatdagi har bir sonning ildizni chiqaring.

3-mashq
Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, 
va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga qo'shing. Ro'yxatni konsolga chiqaring.

4-mashq
4 dan 873 gacha bo'lgan toq sonli ro'yhat tuzing va ro'yhatdagi har bir sonning ildizini chiqaring.

5-mashq
-200 dan 200 gacha bo'lgan toq sonli ro'yhat tuzing va ro'yhatdagi har bir sonning o'zidan 10 taga katta sonni chiqaring.    

6-mashq
Foydalanuvchidan 5 ta eng sevimli multfilmini kiritshni so'rang, va multfilm degan ro'yxatga saqlab oling. 
Natijani konsolga chiqaring. 
 
7-mashq   
5 dan 100 gacha bo'lgan juft sonli ro'yhat tuzing va ro'yhatdagi har bir sonning 3-darajasini chiqaring.

8-mashq
10 dan 50 gacha bo'lgan toq sonli ro'yhat tuzing va ro'yhatdagi har bir sonning ildizni va 2-darajasini toping chiqaring.

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





