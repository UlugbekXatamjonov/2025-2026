"""  """

# son = int(input("Biror son kiriting: "))
# if son > 0:
#     print(f"{son} musbat")
# else:
#     print(f"{son} manfiy")
    

# savol = input("Siz olma yeyishni yoqtirasizmi: ").lower()
# if savol == "ha" or savol == 'albatta' or savol == 'shunday': # == 
#     print("Juda soz, chunki olma foydali")
# else:
#     print("Asus, men sizga olma yeyishni tafsiya qilaman !")


""" elif """
# son1 = int(input("1-sonni kiriting: "))
# son2 = int(input("2-sonni kiriting: "))

# if son1 > son2:
#     print(f"{son1} > {son2}")
# elif son1 < son2: 
#     print(f"{son1} < {son2}")
# elif son1 == son2: 
#     print(f"{son1} = {son2}")
# else:
#     print(f"{son1} = {son2}")




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

# ball = int(input("Imtihonda necha ball oldingiz: "))

# if ball >= 0 and ball <= 10:
#     print("Sizning natijangiz juda yomon") 
# elif 11 <= ball <= 20:
#     print("Sizning natijangiz qoniqarli") 
# elif 21 <= ball <= 30:
#     print("Sizning natijangiz yaxshi") 
# elif 31 <= ball <= 49:
#     print("Sizning natijangiz a'lo") 
# elif ball == 50:
#     print("Tabriklaymiz siz 100% lik natija ko'rsatingiz") 
# else:
#     print("Siz faqatgin 0-50 oralig'idagi sonlarni tanlashingiz mumkin !")


"""
8-mashq
ismlar = ['Ali', 'Olim', 'Kamron', 'Abdulloh', 'Karim', 'Usmon']
Faqat Kamron va Karim uchun: → “Salom Karim(Kamron), ahvollaring yaxshimi?”
Qolganlar uchun: → “Assalomu aleykum Ali(Olim...)”


9-mashq
1 dan 500 gacha juft sonlar ro'yxatini yarating:
    - 1-50 → 2-daraja
    - 100-200 → ildizi
    - 300-400 → 5-daraja
"""

# ismlar = ['Ali', 'Olim', 'Kamron', 'Abdulloh', 'Karim', 'Usmon']
# for ism in ismlar:
#     if ism == "Kamron" or ism == "Karim":
#         print(f"Salom {ism}, ahvollaring yaxshimi?")
#     else:
#         print(f"Assalomu aleykum {ism}")
    
# sonlar = list(range(2, 500, 2))
# from math import sqrt

# for son in sonlar:
#     if 1< son < 50:
#         print(f"{son} ning 2-darajasi {son**2}")    
#     elif 100 < son < 200:
#         print(f"{son} ning ildizi {sqrt(son)}")    
#     elif 300 < son < 400:
#         print(f"{son} ning 5-darajasi  {son ** 5}")    





