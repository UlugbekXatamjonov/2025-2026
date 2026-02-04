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


""" 12) Parametr sifatida uzatilgan sonlarning o'rta arifmetigini topib beruvchi funksiya tuzing. """

def middle(*sonlar:int):
    summa = 0
    length = 0
    for son in sonlar:
        summa += son
        length += 1
        
    return summa/length

# print(middle(2, 5,6))
# print(middle(40, 20, 5, 15 ,20))



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
# print(password_checker("2802010Mm$"))




""" Tub sonlar """
def tub(son1:int, son2:int):
    """  """
    tub_sonlar  = []
    sonlar = list(range(son1, son2))
    
    for son in sonlar:
        if son%2 != 0 and son%3 != 0 and son%4 != 0 and son%5 != 0 and son%6 != 0 and son%7 != 0 and son%8 != 0: 
            tub_sonlar.append(son)
    
    return tub_sonlar



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


# [] - list
# () - tuple
# {} - set
def our_max(*sonlar:int):
    """ Berilgan sonlar ichidan eng sini kattasini qaytaradi """
    
    return sorted(sonlar)[-1]

# print(our_max(-9, 0, 5666, 9999999, -23, 111))
# print(our_max(-9, 0, 5666, 99, 777777, 88, 444, 99999, -23, 111))


def our_min(*sonlar:int):
    """ Berilgan sonlar ichidan eng kichigini qaytaradi """
    return sorted(sonlar)[0]
# print(our_min(-9, 0, -5666,  -23, 111))


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
    
    
# print(our_range(1, 10, 2))
# print(our_range(0, 100))
# print(our_range(30, 60))


