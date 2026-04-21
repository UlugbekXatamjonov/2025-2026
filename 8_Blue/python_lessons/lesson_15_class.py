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




































