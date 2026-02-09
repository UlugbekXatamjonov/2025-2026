"""
Thame: Pythonda OOP va Class lar bilan tanishuv
"""

"""
Python - bu ob'ektga yo'naltirilgan dasturlash tili.
OPP - Object Oriented Programming ya'ni obyektga yo'naltiriglan dasturlash.
OOP haqida ---> https://python.sariq.dev/oop/kirish
Klass-  bu obyekt yasash uchun shablon yoki qolipdir. 
Bitta klassdan biz istalgancha nusxa olishimiz va yangi obyektlar yasashimiz mumkin.
"""

x = 17
# print(type(x))

matn = "python"
# print(type(matn))

def func():
    print("Hello world!")
# print(type(func))

"""
METODLAR
Har bir obyekt uning ustida bajarish mumkin bo'lgan funksiyalar bilan keladi. 
Bu funksiyalar obyekt ichida yashirin bo'ladi, va biz ularga nuqta va funksiya nomi 
orqali murojat qilishimiz mumkin. Bunday funksiyalar shu klass (yoki obyektga) tegishli metodlar deyiladi.
Bir klassga tegishli metodlar, boshqa klassdagi obyketlar uchun mavjud bo'lmasligi tabiiy. 
Misol uchun matnlar uchun mavjud metodlarni, butun yoki o'nli sonlarga qo'llab bo'lmaydi.
"""
matn = "python"
# print(matn.title())

son = 20
# print(son.title()) # error message


""" Class yasash """
"""
Yangi klass yasash uchun class operatoridan foydalanamiz.
klass bu hali obyekt emas, bu obyekt uchun shablon. Shuning uchun klass yasashda 
shu klassdagi obyektlar uchun umumiy bo'lgan xususiyatlar va funksiyalarni o'ylashimiz kerak.
"""

class Car:
    """ Mashina klassi """
    def __init__(self, brend, model, year, price): # klasni hususiyatlarini o'zida saqlovchi funksiya
        """ Mashinaning xusiyatlari 
        self.xususiyat = argument
        """
        self.brend = brend
        self.model = model
        self.year = year
        self.price = price
        
    def get_info(self):
        return f"{self.brend} kompaniyasining  {self.model} rusumli aftomobili {self.year}-yilda ishlab chiqarilgan. Narxi: {self.price} $"


    def full_info(self):
        """ Mashina haqida ma'lumot beruvchi funksiya  """
        print(f"{self.brend} brendining {self.model} modeli. \nIshla chiqarilgan yili {self.year}. \nNarxi: {self.price}")

    def get_year(self):
            """ Mashinaning ishlab chiqarilgan yilini aniqlovchi metod(funksiya)"""
            info = f"Ushbu mashina {self.year} da ishlab chiqarilgan"
            return info
            
    def get_price(self):
            """ Mashinaning narxini aniqlovchi metod(funksiya)"""
            return f"Ushbu mashina {self.price} $ turadi"
        
    def get_date(self, now=2026):
        """ Mashina ishlab chiqarilgan vaqtgacha bo'lgan yil """
        info = ''
        year = now - self.year
        if year:
            info = f"Mashina ishlab chiqarilganiga {year} yil bo'lgan"
        else:
            info = "Mashina shu yili ishlab chiqarilgan" 
        
        return info

