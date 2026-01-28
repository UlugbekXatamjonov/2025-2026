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

print(salom_ber("Saida"))
print(salom_ber("abrorbek"))
print(salom_ber(input("Ism kiriting: ")))









