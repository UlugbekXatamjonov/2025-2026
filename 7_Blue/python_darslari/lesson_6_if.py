""" if-else """


# son = int(input("Son kiriting: "))

# if son > 0:
#     print(f"{son} musbat")
# else:
#     print(f"{son} manfiy")
    


# savol = input("Siz olma yeganmisiz: ").lower()

# if savol == "ha":
#     print(f"Menga qani ?")
# else:
#     print(f"Olma yeyishni tafsiya qilaman !")




# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']

# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else:
#         print(car.title())


# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())


# login = input("Loginni kiriting: ").lower()

# if login == "admin":
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {login}!" )


# son1 = int(input("1-sonni kiriting: "))
# son2 = int(input("2-sonni kiriting: "))
# if son1 == son2:
#     print(f"{son1} = {son2}")
# else:
#     print("Sonlar teng emas !")

from math import sqrt

# son3 = int(input("Sonni kiriting: "))

# if son3 > 0:
#     print(f"{son3} ning ildizi {sqrt(son3)}")
# else:
#     print("Musbat son kiriting")


"""
    ==  ---> teng bo'lsa
    !=  ---> teng bo'lmasa
    >   ---> katta bo'lsa
    <   ---> kichik bo'lsa
    >=  ---> katta yoki teng bo'lsa
    <=  ---> kichik yoki teng bo'lsa
    or   ---> yoki
    and  ---> va 
"""



# ball = float(input("Choraklik ummumiy balingizni kiriting: "))

# if ball < 0 or ball > 200:
#     print("Siz noto'g'ri son kiritingiz !")

# elif ball >= 0 and ball < 120:
#     print("Siz imtihondan o'ta olmadingniz !")
    
# elif ball >= 120 and ball < 170:
#     print("Siz imtihondan o'tdingniz !")
    
# elif ball >= 170 and ball <= 200:
#     print("Siz imtihondan o'tdingniz va grant yutib oldingiz !")


""" 
1-Mashq | Foydalanuvching bahosini so'rab, uning natijasini ayting 
0 va 1 --> juda yomon
2  --> qoniqarsiz
3  --> qoniqarli
4  --> yaxshi
5  --> a'lo

Namuna: D:Bahoningni kiriting: 4
        D: Sizning natijangiz yaxshi.


2_mashq
Istalgan son kiritlsa uni musbat, manfiy yoki 0 ga teng ekanligini topib beradigan dastur tuzing
musbat 0 dan katta sonllar +
manfiy 0 dan kichik sonlar -

3-Mashq
Foydalanuvchidan imtihonda olgan balini so'rang. Agar uning bali:
0-10 ball oralig'ida bo'sa unga, “Sizning natijangiz juda yomon”;
11-20 ball oralig'ida bo'sa unga, “Sizning natijangiz qoniqarli”;
21-30 ball oralig'ida bo'sa unga, “Sizning natijangiz yaxshi”;
31-49 ball oralig'ida bo'sa unga, “Sizning natijangiz a'lo”;
Agar uning bali 50 ball bo'lsa unga “Tabriklaymiz siz 100% lik natija ko'rsatingiz”:
degan habarni konsulga chiqaring.
Shuningdek dasturga manfiy(-) va 50 dan katta sonlar kiritilganda;
“-Siz faqatgin 0-50 oralig'idagi sonlarni tanlashingiz mumkin !”, degan habar chiqsin.
"""


""" 1-mashq """
# baho = int(input("Bahoni kirit: "))

# if baho == 0 or baho == 1:
#     print("Juda yomon !")
# elif baho == 2:
#     print("Qoniqarsiz !")
# elif baho == 3:
#     print("Qoniqarli !")
# elif baho == 4:
#     print("Yaxshi !")
# elif baho == 5:
#     print("A'lo !")

"""
2_mashq
Istalgan son kiritlsa uni musbat, manfiy yoki 0 ga teng ekanligini topib beradigan dastur tuzing
musbat 0 dan katta sonllar +
manfiy 0 dan kichik sonlar -

"""

""" 2-mashq """
# son = int(input("Son kirit: "))

