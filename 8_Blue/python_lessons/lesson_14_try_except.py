try:
    son  = int(input("Son kiriting: "))
except:
    print("dasturda xatolikj bo'ldi")
else:
    print(f"{son} ning kvadrati {son**2} ga teng")

print("dasturning davomi ...")
print("dasturning davomi ...")
print("dasturning davomi ...")
print("dasturning davomi ...")


try:
    son1  = int(input("Son kiriting: "))
    son2  = int(input("Son kiriting: "))
    print(f"{son1}:{son2}={son1/son2}")
except ZeroDivisionError:
    print("0 ni kiritmang !")
except ValueError:
    print("Faqat son kiritishingiz kerak !!")
except:
    print("Xatolik !!!")





