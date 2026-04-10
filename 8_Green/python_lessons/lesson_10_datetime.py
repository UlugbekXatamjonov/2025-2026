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

# print(hozir.year) # yilni ajratib olish
# print(hozir.month) # oyni ajratib olish
# print(hozir.day) # kunni ajratib olish
# print(hozir.hour) # soatni ajratib olish
# print(hozir.minute) # minutni ajratib olish
# print(hozir.second) # sekundni ajratib olish
# print(hozir.microsecond) # microsekundni ajratib olish

# print(f"Hozir soat: {hozir.time()}")
# print(f"Hozir soat: {hozir.hour}:{hozir.minute}")

""" Sana yasash """
# yil = int(input("Yil: "))
# oy = int(input("Oy: "))
# kun = int(input("Kun: "))

# sana1 = date(yil,oy, kun)
# print(sana1)

# vaqt1 = datetime(2023, 8, 6, 21, 30)
# print(vaqt1)

# """ Sanadan sanani ayrish """
bugun = date.today()
# print(bugun- sana1)


""" 
2-mashq.
Bu yilgi Ramazon oyi 29-mart kuni tugagan. Bugungi sanadan foydalanib,
Ramazon oyining necha kun avval tugaganini hisoblab beradigan dastur tuzing.
Namuna: Ramazon 5 kun avval tugadi.

3-mashq.
Bugungi sanadan foydalanuvchi kiritgan sanagacha bo'lgan kunlar sonini hisoblab chiqaring.
Bunda kiritilgan sana bugungi sanadan kichik bo'lmasligi kerak.

4-mashq.
Keyingi o'quv yili 2-sentyabr sanasida boshlanadi.
Bugungi sanadan boshlab, o'sha kungacha necha kun qolganini hisoblab beradigan dastur tuzing.
"""

""" timedelta """
# print(hozir - timedelta(days=21, hours=5))

"""
13-mashq.
Foydalanuvchidan uning tug'ilgan sanasini so'rang va
keyingi tug'ilgan kuniga necha kun qolganini aniqlang.
Namuna: Sizning keyingi tug'ilgan kuningiz 234 kundan keyin keladi.
"""


oy = int(input("Oy: "))
kun = int(input("Kun: "))

t_sana = date(bugun.year, oy, kun)
if t_sana > bugun:
    print(f"Sizning keyingi tug'ilgan kuningiz {(t_sana-bugun).days} kundan keyin keladi !")
elif t_sana < bugun:
    t_sana = date(bugun.year+1, oy, kun)
    print(f"Sizning keyingi tug'ilgan kuningiz {(t_sana-bugun).days} kundan keyin keladi !")

"""
17-mashq.
Foydalanuvchining tug'ilgan sanasi (faqat kun va oy) ni so'rab oling va
uning so'nggi nishonlagan tug'ilgan kuni nechta kun avval o'tib ketganini hisoblab bering.
"""
