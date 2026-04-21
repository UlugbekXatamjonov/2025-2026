
# try:
#     son = int(input("Son kiriting: "))
# except:
#     print("Harf kiritish mumkin emas edi !!")
# else:
#     print(son**2)

    
# print("dasturning ndavomi ........")
# print("dasturning ndavomi ........")
# print("dasturning ndavomi ........")
# print("dasturning ndavomi ........")
# print("dasturning ndavomi ........")

""" 2-mashq """
# try:
#     ball = float(input("balingizni kiriting: "))

#     if ball >= 160: 
#         print("“Bu juda yaxshi natija")
#     else:
#         print("Keyingi safar bundanda yaxshiroq natijani qo'lga kiritishga harakat qiling")
# except:
#     print("Faqat son kiritish kerak !!")

""" 3-mashq """
# try:
#     son1 = int(input("1-sonni kiriting: "))
#     son2 = int(input("2-sonni kiriting: "))
#     print(f"{son1}:{son2}={son1/son2}")
# except ValueError:
#     print("Faqat son kiritish kerak !!")
# except ZeroDivisionError:
#     print("Sonni 0 ga bo'lib bo'lmaydi !!!  2-sonni o'zgartiring !")
# except:
#     print("Xatolik !! Qaytadan urinib ko'ring !")


"""
15-mashq.
Foydalanuvchidan uning maktabga birinchi marta borgan sanasini so'rang va
o'sha kundan bugungi kungacha qancha vaqt o'tganini hisoblab, konsolga chiqaring.
"""


"""
https://www.tutorialsteacher.com/python/error-types-in-python

AssertionError -     Assert bayonoti bajarilmaganda ko'tariladi.
AttributeError -     Atribut tayinlashda ko'tarildi yoki mos yozuvlar bajarilmadi.
EOFError -   Input() funksiyasi faylning oxiri holatiga tushganda ko'tariladi.
FloatingPointError -     Suzuvchi nuqta operatsiyasi bajarilmaganda ko'tariladi.
GeneratorExit -  Jeneratorning close() usuli chaqirilganda ko'tariladi.
Import -     xatosi Import qilingan modul topilmaganda ko'tariladi.
IndexError -     Ketma-ketlik indeksi diapazondan tashqarida bo'lganda ko'tariladi.
KeyError -   Kalit lug'atda topilmasa ko'tariladi.
KeyboardInterrupt -  Foydalanuvchi uzilish tugmachasini bosganda ko'tariladi (Ctrl+c yoki o'chirish).
MemoryError -    Operatsiya xotirasi tugashi bilan ko'tariladi.
NameError -  O'zgaruvchi mahalliy yoki global miqyosda topilmasa ko'tariladi.
NotImplementedError -    Mavhum usullar bilan ko'tarilgan.
OSError -    Tizim ishi tizim bilan bog'liq xatolikka sabab bo'lganda ko'tariladi.
OverflowError -  Arifmetik amal natijasi koʻrsatish uchun juda katta boʻlganda koʻtariladi.
ReferenceError -     Axlat yig'ilgan referentga kirish uchun zaif havola proksi-serverdan foydalanilganda ko'tariladi.
RuntimeError -   Xato boshqa toifaga kirmasa ko'tariladi.
StopIteration -  iterator tomonidan qaytariladigan boshqa element yo'qligini bildirish uchun keyingi() funktsiyasi tomonidan ko'tariladi.
SyntaxError -    Sintaksis xatosiga duch kelganda tahlilchi tomonidan ko'tariladi.
IndentationError -   Noto'g'ri chiziq mavjud bo'lganda ko'tariladi.
TabError -   Qachonki chekinish mos kelmaydigan yorliqlar va bo'shliqlardan iborat bo'lsa ko'tariladi.
Tizim -  xatosi Tarjimon ichki xatoni aniqlaganida ko'tariladi.
SystemExit -     sys.exit() funksiyasi tomonidan ko'tarilgan.
TypeError -  Funktsiya yoki operatsiya noto'g'ri turdagi ob'ektga qo'llanilganda ko'tariladi.
UnboundLocalError -  Funksiya yoki usulda mahalliy o‘zgaruvchiga havola qilinganda ko‘tariladi, lekin bu o‘zgaruvchiga hech qanday qiymat bog‘lanmagan.
UnicodeError -   Unicode bilan bog'liq kodlash yoki dekodlash xatosi yuzaga kelganda ko'tariladi.
UnicodeEncodeError -     Kodlash paytida Unicode bilan bog'liq xatolik yuzaga kelganda ko'tariladi.
UnicodeDecodeError -     Unicode bilan bog'liq xato dekodlash vaqtida yuzaga kelganda ko'tariladi.
UnicodeTranslateError -  Unicode bilan bog'liq xato tarjima paytida yuzaga kelganda ko'tariladi.
ValueError -     Funktsiya to'g'ri turdagi, lekin noto'g'ri qiymatdagi argumentni olganida ko'tariladi.
ZeroDivisionError -  Bo'linish yoki modul operatsiyasining ikkinchi operandi nolga teng bo'lganda ko'tariladi.

""" 


"""
1) Sonlar deb nomlangan ro'yhat tuzing ro'yhatda bir nechta sonlar va 0 ham bo'lsin.
    Keyin foydalanuvchidan biror son kiritishini so'rab, qabul qilingan sonni sonlar ro'yhatidagi 
    sonlarga bo'ling va natijani konsulga chiqaring.
    Dastur tuzishda 'try-except' dan foydalaning va yuzaga kelishi mumkin bo'lgan barcha xatoliklarni oldini oling !
 """

# sonlar = [5, -6, 9, 234, -5, 0, 34]
# try:
#     yangi_son = int(input("Son kiriting: "))
#     for son in sonlar:
#         print(son/yangi_son)

# except ValueError:
#     print("Harf kiriitsh mumkin emas !")
# except ZeroDivisionError:
#     print("Sonni 0 ga bo'lib bo'lmaydi ! Boshqa son kiriting")


"""
2) Foydalanuvchidan uning yoshini qabul qilib olib uni 0 dan 1,000 gacha bo'lgan sonlardan qaysilariga 
    qoldiqsiz bo'linnishini aniqlab, qoldiqsiz bo'linadigan sonlarni ro'yhatga saqlab konsulga chiqaring.
    Va bu dasturni funksiyaga joylang. Hamda uni yozishda 'try-except' dan foydalaning va yuzaga kelishi
    mumiin bo'lgan xatoliklarni oldini oling
"""