"""
class Car — Car nomli klass yasadik. Klasslarga nom berishda uning birinchi harfini katta harfdan 
    boshlash tavsiya qilinadi. Agar klass nomi 2 va undan ko'p so'zdan iborat bo'lsa har bir so'zni 
    katta harf bilan boshlang.
def __init__(self) — klassga tegishli xususiyatlarni saqlovchi maxsus metod (funksiya). 
    'self' kalit so'zi ingliz tilidan "o'zi" deb tarjima qilinadi, va bu klassdan yasashilgan obyektning 
    o'ziga ishora qiladi. Ya'ni keyinchalik biz obyekt ichidagi metodga murojat qilganimizda 
    shu obyektning o'zi birinchi bo'lib funksiyaga argument sifatida uzatiladi, obyket ustida 
    turli amallar bajarish imkonin beradi. Har bir classda albatta bir marta yozilishi shart
def __init__(self, brend, model, name, year, price) — yasayotgan klassimizga xos xususiyatlarni 
    def __init__(self) funksiyasiga argument sifatida uzatamiz. Bizning Car klassimiz brend, model, 
    name, year, pricega ega bo'ladi. 
Keyingi qatorlarda esa 'self.xususiyat = argument' komandasi yordamida uzatilgan argumentlarni 
    klassning xususiyatlari bilan bo'glayapmiz. Bu yerda xususiyat nomi uzatilgan argument nomi 
    bilan mos tushishi shart emas, unga istalgan nom berishimiz mumkin (masalan self.name = ism)
"""

""" Obyekt yasash """        
car1 = Car("BMW", "A21", 202, 23000)
car2 = Car("Tesla", "Model S", 2020, 75000)
car3 = Car("Toyota", "X2", 2018, 3400)

"""
car1 obyektimiz tayyor. Obyektni yasash uchun Car klassiga murojat qildik va mashinaning modeli,
nomi, narxini parameter sifatida uzatdik. 
"""
   
""" Obyektning xususiyatlarini ko'rish """   
# print(car1.brend)   
# print(car1.model)   
# print(car1.price)   
# print(car2.brend)    
   
""" Classga metod qo'shamiz 👆👆👆 """

def get_info(self):
    return f"{self.brend} kompaniyasining  {self.model} rusumli aftomobili {self.year}-yilda ishlab chiqarilgan. Narxi: {self.price} $"

# print(car1.get_info())
# print(car2.get_info())
# print(car3.get_info())


def full_info(self):
        """ Mashina haqida ma'lumot beruvchi funksiya  """
        print(f"{self.brend} brendining {self.model} modeli. \nIshla chiqarilgan yili {self.year}. \nNarxi: {self.price}")

def get_year(self):
        """ Mashinaning ishlab chiqarilgan yilini aniqlovchi metod(funksiya)"""
        info = f"Ushbu mashina {self.year} da ishlab chiqarilgan"
        return info
        
def get_price(self):
        """ Mashinaning narxini aniqlovchi metod(funksiya)"""
        return f"Ushbu mashina {self.price} $ turadi"


# print(car1.full_info())   
# print(car1.get_year())   
# print(car1.get_price())   
   

""" Argument qabul qiluvchi metodlar """
   
def get_date(self, now=2023):
        """ Mashina ishlab chiqarilgan vaqtgacha bo'lgan yil """
        info = ''
        year = now - self.year
        if year:
            info = f"Mashina ishlab chiqarilganiga {year} yil bo'lgan"
        else:
            info = "Mashina shu yili ishlab chiqarilgan" 
        
        return info
   
# print(car1.get_date(2023))
# print(car1.get_date(2025))
   

""" Classlar bilan ishlash """
""" Classlarga argument sifatida turli ma'lumot turlarini uzatish """

class Student:
    """ O'quvchi classi """
    def __init__(self, FULL_NAME, YEAR, MARKS,FRIENDS, FACULTY,LEVEL=1,):
        """ Student haqidagi malumotlarni o'zida saqlovchi funksiya """
        self.full_name = FULL_NAME
        self.year = YEAR
        self.marks = MARKS
        self.friends = FRIENDS
        self.faculty = FACULTY
        self.level = LEVEL

    def get_name(self):
        return self.full_name
    
    def get_info(self):
        return f"{self.full_name} {self.year} yoshda. Va u {self.level} - bosqich talabasi "
    
    def get_marks(self):
        text = f"\t{self.full_name}ning olgan baholari:\n"
        for fan, baho in self.marks.items():
            text += f"{fan} - {baho}\n"
        return text
    
    def get_friends(self):
        text = f"{self.full_name}ning ulfatlari:\n"
        for i in self.friends:
            text += f"{i}  "
        return text
    
    def set_level(self, new_level):
        self.level = new_level
        return self.level
    
    def update_level(self):
        if self.level < 4:
            self.level += 1
        else:
            return "5 - bosqich mavjud emas !!!"
        return self.level
    
    def get_faculty(self):
        return f"{self.full_name} {self.faculty}  fakulteti talabasi"
    
    def set_faculty(self, new_faculty):
        self.faculty = new_faculty
        return self.faculty

