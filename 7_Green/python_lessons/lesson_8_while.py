"""
While tsikli
"""

""" for() """
# sonlar = [1,2,3,4,5,6,7,8,9,10]
# for son in sonlar:
#     print(son)


while True:
    son = input("son kiriting(stop):") # "22"

    if son == 'stop':
        print("dastur to'xtadi!")
        break
    
    if son.isdigit(): # "22"
        son = int(son)
        print(f"{son} ning ikkinchi darajasi {son**2}")











