""" if-else """

# son = int(input("Son kiriting: "))

# if son > 0:
#     print(f"{son} musbat")
# else:
#     print(f"{son} manfiy")
    


# savol = input("Siz behini yaxshi ko'rasizmi: ").lower()

# if savol == "ha":
#     print("Siz to'g'ri tanlov qilgansiz !")
# else:
#     print("Behi juda foydali. Men sizga uniu istemol qilishni tafsiya beraman.")


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

""" != """
# savol = input("Siz olma yeganmisiz: ").lower()

# if savol != "ha":
#     print(f"Olma yeyishni tafsiya qilaman !")
# else:
#     print(f"Menga qani ?")

"""
1-mashq 

Foydalanuvchidan son kiritishini so'rang. Agar son musbat(+) bo'lsa uning ildizni toping.
Agar son manfiy bo'lsa unda uning 4-darajasini toping.
"""
# from math import sqrt
# son = int(input("Son kiriting: "))
# if son > 0:
#     print(f"Siz kiritkan sonning ildizi {sqrt(son)}")
# else:
#     print(f"Siz kiritkan sonning 4-chi darajasi {son**4}")


"""
2-mashq 

Foydalanuvchidan uning o'tgan haftalik imtihondan to'plagan ballini so'rang. Agar u 160 balldan ko'p ball to'plagan bo'lsa unga “Bu juda yaxshi natija” degan habarni aks holda, “Keyingi safar bundanda yaxshiroq natijani qo'lga kiritishga harakat qiling” degan habar chiqsin.
"""
# ball = float(input("balingizni kiriting: "))

# if ball >= 160: 
#     print("“Bu juda yaxshi natija")
# else:
#     print("Keyingi safar bundanda yaxshiroq natijani qo'lga kiritishga harakat qiling")



"""
Foydalanuvchidan uning ismini so'rang. Agar uning ismi “Ahmad” bo'lsa, “Salom Ahmad ishlaring yaxshimi ?” degan habar, aks holda “Kechirasiz biz faqat Ahmadni kutyapmiz” degan habarni chiqaring.
"""

# ism = input("Ismingizni kiriting: ").lower()
# if ism  == "ahmad":
#     print("Salom Ahmad ishlaring yaxshimin ?")
# else:
#     print("Kechirasiz biz faqat Ahmadni kutyapmiz.")



# son1 = int(input("1-sonni kiriting: "))
# son2 = int(input("2-sonni kiriting: "))

# if son1 > son2:
#     print(f"{son1} > {son2}")
    
# elif son1 < son2:
#     print(f"{son1} < {son2}")
    
# elif son1 == son2:
#     print(f"{son1} = {son2}")
    
# else:
#     print(f"{son1} va {son2} teng")


"""
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
(“and” operatori shart.)
"""

""" 3-mashq """
# a = int(input("1-sonni kirirting:"))
# b = int(input("2-sonni kirirting:"))
# if a>b:
#     print(f"{a}>{b}")
# elif a<b:
#     print(f"{a}<{b}")
# elif a == b :
#     print(f"{a}={b}")


""" 4-mashq """
# ism = input("Ismningizni kiriting: ").lower()
# if ism == "muslima":
#     print("Salom Muslima. Davramizda hush ko'rdik.")
# elif ism == "zilola":
#     print("Assalomu aleykum. Zilola sizga qanday yordam berishim mumkin?")
# elif ism == 'anvar':
#     print("Salom Anvar. Bugun qayerga boramiz?")
# else:
#     print(f"Salom {ism}")


""" 
5-mashq
Foydalanuvchidan uning ismini so'rang:
Azizbek and Anvar bo'lsa — “Salom Azizbek/Anvar. Ishlaring yaxshimi?”
Hadicha and Muslima bo'lsa — “Hayrli kun Hadicha/Muslima.”
(“and” operatori shart.)
"""


""" or """
# ism = input("ismingizni kiriting: ").lower()

# if ism == "azizbek" or ism == "anvar": # or - yoki   | Anvar yoki Azizbek uchun
#     print(f"Salom {ism.title()}. Ishlaring yaxshimi?")
  
