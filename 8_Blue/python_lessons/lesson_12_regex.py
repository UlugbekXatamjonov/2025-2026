
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


regex14 = r"^[a-z0-9]{4,12}$"
regex15 = r"^[+]7 [0-9]{3} [0-9]{3}[-][0-9]{2}[-][0-9]{2}$"
regex16 = r"^[+]998[(][0-9]{2}[)][0-9]{3}[-][0-9]{2}[-][0-9]{2}$"
regex17 = r"^[A-Z] [0-9]{3} [A-Z]{3}$"
regex18_1 = r"^[0-9]{2} [A-Z] [0-9]{3}[A-Z]{2}$"
regex18_2 = r"^[0-9]{2} [0-9]{3}[A-Z]{3}$"
regex19 = r"^[#][a-z_-0-9]{1,12}$"

regex14 = r"^$"



matn1 = """
    Bugun kun quyoshli va issiq bo'lyapdi. Aziz dadasining  6-2-2021 mashinasida maktabga keldi. 
    Mashinaning raqami Ahror 50 A327CB ed. Uning do'sti Maruf esa 40 V456AA raqamli mashinada keldi.
    Abduvali yangi telefon raqami oldi u +998(90) 545-50-75 edi. Anvar  Uning oldingi raqami esa 
    +998(95) 963-12-81 edi. Oyisiniki esa +998(55) 325-65-95 bo'lgan. 12-12-2023
"""


""" finall() """
phone2_pattern = r"[+]998[(][0-9]{2}[)] [0-9]{3}-[0-9]{2}-[0-9]{2}"
a_name = r"A[a-zA-Z]{3,10}"
print(findall(a_name, matn1))


""" search() - """
# sana = r"[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}"
# print(search(phone2_pattern, matn1))









