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


""" Funksiya yasash """
def salom():
    """ Ushbu funksiyaning vazifasi Salomlashish """
    
    return "Assalom aleykum"
# print(salom())



""" DOCSTRING """
""" 
    DOCSTRING ---> Defenition
    Docstringni konsolga chiqarish uchun print(funksiya_nomi.__doc__) deb ham yozishimiz mumkin: 
"""

# print(len.__doc__)
# print(print.__doc__)


def salom_ber(ism:str): # parametr
    """ Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya. ism -> Matn kiritish kerak """
    return f"Assalomu alaykum, hurmatli {ism}!"
    
# print(salom_ber("Ali"))
# print(salom_ber("Vali"))
# print(salom_ber('Umar'))


"""
    Funksiyaga nom berishda fe'l, ya'ni harakatni bildiruvchi so'zlar yoki jumlalardan foydalaning. 
    Bu bilan siz o'zgaruvchi va funksiya o'rtasini farqlashingiz oson bo'ladi. 
    Misol uchun, yuqorida biz funksiyamizni salom emas salom_ber deb nomladik.
"""

""" Funksiyaga qiymat uzatish """
def hisobla(tyil:int, yil:int):
    """
    Foydalanuvchi yoshini hisoblovchi funksiya. 
    tyil - Tug'ilgan yilingizni kiriting
    yil- hozirgi yil
    """
    yosh = yil - tyil
    
    return f"Siz {yosh} da ekansiz"
    
# print(hisobla(1985, 2026))
# print(hisobla(2001, 2026))


""" Argumentni kalit so'z bilan uzatish """
def plus(son1, son2):
    """ Foydalanuvchi kiritgan sonlarni bir biriga qo'shib beradi. """
    son3 = son1 + son2
    
    return f"Siz kiritgan {son1} va {son2} larning yig'indisi {son3} ga teng."
# plus(son2=5, son1=5)


def full_name(name, surname, father):
    """
    full_name - To'liq ism sharifni qaytarish uchun funksiya
    
    Arguments:
        name - str
        suename - str
        father - str 
    """
    
    return f"{surname} {name} {father}"

# full_name(name="Olimjon", surname="Aliyev", father="Baxodirovich")


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
    elif son1 == son2:
        return f"{son1} = {son2}"

# print(katta_kichik(15, 8))
# print(katta_kichik(23, 55))
# print(katta_kichik(4, 4))


""" 6-mashq """

def info(ism:str, familiya:str, tyil:int, tjoy:str, email:str, phone:int):
    """ """

    m = {
        'ism':ism,
        'familiya':familiya,
        'tyil':tyil,
        'tjoy':tjoy,
        'email':email,
        'phone':phone,
    }
    return m

# print(info("Ali", "Sobirov", 2011, "Mingbuloq", "qwer@gmail.com", 977776655))


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
    return f"Shu aylananing radiusi: {r}, diametri: {2 * r}, perimetri: {2 * 3.14 * r}, yuzi: {3.14 * r ** 2} "
    
# print(aylananing_radiusi(3))

"""" 9-mashq """
def togri_tortburchak(eni:int,boyi:int):
    """ """
    return f"Shu tugri tortburchakning perimetri {2*(eni+boyi)} yuzi esa {eni*boyi}"
    

# print(togri_tortburchak(2,3)) 
# print(togri_tortburchak(4,3))


""" *args - arguments """

def our_sum(*sonlar:int):
    summa = 0
    for son in sonlar:
        summa += son
    
    return summa


# print(our_sum(2, 5,6))
# print(our_sum(40, 20, 5, 15 ,20))



"""  10) Parametr sifatida uzatilgan matnning  uzunligini topuvchi funksiya tuzing."""

def our_len(matn:str):
    length = 0
    
    for m in matn:
        if m != " ":
            length += 1
    
    return length

# print(our_len("Salom hammaga"))
# print(our_len("Mirziyo"))



"""    
11) parametr sifatida uzatilgan sonlar ichidan faqat toq sonlarni ajratib qaytaradigan funksiya yozing.
 """


def toq(*sonlar:int):
    toqlar = []
    for son in sonlar:
        if son%2 != 0:
            toqlar.append(son)
            
    return toqlar


# print(toq(4, 8, 9,2, 3, 5, 7, 6))










