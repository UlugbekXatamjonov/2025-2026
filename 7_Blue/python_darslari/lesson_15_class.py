"""
Thame: Pythonda OOP va Class lar bilan tanishuv
"""

from datetime import date

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
# from datetime import date

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
    
    def add_friend(self, new_friend):
        self.friends.append(new_friend)

        return f"{self.full_name} ning do'stlari qatoriga {new_friend} qo'shildi !"

    def add_friends(self, *new_friend):

        for new_name in new_friend:
            self.friends.append(new_name)

        return f"{self.full_name} ning do'stlari qatoriga {new_friend} qo'shildi !"

    def remove_friend(self, name:str):

        if name in self.friends:
            self.friends.remove(name)
            return f"{name} o'chirilib yuborildi !"
        else:
            return f"{name} sizning do'stingiz emas, uni o'chirilib bo'lmaydi !"

    def get_class(self):
        return f"{self.full_name} hozirda {self.grade} sinf o'quvchisi"

    def change_class(self):
        if 1 < self.grade < 11:
            self.grade += 1
            return f"{self.full_name} ning sinfi endi {self.grade} ga o'zgardi"
        else:
            return f"{self.full_name} boshqa sinfga o'ta olmaydi !!!"


student1 = Student("Aziz Alimov",13, [20,26,42,36], ["Olim", "Abbos", "Ali"], 'Matematika', 7)
student2 = Student("Sarvinoz", 17, [17, 45, 43, 50], ['Guli', "Aziza", "Husnora", "Madina", "Barno"], "Kimyo", 11)

# print(student1.get_name())
# print(student2.get_friends())
# print(student2.add_friend("Bobur"))
# print(student2.add_friends("Anvar", "Olim", "Nurmuhammad"))
# print(student2.get_friends())
# print(student2.remove_friend("Aziza"))
# print(student2.remove_friend("Madina"))
# print(student2.get_friends())

# print(student1.get_class())
# print(student1.change_class())
# print(student1.change_class())
# print(student1.change_class())
# print(student1.change_class())
# print(student1.change_class())
# print(student1.change_class())

# print(student1.get_class())

"""
3) Avto degan yangi klass yasang. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar
    (model, rang, korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga standart 
    qiymat bering (masalan, kilometer=0). Avto ga oid obyektning xususiyatlarini qaytaradigan 
    metodlar yozing. get_info() metodi avto haqida to'liq ma'lumotni matn ko'rinishida qaytarsin
    Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.
    update_km(200) metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin
"""


class Fanlar:
    """  """
    def __init__(self, nomi:str, turi:str):
        self.nomi = nomi
        self.turi = turi
 
    def __str__(self):
        return self.nomi

informatika = Fanlar("Informatika", "Chuqirlashtirilgan")
matematika = Fanlar("Matematika", "Chuqirlashtirilgan")
ingliz_tili = Fanlar("Ingliz tili", "Chuqirlashtirilgan")
rus_tili = Fanlar("Rus tili", "Chuqirlashtirilgan")
kimyo = Fanlar("Kimyo", "Chuqirlashtirilgan")
biologiya = Fanlar("Biologiya", "Chuqirlashtirilgan")
j_tarbiya = Fanlar("Jismoniy tarbiya", "Chuqirlashtirilgan")

# print(matematika)
# print(informatika)

class Sinf:
    """ """
    def __init__(self, nomi, sinf_rahbar:str, oqituvchilar:list, fanlar:list, students:list):
        self.nomi = nomi
        self.sinf_rahbar =sinf_rahbar 
        self.oqituvchilar =oqituvchilar 
        self.fanlar =fanlar 
        self.students =students 

    def __str__(self):
        return self.nomi

    def get_sinfrahber(self):
        return f"Bu sinfning sinf rahbari {self.sinf_rahbar}"
    
    def get_fanlar(self):
        return f"{self.fanlar}"
    
    def get_oqituvchilar(self):
        return self.oqituvchilar
    
    def get_students(self):
        return self.students
    
    def get_students_number(self):
        return len(self.students)
    

seven_blue = Sinf("7 Blue","Malika", ["Ibrohim", "Ulug'bek", "Malika", "Botir"], 
                  [informatika, matematika, ingliz_tili, rus_tili], ["Inomjon", "Shavkat", "Javohir", "Saidbek", "Shavkat", "Javohir", "Saidbek", "Shavkat", "Javohir", "Saidbek"])
# print(seven_blue.get_fanlar())
# print(seven_blue.get_oqituvchilar())
# print(seven_blue.get_students())
# print(seven_blue.get_sinfrahber())
# print(seven_blue.get_students_number())


""" Super class - Vorislik class """

class Qahramon:
    """  """
    def __init__(self, nom:str, jon:int, qobilyatlar:list, qurol:str):
        self.nom = nom
        self. jon = jon
        self.qobilyatlar = qobilyatlar
        self.qurol = qurol

    def __str__(self):
        return self.nom
    
    def get_health(self):
        """  """
        return f"{self.nom} - {self.jon}% joni bor"

    def get_skills(self):
        """  """
        return f"{self.nom} ning qobilyatlari {len(self.qobilyatlar)} ta. {self.qobilyatlar}"
    
    def get_info(self):

        return f"Nom: {self.nom} \nJon: {self.jon} \nQobilyatlar: {self.qobilyatlar} \nQurol: {self.qurol}"


uranus = Qahramon("Uranus", 120, ["Sakrash", "Ko'rinmaslik"], "Pistolet")

# print(uranus)
# print(uranus.get_health())
# print(uranus.get_skills())


class Avangers(Qahramon):
    """ """
    def __init__(self, nom, jon, qobilyatlar, qurol, kostyum, kozoynak):
        super().__init__(nom, jon, qobilyatlar, qurol)

        self.kostyum = kostyum
        self.kozoynak = kozoynak

    def heal(self):
        """ Qahramonning jonini ko'paytiradi """

        if self.jon < 100 and self.jon > 0:
            self.jon += 10
            return f"{self.nom}ning jonni 10 ga ortdi"
        else:
            return f"{self.nom}ning joni yetarli ! qo'shish shart, emas !"

    def get_info(self):

        return f"Nom 🧑: {self.nom} \nJon🔋 : {self.jon} \nQobilyatlar ⚡: {self.qobilyatlar} \nQurol 🔫: {self.qurol} \nKostyum: {self.kostyum} \n ko'zoynak: {self.kozoynak}"

spider_man = Avangers("Spiderman", 60, ['uchish', 'tirmashish', 'super sezgirlik', "to'r"], "To'r", "Super X kastyum", "Aqilli ko'zoynak")
# print(spider_man)
# print(spider_man.get_health())
# print(spider_man.get_skills())
# print(spider_man.heal())
# print(spider_man.heal())
# print(spider_man.get_health())

print(uranus.get_info())
print(spider_man.get_info())


