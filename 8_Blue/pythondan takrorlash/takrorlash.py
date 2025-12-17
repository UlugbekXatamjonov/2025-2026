
"""   Vazifa
1) ism, familya, yosh, kasb va manzil degan o'zgaruvchilar yaratamiz va ularni bitta print() da chiqaramiz.
2) Kvadratning perimetri va yuzuni topuvchi dastur
3) To'g'ri to'rtburchakning perimetri va yuzuni topuvchi dastur 

4) Quidagi o'zgaruvchini ---> gul = “  BoyCHeCHak  ” 
    -Chap tomonidagi bo'shliqni olib tashlab;
    -Har ikki tomonidagi bo'shliqni olib tashlab;
    -Birinchi harifni katta qilib;
    -Barcha hariflarini katta qilib;
    -Barcha hariflarini kichik qilib konsulga chiqaring.

5)
    -15 ning ildizini toping
    -1 ning 100-darajasini toping
    -100 ning 2 darajasiga 42342 ning ildizni qo'shing
    -3434 ning 3 darajasiga 123 ning 2 darajasini qo'shing
    -834 va 5 ning yig'indisiga 34355 ning ildizni qo'shing
"""



""" Mashqlar """
"""
1) Foydalanuvchidan uning ismini va u o'qigan kitoblaridan 5 tasini so'rab kitoblar deb nomlangan ro'yhatga qo'shing.
Keyin esa ro'yhatdan 1 ta kitobni o'chirib tashlang. So'ngra ro'yhatning 2- va 3- indexlarga yangi kitoblar nomini qo'shing.

2) Fanlar deb nomlangan ro'yhat yarating, 5 ta fan bo'lsin. Keyin esa:
    2 ta yangi qiymat qo'shing(2 xil usulda);
    4 ta qiymatni o'chiring(4 xil usulda);

3) sinfdoshar deb nomlangan ro'yhat yarating va unda 4 ta sinfdoshingizning ismini bo'lsin. Keyin ro'yhatning boshiga,
    o'rtasiga va oxiriga 1 tadan yangi ismlar qo'shing.

4) sonlar = [-34, 45, 0, -65.3, 3.6, 2, 62]  ushbu ro'yhatdagi:
    birinchi va to'rtinchi elementlar ayirmasini toping.
    minus birinchi elementni minus uchinchi elementga ko'paytiring.
    uchinchi element ildizini toping.
    birinchi elementga uchinchi elementni qo'shib chiqqan natijani, -ikkinchi elementga bo'ling

5) O'zingizga ma'lum mashinalar ro'yxatini tuzing(eng kamida 7 ta) va ro'yxatni konsolga chiqaring.
    -ro'yxatning uzunligini konsolga chiqaring;
    
6) -200 dan 430 gacha bo'lgan toq sonlar ro'yxatini tuzing. 
7) 101 dan 2020 gacha bo'lgan juft sonladan iborat ro'yhat yarating.
8) -322 dan -2 gacha bo'lgan toq sonlardan iborat ro'yhat yarating va to'yhatning uzunligini toping.

9) O'zingizga ma'lum davlatlarning ro'yxatini tuzing(eng kamida 7 ta) va ro'yxatni konsolga chiqaring.
    -ro'yxatning uzunligini konsolga chiqaring;
    -sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring;
    -sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring;
    -reverse() metodi yordamida ro'yxatni aylantirib chiqaring;
    -sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring;

10) sonlar = [2, 6, -9, 0, 8.5, 21, 65, -34, 43.6, -44, 847, 0, 32, -4]
    Ushbu ro'yhatdagi:
    -sonlarning yig'indisini toping;
    -ro'yhatning uzunligini toping;
    -eng katta va eng kichik sonni toping;

"""


"""
---------------------- For ---------------------- 
"""

""" for operatori """
# ismlar = ["Laylo", "Muslima", "Ma'rifat", "Odina", "Umida", "Dilshoda"]
# print(f"Salom {ismlar[0]}, ertaga qayerga borasan.")

# for ism in ismlar:
#     print(f"Salom {ism}, ertaga qayerga borasan.")
#     print("Agar ertaga vaqting bo'lsa hayvonot bog'iga borsak nima deysan ?")
    
# print("Bu habar hammaga yuborildi")