baxolar = {
    'matematika':3, 
    "ingliz_tili":5, 
    "ona_tili":5, 
    "geografiya":4
}
friends = ['Ali', "Olim", "Hasan", "Husan", "Vali"]

student1 = Student("Aziz Alimov",23,baxolar, friends, 'Matematika', 4)
student2 = Student("Olimjon", 43,baxolar, friends)
student3 = Student("Boburov", 1999, baxolar, friends)
student4 = Student("Nodira Jamilova", 2002, {'matematika':5, 
                                            "ingliz_tili":4, 
                                            "ona_tili":3, 
                                            "geografiya":5
                                        }, ['Guli', "Aziza", "Husnora", "Madina", "Barno"])
# print(student1.get_marks())
# print(student1.get_friends())

# print(student1.set_level(3))
# print(student1.get_info())

# print(student1.get_faculty())
# print(student1.set_faculty('Iqtisot'))
# print(student1.get_faculty())




""" Obyektlar o'rtasidagi munosabat """
class MyLibrary:
    """ Kutubxona classi """
    def __init__(self, NAME, ADRESS):
        self.name = NAME
        self.adress = ADRESS
        self.books = [] # kitoblar
        self.books_count = 0 # kitoblar miqdori
        
    def get_info(self):
        text = f"{self.name} kutubxonasining Manzili: {self.adress} "
        text += f"Kitoblar soni {self.books_count} ta. "
        return text
    
    def add_book(self, new_book):
        self.books.append(new_book)
        self.books_count += 1

    def get_books(self):
        return [book.get_book_info() for book in self.books]
    
    """
    for book in self.books
        book.get_book_info()
    """
    
            
    
mylibrary1 = MyLibrary("Common Library", "A. Navoiy ko'chasi 34-uy")
# print(mylibrary1.get_info())
    
    
class Book:
    """ Kitob haqidagi class """
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
        
    def get_book_info(self):
        return f"\"{self.name}\" kitobining muallifi {self.author}. Kitob {self.year}-yili chiqarilgan."


book1 = Book("101 day", "Jek Darken", 2019)
book2 = Book("Bad habbits", "Drayn Pool", 1988)

print(book1.get_book_info())
print(book2.get_book_info())+3

print(mylibrary1.get_info())

mylibrary1.add_book(book1)
mylibrary1.add_book(book2)

# print(mylibrary1.get_books())


""" Obyektning hususiyat va metodlarini ko'rish  """
""" dir() funksiyasi """
from pprint import pprint # prety print
# 
# pprint(dir(mylibrary1))
# pprint(dir(book1))


""" __dict__ metodi """
""" __dict__metodi obyketning xususiyatlarini lug'at ko'rinishida qaytaradi """
# print(mylibrary1.__dict__)
# print(book1.__dict__)
# print(book2.__dict__)




""" Super class - Vorislik """
class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
    
    def get_full_name(self):
        return f"{self.ism} {self.familiya}"
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil

inson = Shaxs("Hasan","Alimov","FB001122",1995)
# print(f"{inson.get_info()}. {inson.get_age(2021)} yoshda.")



