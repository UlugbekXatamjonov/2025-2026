
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
while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():
        yosh = int(yosh)
        print(f"Siz {2025-yosh}-yilda tug'ilgansiz")
    
    elif yosh == "exit":
        print("Dastur tugadi")
        break
    
    else:
        print("Siz son kiritmadingiz !!!")
 


""" Abadiyt tsikl """
x = 1
while 1:
    x = x + 1
    print(x)


""" ishora | 1-0"""
print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")

ishora = True # True -1 | False - 0
while ishora: # = while True -> abadiy tsikl
    savol = input("Istalgan son kiriting(dasturni to'xtatish uchun 'exit' deb yozing):")
    if savol == 'exit':
        ishora = False # dastur to'xtashi uchun
        
    elif savol.isdigit():
        print(int(savol)**2)
    else:
        print("Siz son kiritmadingiz!!!")
































