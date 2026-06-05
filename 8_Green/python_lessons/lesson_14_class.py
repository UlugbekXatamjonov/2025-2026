"""
OOP - Opject orented programming 
"""

from datetime import date
yil = date.today().year

class Inson:
    """  """
    def __init__(self, name:str, surname:str, year:int, adress:str):
        self.name = name
        self.surname = surname
        self.year = year
        self.adress = adress

    def __str__(self):
        return f"{self.name} {self.surname}"

    def get_info(self):
        return f"{self.name} {self.surname} {self.year}-yili tug'ilgan va hozirda {yil - self.year} yoshda. {self.adress} da yashaydi"

    def get_age(self):
        return f"{self.name} {yil - self.year} yoshda"
    
    def change_adress(self, new_adress):
        self.adress = new_adress      
        return f"{self.name}ning manzili {self.adress}ga o'zgardi "  


nozima  = Inson("Zuhra", "Abduboqiyeva", 2011, "Namangan region, Mingchinor street")
olimjon  = Inson("Olimjon", "Murodov", 2022, "Namangan region, Mingchinor street")

# print(nozima)
# print(olimjon)
# print(nozima.get_info())
# print(olimjon.get_info())
# print(nozima.get_age())
# print(olimjon.get_age())
# print(nozima.change_adress("Andijon viloyati, Baliqchi tumani"))
# print(olimjon.change_adress("Farg'ona viloyati, Oltiariq tumani"))

# print(nozima.get_info())
# print(olimjon.get_info())



class Student:
    """ O'quvchi classi """
    def __init__(self, full_name:str, year:int, marks:list,friends:list, facultety:str,level=1,):
        """ Student haqidagi malumotlarni o'zida saqlovchi funksiya """
        self.full_name = full_name
        self.year = year
        self.marks = marks
        self.friends = friends
        self.faculty = facultety
        self.level = level

    def get_name(self):
        return self.full_name
    
    def get_info(self):
        return f"{self.full_name} {self.year} yoshda. Va u {self.level} - bosqich talabasi "
    
    def get_marks(self):
        info =  f"{self.full_name}ning olgan baholari: "
        for mark in self.marks:
            info += f"{mark} "
        return info

    def get_friends(self):
        text = f"{self.full_name}ning ulfatlari: "
        for frined in self.friends:
            text += f"{frined}  "
        return text
     
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

baxolar = [3,7,5,3,2,1,8]
friends = ['Ali', "Olim", "Hasan", "Husan", "Vali"]

student1 = Student("Aziz Alimov",23,baxolar, friends, 'Matematika', 4)
student2 = Student("Olimjon", 43,baxolar, friends, "Ingliz tili", 2)
student3 = Student("Boburov", 1999, baxolar, friends, "Shifokor")
student4 = Student("Nodira Jamilova", 2002, [7,7,8,3,5,7], ['Guli', "Aziza", "Husnora", "Madina", "Barno"], 'Rus tili')

print(student1.get_marks())
print(student1.get_friends())

print(student1.get_faculty())
print(student1.set_faculty('Iqtisot'))
print(student1.get_faculty())









