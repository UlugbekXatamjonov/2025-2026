from random import choice

""" ✋ ✌ ✊  - tosh qaychi qog'oz """
tqq = ["tosh", "qaychi", "qog'oz"]
komputer = choice(tqq)
player = input("Don don ziki: ").lower()

if player in tqq:
    if player == "tosh" and komputer == "qaychi":
        print("Siz yutdingiz ✅")
        
    elif player == "qaychi" and komputer == "qog'oz":
        print("Siz yutdingiz ✅")
        
    elif player == "qog'oz" and komputer == "tosh":
        print("Siz yutdingiz ✅")

    elif player == "qog'oz" and komputer == "qaychi":
        print("Siz yutqazdingiz ❌")

    elif player == "tosh" and komputer == "qog'oz":
        print("Siz yutqazdingiz ❌")

    elif player == "qaychi" and komputer == "tosh":
        print("Siz yutqazdingiz ❌")
        
    elif player == komputer:
        print("Durrang 🤝")
        
    print(f"Komputer: {komputer}")
    
else:
    print("Siz noto'g'ri tanlov kiritdingiz ❗❌❌❌")

