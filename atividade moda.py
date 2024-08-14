def calcular_moda(lista):
    frequencias = {}
    for elemento in lista:
        if elemento in frequencias:
            frequencias[elemento] += 1
        else:
            frequencias[elemento] = 1

    moda = []
    maior_frequencia = 0

    for elemento, frequencia in frequencias.items():
        if frequencia > maior_frequencia:
            moda = [elemento]
            maior_frequencia = frequencia
        elif frequencia == maior_frequencia:
            moda.append(elemento)

    return moda, maior_frequencia


# Entrada dos dados
lista = []
for i in range(10):
    elem = int(input('Digite um elemento da lista: '))
    lista.append(elem)

# Resultados
moda, frequencia = calcular_moda(lista)
print('Lista:', lista)
print('Moda:', moda)
print('Frequência:', frequencia)
