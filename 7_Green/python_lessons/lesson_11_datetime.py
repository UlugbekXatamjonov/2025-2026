"""
Thame: Pythonda Kutubxonalar: datetime, math, RegEx

Kutubxona — bu tayyor yozilgan foydali kodlar to'plami.
"""
from datetime import date, time, datetime, timedelta


""" date """
bugun = date.today()
# print(bugun)
# print(bugun.year)
# print(bugun.month)
# print(bugun.day)

# yil = int(input("Yil: "))
# oy = int(input("Oy: "))
# kun = int(input("Kun: "))

# sana  = date(yil, oy, kun)
# print(sana)
# print(type(sana))

""" datetime """
hozir = datetime.now()
# print(hozir)
# print(hozir.year)
# print(hozir.hour)
# print(hozir.minute)
# print(hozir.microsecond)

# sana2 = datetime(2023, 6, 9)
# print(sana2)

# sana3 = datetime(2023, 6, 9, 23, 45)
# print(sana3)


"""
2-mashq.
Bu yilgi Ramazon oyi 20-mart kuni tugaydi. Bugungi sanadan foydalanib,
Ramazon oyining necha kundan keyin tugashini hisoblab beradigan dastur tuzing.
Namuna: Ramazon 5 kundan keyin tugaydi.
"""
# ramazon = date(2026, 3, 20)
# print(ramazon)

# print(f"Ramazon {(ramazon-bugun).days} kundan keyin tugaydi.")


"""
1-mashq.
Foydalanuvchidan biror sana so'rang. Agar kiritilgan sana o'tib ketgan bo'lsa —
“Bu o'tib ketgan sana”,
agar hali kelmagan bo'lsa — “Bu sana endi keladi”,
agar bugungi sana bo'lsa — “Siz bugungi sanani kiritdingiz” degan xabar konsolga chiqsin.
"""


yil = int(input("Yil: "))
oy = int(input("Oy: "))
kun = int(input("Kun: "))

sana1  = date(yil, oy, kun)

if bugun > sana1:
    print("O'tib ketgan sana")
elif bugun < sana1:
    print("Endi keladigan sana")
elif bugun == sana1:
    print("Siz bugungi sanani kiritdingiz")