# sonlar = [1,2,3,4,5,]
# sonlar = list(range(1, 20)) # 1,2,3,4,5,6,7,8,9,10,, ...20
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2}")
#     print(f"{son} ning kubi {son**3}")
    # print(f"{son} dan 1 ta kichik son {son-1} va 3 ta katta son  {son+3}")


# for x in range(100):
#     print(f"I will not talk on English lesson({x+1} row)")


# son = int(input("Nechta oila azoingiz bor: "))
# ismlar = []
# for i in range(son):
#     ismlar.append(input(f"{i+1} - oila azoingizni ismini kiriting: "))
# print(ismlar)  


"""
1-mashq | Ushbu koddagi bir nechta hatoliklarni to'g'irlang va dasturni to'g'ri ishga tushuring.

son = input("Nechta meva nomini kiritmoqchisiz: ")
mevalar = []

for s in range(Son):
    meva = input(f"{x+3} - meva nomini kiriting: "
sabzavotlar.append(mava)  
print(mevala)

2-mashq | -322 dan -2 gacha bo'lgan barcha toq sonlarning:

1) 5 chi va 7 chi darajasini toping;
2) Ro'yhatdagi har bir sondan 4 taga kichik sonni konsulga chiqaring;
3) Ro'yhatdagi har bir sonning 4 -darajasini toping;
4) Ro'yhatning uzunligini o'lchang;
5) Ro'yhatni avval o'sish tartibida keyin esa kamayish tartibida tartiblab konsulga chiqaring;
"""

# son = int(input("Nechta meva nomini kiritmoqchisiz: "))
# mevalar = []

# for s in range(son):
#     meva = input(f"{s+1} - meva nomini kiriting: ")
#     mevalar.append(meva)  
# print(mevalar)


# sonlar  =list(range(-321, -2, 2))

# for son in sonlar:
#     print(f"{son} ning 5- darajasi {son**5}, 7-darajasi {son**7} ga teng.")
#     print(f"{son} dan 4 ta kichik son {son-4}")
#     print(f"{son} ning 4-darajasi {son**4}")


# print(len(sonlar))

# sonlar.sort()
# print(sonlar)

# sonlar.sort(reverse=True)
# print(sonlar)

"""
1-mashq | Ushbu koddagi bir nechta hatoliklarni to'g'irlang va dasturni to'g'ri ishga tushuring.

son = input("Nechta meva nomini kiritmoqchisiz: ")
mevalar = []

for s in range(Son):
    meva = input(f"{x+3} - meva nomini kiriting: "
sabzavotlar.append(mava)  
print(mevala)

2-mashq | -322 dan -2 gacha bo'lgan barcha toq sonlarning:
    1) 5 chi va 7 chi darajasini toping;
    2) Ro'yhatdagi har bir sondan 4 taga kichik sonni konsulga chiqaring;
    3) Ro'yhatdagi har bir sonning 4 -darajasini toping;

    4) Ro'yhatning uzunligini o'lchang;
    5) Ro'yhatni avval o'sish tartibida keyin esa kamayish tartibida tartiblab konsulga chiqaring;

3-mashq
Foydalanuvchidan uning sinfdoshlari sonini va ularning ismlarini so'rab classmates deb nomlangan 
ro'yhatga qo'shing va ro'yhatni konsulga chiqaring.

"""


# ismlar  = ["Ali", "Olim", "Anvar", "Husan", "Jasur"]
# for ism in ismlar:
#     if ism == "Husan":
#         print(f"Salom {ism}. Hush kelibsan !")
#     elif ism == "Jasur":
#         print(f"Salom {ism}. Hush kelibsan !")
#     else:
#         print(f"Salom {ism}")



"""
    ==  -> teng bo'lsa
    !=  -> teng bo'lmasa
    >   -> katta bo'lsa
    <   -> kichik bo'lsa
    >=  -> katta yoki teng bo'lsa
    <=  -> kichik yoki teng bo'lsa
    or   -> yoki
    and  -> va 
"""






""" Lug'at - Dictionary """
ismlar = {
    "malikova_naima":"olma", # element
    "sarvinoz":"ananas",
    "hadicha":'olcha',
    "mohlaroy":'gilos',
    'oydina':"banan"
}

# print(ismlar)
# print(ismlar["hadicha"])
# print(f"Hadichaning sevimli mevasi {ismlar['hadicha']}")

