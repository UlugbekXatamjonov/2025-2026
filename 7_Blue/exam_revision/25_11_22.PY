""" 1-mashq """
books = []
books_count = int(input("Bu yil nechta kitob o'qidingiz: "))

for b in range(books_count):
    books.append(input(f"{b+1}-kitob nomini kiriting: "))

print(books)

""" 3-mashq """
mevalar = ["olma", "gilos", "oshqovoq", "sabzi", "anjir", "malina"]

for meva in mevalar:
    if meva == 'oshqovoq' or meva == 'sabzi':
         print(meva.upper())
    else:
        print(meva.capitalize())


""" 4-mashq """

from math import sqrt    
    
sonlar = list(range(205, 2024))

for son in sonlar:
    if son < 1000:
        print(f"{son} ning 3-darajasi {son**3} ga teng.")
    elif son > 1500:
        print(f"{son} dan 3 ta kichik son {son-3} ga teng.")
        
for son in sonlar:
    if son%25 == 0:
        print(f"{son} ning ildizi {sqrt(son)} ga teng")


""" 5-mashq """

sonlar = []

for son in range(5):
    sonlar.append(int(input(f"{son+1}- kiriting: ")))
    
for son in sonlar:
    if son < 0:
        print(f"{son}bu son manfiy va uning 5 darajasi {son**5} ga teng.")

    elif son > 0:
        print(f"{son}bu son musbat va uning 4 darajasi {son**4} ga teng.")




