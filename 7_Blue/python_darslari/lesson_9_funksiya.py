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


def t_yil_hisoblovchi(ism:str, yosh:int): # parametr
    """  """
    return f"{ism.title()} {2026-yosh}-yili tug'ilgan"


# print(t_yil_hisoblovchi("Anvar", 26))
# print(t_yil_hisoblovchi("Salima", 64))



""" Argumentni kalit so'z bilan uzatish """

def full_name(name, surname, father):
    """
    full_name - To'liq ism sharifni qaytarish uchun funksiya
    
    Arguments:
        name - str
        suename - str
        father - str 
    """
    
    return f"{surname} {name} {father} o'g'li/qizi"

# full_name(name="Olimjon", surname="Aliyev", father="Baxodirovich")
# print(full_name("Nodirbek", "Saidbekov", "Javohir"))
# print(full_name(surname="Saidbekov", father="Javohir", name="Nodirbek"))


"""
2) Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
3) Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
4) Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. 
    Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
"""

""" 2 """

def kv(son:int):
    """  """
    kv = son**2
    kub = son**3
    
    return f"{son} ning kvadrati {kv}, kubi {kub}"

# print(kv(5))
# print(kv(9))


""" 3 """
def juft_toq(son:int):
    """  """
    
    if son%2 == 0:
        return f"{son} juft"
    else:
        return f"{son} toq"

# print(juft_toq(4))
# print(juft_toq(5))

""" 4 """

def katta_kichik(son1:int, son2:int):
    """  """

    if son1 > son2:
        return f"{son1} > {son2}"
    elif son1 < son2:
        return f"{son1} < {son2}"
    if son1 == son2:
        return f"{son1} = {son2}"

# print(katta_kichik(15, 8))
# print(katta_kichik(23, 55))
# print(katta_kichik(4, 4))


"""
  
5) Tog'ri to'rtburchakli uchburchakning katetlarini qabul qilib olib uning gipotenuzsini hisoblovchi funksiya 
    yozing, 2- katetni o'zgarmas parameter sifatida bering.
    f: c**2 = a**2 + b**2 / c ni topish kk / b - o'zgarmas qiymat   
    Yuqoridagi har bir funksiyaga to'liq tarif(defenition yozing)


6) Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va 
    telefon raqamini qabul qilib, lug'at ko'rinishida malumot qaytaruvchi funksiya yozing. 
    Lug'atda foydalanuvchi yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy 
    qiling (masalan, tel.raqam, el.manzil)

7) Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing

8) Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, 
    perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing

"""

from math import sqrt, pi
def tbu(a:float, b:float):
    """  """
    c = sqrt(a**2 + b**2)
    
    return c

""" Uyga vazifa """

""" 7-mashq """
def eng_katta(son1:int,son2:int,son3:int):
    """ """
    if son1 > son2 and son1 > son3 :
        return f"{son1} eng kattasi"
    elif son2 > son1 and son2 > son3 :
        return f"{son2} eng kattasi"
    elif son3 > son2 and son3 > son1 :
        return f"{son3} eng kattasi"
    elif son1 == son2 == son3:
        return "Hamma son teng"
    
# print(eng_katta(11,11,11))
# print(eng_katta(12,11,10))
# print(eng_katta(11,13,12))
# print(eng_katta(11,11,14))

""" 8-mashq """
def aylananing_radiusi(r):
    """ """
    return f"Shu aylananing radiusi: {r}, diametri: {2 * r}, perimetri: {2 * pi * r}, yuzi: {3.14 * r ** 2} "
    
# print(aylananing_radiusi(3))

"""" 9-mashq """
def togri_tortburchak(eni:int,boyi:int):
    """ """
    return f"Shu tugri tortburchakning perimetri {2*(eni+boyi)} yuzi esa {eni*boyi}"
    

# print(togri_tortburchak(2,3)) 
# print(togri_tortburchak(4,3))


"""
10) Parametr sifatida uzatilgan matnning  uzunligini topuvchi funksiya tuzing.L
"""
def my_len(matn:str):
    """  """
    harflar_soni = 0
    for m in matn:
        if m != ' ':
            harflar_soni += 1
    
    return harflar_soni

# print(my_len("Salom 7 blue. Bugun Chorshanba")) 



""" *args - istalgancha son uzatish usuli """
def my_sum(*sonlar:int):
    """ Berilgan barcha sonlarning yig'indisini hisoblaydi. """
    yigindi = 0
    for son in sonlar:
        yigindi += son

    return yigindi
    
# print(my_sum(2, 5))
# print(my_sum(2))
# print(my_sum())
# print(my_sum(6, 9, 0, -5, 34))


"""
11) parametr sifatida uzatilgan sonlar ichidan faqat toq sonlarni ajratib qaytaradigan funksiya yozing.
"""

def toq_sonlar(*sonlar:int):
    """  """
    toq = []
    for son in sonlar:
        if son%2 != 0:
            toq.append(son)
    toq.sort()
    return toq

# print(toq_sonlar(3, 4, 5, 7, 8, 2, 1))

"""
12) Parametr sifatida uzatilgan sonlarning o'rta arifmetigini topib beruvchi funksiya tuzing.
14) Tasodifiy son o'yinini funksiyaga aylantiring.
"""