# print(type(ismlar)) # dict --> dictionary

buyumlar = {
    "ism":"Ali",
    "yosh":12,
    "student":True,
    "oila":["ota","ona",'aka'],
    "ball":{
        'ict':50,
        'math':23,
        'eng':33
    }
}
# print(buyumlar)


""" Element qo'shish """
""" 1-usul """
# ismlar['rahima'] = "apelsin"
# print(ismlar)

# ismlar[input("Biror ism kiriting: ")] = input("Siz qaysi mevani yoqtirasiz: ")
# print(ismlar)

""" 2-usul """
# ismlar.update({'abror':"shaftoli"})
# print(ismlar)

# ismlar.update({input("Ism kiriting: "):input("Meva kiriting: ")})
# print(ismlar)

""" Elementni o'chirish """
# del ismlar["hadicha"]
# print(ismlar)

# ismlar.pop('sarvinoz')
# print(ismlar)

# ismlar.popitem() #  eng so'ngi elementni o'chirib tashlaydi
# print(ismlar)

""" Lug'atni o'chirib tashlash """
# del ismlar

""" Lug'atni tozalash """
# ismlar.clear()
# print(ismlar)


""" Nusxa olish """
# girls = ismlar.copy()
# print(girls)


"""
4-mashq
taomlar = {
    'ali':'osh',
    'vali':'shashlik',
    'hasan':"lag'mon",
    'husan':"mastava",
    'olim':"somsa",
    'nodir':"kabob",
}
Ushbu lug'atdagi:
2 ta elementning qiymatini o'zgartiting(o'zingiz);
2 ta yangi element qo'shing(o'zingiz)
1 ta elementning qiymatini foydalanuvchidan so'rab o'zgartiting;
2 ta yangi elementni foydalanuvchidan so'rab  qo'shing;

5-mashq
Fanlar deb nomlangan lug'at yarating, unda {“kalit”:”fan nomi”}  ko'rinishidagi
2 ta fan bo'lsin.  Keyin esa:
    2 ta yangi qiymat qo'shing(2 xil usulda);
    2 ta qiymatni o'zgartiring(2 xil usulda);
    3 ta qiymatni o'chiring(3 xil usulda);
    yangi lug'at yaratib unga Fanlar lug'atidan nusxa oling;
    So'ngra Fanlar ro'yhatini tozalab tashlang;


6-mashq
books deb nomlangan lug'at yarating{“key”:”kitob nomi”}. Ichida 2 ta element bo'lsin. 
Yana  yangi  2 ta elementni 2 xil usulda qo'shing, 2 ta elementni 2 xil usulda yangilang, 
3 ta elementni 3 xil usulda o'chiring va so'ngra lug'atni tozalab tashlang.

"""

taomlar = {
    'ali':'osh',
    'vali':'shashlik',
    'hasan':"lag'mon",
    'husan':"mastava",
    'olim':"somsa",
    'nodir':"kabob",
}


# print(taomlar.keys())
# print(taomlar.values())

# for key, value in taomlar.items():
#     print(f"{key} - {value}")


# davlatlar = {
#     "o'zbekiston":"toshkent",
#     "qatar":"doxa",
#     "turkiya":"anqara"
# }

# savol = input("Davlar yoki poyaxt: ").lower()

# for davlat, poytaxt in davlatlar.items():
#     if savol == davlat:
#         print(f"{davlat.title()}ning poytaxti {poytaxt.title()} shahri")    
#     elif savol == poytaxt:
#         print(f"{poytaxt.title()} shahri {davlat.title()}da joylashgan")    
        
# if savol not in davlatlar.keys() and savol not in davlatlar.values():
#     print(f"Bizda {savol} haqida ma'lumot yo'q") 
    


def daraja(son:int,  daraja:int) -> int:
    """ Sonni darajaga ko'taruvchi funksiya """

    return son**daraja

# print(daraja(3, 6))
# print(daraja(2, 4))

def summa(*sonlar:int) -> int: # *args - arguments
    """  """
    summa = 0
    for son in sonlar:
        summa += son

    return summa

# print(summa(2, 7, 0, -5, 87, 23))

def full_name(name:str, surname:str, **kwargs) -> str: # **kwargs - key word arguments
    """  """

    return f"{name} {surname} {kwargs['father_name']} {kwargs['age']}"

