"""
2-mashq | 2 dan 100 gacha bo'lgan barcha toq sonlarning:

1) 5 chi va 7 chi darajasini toping;
2) Ro'yhatdagi har bir sondan 4 taga kichik sonni konsulga chiqaring;
3) Ro'yhatdagi har bir sonning 4 -darajasini toping;
"""


"""
Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, 
va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga qo'shing. Ro'yxatni konsolga chiqaring.
"""

odamlar = []
odamlar_soni = int(input("Nechta inson bilan ko'rishdingiz: "))

for o in range(odamlar_soni):
    odamlar.append(input(f"{o+1}-inson ismini kiriting: "))

print(odamlar)









