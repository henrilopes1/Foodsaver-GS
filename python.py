# Definição da função para doar alimentos
def doar_alimentos(estabelecimento, alimentos):
    # Verifica se o estabelecimento está cadastrado
    if estabelecimento in cadastrados:
        # Adiciona os alimentos doados à lista de doações
        doacoes.append((estabelecimento, alimentos))
        print(f"Os alimentos doados por {estabelecimento} foram registrados.")
    else:
        print("Estabelecimento não cadastrado. A doação não pode ser realizada.")

# Função para exibir as doações registradas
def exibir_doacoes():
    if len(doacoes) > 0:
        print("Doações registradas:")
        for i, (estabelecimento, alimentos) in enumerate(doacoes, 1):
            alimentos_formatados = ", ".join(alimentos)
            print(f"Doação {i}:")
            print(f"Estabelecimento: {estabelecimento}")
            print(f"Alimentos: {alimentos_formatados}")
            print("-" * 30)
    else:
        print("Nenhuma doação registrada.")

# Função para excluir doações registradas
def excluir_doacao():
    if len(doacoes) > 0:
        exibir_doacoes()
        num_doacao = input("Digite o número da doação que deseja excluir: ")
        try:
            num_doacao = int(num_doacao)
            if 1 <= num_doacao <= len(doacoes):
                doacao_excluida = doacoes.pop(num_doacao - 1)
                print(f"Doação {num_doacao} excluída:")
                print(f"Estabelecimento: {doacao_excluida[0]}")
                print(f"Alimentos: {', '.join(doacao_excluida[1])}")
            else:
                print("Número de doação inválido.")
        except ValueError:
            print("Número de doação inválido.")
    else:
        print("Nenhuma doação registrada.")

#Funçao para exibir estabelecimentos cadastrados
def exibir_estabelecimentos():
    if len(cadastrados) > 0:
        print("Estabelecimentos cadastrados:")
        for i, estabelecimento in enumerate(cadastrados, 1):
            print(f"{i}. {estabelecimento}")
    else:
        print("Nenhum estabelecimento cadastrado.")


# Lista para armazenar os estabelecimentos cadastrados
cadastrados = []

# Lista para armazenar as doações
doacoes = []


# Loop principal do programa
while True:
    print("\n-------- FoodSaver - Doação de Alimentos --------")
    print("1. Cadastrar estabelecimento")
    print("2. Fazer doação de alimentos")
    print("3. Exibir doações registradas")
    print("4. Excluir uma doação")
    print("5. Exibir estabelecimentos cadastrados")
    print("6. Sair do programa")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        estabelecimento = input("Digite o nome do estabelecimento: ")
        cadastrados.append(estabelecimento)
        print(f"{estabelecimento} cadastrado com sucesso!")
    elif opcao == "2":
        estabelecimento = input("Digite o nome do estabelecimento: ")
        alimentos = input("Digite os alimentos doados (separados por vírgula): ").split(",")
        doar_alimentos(estabelecimento, alimentos)
    elif opcao == "3":
        exibir_doacoes()
    elif opcao == "4":
        excluir_doacao()
    elif opcao == "5":
        exibir_estabelecimentos()    
    elif opcao == "6":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Digite um número de 1 a 5.")


#Função para cadastrar um estabelecimento
def cadastrar_estabelecimento():
    exibir_estabelecimentos()
    estabelecimento = input("Digite o nome do estabelecimento: ")
    
    # Verifica se o nome do estabelecimento não está vazio
    if estabelecimento.strip() != "":
        cadastrados.append(estabelecimento)
        print(f"{estabelecimento} cadastrado com sucesso!")
    else:
        print("Nome do estabelecimento inválido. O cadastro não foi realizado.")

# Função para fazer uma doação de alimentos
def fazer_doacao():
    exibir_estabelecimentos()
    estabelecimento = input("Digite o nome do estabelecimento: ")
    alimentos = input("Digite os alimentos doados (separados por vírgula): ")
    
    # Verifica se o nome do estabelecimento e a lista de alimentos não estão vazios
    if estabelecimento.strip() != "" and alimentos.strip() != "":
        alimentos = alimentos.split(",")
        doar_alimentos(estabelecimento, alimentos)
    else:
        print("Dados inválidos. A doação não pode ser realizada.")
