def soma_numeros_pares():
    soma = 0
    for numero in range(50, 101, 2):
        soma += numero
    return soma

resultado = soma_numeros_pares()
print("A soma dos numeros pares entre 50 e 100:", resultado)