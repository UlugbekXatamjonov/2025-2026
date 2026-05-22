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
print(nozima.change_adress("Andijon viloyati, Baliqchi tumani"))
print(olimjon.change_adress("Farg'ona viloyati, Oltiariq tumani"))

print(nozima.get_info())
print(olimjon.get_info())












