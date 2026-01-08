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


def welcome(): # docstring - tarif
    """ Ushbu funksiya chaqirilganda sizga salom beradi !  
    Bu bizning birinchi sodda funksiyamiz
    """
    return "Assalomu aleykum !"


# print(welcome())


def salom_ber(ism:str): # ism = "saida"
    """  """
    return f"Assalomu aleykum {ism}"

# print(salom_ber("Imron"))
# print(salom_ber("Saida"))
# print(salom_ber("Olim"))


def yigindi(x:int, y:int):
    """ Ikki soning yig'indisin hisoblab qaytaradi  
    x - birinchi son
    y - ikkinchi son
    """

    javob = f"{x} + {y} ning yig'indis {x+y}"

    return javob

# print(yigindi(4,5))
# print(yigindi(45,2))

# son1 = int(input("1-: "))
# son2 = int(input("2-: "))
# print(yigindi(son1, son2))


"""
1) Foydalanuvchi ismi va yoshini parametr sifatida olib, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
"""
"""
2) Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
"""


def t_yil_hisoblovchi(ism:str, yosh:int):
    """  """

    return f"{ism.title()} {2026-yosh}-yili tug'ilgan"


# print(t_yil_hisoblovchi("Anvar", 26))
# print(t_yil_hisoblovchi("Salima", 64))





