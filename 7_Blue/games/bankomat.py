person1 = {
    'full_name':"Saidbek Shokirov",
    'card_number' : 1234,
    'card_password': 1111,
    'balance': 4_000_000,
    'block': False
}
person2 = {
    'full_name':"Nodirbek Avazbekov",
    'card_number' : 7777,
    'card_password': 0000,
    'balance': 1_500_000,
    'block': False
}
person3 = {
    'full_name':"Javohir Murodillayev",
    'card_number' : 9966,
    'card_password': 9966,
    'balance': 6_320_000,
    'block': False
}

people = [person1, person2, person3]

# karta raqam va parolni so'raymiz

while True:
    card_number = int(input("Enter the card number: "))
    card_password = int(input("Enter the card password: "))



    for person in people: # Agar parol va raqamni to'g'ri kiritsa, keyingi ishlarga o'tamiz
        if card_number in person.values() and card_password in person.values():
            print("Siz bor siz")


    if card_number not in person.values() or card_password not in person.values(): # Agar parol va raqamni 3 marta noto'g'ri kiritsa, blocklaymiz  
        print("Siz yo'q siz")


















