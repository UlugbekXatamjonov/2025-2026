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
# hozir = datetime.now()
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
# t_kun = date(2012, 11, 19)

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

# yil = int(input("Yil: "))
# oy = int(input("Oy: "))
# kun = int(input("Kun: "))
# sana = date(yil, oy, kun)

# if sana > bugun:
#     print(f"{(sana-bugun).days}")
# else:
#     # print("Siz eski sana kiritdingiz !")


"""
1-mashq.
Foydalanuvchidan biror sana so'rang. Agar kiritilgan sana o'tib ketgan bo'lsa —
“Bu o'tib ketgan sana”,
agar hali kelmagan bo'lsa — “Bu sana endi keladi”,
agar bugungi sana bo'lsa — “Siz bugungi sanani kiritdingiz” degan xabar konsolga chiqsin.
"""


# yil1 = int(input("Yil: "))
# oy1 = int(input("Oy: "))
# kun1 = int(input("Kun: "))
# sana1 = date(yil1, oy1, kun1)

# if sana1 > bugun:
#     print(f"Bu sana endi keladi")
# elif sana1 < bugun:
#     print(f"Bu o'tib ketgan sana")
# else:
#     print("Siz bugungi sanani kiritdingiz")

"""
4-mashq.
Keyingi o'quv yili 2-sentyabr sanasida boshlanadi.
Bugungi sanadan boshlab, o'sha kungacha necha kun qolganini hisoblab beradigan dastur tuzing.
"""

from datetime import datetime , date , time 


# bugun=date.today()
# sana = date(2026,9,2)
# print(f"Keyingi o'quv yiliga {(sana-bugun).days} kun qoldi.")

"""
5-mashq.
Bu yilgi o'quv yili 2025-yil 4-sentyabr sanasida boshlangan bo'lsa,
bugungi kungacha maktab boshlanganiga necha kun bo'lganini aniqlang.
Namuna: Maktab boshlanganiga 153 kun bo'ldi.
"""

# oquv_yili = date(2025, 9,4)
# print(f"Maktab boshlanganiga {( bugun - oquv_yili ).days} kun bo'ldi")



bugun = date.today()
hozir = datetime.now()

""" strftime """
print(hozir.strftime("Today is the day of %A"))
print(hozir.strftime("Today is the day of %A and date %d %B"))
print(hozir.strftime("Bugungi sana va vaqt: %d-%B %Y-year  soat %H:%M:%S  | %j of year  | %U"))


"""
link -> https://docs.python.org/3/library/datetime.html
link -> https://www.w3schools.com/python/python_datetime.asp

%a	  Weekday, short version	                        Wed	
%A	  Weekday, full version	                              Wednesday	
%w	  Weekday as a number 0-6, 0 is Sunday	            3	
%d	  Day of month                                        01-31	31	
%b	  Month name, short version	                        Dec	
%B	  Month name, full version	                        December	
%m	  Month as a number                                   01-12	12	
%y	  Year, short version, without century	            18	
%Y	  Year, full version	                              2018	
%H	  Hour                                                00-23	17	
%I	  Hour                                                00-12	05	
%p	  AM/PM	                                          PM	
%M	  Minute                                              00-59	41	
%S	  Second                                              00-59	08	
%f	  Microsecond 000000-999999	                        548513	
%z	  UTC offset	                                    +0100	
%Z	  Timezone	                                          CST	
%j	  Day number of year 001-366          	            365	
%U	  Week number of year, 
        Sunday as the first day of week, 00-53	            52	
%W	  Week number of year, 
        Monday as the first day of week, 00-53	            52	
%c	  Local version of date and time	                  Mon Dec 31 17:41:00 2018	
%C	  Century	                                          20	
%x	  Local version of date	                              12/31/18	
%X	  Local version of time	                              17:41:00	
%%	  A % character	                                    %	
%G	  ISO 8601 year	                                    2018	
%u	  ISO 8601 weekday (1-7)	                        1	
%V	  ISO 8601 weeknumber (01-53)	                        01
"""

"""
6-mashq.
Bugungi sanani haftaning qaysi kuni ekanligini raqam ko'rinishida konsolga chiqaring.
Namuna: 0 — dushanba, 6 — yakshanba.
""" 
print(bugun.strftime("Bugun haftaning %w-kuni"))


"""
7-mashq.
Bugungi sanani olib, uni quyidagi ko'rinishda konsolga chiqaring:
Bugun 2025-yil, 4-oyning 4-kuni.
"""
print(bugun.strftime("Bugun %Y-yilning %m-oyning  %d-kuni"))











