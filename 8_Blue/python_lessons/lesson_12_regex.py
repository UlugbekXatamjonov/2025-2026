
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

# word = input("sO'Z KIRITING: ")
regex1 = r"^[\w]{4}\b"

# print(match(regex1, word))

"""50 T 445 BB"""
# car_number = input("Car number: ")
car_regex = r"^[0-9]{2}[\s][A-Z] [\d]{3} ?[A-Z]{2}$"
# print(match(car_regex, car_number))


""" 16-mashq
+998(90)233-25-66 formatdagi telefon raqami uchun RegEx tuzing va match() funksiyasi bilan tekshiring.
"""
phone_regex = r"^[+]998[(][0-9]{2}[)][0-9]{3}[-][0-9]{2}[-][0-9]{2}$"















