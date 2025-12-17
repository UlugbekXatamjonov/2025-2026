"""
Sonlar(Numbers) bilan ishalsh
"""
""" Sonlarning turlari """
x = 1    # integer - int - butun son
y = 2.8  # float - float - o'nlik son
z = 1j   # complex


a = 23e8
# print(a)


"""Arifmetik amallar"""
a = 5
b = 7
# print(a+b) # qo'shish
# print(a-b) # ayrish
# print(a/b) # bo'lish
# print(a*b) # ko'paytirish


from math import sqrt, pow
""" Darajaga ko'tarish """  
# print(pow(3, 5))
# print(pow(2, 2))
# print(4**3)
# print(9**6)

""" sqrt() - ildiz chiqarish """
# print(sqrt(4))
# print(sqrt(9))
# print(sqrt(25))
# print(sqrt(25))

"""
1) 15 ning ildizini toping.
2) 1 ning 100-darajasini toping.
3) 100 ning 2 darajasiga 42342 ning ildizni qo'shing.
4) 3434 ning 3 darajasiga 123 ning 2 darajasini qo'shing.
5) 834 va 5 ning yig'indisiga 34355 ning ildizni qo'shin.
6) 45 dan  5 ni airing va natijani 10 ga bo'ling
7) 752 ning ildizini toping
8) 23 ning 4 darajasiga, 32654 ning ildizni qo'shing.
9) 95 ning 3 darajasidan, 6 ning 4 darajasini ayring.
10) 225 ning ildizini toping.
"""
# print(pow(23, 4) + sqrt(32654))


# print(sqrt(15))

# print(pow(100, 2) + sqrt(42342))

""" round() --> Sonni yaxlidlash """

# print(round(5.678))
# print(round(5.489455545, 3))


""" Mashqlar """
"""
1) 345345.456754645 sonini 3 hona aniqlikda yaxlidlang
2) 34343 dan ildiz chiqaring
3) 345435.43 sonini yaxlidlang
"""

""" 2-mashq """ 
""" ism, familiya, yosh, sharif, manzil deb nomlangan o'zgaruvchilar yarating.
Va ularni matnlar bilan birgalikda ishlatib quidagicha natijani konsulga chiqaring:
- Salom mening ismim Asadbek . Toliq ism sharifim Asadbek Mirzaanvarov Otabek o'g'li . 
- Hozirda 22 yoshdaman va hozirda Namangan viloyati Chust tumani Yorqishloq qishlog'i da yashayman.
"""

# ism = input("Ismingiz nima: ")


""" type()"""

a = 36
# print(a)
# print(type(a))

""" str(), float(), int() """

# a = float(a)
# print(a)
# print(type(a))


# ism = input("Ismingizni kiriting: ").title()
# yosh = int(input(f"{ism} yoshingiz nechida: "))
# t_yil = 2025 - yosh

# print(f"{ism} {yosh} yoshdasiz va {t_yil} yilda tug'ilgansiz.")



""" O'rta arifmetik """
son1 = int(input("1-sonni kiriting: "))
son2 = int(input("2-sonni kiriting: "))

print(f"{son1} va {son2} ning o'rta arifmetigi {(son1+son2)/2} ga teng.")





