# if son > 0:
#     print("Musbat")
# elif son == 0:
#     print("0 ga teng !")
# elif son < 0:
#     print("Manfiy")

""" 
3-Mashq
Foydalanuvchidan imtihonda olgan balini so'rang. Agar uning bali:
0-10 ball oralig'ida bo'sa unga, “Sizning natijangiz juda yomon”;
11-20 ball oralig'ida bo'sa unga, “Sizning natijangiz qoniqarli”;
21-30 ball oralig'ida bo'sa unga, “Sizning natijangiz yaxshi”;
31-49 ball oralig'ida bo'sa unga, “Sizning natijangiz a'lo”;
Agar uning bali 50 ball bo'lsa unga “Tabriklaymiz siz 100% lik natija ko'rsatingiz”:
degan habarni konsulga chiqaring.
Shuningdek dasturga manfiy(-) va 50 dan katta sonlar kiritilganda;
“-Siz faqatgin 0-50 oralig'idagi sonlarni tanlashingiz mumkin !”, degan habar chiqsin.

"""
""" 3-mashq """
# ball = float(input("Imtihonda olgan balingizni kiriting: "))

# if ball >= 0 and ball <= 10:
#     print("Sizning natijangiz juda yomon !")
# elif ball >= 11 and ball <= 20:
#     print("Sizning natijangiz qoniqarli !")
# elif ball >= 21 and ball <= 30:
#     print("Sizning natijangiz yaxshi")
# elif ball >= 31 and ball <= 49:
#     print("Sizning natijangiz a'lo")
# elif ball == 50:
#     print("Tabriklaymiz siz 100% lik natija ko'rsatingiz")
# elif ball < 0 or ball > 50:
#     print("Siz faqatgin 0-50 oralig'idagi sonlarni tanlashingiz mumkin !")
    
    

# son1 = int(input("1-sonni kiriting: "))
# son2 = int(input("2-sonni kiriting: "))
    
# if son1 > son2:
#     print(f"{son1} > {son2}")
# elif son1 < son2:
#     print(f"{son1} < {son2}")
# # elif son1 == son2:
# #     print(f"{son1} = {son2}")
# else:
#     print(f"{son1} = {son2}")
    
    
    
""" Toq-juft """

# son = int(input("Son kiriting: "))
# if son%2 == 0: # % - sonni bir songa bo'lganda necha xona qoldiq qolishini ifodalaydi
#     print(f"{son} - juft")
# elif son%2 == 1:
#     print(f"{son} - toq")
    
    
# son = int(input("Son kiriting, men uni 5 ga bo'linish yoki bo'linmasligini topib beraman: "))
# if son%5 == 0: # % - sonni bir songa bo'lganda necha xona qoldiq qolishini ifodalaydi
#     print(f"{son} --> 5 ga qoldiqsiz bo'linadi ✅")
# else:
#     print(f"{son} --> 5 ga qoldiqsiz bo'linmaydi ❌")

    
"""  3/2/1 Ball
6-mashq | 
ismlar = ['Ali', 'Olim', 'Kamron', 'Abdulloh', 'Karim', “Usmon”]
Yuqoridagi ro'yhatdagi isimlar ichidan faqat “Kamron” va “Karim” uchun:
“Salom Karim(Kamron) ahvollaring yaxshimi ?”  degan habarni konsulga chiqaring. 
Qolgan barcha ismlar uchun esa:  “Assalomu aleykum Ali”      ko'rinishidagi habarni konsulga chiqaring.

7-mashq
Foydalanuvchidan uning ismini so'rang va unga quida keltirilgan javoblardan mosini qaytaring.
Muslima  Salom Muslima. Davramizda hush ko'rdik.
Zilola  Assalomu aleykum. Zilola sizga qanday yordam berishim mumkin?
Anvar  Salom Anvar. Bugun Qayerga boramiz ?
Qolgan barcha ismlar uchun   - Salom {ism}.
"""


""" 6-mashq """
ismlar = ['Ali', 'Olim', 'Kamron', 'Abdulloh', 'Karim', 'Usmon']

