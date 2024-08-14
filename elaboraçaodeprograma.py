def separar_positivos_negativo(lista):
    positivos = []
    negativos = []

    for i in lista:
        if i >= 0:
            positivos.append(i)
        else:
            negativos.append(i)

    return positivos, negativos

lista_numeros = [1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
positivos, negaivos = separar_positivos_negativo(lista_numeros)

print("numeros positivos:", positivos)
print("numeros negativos:", negativos)
