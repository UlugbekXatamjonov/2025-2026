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

# regex13 = r"^[A-Z][a-z]{2,14}$"
# ism13 = input("ism kiriting: ").title()

# if match(regex13, ism13):
#     print(f"Siz kiritildingiz {ism13}")
# else:
#     print("Xatoooo !!!!")


"""

14-mashq
Foydalanuvchidan tizimga kirish uchun faqat kichik harflar va raqamlardan iborat, 
uzunligi 4 dan 12 gacha bo'lgan login kiriting. Ushbu shartlar uchun RegEx tuzing.

15-mashq
+7 921 014-96-13 formatdagi telefon raqami uchun RegEx tuzing va match() yordamida tekshiring.
"""
""" 14-mashq """
# regex14 = r"^[a-z0-9]{4,12}$"
# savol14 = input("Login kiriting: ") 
# if match(regex14, savol14):
#     print("Login to'g'ri")
# else:
#     print("Xatoo ! Qayta urining !")


""" 15-mashq """
# regex15 = r"^[\+]7 [0-9]{3}[\s][0-9]{3}[-][0-9]{2}[-][0-9]{2}"
# savol15 = input("Tel kiriting: ") 
# if match(regex15, savol15):
#     print("Login to'g'ri")
# else:
#     print("Xatoo ! Qayta urining !")

"""
19-mashq
Matndan # belgisi bilan boshlanib, maksimal 12 ta belgigacha bo'lgan so'zlarni topib bering.
Masalan: #python_darsi
"""
# regex19= r"^[#][A-Za-z]{,11}"

"""
16-mashq
+998(90)233-25-66 formatdagi telefon raqami uchun RegEx tuzing va match() funksiyasi bilan tekshiring.

17-mashq
Quyidagi avtomobil raqami uchun RegEx tuzing va match() bilan tekshiring:
D 234 OKJ

18-mashq
Quyidagi avtomobil raqamlari uchun bitta RegEx tuzing:
50 A 117BD va 50 117ABC
"""


matn1 = " Bugun kun quyoshli va issiq bo'lyapdi. Aziz dadasining  6-2-2021 mashinasida maktabga keldi.  Mashinaning raqami 50 A327CB ed. Uning do'sti Maruf esa 40 V456AA raqamli mashinada keldi. Abduvali yangi telefon raqami oldi u +998(90) 545-50-75 edi.  Uning oldingi raqami esa +998(95) 963-12-81 edi. Oyisiniki esa +998(55) 325-65-95 bo'lgan. 12-12-2023"

regex = r"^[\+][0-9]{3}[(][0-9]{2}[)][\s][0-9]{3}[-][0-9]{2}[-][0-9]{20}$"

print(findall(regex, matn1))
print(search(regex, matn1))