# for ism in ismlar:
#     if ism == "Kamron" or ism == "Karim":
#         print(f"Salom {ism} ahvollaring yaxshimi ?")
#     else:
#         print(f"Assalomu aleykum {ism}")

""" 7-mashq """
# ism  = input("Salom ismingiz nima: ").lower()
# if ism == "muslima":
#     print(f"Salom {ism.title()}. Davramizda hush ko'rdik")
# elif ism == "zilola":
#     print(f"{ism.title()} sizga qanday yordam berishim mumkin?")
# elif ism == "anvar":
#     print(f"Salom {ism.title()}. Bugun Qayerga boramiz ?")
# else:
#     print(f"Salom {ism.title()}")


"""  """

# sonlar = list(range(300, 900, 2))
# for son in sonlar:
#     if son > 300 and son < 400:
#         print(f"{son} ning 3-darajasi {son**3}") 
#     elif son > 400 and son < 600:
#         print(f"{son} ning 4-darajasi {son**4}") 
#     elif son > 600 and son < 900:
#         print(f"{son} ning 5-darajasi {son**5}") 


""" parol """
# password1 = input("Yangi parol kiriting: ")
# password2 = input("Parolni takrorlang: ")

# if password1 == password2:
#     if len(password1) >= 8:
#         print("Parol muvaffaqiyatli o’rnatildi !")
#     else:
#         print("Parolda eng kamida 8 ta belgi bo’lishi shart !")
# else:
#     print("Parollar bir biriga mos emas !")

"""
8-mashq 
Foydalanuvchidan 5 ta son qabul qilib olib ular ichidan musbatlarini(+):
ildizini toping;
4-darajaga ko’taring;
o’zidan 2 ta katta sonni toping;
"""

# sonlar = []
# for son in range(5):
#     sonlar.append(int(input(f"{son+1}-sonni kiriting: ")))

# for son in sonlar:
#     if son > 0:
#         print(f"{son} ning ildizi {sqrt(son)}")
#         print(f"{son} ning 4-darajasi {son**4}")
#         print(f"{son} dan 2 ta katta son {son+2}")


"""
9-mashq
Foydalanuvchiga aftobusga chiqish uchun, uning yoshini so’rab, yoshiga qarab chipta narxini chiqarib beradigan dastur tuzing.
7 yoshgacha bo’lgan bolalarga va 70 yoshdan kattalarga kirish bepul;
7 yoshdan 18 yoshgacha bo’lgan o’quvchilarga 2000 so’m
19 yoshdan 70 yoshgacha bo’lgan insonlarga 5000 so’m
Manfiy son kiritilsa, “Noto’g’ri son kiritildi” degan habar chiqsin.
"""

# yosh = int(input("Yoshingizni kiriting: "))

# if yosh < 0:
#     print("xato son")
# elif yosh >= 0 and yosh <= 7:
#      print("Sizga kirish bepul :)")
# elif yosh >= 8 and yosh <= 18:
#     print("Sizga kirish 2000 so'm")
# elif yosh >= 19 and yosh <= 70:
#     print("Sizga kirish 5000 so'm")
# elif yosh > 70:
#     print("Sizga kirish bepul :)")


"""
Kompyuter tanlagan sonni topish o‘yinini yasang. Komputer 1 dan 10 gacha bo’lgan biror sonni taxmin qilsin. 
Foydalauvchidan komputer taxmin qilgan sonni topishini so’rang. Agar foydalanuvchi kiritgan son komputer taxmin qilgan son bilan 
bir xil bo’lsa, foydalanuvchi g’olib bo’lgan bo’ladi, aks holda yutqazadi.  
Agar foydalanuvchi mag’lub bo’lsa unga komputer qaysi sonni taxmin qilganini ayting.
"""

""" Random moduli """
from random import randrange, choice

# komputer = randrange(1, 10)
# player = int(input("1 dan 10 gacha biror son tanlang: "))

# if komputer == player:
#     print(f"Siz g'olib bo'ldingiz !")
# else:
#     print(f"Siz topa olmadingiz.")
#     print(f"Komputer {komputer} sonni o'ylagan edi")



""" ✋ ✌ ✊  - tosh qaychi qog'oz """
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


