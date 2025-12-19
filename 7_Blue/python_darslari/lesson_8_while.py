
"""
While tsikli
"""

""" for() """
# sonlar = [1,2,3,4,5,6,7,8,9,10]
# for son in sonlar:
#     print(son)

# print("Dasturni to'xtatmoqchi bo'lsangiz 'exit' deb yozing !")
# while True: # True / False
#     son1 = input("Birinchi sonni kiriting: ")
#     if son1 == 'exit':
#         print("Dastur to'xtadi !")
#         break
    
#     son2 = input("Ikkinchi sonni kiriting: ")
#     if son2 == 'exit':
#         print("Dastur to'xtadi !")
#         break

    
#     if son1.isdigit() and son2.isdigit(): # "434"
#         son1 = int(son1)
#         son2 = int(son2)
        
#         if son1 > son2:
#             print(f"{son1} > {son2}")
#         elif son1 < son2:
#             print(f"{son1} < {son2}")
#         elif son1 == son2:
#             print(f"{son1} = {son2}")


# while True:
#     print("Dasturni to'xtatish uchun 'exit' yoki 'quit' deb yozing !")
#     son = input("Biror son kiriting: ").lower()
#     if son == "exit" or son =="quit":
#         print("Dastur to'xtadi !")
#         break 
    
#     if son.isdigit():
#         son = int(son)
        
#         print(f"{son} ning ikkinchidarajasi {son**2} ga teng.")
        


"""  
1-mashq
Foydalanuvchidan yoshini so'rab tug'ilgan yilini hisoblab beradigan dastur yozing. Dastur faqat 'chiqish' so'zi yozilsa tugasin. 
"""

# print("Chiqish uchun 'chiqish' deb yozing !")
# while True:

#     yosh = input("Yoshingizni kiriting(chiqish): ").lower()
    
#     if yosh == 'chiqish':
#         print("Dastur to'xtadi !")
#         break
    
#     elif yosh.isdigit():
#         yosh = int(yosh)
#         # if yosh > 0 and yosh < 150 :
#         if 0 < yosh < 150 :
#             print(f"Sizning yoshingiz {yosh} da va siz {2025-yosh}-yili tug'ilgansiz")


"""
1) Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rab biror ro'yhatga qo'shib yig'ing. 
    Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating.
    
2) 1 dan 100 gacha bo‘lgan sonlar yig‘indisini while yordamida, sum() funksiyasini ishatmasdan topishga harakat qiling.

3) Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 
7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. 
Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va 
chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur 
to'xtasin (ikkita shartni ham tekshiring)
"""


""" 1-mashq """
# books = []
# while 1:  # True = 1 | False  = 0
#     book = input("Enter book name: ").lower()

#     if book == "stop":
#         print("The end !")
#         break
    
#     elif book != "":
#         books.append(book)

# print(books)

""" 2-mashq """
# summa = 0
# number = 1 # 1 ... 100
# while True:
    
#     summa = summa + number
#     number += 1

#     if number > 100:
#         break

# print(summa)

"""
9-mashq
Foydalanuvchidan tizimga kirishi uchun parol so'rang, foydalanuvchi to'gri javob kiritsa unga 'hush keib siz' degan habar chiqsin 
va dastur to'xtasin.
Agar foydalanuvchi 3 marta xato parol kiritsa uni abadiy tsiklga tushurib qo'ying.

"""

# parol = "123"
# urinish = 3

""" Abadiy tsikl """
# while True:
#     print(f"Sizda {urinish} ta urinish imkoniyati bor !")
#     savol = input("Parolni kiriting: ")
    
#     if savol == parol:
#         print("Hush kelibsiz !")
#         break
#     else:
#         urinish -= 1
#         # urinish = urinish -1
#         print("Xato parol ❗")
        
#     if urinish == 0:
#         while True:
#             print("Siz bloklandingiz ❌❌❌")
    



""" sekundli parol """
# import time
# parol = "123"
# urinish = 3


# while True:
#     print(f"Sizda {urinish} ta urinish imkoniyati bor !")
#     savol = input("Parolni kiriting: ")
    
#     if savol == parol:
#         print("Hush kelibsiz !")
#         break
#     else:
#         urinish -= 1
#         # urinish = urinish -1
#         print("Xato parol ❗")
        
#     if urinish == 0:
#         print("Siz 10 sekundaga bloklandingiz !")
        
#         for sekund in range(10, 0, -1):
#             print(f"Sizda {sekund} s qoldi")
#             time.sleep(1)
            
#         print("Siz qaytadan urinib ko'rishingiz mumkin ♻")
#         urinish = 3
    
    










