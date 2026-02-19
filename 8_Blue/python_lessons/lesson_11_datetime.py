"""
Thame: Pythonda Kutubxonalar: datetime, math, RegEx

Kutubxona — bu tayyor yozilgan foydali kodlar to'plami.
"""

""" Datetime - Vaqt moduli 

Datetime nima?
Datetime — sana va vaqt bilan ishlash uchun modul.

Qayerda kerak?
Tug'ilgan kun
Dars jadvali
Vaqt hisoblash
Qancha kun o'tdi?
"""
from datetime import datetime, date, time

""" datetime """
hozir = datetime.now()
# print(hozir)
# print(hozir.date()) # sanani ajratib olish
# print(hozir.time()) # vaqtni ajratib olish

# print(type(hozir))

# print(hozir.year) # yilni ajratib olish
# print(hozir.month) # oyni ajratib olish
# print(hozir.day) # kunni ajratib olish
# print(hozir.hour) # soatni ajratib olish
# print(hozir.minute) # minutni ajratib olish
# print(hozir.second) # sekundni ajratib olish
# print(hozir.microsecond) # microsekundni ajratib olish

# print(f"Hozir soat: {hozir.time()}")
# print(f"Hozir soat: {hozir.hour}:{hozir.minute}")

# sana = date(2028, 2, 6)
# print(sana)
# print(type(sana))

# yil = int(input("Yil: "))
# oy = int(input("Oy: "))
# kun = int(input("Kun: "))

# sana = date(yil, oy, kun)
# print(sana)

# vaqt = datetime(2002, 6, 3)
# print(vaqt)
# print(type(vaqt))


""" sanadan sanani ayrish """
bugun = date.today() 
# tkun = date(2012, 2, 19)
# print((bugun-tkun).days)


"""
1-mashq.
Foydalanuvchidan biror sana so'rang. Agar kiritilgan sana o'tib ketgan bo'lsa —
“Bu o'tib ketgan sana”,
agar hali kelmagan bo'lsa — “Bu sana endi keladi”,
agar bugungi sana bo'lsa — “Siz bugungi sanani kiritdingiz” degan xabar konsolga chiqsin.
"""

# yil = int(input("Yil: "))
# oy = int(input("Oy: "))
# kun = int(input("Kun: "))

# sana = date(yil, oy, kun)
# print(sana)

# if sana == bugun:
#     print("Siz bugungi sanani kiritdingiz")
# elif sana < bugun:
#     print("Bu o'tib ketgan sana")
# elif sana > bugun:
#     print("Bu sana endi keladi")


"""
O'tgan yilgi Ramazon oyi 29-mart kuni tugagan. Bugungi sanadan foydalanib,
Ramazon oyining necha kun avval tugaganini hisoblab beradigan dastur tuzing.
Namuna: Ramazon 5 kun avval tugadi.
"""
# ramazon = date(2025, 3, 29)
# print(f"Ramazon {(bugun-ramazon).days} kun avval o'tib ketgan")

"""
13-mashq.
Foydalanuvchidan uning tug'ilgan sanasini so'rang va
keyingi tug'ilgan kuniga necha kun qolganini aniqlang.
Namuna: Sizning keyingi tug'ilgan kuningiz 234 kundan keyin keladi.
"""


oy = int(input("Oy: "))
kun = int(input("Kun: "))
sana = date(bugun.year, oy, kun)

if bugun < sana:
    print(f"Sizning keyingi tug'ilgan kuningizga {(sana-bugun).days} kun qoldi")
elif bugun == sana:
    print(f"Tug'ilgan kuningiz bilan !")
else:
    sana = date(bugun.year+1, oy, kun)
    print(f"Sizning keyingi tug'ilgan kuningizga {(sana-bugun).days} kun qoldi")
    

"""
17-mashq.
Foydalanuvchining tug'ilgan sanasi (faqat kun va oy) ni so'rab oling va
uning so'nggi nishonlagan tug'ilgan kuni nechta kun avval o'tib ketganini hisoblab bering.
"""






