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