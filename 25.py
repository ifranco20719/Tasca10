def paraula_mes_gran(a):
    a.sort(key=lambda x: len(x))
    return a[-1]

# Programa principal
x = ["hola", "Adeu", "Si", "Matematics", "Alcaufar de Sant Roc", "Un senyor damunt un ruc, el ruc va caure"]
print("La paraula més llarga és:", paraula_mes_gran(x))