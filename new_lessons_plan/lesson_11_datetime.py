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
from datetime import datetime, date

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

""" Vaqt yasash """
# vaqt = datetime(2026, 3, 4, 20, 5, 22)
# print(vaqt)

""" vaqtdan vaqtni ayrish """
# print(vaqt-hozir)
# print((vaqt-hozir).days)
# print((vaqt-hozir).seconds)


""" date - Faqat sana bilan ishlash uchun """
# bugun = date.today()
# print(bugun)
# print(bugun.year)
# print(bugun.month)
# print(bugun.day)

# print(f"Bugun oyning {bugun.day}-kuni")

# kun = int(input("Kun kiriting: "))
# oy = int(input("Oy kiriting: "))
# yil = int(input("Yil kiriting: "))

""" sana yasash """
# sana = date(yil, oy, kun)
# print(sana)


""" Ramazongacha bo'lgan vaqt """
# bugun = datetime.date.today()
# ramazon = datetime.date(2026, 2, 12)
# farq = ramazon-bugun
# print(farq)
# print(f"Ramazonga {farq.days} kun qoldi")



""" strftime """
# hozir = datetime.now()
# print(hozir.strftime("Today is the day of %A"))
# print(hozir.strftime("Today is the day of %A and date %d %B"))
# print(hozir.strftime("Bugungi sana va vaqt: %d-%B %Y-year  soat %H:%M:%S  | %j of year  | %U"))


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


""" Tug'ilgan kunga necha kun qoldi ? """
"""1 mashq"""
"""  """
# oy = int(input("Tug'ilgan oyingizni kiriting:"))
# kun = int(input("Tug'ilgan kuningizni kiriting:"))

# tugilgan_sana = date(bugun.year, oy, kun)

# if tugilgan_sana > bugun:
#     print(f"Sizning tug'ilgan kuningga yana {(tugilgan_sana-bugun).days} kun qoldi.")
    
# elif tugilgan_sana < bugun:
#     tugilgan_sana = date(bugun.year+1, oy, kun)
#     print(f"Sizning tug'ilgan kuningga yana {(tugilgan_sana-bugun).days} kun qoldi.")
# else:
#     print(f"Tug'ilgan kuningiz bilan 😇🥳🥳! Sizning tug'ilgan kuningiz bugun !!!")

"""
-------- Sodda --------
1-mashq.
Foydalanuvchidan biror sana so'rang. Agar kiritilgan sana o'tib ketgan bo'lsa —
“Bu o'tib ketgan sana”,
agar hali kelmagan bo'lsa — “Bu sana endi keladi”,
agar bugungi sana bo'lsa — “Siz bugungi sanani kiritdingiz” degan xabar konsolga chiqsin.

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

5-mashq.
Bu yilgi o'quv yili 2025-yil 4-sentyabr sanasida boshlangan bo'lsa,
bugungi kungacha maktab boshlanganiga necha kun bo'lganini aniqlang.
Namuna: Maktab boshlanganiga 153 kun bo'ldi.


--------- strftime bilan ishlash --------- 
6-mashq.
Bugungi sanani haftaning qaysi kuni ekanligini raqam ko'rinishida konsolga chiqaring.
Namuna: 0 — dushanba, 6 — yakshanba.

7-mashq.
Bugungi sanani olib, uni quyidagi ko'rinishda konsolga chiqaring:
Bugun 2025-yil, 4-oyning 4-kuni.

8-mashq.
Bugungi sanadan foydalanib, yilni, oyini va kunini alohida-alohida qilib konsolga chiqaring.

9-mashq.
strftime metodi yordamida bugungi sananing haftaning qaysi kuni ekanligini
uzun formatda konsolga chiqaring.
Namuna: Today is Friday.

10-mashq.
strftime metodi yordamida bugungi sananing qaysi oy ekanligini
matn ko'rinishida (uzun formatda) konsolga chiqaring.
Namuna: April.

11-mashq.
strftime metodi yordamida bugungi sananing haftaning qaysi kuni ekanligini
qisqa formatda konsolga chiqaring.
Namuna: Fri.

12-mashq.
Hozirgi vaqtni AM/PM formatida konsolga chiqaring.
Namuna: It is 2:13 PM o'clock now.


--------- Murakkab mashqlar--------- 
13-mashq.
Foydalanuvchidan uning tug'ilgan sanasini so'rang va
keyingi tug'ilgan kuniga necha kun qolganini aniqlang.
Namuna: Sizning keyingi tug'ilgan kuningiz 234 kundan keyin keladi.

14-mashq.
2010-03-10 sanasidan 8 hafta, 325 soat va 854 minutni ayring va
hosil bo'lgan sana va vaqtni konsolga chiqaring.

15-mashq.
Foydalanuvchidan uning maktabga birinchi marta borgan sanasini so'rang va
o'sha kundan bugungi kungacha qancha vaqt o'tganini hisoblab, konsolga chiqaring.

16-mashq.
Foydalanuvchidan istalgan soat miqdorini so'rang, uni hozirgi vaqtga qo'shing va
hosil bo'lgan yangi vaqtni konsolga chiqaring.
Namuna: 283 soatdan keyin vaqt 21:45 bo'ladi.

17-mashq.
Foydalanuvchining tug'ilgan sanasi (faqat kun va oy) ni so'rab oling va
uning so'nggi nishonlagan tug'ilgan kuni nechta kun avval o'tib ketganini hisoblab bering.
""" 









