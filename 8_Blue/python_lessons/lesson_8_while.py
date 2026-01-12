
""" for() """
# sonlar = [1,2,3,4,5,6,7,8,9,10]
# for son in sonlar:
#     print(son)


# while True:
#     son = input("Son kiriting(chiqish uchun 'exit' deb yozing): ") # "2"

#     if  son == "exit":
#         print("The end!")
#         break
        
#     if son.isdigit(): # "34"
#         son = int(son)
#         print(f"{son} ning kvadrati {son**2}")




""" Tug'ilgan yil """
# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh.isdigit():
#         yosh = int(yosh)
#         print(f"Siz {2025-yosh}-yilda tug'ilgansiz")
    
#     elif yosh == "exit":
#         print("Dastur tugadi")
#         break
    
#     else:
#         print("Siz son kiritmadingiz !!!")
 


""" Abadiyt tsikl """
# x = 1
# while 1:
#     x = x + 1
#     print(x)


""" ishora | 1-0"""
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")

# ishora = True # True -1 | False - 0
# while ishora: # = while True -> abadiy tsikl
#     savol = input("Istalgan son kiriting(dasturni to'xtatish uchun 'exit' deb yozing):")
#     if savol == 'exit':
#         ishora = False # dastur to'xtashi uchun
        
#     elif savol.isdigit():
#         print(int(savol)**2)
#     else:
#         print("Siz son kiritmadingiz!!!")

"""

4)  Foydalanuvchidan son olib, son juft yoki toqligini topuvchi dastur tuzing.
    Dastur faqat  “chiqish” so’zi kiritilganda to’xtasin.
"""

# while True:
#     son = input("Son kiriting: ").lower()

#     if son == 'exit':
#         break
    
#     elif son.isdigit(): # "5"
#         son = int(son)
        
#         if son % 2 == 0:
#             print(f"{son} juft")
#         else:
#             print(f"{son} toq")
#     else:
#         print("Son kiritin !!!!")

"""
6)  Foydalanuvchidan yaxshi ko'rgan mashinalari nomini kiritishni so'rang  va ularni cars degan ro’yhatga  yig’ing.  
    Foydalanuvchi exit so'zini yozishi bilan dasturni to'xtating va ro’yhatdagi mashinalarni konsulga chiqaring.
"""

# cars = []
# while True:
    
#     car = input("Mashina nomini kiriting:  ")

#     if car == 'exit':
#         break
#     else:
#         cars.append(car)


# print(cars)
    

""" 
12) 1 dan 100 gacha bo‘lgan sonlar yig‘indisini while yordamida, sum() funksiyasini ishatmasdan topishga harakat qiling.
"""

# summa = 0
# x = 0
# while 1:
#     x += 1
#     summa += x

#     if x == 100:
#         break

# print(summa)

# while True:
#     print("xato !!")
"""
8)  Foydalanuvchidan tizimga kirishi uchun parol so'rang, foydalanuvchi to'gri javob 
    kiritsa unga 'hush keib siz' degan habar chiqsin va dastur to'xtasim. 
    Agar foydalanuvchi 3 marta xato parol kiritsa uni abadiy tsiklga tushurib qo'ying.  
"""

# parol = "123"
# imkoniyat = 3

# while True:
#     print(f"Sizda {imkoniyat} ta iumkoniyat bor !")
#     savol = input("Parolni kiriting: ")

#     if savol == parol:
#         print("Hush kelibsiz !")
#         break
#     else:
#         imkoniyat -= 1
    
#     if imkoniyat == 0:
#         while True:
#             print("Siz bloklandiz !!!!!!!")
    

# import time

# parol = "123"
# imkoniyat = 3

# while True:
#     print(f"Sizda {imkoniyat} ta iumkoniyat bor !")
#     savol = input("Parolni kiriting: ")

#     if savol == parol:
#         print("Hush kelibsiz !")
#         break
#     else:
#         imkoniyat -= 1
    
#     if imkoniyat == 0:
#         print(f"Siz bloklandingiz !")

#         for son in range(10, 0, -1):
#             print(son)
#             time.sleep(1)

#         print("Siz qaytadan urinib ko'ring !")
#         imkoniyat = 3

"""

9) "Son topish" o'yinini while yordamisa shunday qilingki, dastur faqat "exit" so'zi kiritilganda to'xtasin, 
    hamda foydalanuvchi va komputerning  nechta g'alaba qozonganini ham hisoblasin.
"""







""" Online do'kon """
# mahsulotlar = {
#     "olma":4_500,
#     "nok":2_000,
#     "non":3_000,
#     "asal":15_000,
#     "tuz":2_500,    
# }


# bor = []
# yoq = []
# summa = 0


# print("Assalomu aleykum do'konimizga hush kelibsiz !")
# print("Bizning do'konda quidagi mahsulotlar bor: ")

# for mahsulot, narx in mahsulotlar.items():
#     print(f"{mahsulot} - {narx} so'm")

# while True:
#     savol = input("Mahsulot nomini kiriting: ")
#     if savol == 'exit' or savol == 'quit':
#         break
#     elif savol in mahsulotlar:
#         bor.append(savol)
#     else:
#         yoq.append(savol)

# for mahsulot, narx in mahsulotlar.items():
#     if mahsulot in bor:
#         summa += narx

# print(f"Bizda siz aytgan quidagi {len(bor)} ta mahsulotlar bor {bor} va ularning umumiy narxi {summa} so'm")
# print(f"Bizda siz aytgan quidagi {len(yoq)} ta mahsulotlar yo'q {yoq}")




""" Son topish o'yini """
# from random import randrange


# computer_score = 0
# plater_score = 0

# while True:
#     komputer = randrange(1, 4)
#     player = input("Son kiriting: ").lower()

#     if player == "exit":
#         print("Game over !")
#         print(f"Siz {plater_score} : {computer_score} Komputer")
#         break
    
#     elif player.isdigit(): 
#         player = int(player)

#         if komputer == player:
#             print("Siz yutdingiz ! ✅")
#             plater_score += 1
#         else:
#             print("Siz yutqazdingiz !❌")
#             computer_score += 1
            
#         print(f"Kompyuter: {komputer}")
#         print(f"Siz {plater_score} : {computer_score} Komputer")
    
#     else:
#         print("Son kioriting ❗")



from random import choice, choices
tqq = ['tosh', 'qaychi', 'qogoz']

komputer = choice(tqq)
print(komputer)

print("Quidagilardan birini tanlang: tosh, qaychi, qog'oz")
player = input("Tanlang: ").lower()








