def es_vocal(a):
    return a.lower() in ['a','e','i','o','u']
lletra = input('Introdueix una lletra per a veure si és vocal o no: ')
if es_vocal(lletra):
    print("És vocal")
else:
    print("No és vocal")