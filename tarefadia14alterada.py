# Inicia a lista vazia para armazenar os contatos
agenda = []

# Variável para marcar uma alteração na agenda
alterada = False


# Função para pedir o nome do contato, com um valor padrão opcional
def pede_nome(padrão=""):
    nome = input("Nome: ")
    if nome == "":
        nome = padrão
    return nome


# Função para pedir o telefone do contato, com um valor padrão opcional
def pede_telefone(padrão=""):
    telefone = input("Telefone: ")
    if telefone == "":
        telefone = padrão
    return telefone


# Função para pedir o endereço do contato, com um valor padrão opcional
def pede_endereço(padrão=""):
    endereço = input("Endereço: ")
    if endereço == "":
        endereço = padrão
    return endereço


# Função para pedir a cidade do contato, com um valor padrão opcional
def pede_cidade(padrão=""):
    cidade = input("Cidade: ")
    if cidade == "":
        cidade = padrão
    return cidade


# Função para pedir o estado do contato, com um valor padrão opcional
def pede_uf(padrão=""):
    uf = input("UF: ")
    if uf == "":
        uf = padrão
    return uf


# Função para exibir os dados de um contato (nome, telefone, endereço, cidade, uf)
def mostra_dados(nome, telefone, endereço, cidade, uf):
    print(f"Nome: {nome} Telefone: {telefone} Endereço: {endereço} Cidade: {cidade} UF: {uf}")


# Função para pedir o nome do arquivo para salvar ou ler
def pede_nome_arquivo():
    return input("Nome do arquivo: ")


# Função para pesquisar um contato na agenda pelo nome
def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None


# Função para verificar se um nome já existe na agenda
def nome_existe(nome):
    return pesquisa(nome) is not None


# Função para adicionar um novo contato à agenda
def novo():
    global agenda, alterada
    nome = pede_nome()

    # Verifica se o nome já existe na agenda
    if nome_existe(nome):
        print("Erro: O nome já existe na agenda.")
        return

    telefone = pede_telefone()
    endereço = pede_endereço()
    cidade = pede_cidade()
    uf = pede_uf()
    agenda.append([nome, telefone, endereço, cidade, uf])
    alterada = True


# Função para confirmar uma operação com o usuário (S/N)
def confirma(operação):
    while True:
        opção = input(f"Confirma {operação} (S/N)? ").upper()
        if opção in "SN":
            return opção
        else:
            print("Resposta inválida. Escolha S ou N.")


# Função para apagar um contato da agenda
def apaga():
    global agenda, alterada
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        if confirma("apagamento") == "S":
            del agenda[p]
            alterada = True
    else:
        print("Nome não encontrado.")


# Função para alterar os dados de um contato existente
def altera():
    global alterada
    p = pesquisa(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        endereço = agenda[p][2]
        cidade = agenda[p][3]
        uf = agenda[p][4]
        print("Encontrado:")
        mostra_dados(nome, telefone, endereço, cidade, uf)
        nome_novo = pede_nome(nome)

        # Verifica se o novo nome já existe na agenda
        if nome_novo != nome and nome_existe(nome_novo):
            print("Erro: O novo nome já existe na agenda.")
            return

        telefone = pede_telefone(telefone)
        endereço = pede_endereço(endereço)
        cidade = pede_cidade(cidade)
        uf = pede_uf(uf)
        if confirma("alteração") == "S":
            agenda[p] = [nome_novo, telefone, endereço, cidade, uf]
            alterada = True
    else:
        print("Nome não encontrado.")


# Função para listar todos os contatos da agenda
def lista():
    print("\nAgenda\n\n------")
    for posição, e in enumerate(agenda):
        print(f"Posição: {posição} ", end="")
        mostra_dados(e[0], e[1], e[2], e[3], e[4])
    print("------\n")


# Função para ler a última agenda gravada automaticamente
def lê_última_agenda_gravada():
    última = última_agenda()
    if última is not None:
        leia_arquivo(última)


# Função para obter o nome do arquivo da última agenda gravada
def última_agenda():
    try:
        arquivo = open("ultima agenda.dat", "r", encoding="utf-8")
        última = arquivo.readline()[:-1]
        arquivo.close()
    except FileNotFoundError:
        return None
    return última


# Função para atualizar o nome do arquivo da última agenda gravada
def atualiza_última(nome):
    arquivo = open("ultima agenda.dat", "w", encoding="utf-8")
    arquivo.write(f"{nome}\n")
    arquivo.close()


# Função para ler os dados da agenda de um arquivo
def leia_arquivo(nome_arquivo):
    global agenda, alterada
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            agenda = []
            for l in arquivo.readlines():
                nome, telefone, endereço, cidade, uf = l.strip().split("#")
                agenda.append([nome, telefone, endereço, cidade, uf])
            alterada = False
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")


# Função para carregar a agenda de um arquivo especificado pelo usuário
def lê():
    global alterada
    if alterada:
        print("Você não salvou a lista desde a última alteração. Deseja gravá-la agora?")
        if confirma("gravação") == "S":
            grava()
    print("Ler\n---")
    nome_arquivo = pede_nome_arquivo()
    leia_arquivo(nome_arquivo)
    atualiza_última(nome_arquivo)


# Função para ordenar a agenda por nome
def ordena():
    global alterada
    fim = len(agenda)
    while fim > 1:
        i = 0
        trocou = False
        while i < (fim - 1):
            if agenda[i] > agenda[i + 1]:
                temp = agenda[i + 1]
                agenda[i + 1] = agenda[i]
                agenda[i] = temp
                trocou = True
            i += 1
        if not trocou:
            break
    alterada = True


# Função para salvar a agenda em um arquivo
def grava():
    global alterada
    if not alterada:
        print("Você não alterou a lista. Deseja gravá-la mesmo assim?")
        if confirma("gravação") == "N":
            return
    print("Gravar\n------")
    nome_arquivo = pede_nome_arquivo()
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            for e in agenda:
                arquivo.write(f"{e[0]}#{e[1]}#{e[2]}#{e[3]}#{e[4]}\n")
        atualiza_última(nome_arquivo)
        alterada = False
    except Exception as e:
        print(f"Ocorreu um erro ao gravar o arquivo: {e}")


# Função para validar a entrada de um número inteiro dentro de uma faixa
def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")


# Menu de opções
def menu():
    print("""
    1 - Novo contato
    2 - Alterar contato
    3 - Apagar contato
    4 - Listar contatos
    5 - Gravar agenda
    6 - Ler agenda
    7 - Ordenar agenda
    0 - Sair
    """)
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 7)


# Função principal do programa
def main():
    lê_última_agenda_gravada()
    while True:
        opção = menu()
        if opção == 0:
            break
        elif opção == 1:
            novo()
        elif opção == 2:
            altera()
        elif opção == 3:
            apaga()
        elif opção == 4:
            lista()
        elif opção == 5:
            grava()
        elif opção == 6:
            lê()
        elif opção == 7:
            ordena()


if __name__ == "__main__":
    main()
