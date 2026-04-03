"""
link -> https://docs.python.org/3/howto/regex.html
link -> https://docs.python.org/3/library/re.html
link -> https://www.w3schools.com/python/python_regex.asp

RegEx funksiyalari
match()     -   Solishtirish uchun  
findall()   -   Barcha mosliklarni o'z ichiga olgan ro'yxatni qaytaradi
search()    -   Agar satrning istalgan joyida moslik mavjud bo'lsa, Match ob'ektini qaytaradi

\w - So'z belgilari -->  a-z / A-Z 
\d - Raqam  --> 0-9
\b - So'z chegarasi --> $
\s - bo'shliq 
^  - boshlanish
? - ixtiyoriylik
"""

from re import match, findall, search
""" match """
regex = r"^[\+][0-9]{3}[(][0-9]{2}[)][\s][0-9]{3}[-][0-9]{2}[-][0-9]{2}$"
# raqam = input("Raqam kiriting: ")

#1-usul
# print(match(regex, input("Raqam kiriting: ")))

#2-usul
# if match(regex, raqam):
#     print("Siz to'g'ri ma'lumot kiritdingiz !")
# else:
#     print("Siz xato ma'lumot kiritdingiz !!!")

""" +998(93) 261-92-00 """  

"""
13-mashq
Foydalanuvchidan ismini so'rang. Ism faqat harflardan iborat va uzunligi 3 dan 15 gacha bo'lishi kerak. 
Uni match() yordamida tekshiring.
"""

regex13 = r"^[A-Z][a-z]{2,14}$"
ism13 = input("ism kiriting: ").title()

if match(regex13, ism13):
    print(f"Siz kiritildingiz {ism13}")
else:
    print("Xatoooo !!!!")
    