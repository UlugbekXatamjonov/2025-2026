"""
While tsikli
"""

""" for() """
# sonlar = [1,2,3,4,5,6,7,8,9,10]
# for son in sonlar:
#     print(son)



# while True:
#     ism = input("ismingiz nima: ").lower()
#     print(f"Assalomu aleykum {ism.title()} !")

#     if ism == 'exit':
#         print("Dastur to'xtadi !")
#         break # To'xtatish


# while True:
#     son = input("Son kiriting: ").lower().strip()# "34"
#     if son == "exit":
#         break
    
#     if son.isdigit():
#         son = int(son)
#         print(f"{son} ning kvadrati {son ** 2}")


# while True:
#     yosh = input("Yongizni kiriting: ")

#     if yosh == 'exit' or yosh =='quit':
#         print("Dastur to'xtadi !")
#         break
    
#     if yosh.isdigit():
#         yosh = int(yosh)
        
#         print(f"Siz {2026-yosh}-yili tug'ilgansiz !")


""" Abadiyt tsikl """
# x = 1
# while True:
#     print(x)
#     x+=1


"""
2) Foydalanuvchidan uning ismini so’rang agar uning ismi “Abbos” bo’lsa dasturni to’xtating. Aks holda dastur ism so’rashda davom etaversin.

3) Foydalanuvchidan son kiritishini so'rang. agar u faqat manfiy(-) son kiritsa dastur to'xtasin.

4)  Foydalanuvchidan son olib, son juft yoki toqligini topuvchi dastur tuzing.
    Dastur faqat  “chiqish” so’zi kiritilganda to’xtasin.
"""

""" 2-mashq """
while True:
    ism = input("Ismingizni kiriting: ")
    if ism == 'abbos':
        print("Dastur to'xtadi !")
        break
    
""" 3-mashq """
while True:
    son = int(input("Son: "))
    if son < 0:
        print("Dastur to'xtadi !")
        break
    
    
    
    
    
    
    