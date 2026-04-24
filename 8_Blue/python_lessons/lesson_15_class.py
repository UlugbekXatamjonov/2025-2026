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

# x = 17
# print(type(x))

# matn = "python"
# print(type(matn))

# def func():
#     print("Hello world!")
# print(type(func))

"""
METODLAR
Har bir obyekt uning ustida bajarish mumkin bo'lgan funksiyalar bilan keladi. 
Bu funksiyalar obyekt ichida yashirin bo'ladi, va biz ularga nuqta va funksiya nomi 
orqali murojat qilishimiz mumkin. Bunday funksiyalar shu klass (yoki obyektga) tegishli metodlar deyiladi.
Bir klassga tegishli metodlar, boshqa klassdagi obyketlar uchun mavjud bo'lmasligi tabiiy. 
Misol uchun matnlar uchun mavjud metodlarni, butun yoki o'nli sonlarga qo'llab bo'lmaydi.
"""
# matn = "python"
# print(matn.title())

# son = 20
# print(son.title()) # error message


""" Class yasash """
"""
Yangi klass yasash uchun class operatoridan foydalanamiz.
klass bu hali obyekt emas, bu obyekt uchun shablon. Shuning uchun klass yasashda 
shu klassdagi obyektlar uchun umumiy bo'lgan xususiyatlar va funksiyalarni o'ylashimiz kerak.
"""


class Odam():
    """ Inson yasash uchun class """

    def __init__(self, ism:str, familiya:str, t_yil:int, manzil:str, tel_raqam:str):
        self.ism = ism
        self.familiya = familiya
        self.t_yil = t_yil
        self.manzil = manzil
        self.tel_raqam = tel_raqam

    def __str__(self): # dunder - duble under score
        return f"{self.ism} {self.familiya}"

    def get_info(self):
        """ Obyekt haqida batafsil ma'lumot beruvchi metod """

        return f"{self.ism} {self.familiya} {self.t_yil} yilda {self.manzil}da tug'ilgan. "

    def get_age(self):
        from datetime import date
     
        return f"{self.ism} {date.today().year-self.t_yil} yoshda"



odam1 = Odam( "Oybek", "Ahmadullayev",2002, "Yangiqo'rg'on tumani, Birlashgan qishlog'i", "+998941232323")
odam2 = Odam( "Iqboljon", "Nabiyev",1990, "Pop tumani, Sang qishlog'i", "+998944445566")

# print(odam1)
# print(odam1.t_yil)
# print(odam1.manzil)
# print(odam1.get_info())
# print(odam2.get_info())
# print(odam1.get_age())
# print(odam2.get_age())


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
        
    def __str__(self):
        return f"{self.brend} {self.model}"

    def get_info(self):
        return f"{self.brend} kompaniyasining  {self.model} rusumli aftomobili {self.year}-yilda ishlab chiqarilgan. Narxi: {self.price} $"


    def get_year(self):
            """ Mashinaning ishlab chiqarilgan yilini aniqlovchi metod(funksiya)"""
            info = f"Ushbu mashina {self.year} da ishlab chiqarilgan"
            return info
            
    def get_age(self):
        """ Mashina ishlab chiqarilgan vaqtgacha bo'lgan yil """
        from datetime import datetime, date
        bu_yil=date.today().year

        return  f"Mashina ishlab chiqarilganiga {bu_yil - self.year} yil bo'lgan"
        
    def get_price(self):
        """ Mashinaning narxini aniqlovchi metod(funksiya)"""
        return f"Ushbu mashina {self.price} $ turadi"

    def change_price(self, new_price:int):
        """  """
        self.price = new_price
        return f"{self.model} ning narxi {self.price}$ ga o'zgardi"


malibu = Car("Shevrolet", "Malibu 2", 2021, 23000)
k5 = Car("KIA", "K5", 2024, 34000)

# print(malibu)
# print(k5.get_info())
print(k5.get_price())
# print(k5.get_year())
# print(k5.get_age())
# print(malibu.get_age())

print(k5.change_price(12000))
print(k5.get_price())





























