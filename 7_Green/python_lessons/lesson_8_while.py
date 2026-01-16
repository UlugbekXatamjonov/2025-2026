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

while True:
    yosh = input("Yoshingizni kiriting(exit):")

    if yosh == "exit":
        print("The end !")
        break
    
    if yosh.isdigit():
        yosh = int(yosh)

        print(f"Sizning yoshingiz {yosh} yoshda va siz {2026-yosh} yilda tug'ilgansiz")


"""
1) Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rab biror ro'yhatga qo'shib yig'ing. 
    Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating.
    
2) Foydalanuvchidan uning ismini so’rang agar uning ismi “Abbos” bo’lsa dasturni to’xtating. Aks holda dastur ism so’rashda davom etaversin.

3) Foydalanuvchidan son kiritishini so'rang. agar u faqat manfiy(-) son kiritsa dastur to'xtasin.

"""

