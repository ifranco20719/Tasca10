a = int(input("Introdueix el primer nombre: "))
b = int(input("Introdueix el segon nombre: "))

def gran():
    if a>b:
        return a
    elif a<b:
        return b
    else:
        print("Són iguals")

print(gran())