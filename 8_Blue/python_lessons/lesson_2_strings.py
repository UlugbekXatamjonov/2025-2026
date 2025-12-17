""" Matnlar - Strings """

# print("Salom")
# print('Salom')
# print("Abdurahmon juda \"yaxshi\" bola") # \ slesh

matn = "javohir KECHA futbol TomoSHO Qildi"
# print(matn)
# print(matn.title()) # Birinchi harifni katta qilib chiqaradi
# print(matn.capitalize()) #  Matndagi 1-harfini katta qilib beradi
print(matn.upper())# Barcha so'zlardagi harflarni katta qilib beradi
print(matn.lower())# Barcha so'zlarni kichkina qilib beradi


matn2 = "        Salom makatab       "
print(matn2)
print(matn2.strip())
print(matn2.lstrip()) # l - left
print(matn2.rstrip()) # r - right

ism  = input("ismingizni kiriting: ").title().strip()
print(f"Salom {ism}")

gul = "  BoyCHeCHa  "
print(gul.lstrip())









