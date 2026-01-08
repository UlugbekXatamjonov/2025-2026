while True:

    person1 = {
        'full_name':"Saidbek Shokirov",
        'card_number' : 1234,
        'card_password': 1111,
        'balance': 4_000_000,
        'block': False
    }

    print("Assalomu aleykum hurmatli mijoz ! \nHush kelibsiz")
    card_number = int(input("Karta raqamingizni kiriting: "))
    password = int(input("Parolingizni kiriting: "))

    while True:
        if card_number == person1['card_number'] and password == person1['card_password']:
            print("Biror amalni tanlang: \n1) Balansni ko'rish \n2) Naqd pul yechish \n3) Kartani to'ldirish \n4) Parolni o'zgartirish \n5) Chiqish")
            customer = int(input("Amallardan birini tanlang: "))

            if customer == 1:
                print(f"Sizning balansiz {person1['balance']} so'm") 

            if customer == 2:
                withdrawn_money= int(input("Yechiladigan mablag'ni kiriting: "))

                if withdrawn_money <= person1['balance']:
                    person1['balance'] -= withdrawn_money
                    print(f"Sizning hisobingdan {withdrawn_money} so'm yechib olindi !")
                    print(f"Qolgan mablag': {person1['balance']} so'm")
                else:
                    print(f"Sizning balansingizda yetarlicha mablag' yo'q")

            if customer == 3:
                additional_money = int(input("Qo'shiladigan mablag'ni kiriting: "))
                
                if additional_money > 0:
                    person1['balance'] += additional_money
                    print(f"Sizning balansingiz muvoffaqiyatli to'ldirildi !")
                    print(f"Sizning balansiz {person1['balance']} so'm") 
                else:
                    print(f"Siz manfiy mablag' kirita olmaysiz !")

            if customer == 4:
                current_password = int(input("Hozirgi parolingizni kiriting: "))
                if current_password == person1['card_password']:
                    print("Yangi parol 4 ta sondan iborat bo'lishi va sodda bo'lmasligi kerak !")
                    new_password1 = int(input("Yangi parol kiriting: "))
                    new_password2 = int(input("Parolni tasdiqlang: "))

                    if new_password1 == new_password2 and len(str(new_password1)) == 4:
                        person1['card_password'] = new_password1
                        print(f"Parol muvoffaqiyatli o'zgartirildi !")
                    else:
                        print("Parol shartlarga mos kelmadi !!!") 

                else:
                    print("Parolni xato kirgizdingiz !")

            if customer == 5:
                print(f"Xizmatimizdan foydalanganingiz uchun rahmat !\n\n\n\n\n\n\n\n\n\n")
                break
            
            if customer < 1 or customer > 5:
                print(f"Siz noto'g'ri amalni tanladingiz ! Qaytadan urinib ko'ring !")
            
        else:
            print("Karta raqami yoki paroli noto'g'ri !\n\n")
            break
            
            