# elif ism == "hadicha" or ism == "muslima":
#     print(f"Hayrli kun {ism.title()}")


"""
11-mashq
Foydalanuvchidan ism so'rang:
Muhammad or Saidbek — “Bugun nega darsga kelmading Muhammad/Saidbek?”
Mehridil or Hadicha — “Mehridil/Hadicha ertaga qayerga boramiz?”
Nodirbek — “Nodirbek nega vazifani vaqtida bajarmading?”
"""

"""
13-mashq
ismlar = ["HUSNIDA", "UMARBEK", "LAYLO", "UMIDA", "DILSHODA", "ZINNATOY", "JO'RABEK"]
Ro'yxatdan ikki o'g'il bola ismini birinchi harfini katta qilib;
qolgan barcha ismlarni kichik harflarda chiqaring.

14-mashq
ismlar = ["Abror", "Dilmurod", "Nafisa", "Nafosat", "Bobur", "Davron"]
Qizlar ismlarini — barcha harflarini katta,
O'g'il bolalar ismlarini — barcha harflarini kichik qiling.
"""

""" 13-mashq """

# ism_lar = ["HUSNIDA", "UMARBEK", "LAYLO", "UMIDA", "DILSHODA", "ZINNATOY", "JO'RABEK"]
# for ism in ism_lar:
#     if ism == "UMARBEK" or ism == "JO'RABEK":
#        print(f"{ism.capitalize()}")
#     else:
#         print(f"{ism.lower()}") 


""" 14-mashq """

# ism_lar = ["Abror", "Dilmurod", "Nafisa", "Nafosat", "Bobur", "Davron"]

# for ism in ism_lar:
#     if ism == "Abror" or ism == "Dilmurod" or ism == "Bobur" or ism == "Davron":
#         print(f"{ism.lower()}")
#     elif ism == "Nafisa" or ism == "Nafosat":
#         print(f"{ism.upper()}")


# for ism in ism_lar:
#     if ism == "Nafisa" or ism == "Nafosat":
#         print(f"{ism.upper()}")
#     else:
#         print(f"{ism.lower()}")


"""
15-mashq
Sonlar = [34, -9, 0, 83, -12, 4.6, 9, 36, 9.3, 77, 17, -14, 100, -241]
    - Musbat sonlar → ildizi
    - Manfiy sonlar → 5-darajaga ko'tarilsin
"""


"""
16-mashq
mevalar = ["olma", "gilos", "oshqovoq", "sabzi", "anjir", "malina"]
Ro'yxatdagi ikki sabzavot nomini barcha harflarini katta qiling;
qolgan mevalarning nomini birinchi harfini katta qiling.
(“or” operatori ishlatilishi shart.)
"""

from math import sqrt

# sonlar = [34, -9, 0, 83, -12, 4.6, 9, 36, 9.3, 77, 17, -14, 100, -241]

# for son in sonlar:
#     if son > 0:
#         print(f"{son} musbat va uning ildizi {sqrt(son)}")
#     else:
#         print(f"{son} manfiy va uning 5-darajasi {son**5}")
        
    
# mevalar = ["olma", "gilos", "oshqovoq", "sabzi", "anjir", "malina"]
# for meva in mevalar:
#     if meva == "oshqovoq" or meva == "sabzi":  
#         print(meva.upper())
#     else:
#         print(meva.capitalize())    
        
        


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

# ball = float(input("Imtihon balingizni kiriting: "))

# if ball >= 0 and ball <= 10:
#     print("Sizning natijangiz juda yomon")
# elif ball >= 11 and ball <= 20:
#     print("Sizning natijangiz qoniqarli")
# elif ball >= 21 and ball <= 30:
#     print("Sizning natijangiz yaxshi")
# elif ball >= 31 and ball <= 49:
#     print("Sizning natijangiz a'lo")
# elif ball == 50:
#     print("Tabriklaymiz siz 100% lik natija ko'rsatingiz")
# else:
#     print("Siz faqatgin 0-50 oralig'idagi sonlarni tanlashingiz mumkin !")



""" Toq juft """
# son = int(input("Son kiriting: "))

