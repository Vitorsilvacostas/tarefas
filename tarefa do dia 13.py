# Inicia a lista vazia para armazenar os contatos
agenda = []

# Variável para marcar uma alteração na agenda
alterada = False

# Função para pedir o nome do contato, com um valor padrão opcional
def pede_nome(padrão=""):
    # Solicita ao usuário o nome
    nome = input("Nome: ")
    # Se o nome for vazio, usa o nome padrão
    if nome == "":
        nome = padrão
    return nome

# Função para pedir o telefone do contato, com um valor padrão opcional
def pede_telefone(padrão=""):
    # Solicita ao usuário o telefone
    telefone = input("Telefone: ")
    # Se o telefone for vazio, usa o telefone padrão
    if telefone == "":
        telefone = padrão
    return telefone

# Função para exibir os dados de um contato (nome e telefone)
def mostra_dados(nome, telefone):
    print(f"Nome: {nome} Telefone: {telefone}")

# Função para pedir o nome do arquivo para salvar ou ler
def pede_nome_arquivo():
    return input("Nome do arquivo: ")

# Função para pesquisar um contato na agenda pelo nome
def pesquisa(nome):
    # Converte o nome pesquisado para minúsculas para facilitar a comparação
    mnome = nome.lower()
    # Itera pela agenda para encontrar o contato
    for p, e in enumerate(agenda):
        # Se o nome no contato atual coincidir com o pesquisado
        if e[0].lower() == mnome:
            # Retorna a posição do contato na agenda
            return p
    # Se não encontrar, retorna None
    return None

# Função para adicionar um novo contato à agenda
def novo():
    global agenda, alterada
    # Pede o nome e telefone do novo contato
    nome = pede_nome()
    telefone = pede_telefone()
    # Adiciona o novo contato à lista da agenda
    agenda.append([nome, telefone])
    # Marca a agenda como alterada
    alterada = True

# Função para confirmar uma operação com o usuário (S/N)
def confirma(operação):
    while True:
        # Solicita confirmação do usuário
        opção = input(f"Confirma {operação} (S/N)? ").upper()
        # Se a resposta for S ou N, retorna a opção
        if opção in "SN":
            return opção
        else:
            # Se a resposta for inválida, informa o usuário
            print("Resposta inválida. Escolha S ou N.")

# Função para apagar um contato da agenda
def apaga():
    global agenda, alterada
    # Pede o nome do contato a ser apagado
    nome = pede_nome()
    # Pesquisa o contato na agenda
    p = pesquisa(nome)
    # Se o contato for encontrado
    if p is not None:
        # Confirma o apagamento com o usuário
        if confirma("apagamento") == "S":
            # Remove o contato da agenda
            del agenda[p]
            # Marca a agenda como alterada
            alterada = True
    else:
        # Informa que o contato não foi encontrado
        print("Nome não encontrado.")

# Função para alterar os dados de um contato existente
def altera():
    global alterada
    # Pesquisa o contato pelo nome
    p = pesquisa(pede_nome())
    # Se o contato for encontrado
    if p is not None:
        # Obtém os dados atuais do contato
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print("Encontrado:")
        # Mostra os dados atuais do contato
        mostra_dados(nome, telefone)
        # Pede novos dados para o contato, mantendo os atuais se nada for digitado
        nome = pede_nome(nome)
        telefone = pede_telefone(telefone)
        # Confirma a alteração com o usuário
        if confirma("alteração") == "S":
            # Atualiza os dados do contato
            agenda[p] = [nome, telefone]
            # Marca a agenda como alterada
            alterada = True
    else:
        # Informa que o contato não foi encontrado
        print("Nome não encontrado.")

# Função para listar todos os contatos da agenda
def lista():
    print("\nAgenda\n\n------")
    # Itera pela agenda para exibir cada contato
    for posição, e in enumerate(agenda):
        # Imprime a posição do contato na agenda
        print(f"Posição: {posição} ", end="")
        # Mostra os dados do contato
        mostra_dados(e[0], e[1])
    print("------\n")

