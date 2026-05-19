"""
OOP - Opject orented programming 
"""

class Inson:
    """  """
    def __init__(self, name:str, surname:str, year:int, adress:str):
        self.name = name
        self.surname = surname
        self.year = year
        self.adress = adress

    def __str__(self):
        return f"{self.name} {self.surname}"




nozima  = Inson("Nozima", "Xasanova", 2012, "Namangan region, Mingchinor street")
olimjon  = Inson("Olimjon", "Murodov", 2022, "Namangan region, Mingchinor street")

print(nozima)
print(olimjon)