# if son%2 == 0: # % --> sonni bo'lganda necha xona qoldiq qolishini o'lchaydi
#     print(f"{son} juft")
# else:
#     print(f"{son} toq")


# if son%5 == 0: # % --> sonni bo'lganda necha xona qoldiq qolishini o'lchaydi
#     print(f"{son} 5 ga qoldiqsiz bo'linadi ✅") # windows + .
# else:
#     print(f"{son} 5 ga qoldiqsiz bo'linmaydi ❌")

"""
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
"""
    
    
""" 17-dars """ 

# sonlar = list(range(300, 900, 2))
# for son in sonlar:
#     if son < 400:
#         print(f"{son} ning 3-darajasi {son**3}")
#     elif son < 600:
#         print(f"{son} ning 4-darajasi {son**4}")
#     elif son < 900:
#         print(f"{son} ning 5-darajasi {son**5}")
    

# sonlar2 = list(range(301, 900, 2)) 
# for son in sonlar2:
#     if son >= 300 and son < 400:
#         print(f"{son} ning 2-darajasi {son**2}")
#     elif son >= 500 and son < 600:
#         print(f"{son} ning ildizi {sqrt(son)}")
#     elif son >= 700 and son < 800:
#         print(f"{son} ning 4-drajasi {son**4}")
    
    
    
    
"""
1-mashq
Foydalanuvchidan uning eng yaxshi ko'rgan 5 ta raqamini so'rab bir ro'yhatga qo'shing va:
    ro'yhatdagi eng katta sonni;
    ro'yhatdagi eng kichik sonni;
    ro'yhatdagi barcha sonlarning yig'indisini toping;
    ro'yhatdagi barcha sonlarning o'rta arifmetigini;

2-mashq
200 dan 600 gacha toq sonli ro'yhat yarating. Va ro'yhatdagi:
200 dan 300 gacha bo'lgan sonlarning 3-darajasini toping;
400 dan 450 gacha bo'lgan sonlarning ildizni toping;
500 dan 600 gacha bo'lgan sonlarning 5-darajasini toping.
"""


""" random """
from random import randrange, choice, choices

# komputer = randrange(1, 5) # 1 dan 5 gacha ixtiyoriy biro sonni tanlab beradi
# print("Komputer tanlagan sonni taxmin qiling !")
# player = int(input("Biror sonni kiriting: "))

# if komputer == player:
#     print("Siz yutdingiz ✅")
# else:
#     print("Siz yutqazdiz ❌👎")
# print(f"Komputer {komputer} sonini  o'ylagan edi")


""" Tosh, qaychi, qog'oz """

tqq = ["tosh", 'qaychi', "qogoz"]
komputer = choice(tqq)
player = input("Tosh-qaychi-qogoz: ").lower()

if player in tqq:
    if komputer == player:
        print("Durrang 🤝")
    elif komputer == 'tosh' and  player == "qaychi":
        print(f"Siz yutqazdingiz ❌")
    elif komputer == 'qaychi' and  player == "qogoz":
        print(f"Siz yutqazdingiz ❌")
    elif komputer == 'qogoz' and  player == "tosh":
        print(f"Siz yutqazdingiz ❌")
    else:
        print("Siz yutdingiz ✅")
    
    print(f"🤖 Komputer \"{komputer}\" ni tanlagan edi")
else:
    print("Siz noto'g'ri tanlov qildingiz ❗❗❗")



students = [ "Mamadaliyev Abdurashid", "Mirsaydullayev Mirziyo", "Sobirov Muhammadqodir", "Tursunboyev Boburjon", "Tursunboyeva Saida", "Umaraliyev Isroil", "Osimjonov Dilmurod", "Shuxratova Ruxsora", "Shuxratov Abrorbek", "Arabbayev Muhammadyusuf", "Mashrabxanova Oyshaxon", "Mirjalolov Saidakbar", "Imamova Nigora",  "Abdurahimova Nodira",  "Turg'unova Sabina", "Yahyayev Muhammadali", "Saidjalolov Shoxjahon", "Mamadov Abubakr"]


print("O'tgan mavzuni aytib berish uchun biror o'quvchini tanlab beradigan dastur")
print(f"Doskaga {choices(students)} chiqadi 👏")











    