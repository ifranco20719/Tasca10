#Funcions
def menu_principal():
    print("""
          Menú Principal
          1.Calculadora enters
          2.Calculadora reals
          3.Sortir
          
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
    b = 1
    while b>0:
        print("""
            Menú reals
              1. Sumar
              2. Restar
              3. Multiplicar
              4. Dividir
              5. Tornar al menú principal
              """)
#Progama principal
a = 1
while a>0:
    a = menu_principal()
    match a:
        case 1:
            Calculadora_enters()
        case 2:
            Calculadora_reals()
        case 3:
            a = -1
        case other:
            print('Opció no vàlida')