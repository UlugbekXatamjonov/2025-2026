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
car1 = r"^[0-9]{2}[\s][A-Z]{1}[\s][0-9]{3}[\s][A-Z]{2}$"
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

# ism = input("Ism: ")
# pattern13 = r"^[A-Za-z]{3,15}$"
# print(match(pattern13, ism))
# print(len(ism))


"""
14-mashq
Foydalanuvchidan tizimga kirish uchun faqat kichik harflar va raqamlardan iborat, 
uzunligi 4 dan 12 gacha bo'lgan login kiriting. Ushbu shartlar uchun RegEx tuzing.

15-mashq
+7 921 014-96-13 formatdagi telefon raqami uchun RegEx tuzing va match() yordamida tekshiring.
"""

# regex14 = r"^[a-z0-9]{4,12}$"
# regex15 = r"^[+]7[ ][0-9]{3}[ ][0-9]{3}[-][0-9]{2}[-][0-9]{2}$"


""" ---- findall() ---- """

pattern3 = r"[+][0-9]{3}[(][0-9]{2}[)][ ][0-9]{3}[-][0-9]{2}[-][0-9]{2}"
car1 = r"[0-9]{2}[\s][A-Z]{1}[\s][0-9]{3}[\s][A-Z]{2}"

matn = "Salom 444 98 Salima do'stimm python 50 A 117 AD Uyqichining Saida 235 telefon ython 50 A 117 AD raqami +998(96) 333-22-11 50 A 117 AD  va +998(96) \
555-88-5 meniki 11 esa pytho Sasha +998(66) 998-66-33"

# print(findall(pattern3, matn))
# print(findall(car1, matn))


"""
3-mashq
Berilgan matndan 3 xonali raqamlarni toping.

4-mashq
Matndan faqat 5 xonagacha bo'lgan sonlarni ajratib oling.
"""

matn3="4444 333 22 1 55555"
pattern5  = r"[ ][0-9]{3}[ ]"
# print(findall(pattern5, matn3))


""" ---- search() ---- """

"""
1-mashq
Berilgan matnda raqam mavjud yoki yo'qligini search() metodi yordamida tekshiring.

2-mashq
Berilgan matnda "python" so'zi bor-yo'qligini search() metodi orqali aniqlang.
"""
""" 1-mashq """
regex1 = r"[0-9]{1,10}"
# print(search(regex1, matn))
# print(findall(regex1, matn))

""" 2-mashq """
regex2 = r"python"
# print(search(regex2, matn))


""" if-else bilan """
# if findall(regex2, matn):
#     print("Matnda  python so'zi bor")
# else:
#     print("yo'q")

"""
5-mashq
Matndan faqat 7 ta harfdan iborat so'zlarni ajratib oling.

6-mashq
Berilgan matndan “S” harfi bilan boshlanib “a” harfi bilan tugaydigan ismlarni toping.
"""

""" 5 """
pattern5 = r" [\w]{7} "
# print(search(pattern5, matn))

""" 6 """
pattern6 = r" S[\w]{0,15}a "
# print(search(pattern6, matn))
# print(findall(pattern6, matn))


"""
7-mashq
Berilgan matndan barcha email manzillarini toping.
Namuna: olimova@gmail.com

8-mashq
Berilgan matndan @username ko'rinishidagi barcha foydalanuvchi nomlarini findall() metodi yordamida toping.

9-mashq
Berilgan matndan barcha telefon raqamlarini toping. Telefon raqami formati: +998-xx-xxx-xx-xx
"""


matn = "Salom 444 98 Salima 22-10-2026 +998-12-122-44-44  do'stimm python 50 A 117 AD Uyqichining +998-12-122-55-55 Saida 235 telefon ython  22-10-2026 50 A 117 AD \
raqami +998(96) 333-22-11 50 A 117 AD  va +998(96) \
555-88-5 meniki 11 esa pytho Sasha +998(66) 998-66-33 salom@gmail.com s@gmail.com  @asaa +998-12-122-12-12 "

""" 7 """
# gmail = r"[a-z]{1,15}@[a-z]{1,10}[.][a-z]{2,3}"
# print(findall(gmail,matn))

""" 8 """
# gmail1 = r'[ ]@[a-zA-Z0-9_-]{1,15}[ ]'
# print(findall(gmail1,matn))

""" 9 """
phonenumber = r'[+]998[-][0-9]{2}[-][0-9]{3}[-][0-9]{2}[-][0-9]{2}'
print(search(phonenumber,matn))
print(findall(phonenumber,matn))


""" 
10-mashq
Biror matn olib, undan dd-mm-yyyy formatidagi barcha sanalarni toping.
"""
regex10 = r" [0-9]{2}[-][0-9]{2}[-][0-9]{4} "
# regex10 = r"&dd-&m-&y"
# print(findall(regex10,matn))


"""
11-mashq
Biror matndan email mavjud yoki yo'qligini search() yordamida tekshiring.
Email uchun RegEx ni ihateregex.io saytidan oling.

12-mashq. Berilgan matnda passport seriyasi bor-yo'qligini aniqlang.
Namuna: Passport: AC1236547
"""


