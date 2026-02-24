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
    uzunlik = 0
    
    for m in matn:
        if m != " ":
            uzunlik = uzunlik + 1
        
    return uzunlik 
    
# print(len2("Bugun kun juda quyoshli bo'lyapdi"))
# print(len2("Muhammadqodir"))


"""
11) parametr sifatida uzatilgan sonlar ichidan faqat toq sonlarni ajratib qaytaradigan funksiya yozing.
"""
"""
[2, 5, 6, 9, 94] - list
(2, 5, 6, 9, 94) - tuple
{2, 5, 6, 9, 94} - set
"""

def toq(*sonlar:int): #  *args - arguments
    toqlar = []

    for son in sonlar:
        if son%2 != 0:
            toqlar.append(son)
            
    return toqlar

# print(toq(3))
# print(toq(3, 5, 10))
# print(toq(7, 133, 4, 6))


"""  
sum() funksiyasini qo'lda yasash. Haqiqiy sum() ni ishlatmasdan ❗
"""
def our_sum(*sonlar:int):
    """Bu kiritlgan sonlarning yig'indisini aniqlovchi dastur"""
    jami = 0  
    
    for son in sonlar:
        jami = jami + son  
        
    return jami

# print(our_sum(2,2, 6,8))
# print(our_sum(-45, 50))


"""
12) Parametr sifatida uzatilgan sonlarning o'rta arifmetigini topib beruvchi funksiya tuzing.
"""
def middle(*sonlar:int):
    """Bu kiritlgan sonlarning yig'indisini aniqlovchi dastur"""
    jami = 0  
    soni = 0
    
    for son in sonlar:
        jami += son
        soni = soni + 1  
        
    return jami/soni

# print(middle(2,2, 6,8))
# print(middle(-45, 50))


"""
13) 1 dan N gacha bo'lgan sonlar yig'indisini topuvchi funksiya tuzing.
"""

def yigindi(son:int):
    """  """
    sonlar = list(range(1, son))
    
    summa = 0  
    for son in sonlar:
        summa += son  
        
    return summa

# print(yigindi(4))
# print(yigindi(10))


"""
15) Parametr sifatida uzatilgan songacha(0 dan boshlab) bo'lgan juft sonli ro'yhat tuzadigan funksiya yozing.
"""
def juft(son:int):
    juftlar = list(range(0, son, 2))

    return juftlar
    
# print(juft(90))
# print(juft(55))


"""
Tasodifiy son o'yinini funksiyaga aylantiring.
"""

from random import randrange, choice, choices
def game():
 
    komputer = randrange(1, 5) # 1 dan 5 gacha ixtiyoriy biro sonni tanlab beradi
    print("Komputer tanlagan sonni taxmin qiling !")
    player = int(input("Biror sonni kiriting: "))

    if komputer == player:
        print("Siz yutdingiz ✅")
    else:
        print("Siz yutqazdiz ❌👎")
    
    return f"Komputer {komputer} sonini  o'ylagan edi"

# print(game())



"""
*16) Parametr sifatida uzatilgan harfni unli yoki undoshga ajratib beradigan funksiya yozing.
    unli --> e u i o a o'
"""

# def unli(harf:str):
#     if harf == "a" or harf == "o'" or harf == "o" or harf == "e" or harf == "u" or harf == "i": 
#         return f"{harf} unli"
#     else:
#         return f"{harf} undosh"

def unli(harf:str):
    unlilar = ['a', 'o', 'u', 'i', 'e', "o'"]
    ikkitalik = ['ng', 'sh', 'ch', "o'", "g'"]
    
    if len(harf) == 1 or harf in ikkitalik:
        if harf in unlilar:
            return f"{harf} unli"
        else:
            return f"{harf} undosh"
    else:
        return "Siz harf kiritmadingiz !"

# print(unli("a"))
# print(unli("b"))
# print(unli("ng"))
# print(unli("o'"))
# print(unli("oo"))
# print(unli("sh"))
# print(unli("ertaki"))


"""
17*) Foydalanuvchi funksiyaga parametr sifatida o'zi yasagan parolni uzatsin. 
    Siz uni tekshirib parolning kuchli yoki kuchsiz ekanini tekshirib bering. 
    Kuchli parolning xususiyatlari:
        eng kamida 8 ta belgidan ibotar bo'lishi;

"""

def password_chacker(password:str):
    """ Parolni tekshiruvchi funksiya """

    if len(password) >=8:
        return "Bu kuchli parol ✅"
    else:
        return "Bu kuchsiz parol ❌"
        
        

# print(password_chacker("dlsl23sas"))
# print(password_chacker("dlsl2"))        


"""
*20) max() funksiyasini o'zingiz tuzishga urinib ko'ring. max() ni ishlatmasdan ❗
*21) min() funksiyasini o'zingiz tuzishga urinib ko'ring. min() ni ishlatmasdan ❗
"""

"""max"""
def our_max(*sonlar:int):
    return sorted(sonlar)[-1]

# print(our_max(3,3,4,5,6,67,5,3,3))
# print(our_max(3,3,4,5,6,3,13))


"""min"""
def our_min(*sonlar:int):
    return sorted(sonlar)[0]

# print(our_min(3,3,4,5,-6,-67,-5,3,3))


# sonlar = list(range(5, 100))
# print(sonlar)



""" our range() """
def my_range(son1:int, son2:int):
    royhat = [son1,]
    
    for s in  royhat:
        if s < son2-1:
            royhat.append(s+1)
    
    return royhat 

# print(my_range(1, 100))
# print(my_range(50, 90))



""" Standar qiymat uzatish """
"""
    Funksiya yaratishda, standart qiymatga ega parametrlar doim oxirida yozilishi kerak. 
    Aks holda xatolik yuzaga keladi.
"""     
def full_name(ism, familya="Aliyev"):
    return f"Sizning ismingiz {ism} {familya}"
    
# print(full_name("Olim"))
# print(full_name("Asadbek","Mirzanvarov"))



""" our range() """
def my_range(son1:int, son2:int):
    royhat = [son1,]
    
    for s in  royhat:
        if s < son2-1:
            royhat.append(s+1)
    
    return royhat 

# print(my_range(1, 100))
# print(my_range(50, 90))




def my_range(son1=1, son2=int, son3=1):
    royhat = [son1,]


    for s in royhat:
        if s < son2-1:
            royhat.append(s+son3)

    return royhat

# print(my_range(1,100,2))
# print(my_range(50,90))


