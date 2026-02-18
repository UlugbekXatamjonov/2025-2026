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

phone = input("Telefon raqami kiriting: ")
pattern = r"^[+]998[0-9]{2}[-][\d]{3}[-][0-9]{2}[-]?[0-9]{2}$"
print(match(pattern, phone))
