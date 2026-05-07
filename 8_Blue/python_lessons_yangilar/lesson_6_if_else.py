
# savol = int(input("Yoshingiz nechida: "))

# if savol > 18:
#     print("Sizning passportingiz bor")
# else:
#     print("Sizning passportingiz yo'q !")

"""
    ==  ---> teng bo'lsa
    !=  ---> teng bo'lmasa
    >   ---> katta bo'lsa
    <   ---> kichik bo'lsa
    >=  ---> katta yoki teng bo'lsa
    <=  ---> kichik yoki teng bo'lsa
    or   ---> yoki
    and  ---> va 
"""
"""
5-mashq
Foydalanuvchidan uning ismini so'rang:
Azizbek and Anvar bo'lsa — “Salom Azizbek/Anvar. Ishlaring yaxshimi?”
Hadicha and Muslima bo'lsa — “Hayrli kun Hadicha/Muslima.”
("or" operatori shart.)
"""

# ism = input("Ismingiz nima: ").lower()

# if ism == "azizbek" or ism == 'anvar':
#     print(f"Salom {ism}. Ishlaring yaxshimi?")

# elif ism == "hadicha" or ism == "muslima":
#     print(f"Hayrli kun {ism}")

# else:
#     print(f"Salom {ism}")


"""
7-mashq
Foydalanuvchidan yoshini so'rang va quyidagiga mos xabar chiqaring:
0-6 → “Siz bog'cha yoshidasiz”
7-18 → “Siz maktab yoshidasiz”
19-30 → “Siz talaba yoshidasiz”
31-69 → “Siz ishlash yoshidasiz”
70+ → “Siz nafaqa yoshidasiz”
0 dan kichik → “Iltimos musbat son kiriting”
"""

yosh = int(input("Yoshingiz nechida: "))
if yosh >= 0 and yosh <= 6:
    print("Siz bog'cha yoshidasiz")
elif 7 <= yosh <= 18:
    print("Siz maktab yoshidasiz")
elif 19 <= yosh <= 30:
    print("Siz talaba yoshidasiz")
elif 31 <= yosh <= 69:
    print("Siz ishlash yoshidasiz")
elif 70 <= yosh:
    print("Siz nafaqa yoshidasiz")




