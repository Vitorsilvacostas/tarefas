# Dicionário que armazena o estoque dos produtos. Cada chave é o nome do produto, e o valor é uma lista onde
# o primeiro item é a quantidade em estoque e o segundo item é o preço por unidade.
estoque = {
    "tomate": [1000, 2.30],  # Quantidade 1000 e preço 2.30
    "alface": [1000, 1.30],  # Quantidade 1000 e preço 1.30
    "batata": [500, 2.60],   # Quantidade 500 e preço 2.60
    "feijao": [200, 5.30]    # Quantidade 200 e preço 5.30
}

total = 0  # vai Inicializar a variável total das vendas
print("Vendas:\n")  # Imprime o título para a seção de vendas

# Inicia um loop infinito para processar vendas até que o usuário decida sair
while True:
    produto = input("Nome do produto (fim para sair):")  # solicita o nome do produto ao usuario
    if produto == "fim":  # Verifica se o usuário digitou "fim" para encerrar o loop
    break  # Sai do loop se "fim" for digitado

if produto in estoque:  # Verifica se o produto está no estoque
quantidade = int(input("quantidade:"))  # Solicita a quantidade do produto ao usuário
    if quantidade <= estoque[produto][0]:  # Verifica se a quantidade solicitada é menor ou igual à disponível
       preço = estoque[produto][1]  # Obtém o preço do produto
       custo = preço * quantidade  # Calcula o custo total da venda

     # Imprime detalhes da venda formatados: nome do produto, quantidade, preço por unidade e custo total
     print(f"{produto:12s} {quantidade:3d} x {preço:6.2f} = {custo:6.2f}")
     estoque[produto][0] -= quantidade  # Atualiza a quantidade em estoque após a venda
     total += custo  # Adiciona o custo da venda ao total
    else:
            print("Quantidade solicitada não disponível")  # mostra a quantidade solicitada não está disponível
    else:
        print("Nome de produto inválido")  # mostra que o nome do produto não é válido

# Imprime o custo total das vendas formatado com duas casas decimais
print(f" Custo total: {total:21.2f}\n")

print("Estoque:\n")  # Imprime o título para a seção de estoque

# Itera sobre cada item no dicionário de estoque
for chave, dados in estoque.items():
    print("Descrição: ", chave)  # Imprime o nome do produto
    print("Quantidade: ", dados[0])  # Imprime a quantidade restante em estoque
    # Imprime o preço por unidade formatado com duas casas decimais
    print(f"Preço: {dados[1]:6.2f}\n")
