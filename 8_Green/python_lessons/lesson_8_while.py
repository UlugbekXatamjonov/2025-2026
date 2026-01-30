"""
While tsikli
"""

""" for() """
sonlar = [1,2,3,4,5,6,7,8,9,10]
for son in sonlar:
    print(son)



while True:
    ism = input("ismingiz nima: ").lower()
    print(f"Assalomu aleykum {ism.title()} !")

    if ism == 'exit':
        print("Dastur to'xtadi !")
        break


# while True:
#     son = input("Son kiriting: ")# "34"

#     if son == 'exit':
#         print("Dastur to'xtadi !")
#         break 
    
#     if son.isdigit():

#         print(f"{son} ning kvadrati {son ** 2}")







