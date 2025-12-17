
""" for() """
sonlar = [1,2,3,4,5,6,7,8,9,10]
for son in sonlar:
    print(son)


while True:
    son = input("Son kiriting(chiqish uchun 'exit' deb yozing): ")

    if  son == "exit":
        print("The end!")
        break
        
    if son.isdigit(): # "34"
        son = int(son)
        print(f"{son} ning kvadrati {son**2}")








































