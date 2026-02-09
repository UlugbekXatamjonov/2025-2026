def add(a, b): 
    return a + b

def sub(a, b): 
    return a - b

def mul(a, b): 
    return a * b

def div(a, b): 
    return a / b


while True:
    try:
        a = float(input("1-son: "))
        b = float(input("2-son: "))
        op = input("Amal (+ - * /): ")

        if op == "+":
            print(add(a, b))
        elif op == "-":
            print(sub(a, b))
        elif op == "*":
            print(mul(a, b))
        elif op == "/":
            print(div(a, b))
        else:
            print("❌ Noto‘g‘ri amal")
    except ZeroDivisionError:
        print("❌ 0 ga bo‘lib bo‘lmaydi")
    except ValueError:
        print("❌ Son kiriting")

    if input("Davom etamizmi? (no): ") == "no":
        break
