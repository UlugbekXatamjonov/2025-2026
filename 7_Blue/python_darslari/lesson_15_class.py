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
from datetime import date

class Avto():
    """  """

    def __init__(self, kompanya:str, model:str, rang:str, narx:int, tezligi:int, yil:int, raqam:str):
        self.kompanya = kompanya
        self.model = model
        self.rang = rang
        self.narx = narx
        self.tezligi = tezligi
        self.yil = yil
        self.raqam = raqam

    def __str__(self):
        return f"{self.model}"
    
    def get_info(self):
        """ Avto klasinging obyekti haqida ma'lumot beruvchi funksiya """
        return f"Kompaniyasi: {self.kompanya} \nModeli: {self.model} \nRangi: {self.rang} \nNarxi: {self.narx} \nTezligi: {self.tezligi}\n"

    def age(self):
        """ Avtomobilning yoshini hisoblab beruvchi funksiya """
        yosh = date.today().year - self.yil
        if yosh > 0:
            return f"{self.model} ishlab chiqarilganiga {yosh} yil bo'ldi."
        elif yosh == 0:
            return f"{self.model} bu yil ishlab chiqarilgan."

    def get_number(self):
        """ Mashinaning raqamini ko'rsatuvchi metod """
        return f"{self.model} ning davlat raqami {self.raqam}"
    
    def get_price(self):
        """ Mashinang narxini ko'rsatuvchi funksiya """
        return f"{self.model} ning narxi {self.narx} $"
    
    def change_price(self, new_price:int):
        """ 
            Mashinaning narxini o'zgartiruvchi metod 
            new_price -> yangi narx
        """
        self.narx = new_price
        return f"{self.model} ning narxi {self.narx} $ ga o'zgardi"

    def change_color(self, new_color:int):
        """ 
            Mashinaning rangini o'zgartiruvchi metod 
            new_color -> yangi rang
        """
        self.rang = new_color
        return f"{self.model} ning rangi {self.rang} ga o'zgardi"


malibu = Avto("Shevrolet", "Malibu", 'Qora', 10000, 230, 2021, "50A766ZB")
jiguli = Avto("Lada", 'Jiguli 06', 'Sariq', 3200, 120, 1998, "50C423JA")
t55 = Avto('Bestune', 'T55', 'Kulrang', 22000, 300, 2026, "50Z111AA")

# print(malibu)
# print(jiguli)
# print(t55.age())
# print(t55.get_number())


# print(jiguli.get_price())
# print(jiguli.change_price(5100))
# print(jiguli.get_price())


class Student:
    """ O'quvchi classi """
    def __init__(self, FULL_NAME:str, YEAR:int, MARKS:list,FRIENDS:list, class_type:str, grade:int=1,):
        """ Student haqidagi malumotlarni o'zida saqlovchi funksiya """
        self.full_name = FULL_NAME
        self.year = YEAR
        self.marks = MARKS
        self.friends = FRIENDS
        self.class_type = class_type
        self.grade = grade

    def get_name(self):
        return self.full_name
    
    def get_info(self):
        return f"{self.full_name} {self.year} yoshda. Va u {self.grade} - sinf o'quvchisi "
    
    def get_marks(self):
        """ Baholarni ko'rsatuvchi funksiya """

        return f"Ummumiy bahosi: {sum(self.marks)} ball \nO'rtacha bahosi: {sum(self.marks)/len(self.marks)} ball"

    def get_friends(self):
        """  """
        # javob = f"{self.full_name}ning do'stlari: "
        # for ism in self.friends:
        #     javob += f"{ism} "

        # return javob
        return f"{self.full_name}ning do'stlari {self.friends}"
    

student1 = Student("Aziz Alimov",13, [20,26,42,36], ["Olim", "Abbos", "Ali"], 'Matematika', 7)
student2 = Student("Sarvinoz", 17, [17, 45, 43, 50], ['Guli', "Aziza", "Husnora", "Madina", "Barno"], "Kimyo", 11)

# print(student1.get_name())
print(student2.get_friends())

