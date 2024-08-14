# Dicionário com informações sobre o estoque de produtos
estoque = {
    "tomate": [1000, 2.30],  # estoque disponível, custo por unidade
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijao": [100, 1.50],
}

# Função para determinar o preço mais alto e o mais baixo em um dicionário
def encontrar_maior_menor_valor(dicionario):
# Retorna None para ambos os valores se o dicionário estiver vazio
if not dicionario:
        return None, None

# Define valores iniciais extremos para comparações
maior_valor = float('-inf')  # Menor possível valor inicial
menor_valor = float('inf')   # Maior possível valor inicial

# Percorre cada item do dicionário para comparar preços
for chave, dados in dicionario.items():
    valor = dados[1]  # O preço é o segundo item da lista associada
    # Atualiza o maior valor se o valor atual for maior
    if valor > maior_valor:
    maior_valor = valor
        # Atualiza o menor valor se o valor atual for menor
        if valor < menor_valor:
            menor_valor = valor

# Retorna os valores máximo e mínimo encontrados
return maior_valor, menor_valor

# Executa a função e armazena o maior e o menor valor encontrados
maior, menor = encontrar_maior_menor_valor(estoque)

# Imprime os valores máximo e mínimo
print("Maior valor:", maior)
print("Menor valor:", menor)
