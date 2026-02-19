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

# raqam = input("son kiritring: ")
# patern = r'^[\d]{5}$'

# print(match(patern, raqam))

# phone = input("Telefon raqami kiriting: ")
# pattern = r"^[+]998[0-9]{2}[-][\d]{3}[-][0-9]{2}[-]?[0-9]{2}$"
# print(match(pattern, phone))


""" 50 A 117 AD  | 50 030 XAA"""
# car1 = r"^[0-9]{2}[\s][A-Z]{1}[\s][0-9]{3}[\s][A-Z]{2}$"
# savol1 = input("Mashina raqamini kiring: ")
# print(match(car1, savol1))

# car2 = r"^[0-9]{2}[ ][0-9]{3}[ ][A-Z]{3}$"
# savol2 = input("Mashina raqamini kiring: ")
# print(match(car2, savol2))

"""
13-mashq
Foydalanuvchidan ismini so'rang. Ism faqat harflardan iborat va uzunligi 3 dan 15 gacha bo'lishi kerak. 
Uni match() yordamida tekshiring.
"""

ism = input("Ism: ")
pattern13 = r"^[A-Za-z]{3,15}$"
print(match(pattern13, ism))
print(len(ism))


"""

14-mashq
Foydalanuvchidan tizimga kirish uchun faqat kichik harflar va raqamlardan iborat, 
uzunligi 4 dan 12 gacha bo'lgan login kiriting. Ushbu shartlar uchun RegEx tuzing.

15-mashq
+7 921 014-96-13 formatdagi telefon raqami uchun RegEx tuzing va match() yordamida tekshiring.
"""



