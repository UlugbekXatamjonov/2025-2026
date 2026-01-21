"""
While tsikli
"""

""" for() """
# sonlar = [1,2,3,4,5,6,7,8,9,10]
# for son in sonlar:
#     print(son)


# while True:
#     son = input("son kiriting(stop):") # "22"

#     if son == 'stop':
#         print("dastur to'xtadi!")
#         break
    
#     if son.isdigit(): # "22"
#         son = int(son)
#         print(f"{son} ning ikkinchi darajasi {son**2}")
#     else:
#         print(F"Siz faqat son kiritishingiz kerak !")


""" exit() """

# while True:
#     yosh = input("Yoshingizni kiriting(exit):")

#     if yosh == "exit":
#         print("The end !")
#         break
    
#     if yosh.isdigit():
#         yosh = int(yosh)

#         print(f"Sizning yoshingiz {yosh} yoshda va siz {2026-yosh} yilda tug'ilgansiz")


"""
1) Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rab biror ro'yhatga qo'shib yig'ing. 
    Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating.
    
2) Foydalanuvchidan uning ismini so’rang agar uning ismi “Abbos” bo’lsa dasturni to’xtating. Aks holda dastur ism so’rashda davom etaversin.

3) Foydalanuvchidan son kiritishini so'rang. agar u faqat manfiy(-) son kiritsa dastur to'xtasin.

"""

""" 1 """

# books = []
# while True:
#     book = input("Biror kitob nomini kiriting(stop): ")

#     if book == "stop":
#         print("Dastur to'xtadi !")
#         break
    
#     books.append(book)

# print(books)


""" 2 """
# while True:
#     name = input("Ism kiriting: ").lower()

#     if name == "abbos":
#         break


""" 3 """
# while True:
#     son = int(input("Son kiriting: "))
    
#     if son < 0:
#         print("Dastur to`xtadi")
#         break


""" Abadiy stilik """
# x = 1
# while True:
#     print(x)
#     x += 1


"""
4)  Foydalanuvchidan son olib, son juft yoki toqligini topuvchi dastur tuzing.
    Dastur faqat  “chiqish” so’zi kiritilganda to’xtasin.
"""

while True:
    son = input("Son kiriting(chiqish):")

    if son == "chiqish":
        print("The end !")
        break
    
    if son.isdigit():
        son = int(son)
    
        if son%2 ==0:
            print(f"{son} juft")
        else:
            print(f"{son} toq")


"""
7) Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 
    7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. 
    Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va 
    chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur 
    to'xtasin (ikkita shartni ham tekshiring)
"""


"""
6)  Foydalanuvchidan yaxshi ko'rgan mashinalari nomini kiritishni so'rang  va ularni cars degan ro’yhatga  yig’ing.  
    Foydalanuvchi exit so'zini yozishi bilan dasturni to'xtating va ro’yhatdagi mashinalarni konsulga chiqaring.
"""
cars = []
while True:
    car = input("Mashina: ")

    if car == 'stop':
        break
    
    else:
        cars.append(car)
print(cars)
        
"""
8)  Foydalanuvchidan tizimga kirishi uchun parol so'rang, foydalanuvchi to'gri javob 
    kiritsa unga 'hush keib siz' degan habar chiqsin va dastur to'xtasim. 
    Agar foydalanuvchi 3 marta xato parol kiritsa, siz blocklandiungiz.  
"""



