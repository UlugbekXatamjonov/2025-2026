from random import choice

"""  ------------------------------------  Simple version  ---------------------------------------  """
# """ ✋ ✌ ✊  - tosh qaychi qog'oz """
# tqq = ["tosh", "qaychi", "qog'oz"]
# komputer = choice(tqq)
# player = input("Don don ziki: ").lower()

# if player in tqq:
#     if player == "tosh" and komputer == "qaychi":
#         print("Siz yutdingiz ✅")
        
#     elif player == "qaychi" and komputer == "qog'oz":
#         print("Siz yutdingiz ✅")
        
#     elif player == "qog'oz" and komputer == "tosh":
#         print("Siz yutdingiz ✅")

#     elif player == "qog'oz" and komputer == "qaychi":
#         print("Siz yutqazdingiz ❌")

#     elif player == "tosh" and komputer == "qog'oz":
#         print("Siz yutqazdingiz ❌")

#     elif player == "qaychi" and komputer == "tosh":
#         print("Siz yutqazdingiz ❌")
        
#     elif player == komputer:
#         print("Durrang 🤝")
        
#     print(f"Komputer: {komputer}")
    
# else:
#     print("Siz noto'g'ri tanlov kiritdingiz ❗❌❌❌")



"""  ------------------------------------  Perfect version  ---------------------------------------  """
""" ✋ ✌ ✊  - tosh qaychi qog'oz """
tqq = ["tosh", "qaychi", "qog'oz"]

player_score = 0
komputer_score = 0


while True:
    
    # Komputer va o'yinchi tanlov qiladi
    komputer = choice(tqq)
    player = input("Don don ziki: ").lower()

    # Chiqish bo'limi
    if player == 'stop':
        print(f"Game over !")
        print(f"Yakuniy xisob:  🧑 {player_score} : {komputer_score} 🤖 ")
        
        # Kim yutganiga qarab javob qaytaramiz 
        if player_score > komputer_score:
            print(f"Tabriklayman shogirt sen yutding 🥇👋👋👋👋👋👋")
        elif player_score < komputer_score:
            print(f"Shogirt emas ekansan. Botniyam yuta olmading 👎😕")
        else:
            print(f"Bot ekan san 🙄 \nDurrang 👏")
        
        break

    # Kim yutganini aniqlaymiz
    if player in tqq:
        if player == "tosh" and komputer == "qaychi":
            print("Siz yutdingiz ✅")
            # Yutganga 1 ochko beramiz
            player_score += 1
            
        elif player == "qaychi" and komputer == "qog'oz":
            print("Siz yutdingiz ✅")
            player_score += 1
            
        elif player == "qog'oz" and komputer == "tosh":
            print("Siz yutdingiz ✅")
            player_score += 1

        elif player == "qog'oz" and komputer == "qaychi":
            print("Siz yutqazdingiz ❌")
            komputer_score += 1

        elif player == "tosh" and komputer == "qog'oz":
            print("Siz yutqazdingiz ❌")
            komputer_score += 1

        elif player == "qaychi" and komputer == "tosh":
            print("Siz yutqazdingiz ❌")
            komputer_score += 1
            
        elif player == komputer:
            print("Durrang 🤝")
            
        print(f"Komputer: {komputer}")
        print(f"Siz {player_score} : {komputer_score} Komputer")
    
    # Boshqacha javob uchun matn
    else:
        print("Siz noto'g'ri tanlov kiritdingiz ❗❌❌❌")

