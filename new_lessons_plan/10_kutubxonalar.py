"""
Thame: Pythonda Kutubxonalar: datetime, math, RegEx

Kutubxona — bu tayyor yozilgan foydali kodlar to‘plami.
"""

""" Datetime - Vaqt moduli 

Datetime nima?
Datetime — sana va vaqt bilan ishlash uchun modul.

Qayerda kerak?
Tug‘ilgan kun
Dars jadvali
Vaqt hisoblash
Qancha kun o‘tdi?
"""
from datetime import datetime, date

""" datetime """
# hozir = datetime.now()
# print(hozir)
# print(hozir.date()) # sanani ajratib olish
# print(hozir.time()) # vaqtni ajratib olish

# print(hozir.hour) # soatni ajratib olish
# print(hozir.minute) # minutni ajratib olish
# print(hozir.second) # sekundni ajratib olish

# hozir = datetime.now()
# print(f"Hozir soat: {hozir}")

""" Vaqt yasash """
# vaqt = datetime(2026, 3, 4, 20, 5, 22)
# print(vaqt)

""" vaqtdan vaqtni ayrish """
# print(vaqt-hozir)
# print((vaqt-hozir).days)
# print((vaqt-hozir).seconds)


""" date - Faqat sana bilan ishlash uchun """
bugun = date.today()
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
# ramazon = datetime.date(2023, 3, 23)
# farq = ramazon-bugun
# print(farq)
# print(f"Ramazonga {farq.days} kun qoldi")



""" strftime """
hozir = datetime.now()
print(hozir.strftime("Today is the day of %A"))
print(hozir.strftime("Today is the day of %A and date %d %B"))
print(hozir.strftime("Bugungi sana va vaqt: %d-%B %Y-year  soat %H:%M:%S  | %j of year  | %U"))


"""
link -> https://docs.python.org/3/library/datetime.html
link -> https://www.w3schools.com/python/python_datetime.asp

%a	Weekday, short version	                    Wed	
%A	Weekday, full version	                    Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	    3	
%d	Day of month                                01-31	31	
%b	Month name, short version	                Dec	
%B	Month name, full version	                December	
%m	Month as a number                           01-12	12	
%y	Year, short version, without century	    18	
%Y	Year, full version	                        2018	
%H	Hour                                        00-23	17	
%I	Hour                                        00-12	05	
%p	AM/PM	                                    PM	
%M	Minute                                      00-59	41	
%S	Second                                      00-59	08	
%f	Microsecond 000000-999999	                548513	
%z	UTC offset	                                +0100	
%Z	Timezone	                                CST	
%j	Day number of year 001-366          	    365	
%U	Week number of year, 
    Sunday as the first day of week, 00-53	    52	
%W	Week number of year, 
    Monday as the first day of week, 00-53	    52	
%c	Local version of date and time	            Mon Dec 31 17:41:00 2018	
%C	Century	                                    20	
%x	Local version of date	                    12/31/18	
%X	Local version of time	                    17:41:00	
%%	A % character	                            %	
%G	ISO 8601 year	                            2018	
%u	ISO 8601 weekday (1-7)	                    1	
%V	ISO 8601 weeknumber (01-53)	                01
"""

"""
1-mashq | 10 Ball
Bugungi sanani haftaning qaysi kuni ekanligini(raqamda) konsulda chiqaring. 
 
2-mashq | 10 Ball
datetime ning strftime metodi yordamida kiritilgan sananing qaysi oy ekanligini matn ko’rinishida(uzun fotmatda) chiqarib  bering.

3-mashq | 10 Ball
datetime ning strftime metodi yordamida kiritilgan sananing qaysi hafta kuni ekanligini matn ko’rinishida(qisqa fotmatda) chiqarib  bering.
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
1-mashq | 10 Ball
Bugungi sanani haftaning qaysi kuni ekanligini(raqamda) konsulda chiqaring. 
 
2-mashq | 10 Ball
datetime ning strftime metodi yordamida kiritilgan sananing qaysi oy ekanligini 
matn ko’rinishida(uzun fotmatda) chiqarib  bering.

3-mashq | 10 Ball
datetime ning strftime metodi yordamida kiritilgan sananing qaysi hafta kuni 
ekanligini matn ko’rinishida(qisqa fotmatda) chiqarib  bering.

""" 

