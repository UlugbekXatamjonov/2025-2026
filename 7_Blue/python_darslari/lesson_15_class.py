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

class Avto():
    """  """

    def __init__(self, kompanya:str, model:str, rang:str, narx:int, tezligi:int):
        self.kompanya = kompanya
        self.model = model
        self.rang = rang
        self.narx = narx
        self.tezligi = tezligi

    def __str__(self):
        return f"{self.kompanya} {self.model}"


malibu = Avto("Shevrolet", "Malibu", 'Qora', 10000, 230)
jiguli = Avto("Lada", 'Jiguli 06', 'Sariq', 3200, 120)
t55 = Avto('Bestune', 'T55', 'Kulrang', 22000, 300)

print(malibu)
print(jiguli)
print(t55)








