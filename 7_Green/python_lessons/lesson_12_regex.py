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
regex = r"^[+][0-9]{12}$"
raqam = input("Raqam kiriting: ")

#1-usul
# print(match(regex, input("Raqam kiriting: ")))

#2-usul
if match(regex, raqam):
    print("Siz to'g'ri ma'lumot kiritdingiz !")
else:
    print("Siz xato ma'lumot kiritdingiz !!!")


""" +998(93) 261-92-00 """  

