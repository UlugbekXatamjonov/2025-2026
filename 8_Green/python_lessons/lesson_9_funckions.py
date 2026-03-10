"""
Thame: Funkcions - Funksiyalar
"""
"""
Funksiya - Funksiya ma'lum bir vazifani bajarishga mo'ljallangan kodlar yig'indisi.
Biz shu vaqtgacha ko'rib o'tgan funksiyalar: print(), len(), sum(), max(), min()...

Nega funksiya kerak?
    ✔ Kodni takrorlamaslik
    ✔ Kodni tushunarli qilish
    ✔ Katta loyihani bo'laklash
    ✔ Xatolarni oson topish
    ✔ Professional dasturchilik asosi

    ❌ Funksiyasiz kod — tartibsiz va chalkash bo'ladi"""


""" Funksiya yasash """
def salom():
    """ Ushbu funksiyaning vazifasi Salomlashish """
    
    return "Assalom aleykum"
# salom()


""" DOCSTRING """
""" 
    DOCSTRING ---> Defenition
    Docstringni konsolga chiqarish uchun print(funksiya_nomi.__doc__) deb ham yozishimiz mumkin: 
"""

# print(len.__doc__)


def salom_ber(ism):
    """ Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya. ism -> Matn kiritish kerak """
    return f"Assalomu alaykum, hurmatli {ism}!"
    
# salom_ber("Ali")
# salom_ber("Vali")
# salom_ber('Umar')


"""
    Funksiyaga nom berishda fe'l, ya'ni harakatni bildiruvchi so'zlar yoki jumlalardan foydalaning. 
    Bu bilan siz o'zgaruvchi va funksiya o'rtasini farqlashingiz oson bo'ladi. 
    Misol uchun, yuqorida biz funksiyamizni salom emas salom_ber deb nomladik.
"""

""" Funksiyaga qiymat uzatish """
def hisobla(tyil, yil):
    """
    Foydalanuvchi yoshini hisoblovchi funksiya. 
    tyil - Tug'ilgan yilingizni kiriting
    yil- hozirgi yil
    """
    yosh = yil - tyil
    
    return f"Siz {yosh} da ekansiz"
    
# hisobla(2023, 2000)
# hisobla(2001, 2023)


""" Argumentni kalit so'z bilan uzatish """
def plus(son1, son2):
    """ Foydalanuvchi kiritgan sonlarni bir biriga qo'shib beradi. """
    son3 = son1 + son2
    
    return f"Siz kiritgan {son1} va {son2} larning yig'indisi {son3} ga teng."
# plus(son2=5, son1=5)


def full_name(name, surname, father):
    """
    full_name - To'liq ism sharifni qaytarish uchun funksiya
    
    Arguments:
        name - str
        suename - str
        father - str 
    """
    
    return f"{surname} {name} {father}"

# full_name(name="Olimjon", surname="Aliyev", father="Baxodirovich")



""" Standar qiymat uzatish """
"""
    Funksiya yaratishda, standart qiymatga ega parametrlar doim oxirida yozilishi kerak. 
    Aks holda xatolik yuzaga keladi.
"""     
def full_name(familya, ism="Ali"):
    return ism, familya
    
# full_name(familya = "Olimmov")
# full_name("Asadbek","Mirzanvarov")


def kv(son=5):
    """ Kiritilgan sonning kvadratini hisoblovchi funksiya, son - int"""
    son_kv = son**2
    
    return f"Siz kiritgan {son} ning kvadrati {son_kv} ga teng"
# kv(4)
# kv()



""" Funksiyadan sodda qiymat emas, ro'yxat, lu'gat va boshqa ma'lumot turlarini ham  
    qaytarishimiz mumkin """
    
""" Funksiyadan lug'at qaytarish """
def person_info(name, surname, birth, gender, age, job=None):
    """ Inson haqidagi malumotlarni qaytaruvchi funksiya """
    person = {
        'name': name,
        'surname': surname,
        "birth": birth,
        "gender": gender,
        "age": age,
        "job": job
    }
    return person



""" Funksiyadan ro'yhat qaytarish """
def oila(n):
    """ Oila azolaringizning ismini ro'yhat holatida qaytaruvchi funksiya """
    oila = []
    for i in range(n):
        azo = input(f"{i+1}- oila azongizning ismi :")
        oila.append(azo)
        
    return oila

# oila1 = oila(4)
# oila2 = oila(7) 
# print(oila1)
# print(oila2)


""" *args - arguments --> istalgancha parametr berish imkonini beradi """
def our_max(*sonlar:int) ->int:
    """  """
    for son in sonlar:
        

print(our_max(23, 45))
print(our_max(43, 5435, 5 ,36,3 ,3, 45634, 98 ,34 ,3 ))


def our_min(*sonlar:int) ->int:
    """  """
    sonlar = sorted(sonlar)
    return sonlar[0]
# print(our_min(-63, 34, 9, 54, 343, 0, -55))

def our_sum(*sonlar:int) ->int:
    """  """
    summa = 0
    for son in sonlar:
        # summa = summa + son
        summa += son
   
    return summa

# print(our_sum(1,2,3,4,5,6,7,8,9,10))  
# print(our_sum(1,2,3,4,5))  
