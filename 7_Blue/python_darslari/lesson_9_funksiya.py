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
"""
def middle(*sonlar:int):
    """  """
    number = 0
    summa = 0
    
    for son in sonlar:
        number += 1
        summa += son
        
    return summa / number

# print(middle(3, 7, 0, 8))
# print(middle(-4, 8, 12, 9))


"""
14) Tasodifiy son o'yinini funksiyaga aylantiring.
"""
"""14"""

from random import randrange
def taxmin_oyini():
    """ """
    player_score = 0
    computer_score = 0
    
    while True:
        son = randrange(1, 6)
        taxmin = input("1 dan 5 gacha sonni taxmin qiling: ")

        if taxmin == 'stop':
            print("Game end !")
            print(f"Player {player_score}:{computer_score} Komputer")
            break
        
        if taxmin.isdigit():
            taxmin = int(taxmin)
            
            if taxmin == son:
                player_score += 1
                print(f"To‘g‘ri! Kompyuter ham shu sonni o‘ylagan. \n Player {player_score}:{computer_score} Komputer")
            else:
                computer_score += 1
                print(f"Noto‘g‘ri. Kompyuter {son} sonini o‘ylagan edi.\n Player {player_score}:{computer_score} Komputer")
                
# print(taxmin_oyini())



"""
13) Foydalanuvchi funksiyaga parametr sifatida o'zi yasagan parolni uzatsin. 
    Siz uni tekshirib parolning kuchli yoki kuchsiz ekanini tekshirib bering. 
    Kuchli parolning xususiyatlari:
        eng kamida 8 ta belgidan ibotar bo'lishi;
        katta va kichik harflar bo'lishi;
        biror belgi qatnashishi;
"""

def password_checker(password:str):
    """  """
    
    big = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
    small = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    sign = ["!","@","#","$","%","&",")","-","=","+","<",">","?","|","'",":",";"]
    number = "1234567890"

    katta = False
    kichik = False
    belgi = False
    is_number = False
    

    for p in password:
        if p in big:
            katta = True
        
        if p in small:
            kichik = True
            
        if p in sign:
            belgi = True
            
        if p in number:
            is_number = True
            
    if len(password) >= 4 and katta == True and kichik == True and belgi == True and is_number==True:
        return f"Bu parol kuchli ✅"
    else:
        return f"Bu parol kuchsiz ❗ Qaytadan urining "

# print(password_checker("QWer@$12"))
# print(password_checker("QWee12"))
# print(password_checker("QW#$12"))
# print(password_checker("er#$21"))
# print(password_checker("er#$WE"))


""" pass operatori """
"""
pass - operatori malum vaqt funksiyani ishlatmaslik kerak bo'lganda kerak bo'ladi
# """
# def name(ism):
#     pass
    
# print(name("Abbos"))

# def name(ism):
#     pass


""" 
15) 1 dan N gacha bo'lgan sonlar yig'indisini topuvchi funksiya tuzing.
"""

def yigindi(son:int):
    """  """
    if son >= 1:
        sonlar = list(range(1, son+1))
        summa = 0
        
        for son in sonlar:
            summa += son
            
        return summa
    else:
        return 0    

# print(yigindi(10))
# print(yigindi(100))
    

def yigindi2(son:int):
    """  """
    
    if son >= 1:
        return son * (son+1) // 2 #     (n * (n+1)) / 2
    else:
        return 0

# print(yigindi2(10))
# print(yigindi2(100))
    


""" Tub sonlar """
# def tub(son1:int, son2:int):
#     """  """
#     tub_sonlar  = []
#     sonlar = list(range(son1, son2))
    
#     for son in sonlar:
#         if son%2 != 0 and son%3 != 0 and son%4 != 0 and son%5 != 0 and son%6 != 0 and son%7 != 0 and son%8 != 0: 
#             tub_sonlar.append(son)
    
#     return tub_sonlar



# print(tub(10, 50))
# print(tub(10, 123))


def tub(son1:int, son2:int):
    """  """
    tub_sonlar  = []
    sonlar = list(range(son1, son2))
    
    for son in sonlar:
        is_tub = True
        
        for s in range(2, son):
            if son%s == 0:
                is_tub = False
        
        if is_tub == True:
            tub_sonlar.append(son)
    
    
    return tub_sonlar

# print(tub(10, 50))
# print(tub(10, 123))
# print(tub(10, 1000))



def our_max(*sonlar:int):
    """ Berilgan sonlar ichidan eng sini kattasini qaytaradi """
    return sorted(sonlar)[-1]

# print(our_max(-9, 0, 5666, 9999999, -23, 111))



def our_min(*sonlar:int):
    """ Berilgan sonlar ichidan eng kichigini qaytaradi """
    return sorted(sonlar)[0]
# print(our_min(-9, 0, -5666, 9999999, -23, 111))


def our_range(a:int, b:int, c=1): # standart qimat
    """ Sonli oraliq hosil qilib beradi """
    sonlar = [a]
    
    while True:
        if a < b-c:
            a += c
            sonlar.append(a)
        else:
            break  
    return sonlar
    
    
print(our_range(1, 10, 1))
print(our_range(0, 100, 5))
print(our_range(30, 60))