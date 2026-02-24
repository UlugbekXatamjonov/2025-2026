""" Strings - Matnlar """

print("Salom")
print('Salom')

print("U sinf juda ham \"aqilli\" edi")


""" O'zgaruvchi - Veribile """
# ism = "Ali"
# print(ism)

# yosh = 15
# manzil = "Yangi Namangan tumani, Islom Karimov ko'chasi 1-uy"

# print(yosh)
# print(manzil)
# print(yosh, manzil)


""" O'zgaruvchilar """
"""
O'zgaruvchi —kompyuter xotirasida ma'lum bir qiymatni saqlash uchun ajratilgan joy. 
Soddaroq qilib tushuntirsak, o'zgaruvchini quti, quti ichidagi narsani esa qiymat deb tasavvur qilish mumkin. 
Pythonda qiymatlar son, matn, ro'yxat va hokazo ko'rinishida bo'lishi mumkin.

O'zgaruvchi (variable) bunday deyilishiga sabab, uning qiymati istalgan vaqt o'zgartirilishi mumkin

O'zgaruvchilarga nom berishda quyidagi qoidalarga amal qiling:
O'zgaruvchi nomi harf yoki pastki chiziq (_) bilan boshlanishi kerak
O'zgaruvchi nomi raqam bilan boshlanishi mumkin emas
O'zgaruvchi nomida faqatgina lotin alifbosi harflari (a-z), raqamlar (0-9) va pastki chiziq (_) qatnashishi mumkin
O'zgaruvchi nomida bo'shliq (пробел) bo'lishi mumkin emas
O'zgaruvchi nomida katta-kichik harflar turlicha talqin qilinadi (ism, ISM, va Ism uchta turli o'zgaruvchi)
Shuningdek o'zgaruvchilarga Pythonda ishlatiladigan funktsiyalar va maxsus kalit so'zlarning (keywords) nomini bermang.
False, True, and, if, while, in, on, break, await, continue, not, try, from, def, pass ...
"""

ism1 = "Muhammad"
ism2 = "Mansurbek"
ism3 = "Hasanboy"

# print(ism1)
# print(ism2)
# print(ism3)


""" Metodlar """
# matn = "BU PYTHON dasturi"
# print(matn)

# print(matn.capitalize()) # Matndagi 1-harfini katta qilib beradi
# print(matn.title()) # So'zning birinchi harifni katta qilib chiqaradi
# print(matn.upper()) # Barcha so'zlardagi harflarni katta qilib beradi
# print(matn.lower()) # Barcha so'zlarni kichkina qilib beradi

# matn2 = "      Bugun Shavkat uyga kech ketadi.    "
# print(matn2)

# print(matn2.strip())# ikkala tomondagi bo'sh joyni olib tashaydi
# print(matn2.rstrip())# o'ng tomondagi bo'sh joyni olib tashaydi
# print(matn2.lstrip())# chap tomondagi bo'sh joyni olib tashaydi


""" input() """
ism = input("Ismingizni kiriting: ")
familiya = input("Familiyangizni kiriting: ")

print(ism)
print(familiya)


""" f"" --> string """
print(f"Salom {ism} {familiya} tanishganimdan hursandman !")


"""
1-mashq
5 ta turli matnlarni print() da chiqaring. Va ularni kommentga oling.

2-mashq
6 do'stingizning ismini o'zgaruvchiga saqlab, keyin uni konsulga chiqaring.

3-mashq
"Assalomu alaykum" matnini konsulda katta harflarda chiqarib bering.

4-mashq
Foydalanuvchidan qaysi maktabda o'qishini so'rang  va uni kichik harflarda konsulga chiqaring.

5-mashq
Ism, yosh, manzil, maktab, sinf deb nomlangan o'zgaruvchilar yarating va ularning qiymatini 
foydalanuvchidan so'rang. Keyin esa f”” yordamida namunadagi kabi matnni chiqaring.
Namuna: Salom mening ismim Nigora, yoshim 23 da. Namanganda yashayman va BM maktabida o'qiyman.

6-mashq
Mamlakat, viloyat, tuman, mahalla, ko'cha deb nomlangan o'zgaruvchilar yarating va 
ularga qiymatlarni foydalanuvchidan so'rang. Keyin esa ularni f””(f string) yordamida namunadagi kabi qilib konsulga chiqaring.
Namuna: Siz O'zbekiston Respublikasi, Namangan viloyati, Yangi Namangan tumani, A.Navoiy ko'chasi 41-uyda yashaysiz.

7-mashq
Konsulda:
"bugun dars juda qiziqarli bo'ldi"  matnini birinchi harfini katta qilib chiqarib bering.
"ahmadjon toshmatov"                ismini konsulda .title() metodi yordamida chiqaring.
"     Salom o'quvchilar    "        matnini oldi-ortidagi bo'sh joylarsiz chiqaring.
"Python dasturlash tili"            matnini faqat kichik harflarda chiqaring.
"Bugun maktabda imtihon"            matnini chap tomonidagi bo'sh joysiz chiqaring.
"""
