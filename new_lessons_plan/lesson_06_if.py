"""
if-esle-elif operatorlari
"""

""" < va > """
# son = int(input("Son kiriting: "))

# if son > 0:
#     print(f"{son} musbat")
# else:
#     print(f"{son} manfiy")
    

""" == """
# savol = input("Siz olma yeganmisiz: ").lower()

# if savol == "ha":
#     print(f"Menga qani ?")
# else:
#     print(f"Olma yeyishni tafsiya qilaman !")


""" != """
# savol = input("Siz olma yeganmisiz: ").lower()

# if savol != "ha":
#     print(f"Olma yeyishni tafsiya qilaman !")
# else:
#     print(f"Menga qani ?")


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


""" choraklik imtihon """
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


"""4-mashq"""
# son = int(input("Son kirit: "))

# if son > 0:
#     print("Musbat")
# elif son == 0:
#     print("0 ga teng !")
# elif son < 0:
#     print("Manfiy")


""" 
5-Mashq
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
    
    

""" Katta kichik """ 
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
    


""" Bir songa bo'linishlik """
# son = int(input("Son kiriting, men uni 5 ga bo'linish yoki bo'linmasligini topib beraman: "))
# if son%5 == 0: # % - sonni bir songa bo'lganda necha xona qoldiq qolishini ifodalaydi
#     print(f"{son} --> 5 ga qoldiqsiz bo'linadi ✅")
# else:
#     print(f"{son} --> 5 ga qoldiqsiz bo'linmaydi ❌")



""" parol """
# password1 = input("Yangi parol kiriting: ")
# password2 = input("Parolni takrorlang: ")

# if password1 == password2:
#     if len(password1) >= 8:
#         print("Parol muvaffaqiyatli o'rnatildi !")
#     else:
#         print("Parolda eng kamida 8 ta belgi bo'lishi shart !")
# else:
#     print("Parollar bir biriga mos emas !")



"""
Kompyuter tanlagan sonni topish o'yinini yasang. Komputer 1 dan 10 gacha bo'lgan biror sonni taxmin qilsin. 
Foydalauvchidan komputer taxmin qilgan sonni topishini so'rang. Agar foydalanuvchi kiritgan son komputer taxmin qilgan son bilan 
bir xil bo'lsa, foydalanuvchi g'olib bo'lgan bo'ladi, aks holda yutqazadi.  
Agar foydalanuvchi mag'lub bo'lsa unga komputer qaysi sonni taxmin qilganini ayting.
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





""" Mashqlar """
"""
1-mashq
Foydalanuvchidan son kiritilishini so'rang. Agar u musbat(+) bo'lsa — sonning ildizini toping. Aks holda sonning kvadratini hisoblang.

2-mashq
Foydalanuvchidan 2 ta son kiritishini so'rab, qaysi biri katta, qaysi biri kichik yoki tengligini aniqlang.

3-mashq
Quyidagi kodni xatolarini tuzating:

a = float(input("1-sonni kirirting:"))
b = int(input("2-sonni kirirting:"))
if a<b:
    print(f"{a}>{b}")
elif a<b:
    print(f"{a}<{b}")
elif a == a :
    print(f"{a}={b}")

4-mashq
Foydalanuvchidan uning ismini so'rang va mos javob qaytaring:
Muslima → “Salom Muslima. Davramizda hush ko'rdik.”
Zilola → “Assalomu aleykum. Zilola sizga qanday yordam berishim mumkin?”
Anvar → “Salom Anvar. Bugun qayerga boramiz?”
Qolganlar → “Salom {ism}.”

5-mashq
Foydalanuvchidan uning ismini so'rang:
Azizbek and Anvar bo'lsa — “Salom Azizbek/Anvar. Ishlaring yaxshimi?”
Hadicha and Muslima bo'lsa — “Hayrli kun Hadicha/Muslima.”
(“or” operatori shart.)

6-mashq
Foydalanuvchidan o'tgan haftadagi imtihon ballini so'rang:
Agar 160 dan ko'p bo'lsa — “Bu juda yaxshi natija.”
Aks holda — “Keyingi safar bundanda yaxshiroq natija olishga harakat qiling.”

