""" Strings - Matnlar """

# print("Salom")
# print('Salom')

# print("U sinf juda ham \"aqilli\" edi")


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


ism = input("Ismingizni kiriting: ").title()
familiya = input("Familiyangizni kiriting: ").title()

print(f"{ism.upper()} {familiya}")
