def comptar_vocals(a):
    b = ('a', 'e', 'i', 'o', 'u', 'altres')
    vocals = [0, 0, 0, 0, 0, 0]
    for i, e in enumerate(a):
        if e in ['a', 'A', 'à', 'á', 'À', 'Á']:
            vocals[0] += 1
        elif e in ['e', 'E', 'è', 'é', 'È', 'É']:
            vocals[1] += 1
        elif e in ['i', 'I', 'í', 'Í']:
            vocals[2] += 1
        elif e in ['o', 'O', 'ò', 'ó', 'Ò', 'Ó']:
            vocals[3] += 1
        elif e in ['u', 'U', 'ú', 'Ú']:
            vocals[4] += 1
        else:
            vocals[5] += 1
    for i, e in enumerate(vocals):
        print("La vocal {} apareix {} vegades".format(b[i], vocals[i]))

# Programa Principal
a = input("Introdueixi una paraula a analitzar: ")
comptar_vocals(a)
