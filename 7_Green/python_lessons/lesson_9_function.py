"""
Thame: Funkcions - Funksiyalar
"""
"""
Funksiya - Funksiya ma'lum bir vazifani bajarishga mo'ljallangan kodlar yig'indisi.
Biz shu vaqtgacha ko'rib o'tgan funksiyalar: print(), len(), sum(), max(), min()...

Nega funksiya kerak?
    ✔ Kodni takrorlamaslik
    ✔ Kodni tushunarli qilish
    ✔ Katta loyihani bo'laklash
    ✔ Xatolarni oson topish
    ✔ Professional dasturchilik asosi

    ❌ Funksiyasiz kod — tartibsiz va chalkash bo'ladi"""

"""
print() - funksiya - ma'lum bir ish bajaruvchi kodlar
.title() - method - usul
"""

"""
print()
min()
max()
sum()
len()
input()
range()
type()


str()
int()
float()
list()
dict()
"""


def salom_ber(ism:str): # parametr
    """ Bu funksiya salom berish vazifasini bajaradi ! """ #  docstring ->   
    
    return f"Assalomu aleykum {ism.title()} !"

# print(salom_ber("Saida"))
# print(salom_ber("abrorbek"))
# print(salom_ber(input("Ism kiriting: ")))



""" 1) Foydalanuvchi ismi va yoshini olib, uning tug'ilgan yilini hisoblaydigan funksiya yozing. """

def tyil(ism:str, yosh:int):
    """ Foydalanuvchi ismi va yoshini paramert sifatida olib, uning tug'ilgan yilini topib beradigan funksiya  """

    return f"{ism} {2026-yosh}-yili tug'ilgan"


# print(tyil("Saida", 13))
# print(tyil("Bobur", 67))
# print(tyil(input("Ism: "), int(input("yosh: "))))



"""
2) Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
3) Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
"""


"""2-Mashq"""
def kvadrat_va_kub(son:int):
    return f"Kvadrati {son**2} Kubi {son**3}"

# print(kvadrat_va_kub(5))


"""3-Mashq"""
def juft_yoki_toq(son:int):
    if son%2 == 0:
        return "Son juft"
    else:
        return "Son toq"
    
# print(juft_yoki_toq(5))
# print(juft_yoki_toq(2))

"""
4) Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. 
    Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
"""

def katta_kichik(son1:int, son2:int):
    """ Ikki sondan kattasini ko'rsatib beradi """

    if son1 > son2:
        return f"{son1} katta"
    elif son1 < son2:
        return f"{son2} katta"
    elif son1 == son2:
        return f"{son1}={son2}"

# print(katta_kichik(5, 8))
# print(katta_kichik(59, 33))
# print(katta_kichik(5, 5))


"""   
5) Tog'ri to'rtburchakli uchburchakning katetlarini qabul qilib olib uning gipotenuzsini hisoblovchi funksiya 
    yozing, 2- katetni o'zgarmas parameter sifatida bering.
    f: c**2 = a**2 + b**2 / c ni topish kk
    Yuqoridagi har bir funksiyaga to'liq tarif(defenition yozing)
"""


"""
7) Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
"""

def katta_kichik2(son1:int, son2:int, son3:int):
    """ Ikki sondan kattasini ko'rsatib beradi """

    if son1 >= son2 and son1 >= son3:
        return f"{son1} katta"
    elif son1 <= son2 and son3 <= son2:
        return f"{son2} katta"
    elif son1 <= son3 and son2 <= son3:
        return f"{son3} katta"
    elif son1 == son2 and son1 == son3:
        return f"{son1}={son2}={son3}"

# print(katta_kichik2(5, 8 ,4))
# print(katta_kichik2(59, 33, 4))
# print(katta_kichik2(5, 5, 7))
# print(katta_kichik2(0, 1, 1))


"""
10) Parametr sifatida uzatilgan matnning  uzunligini topuvchi funksiya tuzing.
"""
def len2(matn:str):
    
    return 
    
print(("adsa asdas"))
