"""
While tsikli
"""

""" for() """
sonlar = [1,2,3,4,5,6,7,8,9,10]
for son in sonlar:
    print(son)


""" 3 """
while True: # abadiy tsikl
    savol = input("son kiriting: ")
    if savol == 'exit':
        break # tsiklni to'xtatish uchun 
    elif savol.isdigit():
        savol = int(savol)
        print(f"{savol} ning kavadrati {savol**2}")
    else:
        print("son kiriting!!!")



""" Tug'ilgan yil """
while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():
        yosh = int(yosh)
        print(f"Siz {2025-yosh}-yilda tug'ilgansiz")
    
    elif yosh == "exit":
        print("Dastur tugadi")
        break
    
    else:
        print("Siz son kiritmadingiz !!!")
 

""" Abadiyt tsikl """
x = 1
while x < 10:
    print(x)


""" ishora | 1-0"""
print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")

ishora = True
while ishora: # = while True -> abadiy tsikl
    savol = input("Istalgan son kiriting(dasturni to'xtatish uchun 'exit' deb yozing):")
    if savol == 'exit':
        ishora = False # dastur to'xtashi uchun
        
    elif savol.isdigit():
        print(int(savol)**2)
    else:
        print("Siz son kiritmadingiz!!!")


""" continue """
sonlar = [1,2,3,4,5,6,7,8,9,10]
for son in sonlar:
    if son == 6:
        continue # davom etish / bu holatda 6 ni tashlab o'tib ketadi
    else:
        print(son, end=' ')



""" parol tizimi """ 
parol = "www"
while True:
    savol = input("Parolni kiriting: ")
    if savol == parol:
        break
    else:
        print("parol xato !!!")
        
""" 
1) Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rab biror ro'yhatga qo'shib yig'ing. 
    Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating.
    
2) Foydalanuvchidan uning ismini so’rang agar uning ismi “Abbos” bo’lsa dasturni to’xtating. Aks holda dastur ism so’rashda davom etaversin.

3) Foydalanuvchidan son kiritishini so'rang. agar u faqat manfiy(-) son kiritsa dastur to'xtasin.

4)  Foydalanuvchidan son olib, son juft yoki toqligini topuvchi dastur tuzing.
    Dastur faqat  “chiqish” so’zi kiritilganda to’xtasin.

5)  Foydalanuvchidan yaxshi ko'rgan ismlarini kiritishni so'rang va ismlar  degan ro'yhatga qo'shing. 
    Foydalanuvchi "stop" so'zini yozishi bilan dasturni to'xtating. va ro'yhatdagi ismlar nomini chiqaring

6)  Foydalanuvchidan yaxshi ko'rgan mashinalari nomini kiritishni so'rang  va ularni cars degan ro’yhatga  yig’ing.  
    Foydalanuvchi exit so'zini yozishi bilan dasturni to'xtating va ro’yhatdagi mashinalarni konsulga chiqaring.

7) Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 
    7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. 
    Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va 
    chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur 
    to'xtasin (ikkita shartni ham tekshiring)

8)  Foydalanuvchidan tizimga kirishi uchun parol so'rang, foydalanuvchi to'gri javob 
    kiritsa unga 'hush keib siz' degan habar chiqsin va dastur to'xtasim. 
    Agar foydalanuvchi 3 marta xato parol kiritsa uni abadiy tsiklga tushurib qo'ying.  

9) "Son topish" o'yinini while yordamisa shunday qilingki, dastur faqat "exit" so'zi kiritilganda to'xtasin, 
    hamda foydalanuvchi va komputerning  nechta g'alaba qozonganini ham hisoblasin.

10) "Tosh, qaychi, qog'oz" o'yinini ham yuqoridagi mashq kabi bajaring.

11) Online bozor loyihasini qiling. Avvaliga foydalanuvchiga do'koningizdagi mahsulotlarni nomi va narxini ko'rsating,
    song foydalanuvchidan nima olishini so'rang, keyin xaridni davom etirasizmi yoki yo'q deb so'rang
    agar ha desa yana mahsulot nomini so'rang, agar yoq dasa jarayoni tugatib, sotib olgan mahsulotlari va 
    ularning narxini ko'rsating. 

12) 1 dan 100 gacha bo‘lgan sonlar yig‘indisini while yordamida, sum() funksiyasini ishatmasdan topishga harakat qiling.

"""


