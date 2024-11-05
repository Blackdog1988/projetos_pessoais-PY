# Dicionário para armazenar os itens e seus preços
# Cada item é uma chave e o preço é o valor correspondente
itens = {
    'alface': 2.50,
    'maça': 3.00,
    'pera': 2.80,
    'banana': 2.00,
    'uva': 4.50,
    'batata doce': 2.20,
    'batata inglesa': 1.80
}

# Constantes para opções do menu principal
OPCAO_EXIBIR_ITENS = '1'
OPCAO_ADICIONAR_CARRINHO = '2'
OPCAO_VISUALIZAR_CARRINHO = '3'
OPCAO_PAGAR = '4'

# Função para exibir os itens disponíveis no mercado
def exibir_itens():
    print("Itens disponíveis:")
    # Percorre o dicionário 'itens' e exibe cada item com seu preço formatado
    for item, preco in itens.items():
        print(f"{item}: R${preco:.2f}")

# Função para registrar uma compra, adicionando o item ao carrinho
def registrar_compra(carrinho, item, quantidade):
    # Verifica se o item está no dicionário 'itens'
    if item in itens:
        # Calcula o preço total com base na quantidade
        preco_total = itens[item] * quantidade
        # Se o item já está no carrinho, soma a quantidade e o preço total
        if item in carrinho:
            quantidade_atual, preco_atual = carrinho[item]
            carrinho[item] = quantidade_atual + quantidade, preco_atual + preco_total
        else:
            # Se o item não está no carrinho, adiciona diretamente
            carrinho[item] = quantidade, preco_total
        print(f"{quantidade} {item}(s) adicionado(s) ao carrinho.")
    else:
        # Caso o item não exista no mercado, exibe mensagem de erro
        print("Item não encontrado.")

# Função para exibir o conteúdo do carrinho e o total a pagar
def exibir_carrinho(carrinho):
    # Verifica se o carrinho está vazio
    if not carrinho:
        print("O carrinho está vazio.")
    else:
        print("\nCarrinho:")
        # Exibe cada item no carrinho com sua quantidade e preço total
        for item, (quantidade, preco_total) in carrinho.items():
            print(f"{quantidade} {item}(s) - Total: R${preco_total:.2f}")
        # Exibe o valor total do carrinho
        print(f"\nTotal a pagar: R${calcular_total(carrinho):.2f}")

# Função para calcular o valor total do carrinho
def calcular_total(carrinho):
    # Calcula a soma de todos os preços totais dos itens no carrinho
    return sum(preco_total for _, preco_total in carrinho.values())

# Função para solicitar e validar a quantidade do item
def solicitar_quantidade():
    while True:
        try:
            # Solicita a quantidade ao usuário
            quantidade = int(input("Digite a quantidade: "))
            # Garante que a quantidade seja positiva
            if quantidade > 0:
                return quantidade
            else:
                print("A quantidade deve ser maior que zero.")
        except ValueError:
            # Caso o usuário insira um valor inválido, exibe mensagem de erro
            print("Por favor, insira um número válido.")

# Função principal que gerencia a interação do usuário
def main():
    carrinho = {}  # Dicionário para armazenar os itens do carrinho

    while True:
        # Exibe o menu principal
        print("\nBem-vindo ao Mercado!")
        print(f"{OPCAO_EXIBIR_ITENS}. Exibir itens disponíveis")
        print(f"{OPCAO_ADICIONAR_CARRINHO}. Adicionar item ao carrinho")
        print(f"{OPCAO_VISUALIZAR_CARRINHO}. Visualizar carrinho")
        print(f"{OPCAO_PAGAR}. Pagar")

        # Lê a opção escolhida pelo usuário
        opcao = input("Escolha uma opção: ")

        # Executa ações com base na opção escolhida
        if opcao == OPCAO_EXIBIR_ITENS:
            # Exibe os itens disponíveis no mercado
            exibir_itens()
        elif opcao == OPCAO_ADICIONAR_CARRINHO:
            # Solicita o nome do item e a quantidade para adicionar ao carrinho
            item = input("Digite o nome do item: ").lower()
            quantidade = solicitar_quantidade()
            registrar_compra(carrinho, item, quantidade)
        elif opcao == OPCAO_VISUALIZAR_CARRINHO:
            # Exibe o conteúdo do carrinho e o total a pagar
            exibir_carrinho(carrinho)
        elif opcao == OPCAO_PAGAR:
            # Encerra o programa, exibindo uma mensagem final e o conteúdo do carrinho
            print("Obrigado por comprar conosco!")
            exibir_carrinho(carrinho)
            break
        else:
            # Exibe mensagem de erro caso a opção seja inválida
            print("Opção inválida. Tente novamente.")

# Ponto de entrada do programa
# Garante que 'main()' seja executada apenas se o script for executado diretamente
if __name__ == "__main__":
    main()
