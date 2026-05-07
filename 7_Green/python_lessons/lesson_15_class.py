from datetime import date
this_year = date.today().year

class Student: # class
    """ O'quvchi haqidagi klass """
    """ dunder - duble under score """
    def __init__(self, ism:str, familiya:str, t_yil:int, manzil:str, sinf:int, dostlar:list, ballar:list): # class ning xususiystlarini o'zida saqlovchi funksiya
        self.ism = ism # class ning xususiyati 
        self.familiya = familiya # class ning xususiyati
        self.t_yil = t_yil # class ning xususiyati
        self.manzil = manzil
        self.sinf = sinf
        self.dostlar = dostlar
        self.ballar = ballar

    def __str__(self): 
        return f"O'quvchi: {self.ism} {self.familiya}"
    
    def get_info(self): # metod
        return f"{self.ism} {self.familiya} {self.t_yil} yilda tug'ilgan va u {self.manzil}da yashaydi. Hozirda {self.sinf} sinf o'quvchisi"

    def get_age(self):
        return f"{self.ism} {this_year-self.t_yil} yoshda"

    def get_adress(self):
        return f"{self.ism}ning manzili  {self.manzil}"
    
    def get_friends(self):
        """ """
        return f"{self.ism}ning dostlari {self.dostlar}"

    def add_friend(self, new_frined):
        self.dostlar.append(new_frined)

        return f"{new_frined} do'stlaringiz qatoriga qo'shildi"

    def delete_friend(self, delf):
        if delf in self.dostlar:
            self.dostlar.remove(delf)
            return f"{delf} do'stlaringiz qatoridan o'chirildi !"
        else:
            return f"{delf} sizning do'stingiz emas ! uni o'chira olmaysiz !"
        
dilmurod = Student("Dilmurod", 'Osimjonov', 2013, "To'raqo'rg'on tumani", 7, ["Siadakbar", "Isroil", "Muhammadyusuf", "Abror"],[50, 40, 35, 45]) # obyekt
saida = Student("Saida", "Tursunboyeva", 2012, "To'raqo'rg'on tumani", 7, ['Nodira', "Oysha", "Nigora"], [45, 36, 29, 50]) # obyekt


# print(dilmurod)
# print(saida.familiya)
# print(saida.sinf)
# print(saida.manzil)
# print(saida.get_info())
# print(dilmurod.get_info())
# print(saida.get_age())
# print(dilmurod.get_adress())
# print(saida.get_adress())
# print(saida.add_friend("Mehridil"))
print(saida.get_friends())
print(saida.delete_friend("Oysha"))
print(saida.delete_friend("Muhammadyusuf"))

print(saida.get_friends())






