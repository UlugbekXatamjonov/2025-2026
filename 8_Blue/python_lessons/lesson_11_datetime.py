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
from datetime import datetime, date, timedelta
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


# oy = int(input("Oy: "))
# kun = int(input("Kun: "))
# sana = date(bugun.year, oy, kun)

# if bugun < sana:
#     print(f"Sizning keyingi tug'ilgan kuningizga {(sana-bugun).days} kun qoldi")
# elif bugun == sana:
#     print(f"Tug'ilgan kuningiz bilan !")
# else:
#     sana = date(bugun.year+1, oy, kun)
#     print(f"Sizning keyingi tug'ilgan kuningizga {(sana-bugun).days} kun qoldi")
    

"""
17-mashq.
Foydalanuvchining tug'ilgan sanasi (faqat kun va oy) ni so'rab oling va
uning so'nggi nishonlagan tug'ilgan kuni nechta kun avval o'tib ketganini hisoblab bering.
"""
# oy = int(input("Oy: "))
# kun = int(input("Kun: "))
# sana = date(bugun.year, oy, kun)

# if bugun < sana:
#     sana = date(bugun.year-1, oy, kun)
#     print(f"Sizning eng oxirgi  tug'ilgan kuningiz {(bugun-sana).days} kun oldin bo'lgan")
# elif bugun == sana:
#     print(f"Tug'ilgan kuningiz bilan !")
# else:
#     print(f"Sizning eng oxirgi  tug'ilgan kuningiz {(bugun-sana).days} kun oldin bo'lgan")
    

"""  timedelta"""
# print(bugun - timedelta(weeks=2))
# print(hozir + timedelta(hours=66))


"""
14-mashq.
2010-03-10 sanasidan 8 hafta, 325 soat va 854 minutni ayring va
hosil bo'lgan sana va vaqtni konsolga chiqaring.
"""
# sana14 = date(2010, 3, 10)
# print(sana14 - timedelta(weeks=8, hours=325, minutes=854))


"""
15-mashq.
Foydalanuvchidan uning maktabga birinchi marta borgan sanasini so'rang va
o'sha kundan bugungi kungacha qancha vaqt o'tganini hisoblab, konsolga chiqaring.

16-mashq.
Foydalanuvchidan istalgan soat miqdorini so'rang, uni hozirgi vaqtga qo'shing va
hosil bo'lgan yangi vaqtni konsolga chiqaring.
Namuna: 283 soatdan keyin vaqt 21:45 bo'ladi.
"""
""" 16-mashq """
hozir = datetime.now()

soat = int(input("Biror soatning kiring: "))
yangi_vaqt = hozir + timedelta(hours=soat)
print(f"{soat} soatdan keyin vaqt {yangi_vaqt.strftime("%H:%M")} bo'ladi.")


