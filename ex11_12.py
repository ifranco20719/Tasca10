#Funcions
def menu_principal():
    print("""
          Menú Principal
          1.Calculadora enters
          2.Calculadora reals
          3.Canvis base
          4.Sortir
          
    """)
    a = int(input("Tria una opció: "))
    return a
def Calculadora_enters():
    op = 1
    while op>0:
        print("""
            Menú enters
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Sortir
        """)
        op = int(input("Elegeix una opció: "))
        match op:
            case 1: # Sumar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introsueix el segon nombre: "))
                print("{} + {} = {}".format(x, y, x+y))
            case 2: # Restar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introsueix el segon nombre: "))
                print("{} - {} = {}".format(x, y, x-y))
            case 3: # Multiplicar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introsueix el segon nombre: "))
                print("{} * {} = {}".format(x, y, x*y))
            case 4: # Dividir
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introsueix el segon nombre: "))
                print("{} / {} = {}".format(x, y, x/y))
            case 5: # Sortir
                print("Adéu, ja tornara a la calculadora inicial \n\n")
                op = -1

def Calculadora_reals():
    op = 1
    while op>0:
        print("""
            Menú enters
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Sortir
        """)
        op = int(input("Elegeix una opció: "))
        match op:
            case 1: # Sumar
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Introsueix el segon nombre: "))
                print("{} + {} = {}".format(x, y, x+y))
            case 2: # Restar
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Introsueix el segon nombre: "))
                print("{} - {} = {}".format(x, y, x-y))
            case 3: # Multiplicar
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Introsueix el segon nombre: "))
                print("{} * {} = {}".format(x, y, x*y))
            case 4: # Dividir
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Introsueix el segon nombre: "))
                print("{} / {} = {}".format(x, y, x/y))
            case 5: # Sortir
                print("Adéu, ja tornaràs a la calculadora inicial \n\n")
                op =-1

# Funcions canvis de base
# De decimal a binari, octal i hexadecimal
def dectobin(numero):
    # Prec: numero sigui enter
    # Post: Escriu el valor de l'enter en binari
    return bin(numero)
def dectooct(numero):
    # Prec: numero sigui enter
    # Post: Escriu el valor de l'enter en octal
    return oct(numero)
def dectohex(numero):
    # Prec: numero sigui enter
    # Post: Escriu el valor de l'enter en hexadecimal
    return hex(numero)
# De binari a octal, decimal i hexadecimal
def bintooct(numero):
    # Prec: numero sigui binari
    # Post: Escriu el valor del binari en octal
    a=int(numero,2)
    return dectooct(a)
def bintodec(numero):
    # Prec: numero sigui binari
    # Post: Escriu el valor del binari en decimal
    a=int(numero,2)
    return a
def bintohex(numero):
    # Prec: numero sigui binari
    # Post: Escriu el valor del binari en hexadecimal
    a=int(numero,2)
    return dectohex(a)
# De octal a binari, decimal i hexadecimal
def octtobin(numero):
    # Prec: numero sigui octal
    # Post: Escriu el valor de l'octal en binari
    a = int(numero,8)
    return dectobin(a)
def octtodec(numero):
    # Prec: numero sigui octal
    # Post: Escriu el valor de l'octal en decimal
    a = int(numero,8)
    return a
def octtohex(numero):
    # Prec: numero sigui octal
    # Post: Escriu el valor de l'octal en hexadecimal
    a=int(numero,8)
    return dectohex(a)
def hextonum(hex):
    pnum = {
        "f": 15,
        "e": 14,
        "d": 13,
        "c": 12,
        "b": 11,
        "a": 10,
    }
    if hex in pnum:
        return pnum[hex]
    else:
        return int(hex)
def hextodec2(hex):
    hex = hex.lower()
    hex = hex[::-1]
    decimal = 0
    posicio = 0
    for digit in hex: 
        valor = hextonum(digit)
        elevat = 16 ** posicio
        pnum = elevat * valor
        decimal += pnum
        posicio += 1
    return decimal
def hextobin(numero):
    a=int(numero,16)
    return dectobin(a)
def hextooct(numero):
    a=int(numero,16)
    return dectooct(a)
def hextodec(numero): 
    a = int(hextodec2(numero))
    return a

def canvis_base():
    op = 1
    while op>0:
        print("""
            Menú canvis de base
            1. Donat un binari ho passem a tota la resta
            2. Donat un octal ho passem a tota la resta
            3. Donat un decimal ho passem a tota la resta
            4. Donat un hexadecimal ho passem a tota la resta
            5. Sortir
        """)
        op = int(input("Elegeixi una opció: "))
        match op:
            case 1: # Binari to
                b = input("Introdueixi el número binari: ")
                o = bintooct(b)
                d = bintodec(b)
                h = bintohex(b)
                print("El número binari {} és: \n oct -> {} \n dec -> {} \n hex -> {}".format(b,o,d,h))
            case 2: # Octal to
                o = input("Introdueixi el número octal: ")
                b = octtobin(o)
                d = octtodec(o)
                h = octtohex(o)
                print("El número octal {} és: \n bin -> {} \n dec -> {} \n hex -> {}".format(b,o,d,h))
            case 3: # Decimal to
                d = input("Introdueixi el número decimal: ")
                b = dectobin(d)
                o = dectooct(d)
                h = dectohex(d)
                print("El número decimal {} és: \n oct -> {} \n bin -> {} \n hex -> {}".format(b,o,d,h))
            case 4: # Hexadecimal to
                h = input("Introdueixi el número hexadecimal: ")
                b = hextobin(h)
                o = hextooct(h)
                d = hextodec(h)
                print("El número hexadecimal {} és: \n oct -> {} \n dec -> {} \n bin -> {}".format(b,o,d,h))
            case 5: # Sortir
                print("Adéu, ja tornaràs a la calculadora inicial \n\n")
                op=-1
# Progama principal
a = 1
while a>0:
    a = menu_principal()
    match a:
        case 1:
            Calculadora_enters()
        case 2:
            Calculadora_reals()
        case 3:
            canvis_base()
        case 4:
            a = -1
        case other:
            print('Opció no vàlida')