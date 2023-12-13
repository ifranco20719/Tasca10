def crear_repetits(a, b):
    c = b * int(a)
    return c

x = input("Introdueixi un número: ")
y = input("Introdueixi un caràcter: ")

print("El caràcter", y, "repetit", x, "-vegades és:", crear_repetits(x, y))
