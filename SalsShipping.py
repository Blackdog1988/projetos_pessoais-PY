def mostrar_lista_precos():
    """Exibe a tabela de preços de envio por peso."""
    print("Tabela de Preços de Envio:")
    print("Peso do Pacote\t\tPreço por Libra\t\tTaxa Fixa")
    print("Até 2 lb\t\t$1.50\t\t\t$20.00")
    print("De 2 a 6 lb\t\t$3.00\t\t\t$20.00")
    print("De 6 a 10 lb\t\t$4.00\t\t\t$20.00")
    print("Mais de 10 lb\t\t$4.75\t\t\t$20.00")
    print("Envio Premium\t\tN/A\t\t\t$125.00\n")

def calcular_custo_envio(weight):
    """Calcula o custo de envio com base no peso fornecido."""
    cost_ground_premium = 125.00  # Taxa fixa de envio premium
    cost = None  # Inicializar com valor nulo para controle de erro

    # Determinar o custo com base no peso
    if weight <= 2:
        cost = weight * 1.50 + 20.00
    elif weight <= 6:
        cost = weight * 3.00 + 20.00
    elif weight <= 10:
        cost = weight * 4.00 + 20.00
    elif weight > 10:
        cost = weight * 4.75 + 20.00
    else:
        print("Peso inválido.")
    
    return cost, cost_ground_premium

# Exibir a lista de preços
mostrar_lista_precos()

# Entrada de peso
try:
    weight = float(input("Informe o peso do pacote em libras: "))
    cost, cost_ground_premium = calcular_custo_envio(weight)

    if cost is not None:
        print(f"\nCusto de envio: ${cost:.2f}")
    else:
        print("\nNão foi possível calcular o custo de envio devido a um peso inválido.")
        
    print(f"Custo do Envio Premium (fixo): ${cost_ground_premium:.2f}")
    
except ValueError:
    print("\nPor favor, insira um número válido para o peso.")
