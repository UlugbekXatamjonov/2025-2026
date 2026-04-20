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

# regex1 = r"^[\d]{4}$"
# savol1 = input("4 honalik raqam kiriting: ")

# if match(regex1, savol1):
#     print(f"Tog'ri ")
# else:
#     print(f"Notog'ri ")

phone = input("Telefon raqami kiriting: ")
pattern = r"^[+]998[\d]{2}$"
print(match(pattern, phone))

""" +998(99) 325-74-74 """
















