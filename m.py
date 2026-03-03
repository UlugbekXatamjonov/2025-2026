# 1. ismlar ro'yxati
ismlar = ["Ali", "Vali", "Hasan"]

for ism in ismlar:
    print(f"Salom {ism}. Bugun 1-paraga boramizmi?")
    
    
# 2. sonlar ro'yxati
sonlar = [10, -5, 3.14, 7, -2.5]

# Arifmetik amallar
print(f"Yig'indi: {sonlar[0] + sonlar[2]}")
print(f"Ayirma: {sonlar[3] - sonlar[1]}")
print(f"ko'paytma: {sonlar[0] * sonlar[2]}")

sonlar[0] = 100        
sonlar[2] = 6.28       


# 3. Tarixiy va zamonaviy shaxslar
t_shaxslar = ["Amir Temur", "Al-Xorazmiy"]
z_shaxslar = ["Ilon Mask", "Cristiano Ronaldo"]

# pop() orqali bittadan sug'urib olish
tarixiy = t_shaxslar.pop(0)
zamonaviy = z_shaxslar.pop(0)

print(f"Men tarixiy shaxslardan {tarixiy} ning davrida yashashni istardim.")
print(f"Zamonamizning mashhur shaxslaridan esa {zamonaviy} bilan uchrashishni istardim.")


# 4. friends ro'yxati
friends = []

# append() orqali 5-6 ta do'st qo'shish
friends.append("Aziz")
friends.append("Bekzod")
friends.append("Sardor")
friends.append("Jasur")
friends.append("Bobur")
friends.append("Shaxzod")

print("Boshlang'ich ro'yxat:", friends)

# Mehmon bo'la olmaydiganlarni remove() bilan o'chirish
friends.remove("Sardor")
friends.remove("Bobur")

print("O'chirilgandan keyin:", friends)

# Boshiga, oxiriga va o'rtasiga yangi ismlar qo'shish
friends.insert(0, "Dilshod")      # boshiga
friends.append("Umid")            # oxiriga
friends.insert(2, "Kamron")       # o'rtasiga

print("Yakuniy ro'yxat:", friends)

# 5. Yangi mehmonlar ro'yxati
yangi_mehmonlar = []

# friends ro'yxatidan pop() qilib yangi ro'yxatga o'tkazish
yangi_mehmonlar.append(friends.pop())
yangi_mehmonlar.append(friends.pop())

print("Friends ro'yxati:", friends)
print("Yangi mehmonlar:", yangi_mehmonlar)

