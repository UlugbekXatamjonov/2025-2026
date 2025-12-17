""" == """
ismlar = ['Ali', 'Olim', 'Kamron', 'Abdulloh']
# for ism in ismlar: # == -> teng bo'lsa, tengmi ?
#     if ism == "Ali":
#         print(f"Salom {ism}. Ahvollaring yaxhimi ?")
#     else:
#         print(f"Salom {ism}")


""" != """
# for ism in ismlar: 
#     if ism != "Olim": # teng bo'lmasa
#         print(f"Salom {ism}, Olim kelmadimi ?")
#     else:
#         print(f"Salom {ism}")

"""
    ==  ---> teng bo'lsa
    !=  ---> teng bo'lmasa
    >   ---> katta bo'lsa
    <   ---> kichik bo'lsa
    >=  ---> katta yoki teng bo'lsa
    <=  ---> kichik yoki teng bo'lsa
    or   ---> yoki
    and  ---> va 
"""

# son = int(input("Son kiriting: "))

# if son > 0:
#     print(f"{son} musbat son")
# elif son == 0:
#     print(f"{son} musbat son ham manfiy son ham emas !")
# else:
#     print(f"{son} manfiy son")

# print("Dasturning davomi")

# from math import sqrt
# son3 = int(input("Sonni kiriting: "))

# if son3 > 0:
#     print(f"{son3} ning ildizi {sqrt(son3)}")
# else:
#     print("Musbat son kiriting")


# son1 = int(input("1-sonni kiriting: "))
# son2 = int(input("2-sonni kiriting: "))

# if son1 > son2:
#     print(f"{son1} > {son2}")
# elif son1 < son2:
#     print(f"{son1} < {son2}")
# elif son1 == son2:
#     print(f"{son1} = {son2}")
# else:
#     print(f"{son1} = {son2}")







# ball = float(input("Choraklik ummumiy balingizni kiriting: "))

# if ball < 0 or ball > 200:
#     print("Siz noto'g'ri son kiritingiz !")

# elif ball >= 0 and ball < 120:
#     print("Siz imtihondan o'ta olmadingniz !")
    
# elif ball >= 120 and ball < 170:
#     print("Siz imtihondan o'tdingniz !")
    
# elif ball >= 170 and ball <= 200:
#     print("Siz imtihondan o'tdingniz va grant yutib oldingiz !")




"""
1-Mashq | Foydalanuvching bahosini so'rab, uning natijasini ayting 
0 va 1 --> juda yomon
2  --> qoniqarsiz
3  --> qoniqarli
4  --> yaxshi
5  --> a'lo

Namuna: D:Bahoningni kiriting: 4
        D: Sizning natijangiz yaxshi.

"""

# baxo = int(input("Baxongizni kiriting: "))

# if baxo == 0 or baxo == 1:
#     print("Sizning natijaning juda yomon")

# elif baxo == 2:
#     print("Sizning natijaning qoniqarsiz")
# elif baxo == 3:
#     print("Sizning natijaning qoniqarli")
# elif baxo == 4:
#     print("Sizning natijaning yaxshi")
# elif baxo == 5:
#     print("Sizning natijaning alo")
# else:
#     print("Siz noto'g'ri son kiritdingiz !!!")




   
""" Toq-juft """

# son = int(input("Son kiriting: "))
# if son%2 == 0: # % - sonni bir songa bo'lganda necha xona qoldiq qolishini ifodalaydi
#     print(f"{son} - juft")
# elif son%2 == 1:
#     print(f"{son} - toq")
    

""" Bir songa bo'linishlik """
# son = int(input("Son kiriting, men uni 5 ga bo'linish yoki bo'linmasligini topib beraman: "))
# if son%5 == 0: # % - sonni bir songa bo'lganda necha xona qoldiq qolishini ifodalaydi
#     print(f"{son} --> 5 ga qoldiqsiz bo'linadi ✅")
# else:
    # print(f"{son} --> 5 ga qoldiqsiz bo'linmaydi ❌")

""" parol """
# password1 = input("Yangi parol kiriting: ")
# password2 = input("Parolni takrorlang: ")

# if password1 == password2:
#     if len(password1) >= 8:
#         print("parol muvaffaqiyatli o'rnatildi ✅")
#     else:
#         print("Parol eng kamida 8 ta belgidan iborat bo'lishi kerak ⚠")
# else:
#     print("Parollar bir biriga mos kelmadi ❌")


"""
12-mashq
Foydalanuvchidan 5 ta son qabul qiling. Ular ichidan musbat bo'lganlari uchun:
    - ildizini toping
    - 4-darajaga ko'tarib bering
    - o'zidan 2 ta katta sonni toping
"""

sonlar = []

for s in range(5):
    sonlar.append(int(input(f"{s+1}-sonni kiriting: ")))

print(sonlar)

from math import sqrt

for son in sonlar:
    if son > 0:
        print(f"{son} uchun -------------")
        print(sqrt(son))
        print(son**4)
        print(son+2)

