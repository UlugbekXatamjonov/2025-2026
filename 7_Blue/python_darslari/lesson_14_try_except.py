""" try-except """

# son = int(input("Son kiriting: "))
# natija = 10/son
# print(f"10 ni {son} ga bo'lganda natija {natija} ")

# try:
#     son = int(input("Son kiriting: "))
#     natija = 10/son
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
# except ValueError:
#     print("Faqat raqam kiriting !")
# except:
#     print("Xatolik yuzaga keldi !!")
# else:
#     print(f"10 ni {son} ga bo'lganda natija {natija} ")
# finally:
#     print("Doim ishlashiu kerak bo'lgan qism")

# print("dasturning davomi .......................")


""" raise """
""" 'raise' xato matnini dasturchiga o'zimiz hohlagan ko'rinishda ko'rsatishga imkon beradi
"""

# a = 4
# b = 10

# try:
#     print(c+b) # Atayin xato qilindi ❗ NameErorni ko'rish uchun
# except NameError:
#     print("Name Error")
#     raise NameError("Berilgan nomdagi o'zgaruvchi topilmadi !!!") 


""" misol """
# try:
#     son1 = int(input("1-sonni kiriting: "))
#     son2 = int(input("2-sonni kiriting: "))
# except:
#     print("Siz notog'rfi qiymat kiritdingiz !")
# else:
#     if son1 == son2:
#         print(f"{son1} = {son2}")
#     else:
#         print("Sonlar teng emas !")


"""
1) Sonlar deb nomlangan ro'yhat tuzing ro'yhatda bir nechta sonlar va 0 ham bo'lsin.
    Keyin foydalanuvchidan biror son kiritishini so'rab, qabul qilingan sonni sonlar ro'yhatidagi 
    sonlarga bo'ling va natijani konsulga chiqaring.
    Dastur tuzishda 'try-except' dan foydalaning va yuzaga kelishi mumkin bo'lgan barcha xatoliklarni oldini oling !
"""


# sonlar = [4, 0, 2, 8]

# try:
#     x = int(input("Butun son kiriting: "))
#     for s in sonlar:
#         try:
#             print(s/x)
#         except ZeroDivisionError:
#             print(f"{x} - 0 ga bo'lish mumkin emas")
# except ValueError:
#     print("Noto'g'ri butun son kiritildi")
# except:
#     print("Xatolik yuz berdi")



"""
2) Foydalanuvchidan uning yoshini qabul qilib olib uni 0 dan 1,000 gacha bo'lgan sonlardan qaysilariga 
    qoldiqsiz bo'linnishini aniqlab, qoldiqsiz bo'linadigan sonlarni ro'yhatga saqlab konsulga chiqaring.
    Va bu dasturni funksiyaga joylang. Hamda uni yozishda 'try-except' dan foydalaning va yuzaga kelishi
    mumiin bo'lgan xatoliklarni oldini oling
"""

# def mashq(son):
#     natija = []
    
#     for s in range(0, 1000):
#         try:
#             if s%son == 0:
#                 natija.append(s)
#         except:
#             print("0 dan boshqa son kiriting !")    
#     return natija

# try:
#     yosh = int(input("Yosh kitiring: "))
# except:
#     print("faqat son kiriting !!!")
# else:
#     print(mashq(yosh))


"""
3) To'g'ri burchakli uchburchakning gipotenuzasini hisoblash. Ushbu kodda yuzaga kelishi mumkin bo'lgan hatoliklarni
    'try-except' yordamida oldini oling
    a = int(input("Birinchi katetni kiriting: "))
    b = int(input("Ikkinchi katetni kiriting: "))
    c**2=a**2+b**2

print(f"Katetlari {a} va {b} ga teng bo'lgan uchburchakning giputenuzasi {c} ga teng")
"""

try:
    a = int(input("Birinchi katetni kiriting: "))
    b = int(input("Ikkinchi katetni kiriting: "))
except ValueError:
    print("Siz faqat raqam kiritishingiz kerak !!!")
except:
    print("Uzr dasturda xatolik sodir bo'ldi !")
else:
    from math import sqrt
    if a > 0 and b > 0:
        c = round(sqrt(a**2+b**2),2)
        print(f"Katetlari {a} va {b} ga teng bo'lgan uchburchakning giputenuzasi {c} ga teng")  
    else:
        print("Katetlarning uzunligi 0 bo'lmasligi kerak !")
        