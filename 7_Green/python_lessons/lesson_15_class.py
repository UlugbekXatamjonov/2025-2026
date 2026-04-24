class Student: # class
    """ O'quvchi haqidagi klass """
    def __init__(self, ism:str, familiya:str, yosh:int, manzil:str, sinf:int): # class ning xususiystlarini o'zida saqlovchi funksiya
        self.ism = ism # class ning xususiyati 
        self.familiya = familiya # class ning xususiyati
        self.yosh = yosh # class ning xususiyati
        self.manzil = manzil
        self.sinf = sinf


dilmurod = Student("Dilmurod", 'Osimjonov', 12, "To'raqo'rg'on tumani", 7) # obyekt
saida = Student("Saida", "Tursunboyeva", 14, "To'raqo'rg'on tumani", 7) # obyekt






