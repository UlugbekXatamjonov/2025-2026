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

# phone = input("Telefon raqami kiriting: ")
# pattern = r"^[+]998[\d]{2}$"
# print(match(pattern, phone))

""" +998(99) 325-74-74 """

# regex = r"^[+]998[(][0-9]{2}[)][\s][0-9]{3}[-][0-9]{2}[-][0-9]{2}$"



regex14 = r"^[a-z0-9]{4,12}$"
regex15 = r"^[+]7 [0-9]{3} [0-9]{3}[-][0-9]{2}[-][0-9]{2}$"
regex16 = r"^[+]998[(][0-9]{2}[)][0-9]{3}[-][0-9]{2}[-][0-9]{2}$"
regex17 = r"^[A-Z] [0-9]{3} [A-Z]{3}$"
regex18_1 = r"^[0-9]{2} [A-Z] [0-9]{3}[A-Z]{2}$"
regex18_2 = r"^[0-9]{2} [0-9]{3}[A-Z]{3}$"
regex19 = r"^[#][a-z_-0-9]{1,12}$"



matn1 = """
    Bugun kun quyoshli va issiq bo'lyapdi. Aziz dadasining  6-2-2021 mashinasida +998(90) 545-5075 maktabga keldi. 
    Mashinaning raqami 50 A327CB ed. Uning do'sti Maruf esa 40 V456AA raqamli mashinada keldi.
    Abduvali yangi telefon raqami oldi u +998(90) 545-50-75 edi.  Uning oldingi raqami esa 
    +998(95) 963-12-81 edi. Oyisiniki esa +998(55) 325-65-95 bo'lgan. 12-12-2023
"""

regexx = r"[+]998[(][0-9]{2}[)] [0-9]{3}[-][0-9]{2}[-][0-9]{2}"
print(findall(regexx, matn1))
print(search(regexx, matn1))