# Função para ler a última agenda gravada automaticamente
def lê_última_agenda_gravada():
    # Obtém o nome do arquivo da última agenda gravada
    última = última_agenda()
    if última is not None:
        # Se existir, lê os dados do arquivo
        leia_arquivo(última)

# Função para obter o nome do arquivo da última agenda gravada
def última_agenda():
    try:
        # Abre o arquivo que contém o nome da última agenda gravada
        arquivo = open("ultima agenda.dat", "r", encoding="utf-8")
        # Lê o nome do arquivo
        última = arquivo.readline()[:-1]
        arquivo.close()
    except FileNotFoundError:
        # Se o arquivo não existir, retorna None
        return None
    return última

# Função para atualizar o nome do arquivo da última agenda gravada
def atualiza_última(nome):
    # Abre o arquivo para escrita
    arquivo = open("ultima agenda.dat", "w", encoding="utf-8")
    # Escreve o nome do arquivo da agenda atual
    arquivo.write(f"{nome}\n")
    arquivo.close()

# Função para ler os dados da agenda de um arquivo
def leia_arquivo(nome_arquivo):
    global agenda, alterada
    # Abre o arquivo para leitura
    arquivo = open(nome_arquivo, "r", encoding="utf-8")
    # Limpa a agenda atual
    agenda = []
    # Lê cada linha do arquivo e adiciona à agenda
    for l in arquivo.readlines():
        nome, telefone = l.strip().split("#")
        agenda.append([nome, telefone])
    arquivo.close()
    # Marca a agenda como não alterada
    alterada = False

# Função para carregar a agenda de um arquivo especificado pelo usuário
def lê():
    global alterada
    # Se a agenda foi alterada, pergunta se o usuário deseja salvá-la
    if alterada:
        print("Você não salvou a lista desde a última alteração. Deseja gravá-la agora?")
        if confirma("gravação") == "S":
            grava()
    print("Ler\n---")
    # Pede o nome do arquivo para leitura
    nome_arquivo = pede_nome_arquivo()
    # Lê os dados do arquivo especificado
    leia_arquivo(nome_arquivo)
    # Atualiza o nome do último arquivo lido
    atualiza_última(nome_arquivo)

# Função para ordenar a agenda por nome
def ordena():
    global alterada
    # Implementação de um algoritmo de ordenação simples (bubble sort)
    fim = len(agenda)
    while fim > 1:
        i = 0
        trocou = False
        while i < (fim - 1):
            if agenda[i] > agenda[i + 1]:
                # Troca a posição dos contatos se estiverem fora de ordem
                temp = agenda[i + 1]
                agenda[i + 1] = agenda[i]
                agenda[i] = temp
                trocou = True
            i += 1
        if not trocou:
            break
    # Marca a agenda como alterada
    alterada = True

# Função para salvar a agenda em um arquivo
def grava():
    global alterada
    # Se a agenda não foi alterada, pergunta se o usuário deseja salvá-la mesmo assim
    if not alterada:
        print("Você não alterou a lista. Deseja gravá-la mesmo assim?")
        if confirma("gravação") == "N":
            return
    print("Gravar\n------")
    # Pede o nome do arquivo para gravação
    nome_arquivo = pede_nome_arquivo()
    # Abre o arquivo para escrita
    arquivo = open(nome_arquivo, "w", encoding="utf-8")
    # Escreve cada contato no arquivo
    for e in agenda:
        arquivo.write(f"{e[0]}#{e[1]}\n")
    arquivo.close()
    # Atualiza o nome do último arquivo gravado
    atualiza_última(nome_arquivo)
    # Marca a agenda como não alterada
    alterada = False

# Função para validar a entrada de um número inteiro dentro de uma faixa
def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            # Solicita ao usuário um número inteiro
            valor = int(input(pergunta))
            # Verifica se o valor está dentro da faixa especificada
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            # Informa ao usuário se a entrada não for um número inteiro válido
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")

# Função para
