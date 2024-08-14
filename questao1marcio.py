# Função para calcular a frequência de cada caractere em uma string
def contar_caracteres(frase):
# Inicializa um dicionário para registrar a quantidade de cada caractere
contagem = {}

# Percorre cada caractere na string fornecida
for caractere in frase:
     # Se o caractere já estiver presente no dicionário, atualiza sua contagem
     if caractere in contagem:
            contagem[caractere] += 1
        # Caso o caractere não esteja no dicionário, adiciona-o com contagem inicial de 1
        else:
            contagem[caractere] = 1

 # Devolve o dicionário contendo a frequência de cada caractere
return contagem


# Solicita ao usuário que insira uma frase
frase = input("Digite uma frase: ")

# Executa a função de contagem e armazena o resultado
resultado = contar_caracteres(frase)

# Mostra a frequência de cada caractere na frase inserida
print("Contagem de caracteres:", resultado)
