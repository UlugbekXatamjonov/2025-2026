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


while True:
    son = input("Son kiriting: ").lower().strip()# "34"
    if son == "exit":
        break
    
    if son.isdigit():
        son = int(son)
        print(f"{son} ning kvadrati {son ** 2}")


while True:
    yosh = input("Yongizni kiriting: ")

    if yosh == 'exit' or yosh =='quit':
        print("Dastur to'xtadi !")
        break
    
    if yosh.isdigit():
        yosh = int(yosh)
        
        print(f"Siz {2026-yosh}-yili tug'ilgansiz !")


""" Abadiyt tsikl """
# x = 1
# while True:
#     print(x)
#     x+=1