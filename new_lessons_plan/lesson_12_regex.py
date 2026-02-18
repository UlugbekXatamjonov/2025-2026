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

# phone = input("Telefon raqami kiriting: ")
# pattern = r"^[+]998[\d]{9}$"
# print(match(pattern, phone))


# car_number = input("Car number: ")
# car_pattern = r"^[A-Z]{2}[\s][0-9]{4}[A-Z]{2}$"
# print(match(car_pattern, car_number))


# word = input("Enter a word: ")
# word_regex = r"^[a-z]{3,8}$"
# print(match(word_regex, word))

# if match(word_regex, word):
#     print(f"Siz tog'ri so'z kiritdingiz. U: {word}")
# else:
#     print(f"Siz notog'ri so'z kiritdingiz 🔴")
    

matn1 = """
    Bugun kun quyoshli va issiq bo'lyapdi. Aziz dadasining  6-2-2021 mashinasida maktabga keldi. 
    Mashinaning raqami 50 A327CB ed. Uning do'sti Maruf esa 40 V456AA raqamli mashinada keldi.
    Abduvali yangi telefon raqami oldi u +998(90) 545-50-75 edi.  Uning oldingi raqami esa 
    +998(95) 963-12-81 edi. Oyisiniki esa +998(55) 325-65-95 bo'lgan. 12-12-2023
"""


""" finall() """
# phone2_pattern = r"[+]998[(][0-9]{2}[)] [0-9]{3}-[0-9]{2}-[0-9]{2}"
# a_name = r"A[a-zA-Z]{3,10}"
# print(findall(phone2_pattern, matn1))


""" search() - """
# sana = r"[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}"
# print(search(sana, matn1))



"""  Mashqlar

1-mashq
Berilgan matnda raqam mavjud yoki yo'qligini search() metodi yordamida tekshiring.

2-mashq
Berilgan matnda "python" so'zi bor-yo'qligini search() metodi orqali aniqlang.

3-mashq
Berilgan matndan 3 xonali raqamlarni toping.

4-mashq
Matndan faqat 5 xonagacha bo'lgan sonlarni ajratib oling.

5-mashq
Matndan faqat 7 ta harfdan iborat so'zlarni ajratib oling.

6-mashq
Berilgan matndan “S” harfi bilan boshlanib “a” harfi bilan tugaydigan ismlarni toping.

7-mashq
Berilgan matndan barcha email manzillarini toping.
Namuna: olimova@gmail.com

8-mashq
Berilgan matndan @username ko'rinishidagi barcha foydalanuvchi nomlarini findall() metodi yordamida toping. (10 ball)

9-mashq
Berilgan matndan barcha telefon raqamlarini toping. Telefon raqami formati: +998-xx-xxx-xx-xx

10-mashq
Biror matn olib, undan dd-mm-yyyy formatidagi barcha sanalarni toping.

11-mashq
Biror matndan email mavjud yoki yo'qligini search() yordamida tekshiring.
Email uchun RegEx ni ihateregex.io saytidan oling.

12-mashq. Berilgan matnda passport seriyasi bor-yo'qligini aniqlang.
Namuna: Passport: AC1236547

13-mashq
Foydalanuvchidan ismini so'rang. Ism faqat harflardan iborat va uzunligi 3 dan 15 gacha bo'lishi kerak. 
Uni match() yordamida tekshiring.

14-mashq
Foydalanuvchidan tizimga kirish uchun faqat kichik harflar va raqamlardan iborat, 
uzunligi 4 dan 12 gacha bo'lgan login kiriting. Ushbu shartlar uchun RegEx tuzing.

15-mashq
+7 921 014-96-13 formatdagi telefon raqami uchun RegEx tuzing va match() yordamida tekshiring.

16-mashq
+998(90)233-25-66 formatdagi telefon raqami uchun RegEx tuzing va match() funksiyasi bilan tekshiring.

17-mashq
Quyidagi avtomobil raqami uchun RegEx tuzing va match() bilan tekshiring:
D 234 OKJ

18-mashq
Quyidagi avtomobil raqamlari uchun bitta RegEx tuzing:
50 A 117BD va 50 117ABC

19-mashq
Matndan # belgisi bilan boshlanib, maksimal 12 ta belgigacha bo'lgan so'zlarni topib bering.
Masalan: #python_darsi

"""



