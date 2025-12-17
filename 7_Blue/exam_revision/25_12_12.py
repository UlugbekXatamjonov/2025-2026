from random import randrange

# kompyuter=randrange(1,6)
# player=int(input("1,5 gacha son kiriting:"))

# if player==kompyuter:
#     print("Siz yutdingiz ✅")
# elif player != kompyuter and 1<= player <= 5:
#     print("Siz yutqizdingiz ! ❌")
# else:
#     print(f"Siz faqat 1-5 orasidagi sonni tanlashingiz kerak edi ⚠")

# print(f"kompyuter tanlagan son {kompyuter}ga teng")

""" 4-mashq """
# while True:
#     foydalanuvchi = input("Biror son kiriting: ").lower()
#     if foydalanuvchi == "chiqish":
#         print("Dastur to'xtadi")
#         break
    
#     if foydalanuvchi.isdigit():
#         foydalanuvchi = int(foydalanuvchi)
#         if foydalanuvchi%2 == 0:
#             print("Bu son juft")
#         else:
#             print("Bu son toq")\
    
""" mashq_5"""

# ismlar=  list()
# while True :
#     ism =  input("ism kiriting: ")
#     if ism == "stop":
#         break
#     else  :
#         ismlar.append(ism) 
        
# print(ismlar)        


""" 3-mashq """


eng_uzb = {
    'apple':"olma",
    'bread':"non",
    'bear':"ayiq",
    'fish':"baliq"
    
}


word = input("So'z kiriting: ")

for eng, uzb in eng_uzb.items():
    if word == eng:
        print(f"{eng} - {uzb}")
        
    elif word == uzb:
        print(f"{uzb} - {eng}")

if word not in eng_uzb.keys() and word not in eng_uzb.values():
    print(f"Bizda bu so'z haqida ma'lumot yo'q")











