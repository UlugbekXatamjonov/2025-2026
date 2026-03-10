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


# yil = int(input("Yil: "))
# oy = int(input("Oy: "))
# kun = int(input("Kun: "))

# sana1  = date(yil, oy, kun)

# if bugun > sana1:
#     print("O'tib ketgan sana")
# elif bugun < sana1:
#     print("Endi keladigan sana")
# elif bugun == sana1:
#     print("Siz bugungi sanani kiritdingiz")
    
    
    
"""
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
"""


"""
3-mashq
Eng yaqin do’stingiz va sizning o’rtangizda necha kun farq bor ? Dastur yordamida buni  aniqlang. 
Namuna: Abdulloh va mening oramizda 35 kun farq bor.
"""
# yil = int(input("Yil: "))
# oy = int(input("Oy: "))
# kun = int(input("Kun: "))
# friend = date(yil, oy, kun)

# my = date(2013, 5, 2)

# if my > friend:
#     print(f"Bizning oramizdagi farq {(my - friend).days} kun qoldi")
# else:
#     print(f"Bizning oramizdagi farq {(friend - my).days} kun qoldi")

""" strftime """

# sana = date(2026, 3, 4)
# print(sana.strftime("Today is the week of %j"))

""" strftime """
hozir = datetime.now()
# print(hozir.strftime("Today is the day of %A"))
# print(hozir.strftime("Today is the day of %A and date %d %B"))
# print(hozir.strftime("Bugungi sana va vaqt: %d-%B %Y-year  soat %H:%M:%S  | %j of year  | %U"))



"""
link -> https://docs.python.org/3/library/datetime.html
link -> https://www.w3schools.com/python/python_datetime.asp

%a	  Weekday, short version	                        Wed	
%A	  Weekday, full version	                                Wednesday	
%w	  Weekday as a number 0-6, 0 is Sunday	                3	
%d	  Day of month                                          01-31	31	
%b	  Month name, short version	                        Dec	
%B	  Month name, full version	                        December	
%m	  Month as a number                                     01-12	12	
%y	  Year, short version, without century	                18	
%Y	  Year, full version	                                2018	
%H	  Hour                                                  00-23	17	
%I	  Hour                                                  00-12	05	
%p	  AM/PM	                                                PM	
%M	  Minute                                                00-59	41	
%S	  Second                                                00-59	08	
%f	  Microsecond 000000-999999	                        548513	
%z	  UTC offset	                                        +0100	
%Z	  Timezone	                                        CST	
%j	  Day number of year 001-366          	                365	
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

7-mashq.
Bugungi sanani olib, uni quyidagi ko'rinishda konsolga chiqaring:
Bugun 2025-yil, 4-oyning 4-kuni.

8-mashq.
Bugungi sanadan foydalanib, yilni, oyini va kunini alohida-alohida qilib konsolga chiqaring.
"""


# """ 6-mashq """
# hozir = datetime.now()
# print(bugun.strftime("%w"))

# """ 7-mashq """
# sana = date.today()
# print(sana.strftime("%Y-yil, %m-oyining, %d - kuni."))

# """ 8-mashq """
# print(sana.strftime("%Y-yil."))
# print(sana.strftime("%m-oyi. "))
# print(sana.strftime("%d - kun."))


"""
9-mashq.
strftime metodi yordamida bugungi sananing haftaning qaysi kuni ekanligini
uzun formatda konsolga chiqaring.
Namuna: Today is Friday.
"""
# print(bugun.strftime("Today is %A."))


"""
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
"""

print(bugun.strftime("%B"))
print(bugun.strftime("%b"))
print(hozir.strftime("%I:%M %p"))


""" timedelta """
sana1 = date(2012, 9, 23)
print(sana1)
print(sana1-timedelta(weeks=2, days=3))

print(hozir)
print(hozir+timedelta(hours=200))


"""
14-mashq.
2010-03-10 sanasidan 8 hafta, 325 soat va 854 minutni ayring va
hosil bo'lgan sana va vaqtni konsolga chiqaring.

15-mashq.
Foydalanuvchidan uning maktabga birinchi marta borgan sanasini so'rang va
o'sha kundan bugungi kungacha qancha vaqt o'tganini hisoblab, konsolga chiqaring.
"""
