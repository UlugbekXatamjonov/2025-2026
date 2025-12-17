"""
Sonlar(Numbers) bilan ishlash
"""
""" Sonlarning turlari """
x = 1    # integer - int
y = 2.8  # float - float
z = 1j   # complex

# print(x)
# print(y)
# print(z)
    
""" O'nlik son turlari """
# x = 35e12 # 35000.0
# y = 12E4 # 120000.0
# z = 14.76
# print(x)


"""Arifmetik amallar"""

# print(5+7) # qo'shish
# print(5-7) # ayrish
# print(5/7) # bo'lish
# print(5*7) # ko'paytirish

# c = 5+(7-5)*7
# print(c)

""" Darajaga ko'tarish va ildiz chiqarish """
from math import sqrt, pow
# print(sqrt(81))
# print(sqrt(225))

# print(pow(7,6)) # power - daraja
# print(5**9)



"""
1) 15 ning ildizini toping.
2) 1 ning 100-darajasini toping.
3) 100 ning 2 darajasiga 42342 ning ildizni qo'shing.
4) 3434 ning 3 darajasiga 123 ning 2 darajasini qo'shing.
5) 834 va 5 ning yig'indisiga 34355 ning ildizni qo'shin.
6) 45 dan  5 ni airing va natijani 10 ga bo’ling
7) 752 ning ildizini toping
8) 23 ning 4 darajasiga, 32654 ning ildizni qo'shing.
9) 95 ning 3 darajasidan, 6 ning 4 darajasini ayring.
10) 225 ning ildizini toping.
"""


""" round() - sonni yaxlidlash """

# print(round(3.4347565))
# print(round(123.4746548, 2))

""" type() - ma'lumotni turini aniqlab beradi """
# print(type(2))  # int  - integer - Butun son
# print(type(2.5)) # float - float - O'nlik son
# print(type("2")) # str - string - Matn


""" str(), int(), float() """
# a = "20"
# print(a)
# print(type(a))

# a = int(a)
# print(a)
# print(type(a))


# ism = input("Ismingizni kiriting: ").title().strip()
# t_yil = int(input(f"{ism} qachon tug'ilgansiz: "))

# yosh = 2025 - t_yil
# print(f"{ism} siz {yosh} yoshda ekansiz.")


# son1 = int(input("1-sonni kirititng: "))
# son2 = int(input("2-sonni kirititng: "))

# print(f"Siz kiritgan {son1} va {son2} sonlarining o'rta arifmetigi {(son1+son2)/2} ga teng.")


# kv = int(input("Kvadratning tomonini kirititng: "))
# print(f"Tomoni {kv} ga teng bo'lgan kvadratning perimetri P={kv*4} ga, yuzi esa S={kv*kv} ga teng.")

