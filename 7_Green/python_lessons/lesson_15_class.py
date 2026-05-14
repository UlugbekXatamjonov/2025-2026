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

    def overall_ball(self):
        """ ummumiy ballni hisoablab beradi """
        return sum(self.ballar)

    def middle_ball(self):
        """ o'rtacha bahoni hisoblab beradi """
        return sum(self.ballar) / len(self.ballar)

    def change_class(self):
        if 1 <= self.sinf < 11:
            self.sinf += 1
            return f"Siz endi {self.sinf} ga o'tdingiz !"
        else:
            return f"Siz endi yangi sinfga o'ta olmaysiz !"


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
# print(saida.get_friends())
# print(saida.delete_friend("Oysha"))
# print(saida.delete_friend("Muhammadyusuf"))

# print(saida.get_info())
# print(saida.change_class())
# print(saida.change_class())
# print(saida.change_class())
# print(saida.change_class())
# print(saida.change_class())
# print(saida.change_class())
# print(saida.get_info())


class Book:
    """ Kitob haqidagi class """
    def __init__(self, name:str, author:str, year:int, price:int, pages:int, heroes:list):
        self.name = name
        self.author = author
        self.year = year
        self.price = price
        self.pages = pages
        self.heros = heroes
    
    def __str__(self):
        return f"{self.name} - {self.author}"

    def get_book_info(self):
        return f"\"{self.name}\" kitobining muallifi {self.author}. Kitob {self.year}-yili chiqarilgan. Narxi {self.price} so'm va u {self.pages} sahifadan iborat"

    def change_price(self, new_price):
        self.price = new_price
        return f"Kitobning yangi narxi {self.price} so'm"


book1 = Book("101 day", "Jek Darken", 2019, 45_000, 340, ['Jek', 'Antony', 'Lily'])
book2 = Book("Bad habbits", "Drayn Pool", 1988, 23_00, 160, ['Sara', 'Hook', 'Anna', 'Tom'])

print(book1)
print(book2)
print(book1.get_book_info())
print(book2.get_book_info())
print(book2.change_price(23000))
print(book2.get_book_info())



class MyLibrary:
    """ Kutubxona classi """
    def __init__(self, name, addres):
        self.name = name
        self.adress = addres
        self.books = [] # kitoblar
        self.books_count = 0 # kitoblar miqdori
        
    def get_info(self):
        text = f"{self.name} kutubxonasining Manzili: {self.adress} "
        text += f"Kitoblar soni {self.books_count} ta. "
        return text
    
    def add_book(self, new_book):
        self.books.append(new_book)
        self.books_count += 1

