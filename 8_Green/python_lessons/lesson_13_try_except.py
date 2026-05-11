

"""
15-mashq.
Foydalanuvchidan uning maktabga birinchi marta borgan sanasini so'rang va
o'sha kundan bugungi kungacha qancha vaqt o'tganini hisoblab, konsolga chiqaring.
"""

from datetime import date, datetime

bugun = date.today()

try:
    yil = int(input("Yil: "))
    oy = int(input("Oy: "))
    kun = int(input("Kun: "))
except ValueError:
    print("Yil, oy yoki kunni kirgizishda xato qildingiz !!!")
except:
    print("Qaytadan urinib ko'ring !")
else:
    sana1 = date(yil, oy, kun)
    print(f"o'sha sanadan bugungacha {(bugun-sana1).days} kun o'tdi !")























