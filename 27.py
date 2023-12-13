def majuscules(llista):
    result = []
    for palabra in llista:
        if any(char.isupper() for char in palabra):
            result.append(palabra)
    return result

llista = input("Ingrese una lista de palabras separadas por comas: ").split(',')

resultat = majuscules(llista)

print("Les paraules que tenen majúscula són:", resultat)