# print(full_name("Alisher", "Sobirov", father_name="Otabek o'gli", age=34))





""" RegEx """
from re import match, findall, search


# phone = input("Telefon raqamni kiriting: ")
# pattern = "^[+]998[0-9]{9}$"

# print(match(pattern, phone))


"""
link -> https://docs.python.org/3/howto/regex.html
link -> https://docs.python.org/3/library/re.html
link -> https://www.w3schools.com/python/python_regex.asp

RegEx funksiyalari
match()     -   Solishtirish uchun  
findall()   -   Barcha mosliklarni o'z ichiga olgan ro'yxatni qaytaradi
search()    -   Agar matnning istalgan joyida moslik mavjud bo'lsa, Match ob'ektini qaytaradi

\w - So'z belgilari -->  a-z / A-Z 
\d - Raqam  --> 0-9
\b - So'z chegarasi --> $
\s - bo'shliq
^  - boshlanish
"""

"""
1-mashq
Foydalanuvchi nomi so'rang, u faqat harflardan iborat va 3-15 belgidan iborat bo'lishi kerak. 
Uni re.match() yordamida tekshiring.
2-mashq
Berilgan matndan barcha telefon raqamlarini toping. Telefon raqami formati quidagicha bo'lsin : +998-xx-xxx-xx-xx
3-mashq
Biror matn olib,  matndan dd-mm-yyyy formatidagi eng birinchi sanani toping.
4-mashq
Biror matndan email mavjudligini findall() orqali tekshiring.
email uchun RegEx ni ihateregex.io saytidan oling !
5-mashq
Biror matnda "python" so‘zi borligini tekshiring
6-mashq
Matnda raqam borligini tekshiring
"""



from datetime import date, datetime, timedelta

"""
1-mashq | 10 Ball
2010-03-10 sanasidan 8 hafta,  325 soat va  854 minutni ayring va hosil bo'lgan vaqtni konsulga 
chiqaring.
"""

sana  = date(2010, 3, 10)
# print(sana)
# print(sana - timedelta(weeks=8, hours=325, minutes=854))


"""
Foydalanuvchidan uning maktabga birinchi marta borgan sanasini so'rang va o'sha kundan bugungi kungacha qancha vaqt o'tganini hisoblab konsulga chiqaring.
"""

bugun = date.today()
maktab = date(2008, 9, 2)
# print((bugun - maktab).days)


# print(bugun.strftime("%A %B %Y"))


"""
Foydalanuvchidan biror sanani so'ng. Agar u eski sana kiritsa – “Bu o'tib ketgan sana”. 
Agar hali kelmagan sana bo'lsa – “Bu sana endi keladi”, 
Agar u bugungi sanani kiritsa – “Siz bugungi sanani kirgazdingiz” degan habar chiqsin.
"""

"""
Foydalanuvchidan  uning tug'ilgan sanasini so'rab, uning keyingi tug'ilgan kuniga yana necha 
kun qolganini topib beruvchi dastur tuzing.
Namuna: Sizning keyingi tug'ilgan kuningiz 234 kundan keyin keladi va haftaning Friday kuni bo'ladi.
"""

# kun = int(input("Kun kiriting: "))
# oy = int(input("Oy kiriting: "))
# # yil = int(input("Yil kiriting: "))

# t_sana = date(bugun.year, oy, kun)

# if t_sana > bugun:
#     print((t_sana - bugun).days)
# elif t_sana < bugun:
#     t_sana = date(bugun.year+1, oy, kun)
#     print((t_sana - bugun).days)
# else:
#     print("Bugun")




""" try-except """
# kun = input("Kun kiriting: ")
# oy = int(input("Oy kiriting: "))
# # yil = int(input("Yil kiriting: "))

# try:
#     t_sana = date(bugun.year, oy, kun)
# except TypeError:
#     print("Siz noto'g'ri ma'lumot kiritdingiz !!!")
# except NameError:
#     print("....")
# except:
#     print("Xatolik !!!!")


# if t_sana > bugun:
#     print((t_sana - bugun).days)
# elif t_sana < bugun:
#     t_sana = date(bugun.year+1, oy, kun)
#     print((t_sana - bugun).days)
# else:
#     print("Bugun")

