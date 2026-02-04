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
print(hozir)
print(hozir.date()) # sanani ajratib olish
print(hozir.time()) # vaqtni ajratib olish

print(hozir.year) # yilni ajratib olish
print(hozir.month) # oyni ajratib olish
print(hozir.day) # kunni ajratib olish
print(hozir.hour) # soatni ajratib olish
print(hozir.minute) # minutni ajratib olish
print(hozir.second) # sekundni ajratib olish
print(hozir.microsecond) # microsekundni ajratib olish

print(f"Hozir soat: {hozir.time()}")
print(f"Hozir soat: {hozir.hour}:{hozir.minute}")


















