from re import match, findall, search
phone = input("Telefon raqami kiriting: ")
pattern = r"^[+]998[\d]{9}$"

print(match(pattern, phone))


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

"""

# car_number = input("Car number: ")
# car_pattern = r"^[A-Z]{2}[\s][0-9]{4}[A-Z]{2}$"
# print(match(car_pattern, car_number))


"""
Vazifa:

50 A 117BD
50 117ABC
Yuqoridagi avtomobil raqamlari uchun RegEx tuzish.
"""


"""
+998(90) 233-25-66
"""

# phone2 = input("tel: ")
# phone2_pattern = r"^[+]998[(][0-9]{2}[)] [0-9]{3}-[0-9]{2}-[0-9]{2}$"
# phone2_pattern = r"^[+]998[(]\d{2}[)] \d{3}-\d{2}-\d{2}$"

# print(match(phone2_pattern, phone2))


# word = input("Enter a word: ")
word_regex = r"^[a-z]{3,8}$"
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
phone2_pattern = r"[+]998[(][0-9]{2}[)] [0-9]{3}-[0-9]{2}-[0-9]{2}"
a_name = r"A[a-zA-Z]{3,10}"

# print(findall(phone2_pattern, matn1))



"""
1-mashq
Foydalanuvchidan ismini so'rang, u faqat harflardan iborat va 3-15 belgidan iborat bo'lishi kerak. 
Uni re.match() yordamida tekshiring.

2-mashq
Berilgan matndan barcha telefon raqamlarini toping. Telefon raqami formati quidagicha bo'lsin : +998-xx-xxx-xx-xx

3-mashq
Biror matn olib,  matndan dd-mm-yyyy formatidagi barcha  sanalarni toping.

4-mashq
Biror matndan email mavjudligini search() orqali tekshiring.
email uchun RegEx ni ihateregex.io saytidan oling !

5-mashq
Biror matnda "python" so‘zi borligini search orqali tekshiring

6-mashq
Matnda raqam borligini search orqalitekshiring
"""


""" search() - """
sana = r"[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}"
print(search(sana, matn1))



