7-mashq
Foydalanuvchidan yoshini so'rang va quyidagiga mos xabar chiqaring:
0-6 → “Siz bog'cha yoshidasiz”
7-18 → “Siz maktab yoshidasiz”
19-30 → “Siz talaba yoshidasiz”
31-69 → “Siz ishlash yoshidasiz”
70+ → “Siz nafaqa yoshidasiz”
0 dan kichik → “Iltimos musbat son kiriting”

8-mashq
ismlar = ['Ali', 'Olim', 'Kamron', 'Abdulloh', 'Karim', 'Usmon']
Faqat Kamron va Karim uchun: → “Salom Karim(Kamron), ahvollaring yaxshimi?”
Qolganlar uchun: → “Assalomu aleykum Ali(Olim...)”


9-mashq
1 dan 500 gacha juft sonlar ro'yxatini yarating:
    - 1-50 → 2-daraja
    - 100-200 → ildizi
    - 300-400 → 5-daraja
    
10-mashq
Foydalanuvchidan ism so'rang:
Ahmad or Abror → “Bugun nega darsga kelmading Ahmad/Abror?”
Mehribon or Maftuna → “Mehribon/Maftuna ertaga darsdan keyin qayerga boramiz?”
Muhammadqodir → “Muhammadqodir nega vazifani vaqtida bajarmading?”

11-mashq
Foydalanuvchidan ism so'rang:
Muhammad or Saidbek — “Bugun nega darsga kelmading Muhammad/Saidbek?”
Mehridil or Hadicha — “Mehridil/Hadicha ertaga qayerga boramiz?”
Nodirbek — “Nodirbek nega vazifani vaqtida bajarmading?”

12-mashq
Foydalanuvchidan 5 ta son qabul qiling. Ular ichidan musbat bo'lganlari uchun:
    - ildizini toping
    - 4-darajaga ko'tarib bering
    - o'zidan 2 ta katta sonni toping

13-mashq
ismlar = ["HUSNIDA", "UMARBEK", "LAYLO", "UMIDA", "DILSHODA", "ZINNATOY", "JO'RABEK"]
Ro'yxatdan ikki o'g'il bola ismini birinchi harfini katta qilib;
qolgan barcha ismlarni kichik harflarda chiqaring.

14-mashq
smlar = ["Abror", "Dilmurod", "Nafisa", "Nafosat", "Bobur", "Davron"]
Qizlar ismlarini — barcha harflarini katta,
O'g'il bolalar ismlarini — barcha harflarini kichik qiling.

15-mashq
Sonlar = [34, -9, 0, 83, -12, 4.6, 9, 36, 9.3, 77, 17, -14, 100, -241]
    - Musbat sonlar → ildizi
    - Manfiy sonlar → 5-darajaga ko'tarilsin

16-mashq
mevalar = ["olma", "gilos", "oshqovoq", "sabzi", "anjir", "malina"]
Ro'yxatdagi ikki sabzavot nomini barcha harflarini katta qiling;
qolgan mevalarning nomini birinchi harfini katta qiling.
(“or” operatori ishlatilishi shart.)

17-mashq
300 dan 900 gacha juft sonlar ro'yxatini yarating:
    - 400 gacha → 3-daraja
    - 600 gacha → 4-daraja
    - 900 gacha → 5-daraja

18-mashq
300 dan 900 gacha toq sonlar ro'yxatini yarating:
    - 300-400 → kvadrati
    - 500-600 → ildizi
    - 700-800 → 4-darajasi

19-mashq (eng murakkab)
Foydalanuvchidan avval parol, keyin parolni tasdiqlashni so'rang:
Agar parollar bir-biriga mos va 8 ta belgidan uzun bo'lsa → “Parol o'rnatildi”
Parollar mos kelmasa → “Parollar mos emas”
Parol uzunligi < 8 bo'lsa → “Parolda kamida 8 belgi bo'lishi shart”

"""









