import sys, time, json
 
# Função para imprimir as letras devagar da função print
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)  # Diminui o tempo para tornar mais rápido
 
# Função para imprimir as letras devagar da função input
def input_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)  # Diminui o tempo para tornar mais rápido
    return input()
    
# Arquivo para armazenar senhas
arquivo_senhas = 'senhas.json'
 
# Carregar senhas do arquivo
def carregar_senhas():
    try:
        with open(arquivo_senhas, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
 
# Salvar senhas no arquivo
def salvar_senhas():
    with open(arquivo_senhas, 'w') as file:
        json.dump(minhas_senhas, file)
 
# Lista para armazenar senhas
minhas_senhas = carregar_senhas()
 
senha_admin = "senha"  # Senha do administrador
 
# Função para verificar senha do administrador
def verificar_senha_admin():
    for _ in range(3):  # Dá 3 tentativas ao usuário
        tentativa = input_slow("Informe a senha de administrador: ")
        if tentativa == senha_admin:
            print_slow("Acesso liberado! \n")
            return True
        else:
            print_slow("Senha incorreta! Tente novamente.\n")
    print_slow("Acesso negado. Programa encerrado.\n")
    return False
 
# Função para adicionar uma nova senha
def adicionar_senha(site, senha):
    if len(minhas_senhas) < 50:
        minhas_senhas.append({'site': site, 'senha': senha})
        salvar_senhas()
        print_slow("Senha adicionada com sucesso!\n")
    else:
        print_slow("Limite de 50 senhas atingido!\n")
 
# Consultar todas as senhas
def consultar_senhas():
    if not minhas_senhas:
        print_slow("Nenhuma senha encontrada.\n")
    for entry in minhas_senhas:
        print_slow(f"Site: {entry['site']}, Senha: {entry['senha']}\n")

 
# Função para excluir uma senha
def excluir_senha(site):
    global minhas_senhas
    minhas_senhas = [entry for entry in minhas_senhas if entry['site'] != site]
    salvar_senhas()
    print_slow("Senha excluída com sucesso!\n")
 
# Verifica se o admin tem permissão
if verificar_senha_admin():
    while True:
        acao = input_slow("Deseja adicionar, excluir ou consultar uma senha? <adicionar/excluir/consultar>: ").lower()
        
        if acao == "adicionar":
            site = input_slow("Informe o site que está cadastrando: ")
            senha = input_slow("Informe a senha cadastrada: ")
            adicionar_senha(site, senha)
        
        elif acao == "excluir":
            site = input_slow("Informe o site cuja senha deseja excluir: ")
            excluir_senha(site)
        
        elif acao == "consultar":
            consultar_senhas()

        else:
            print_slow("Ação inválida! Tente novamente.\n")
        
        continuar = input_slow("Deseja realizar outra operação? <sim/nao>: ")
        if continuar.lower() != "sim":
            print_slow("Programa encerrado.\n")
            break