class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism,familiya,passport,tyil)
        
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil

    def get_id(self):
        return f"Talaba ID: {self.idraqam}"
    
    def update_bosqich(self):
        # self.bosqich += 1
        self.bosqich = self.bosqich + 1
        return self.bosqich
    
    def get_bosqich(self):
        return self.bosqich
    
    def get_info(self):
        text = f"{self.ism} {self.familiya}."
        text += f"\nPassport raqami: {self.passport} va {self.tyil} -yilda tug'ilgan"
        text += f"\nTalabaning ID raqami: {self.idraqam} va u {self.bosqich}- bosqich talabasi."
        return text
        
talaba = Talaba("Valijon","Aliyev", "AB2345324", 2000, 123456789)

# print(talaba.get_info())
# print(talaba.get_age(2023))
# print(talaba.get_full_name())
# print(talaba.get_id())
# print(talaba.update_bosqich())


""" 
Dastur davomida super klass voris klasslardan avval yozilgan (chaqirilgan) bo'lishi kerak
Voris klass boshqa klass uchun super klass bo'lishi mumkin
Voris klassga super klassdan meros qolgan istalgan metodni qayta talqin qilish mumkin
"""


""" POLIMORFIZM — Super class metodlarini qaytadan yozish """




"""
1) Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. Klassning xususiyatlari sifatida odatda 
    ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo)
    Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi foydalanuvchi haqida yig'ilgan 
    ma'lumotlarni chiroyli qilib chiqarsin. 
    (masalan: "Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).
    Klassdan bir nechta obyektlar yasashing va uning xususiyatlari va metodlariga murojat qiling.
    
2) Oila classini yasashing Va 1-mashqdagi kabi shartlarni bajaring

3) Avto degan yangi klass yasang. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar
    (model, rang, korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga standart 
    qiymat bering (masalan, kilometer=0). Avto ga oid obyektning xususiyatlarini qaytaradigan 
    metodlar yozing. get_info() metodi avto haqida to'liq ma'lumotni matn ko'rinishida qaytarsin
    Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.
    update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin
    
    
4) Oila va Inson klasini yarating va dars davomida classlar ustida ishlaganimiz dek shu klaslar bilan ishlang.

5) Avto salon va Avtomobil classlarini yarating. Har ikkala kalasda classning hususiyatlarini haqida 
    ma'lumot beruvchi va o'zgartirivchi metodlar yozing. AS(Avto Salon) classi da Avtomobil clasi obyekt
    larini o'zida jamlagan avtomobillar nomi ro'yhat bo'sin va shu ro'yhatda add_avto metodi yordamida 
    avtomobillar qo'shing   

6)  Talaba klassiga yana bir, fanlar degan xususiyat qo'shing. Bu xususiyat parametr sifatida uzatilmasin
    va obyekt yaratilganida bo'sh ro'yxatdan iborat bo'lsin (self.fanlar=[])
    Fan degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektlar yarating.
    Talaba klassiga fanga_yozil() degan yangi metod yozing. Bu metod parametr sifatida Fan klassiga 
    tegishli obyektlarni qabul qilib olsin va talabaning fanlar ro'yxatiga qo'shib qo'ysin.
    Talabaning fanlari ro'yxatidan biror fanni o'chirib tashlash uchun remove_fan() metodini yozing. 
    Agar bu metodga ro'yxatda yo'q fan uzatilsa "Siz bu fanga yozilmagansiz" xabarini qaytarsin.
    
    
7) Yuqoridagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring (masalan Professor, Foydalanuvchi, 
    Sotuvchi, Mijoz va hokazo)
    Har bir klassga o'ziga hoz xususiyatlar va metodlar yuklang.
    Barcha yangi klasslar uchun get_info() metodini qayta yozib chiqing.
    Voris klasslardan yana boshqa voris klass yaratib ko'ring. Misol uchun Foydalanuvchi klassidan 
    Admin klassini yarating. 
    Admin klassiga foydalanuvchida yo'q yangi metodlar yozing, masalan, ban_user() metodi konsolga 
    "Foydalanuvchi bloklandi" degan matn chiqarsin.
 
    
"""
   
   
   
