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

# print(hozir.year) # yilni ajratib olish
# print(hozir.month) # oyni ajratib olish
# print(hozir.day) # kunni ajratib olish
# print(hozir.hour) # soatni ajratib olish
# print(hozir.minute) # minutni ajratib olish
# print(hozir.second) # sekundni ajratib olish
# print(hozir.microsecond) # microsekundni ajratib olish

# print(f"Hozir soat: {hozir.time()}")
# print(f"Hozir soat: {hozir.hour}:{hozir.minute}")


""" Sana va vaqt yasash """
# sana_vaqt = datetime(2023, 9, 3, 4)
# print(sana_vaqt)

# sana = date(4, 12, 29)
# print(sana)

# vaqt = time(8, 30, 56)
# print(vaqt)


""" sanadan sanani ayrish """
hozir = datetime.now()
bugun = date.today()
t_kun = date(2012, 11, 19)

# print((bugun - t_kun).days)


"""
2-mashq.
Bu yilgi Ramazon oyi 29-mart kuni tugagan. Bugungi sanadan foydalanib,
Ramazon oyining necha kun avval tugaganini hisoblab beradigan dastur tuzing.
Namuna: Ramazon 5 kun avval tugadi.
"""
# ramazon = date(2025, 3, 29)
# print(f"Ramazon {(bugun-ramazon).days} kun avval tugagan")

# ramazon1 = date(2026, 2, 18)
# print(f"Ramazon {(ramazon1-bugun).days} kundan keyin keladi.")


"""
3-mashq.
Bugungi sanadan foydalanuvchi kiritgan sanagacha bo'lgan kunlar sonini hisoblab chiqaring.
Bunda kiritilgan sana bugungi sanadan kichik bo'lmasligi kerak.
"""

yil = int(input("Yil: "))
oy = int(input("Oy: "))
kun = int(input("Kun: "))
sana = date(yil, oy, kun)

if sana > bugun:
    print(f"{(sana-bugun).days}")
else:
    print("Siz eski sana kiritdingiz !")


"""
1-mashq.
Foydalanuvchidan biror sana so'rang. Agar kiritilgan sana o'tib ketgan bo'lsa —
“Bu o'tib ketgan sana”,
agar hali kelmagan bo'lsa — “Bu sana endi keladi”,
agar bugungi sana bo'lsa — “Siz bugungi sanani kiritdingiz” degan xabar konsolga chiqsin.
"""


yil1 = int(input("Yil: "))
oy1 = int(input("Oy: "))
kun1 = int(input("Kun: "))
sana1 = date(yil1, oy1, kun1)

if sana1 > bugun:
    print(f"Bu sana endi keladi")
elif sana1 < bugun:
    print(f"Bu o'tib ketgan sana")
else:
    print("Siz bugungi sanani kiritdingiz")

"""
4-mashq.
Keyingi o'quv yili 2-sentyabr sanasida boshlanadi.
Bugungi sanadan boshlab, o'sha kungacha necha kun qolganini hisoblab beradigan dastur tuzing.

5-mashq.
Bu yilgi o'quv yili 2025-yil 4-sentyabr sanasida boshlangan bo'lsa,
bugungi kungacha maktab boshlanganiga necha kun bo'lganini aniqlang.
Namuna: Maktab boshlanganiga 153 kun bo'ldi.
"""
