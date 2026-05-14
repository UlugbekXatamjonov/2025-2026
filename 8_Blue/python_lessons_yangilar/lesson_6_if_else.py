
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

# yosh = int(input("Yoshingiz nechida: "))
# if yosh >= 0 and yosh <= 6:
#     print("Siz bog'cha yoshidasiz")
# elif 7 <= yosh <= 18:
#     print("Siz maktab yoshidasiz")
# elif 19 <= yosh <= 30:
#     print("Siz talaba yoshidasiz")
# elif 31 <= yosh <= 69:
#     print("Siz ishlash yoshidasiz")
# elif 70 <= yosh:
#     print("Siz nafaqa yoshidasiz")

"""
17-mashq
300 dan 900 gacha juft sonlar ro'yxatini yarating:
    - 400 gacha → 3-daraja
    - 600 gacha → 4-daraja
    - 900 gacha → 5-daraja
"""
# sonlar = list(range(300, 900, 2))
# for son in sonlar:
#     if son > 300 and son < 400:
#         print(f"{son}ning  3-darajasi {son**3}")
#     elif 400 < son < 600:
#         print(f"{son}ning  4-darajasi {son**4}")
#     elif 600 < son < 900:
#         print(f"{son}ning  5-darajasi {son**5}")

"""
19-mashq (eng murakkab)
Foydalanuvchidan avval parol, keyin parolni tasdiqlashni so'rang:
Agar parollar bir-biriga mos va 8 ta belgidan uzun bo'lsa → “Parol o'rnatildi”
Parollar mos kelmasa → “Parollar mos emas”
Parol uzunligi < 8 bo'lsa → “Parolda kamida 8 belgi bo'lishi shart”
"""

password1 = input("Parol kirirting: ")
password2 = input("Parol takrorlang: ")


if password1 == password2 and len(password1) >= 8:
    print("Parol o'rnatildi")
elif password1 != password2:
    print("Parollar mos emas")
elif len(password1) < 8:
    print("Parolda kamida 8 belgi bo'lishi shart")

    