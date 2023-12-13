def elements_parells(a):
    for i, e in enumerate(a):
        if i % 2 == 0:
            print(e)

def llegir_llista():
    l = []
    a = ''
    while a != '.':
        a = input("Introdueixi una nova paraula o punt (.) per acabar: ")
        if a != '.':
            l.append(a)
    return l

# Programa Principal
b = llegir_llista()
elements_parells(b)
