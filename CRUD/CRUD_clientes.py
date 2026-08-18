def main():
    lista_clientes = []

    opcao = 1

    while (opcao != 6):
        print("1 - Inserir cliente")
        print("2 - Alterar cliente")
        print("3 - Excluir cliente")
        print("4 - Exibir dados de um cliente")
        print("5 - Exibir os clientes com saldo acima de 10k")
        print("6 - Sair")

        opcao = int(input("Digite a opcao desejada (1 a 6): "))
        if (opcao >= 1 and opcao <= 6):

            match opcao:
                case 1:
                    inserir_cliente(lista_clientes)
                case 2:
                    codigo_alterar = int(input("Digite o codigo do cliente que deseja alterar os dados: "))
                    indice = buscar_cliente(lista_clientes,codigo_alterar)
                    if (indice != -1):
                        alterar_cliente(lista_clientes, indice)
                    else:
                        print("Codigo inexistente")
                case 3:
                    codigo_excluir = int(input("Digite o codigo do cliente que deseja excluir: "))
                    indice = buscar_cliente(lista_clientes, codigo_excluir)
                    if (indice != -1):
                        excluir_cliente(lista_clientes, indice)
                    else:
                        print("Codigo inexistente")
                case 4:
                    codigo_exibir = int(input("Digite o codigo do cliente que deseja exibir os dados: "))
                    indice = buscar_cliente(lista_clientes, codigo_exibir)
                    if (indice != -1):
                        exibir_dados_cliente(lista_clientes, indice)
                    else:
                        print("Codigo inexistente")
                case 5:
                    exibir_clientes_acima_10k(lista_clientes)
        else:
            print("Opcao invalida")


# Funcoes do CRUD
def buscar_cliente(lista_clientes,codigo):
    indice = -1
    for i in range(len(lista_clientes)):
        if (codigo == lista_clientes[i]['Codigo_cliente']):
            indice = i
    return indice

def inserir_cliente(lista_clientes):
    try:
        # Validacao do codigo para simular uma chave primaria
        cod_cliente = int(input("Digite o codigo do cliente: "))
        indice = buscar_cliente(lista_clientes,cod_cliente)
        while(indice != -1):
            print("Esse codigo já existe")
            cod_cliente = int(input("Digite outro codigo do cliente: "))
            indice = buscar_cliente(lista_clientes, cod_cliente)
        
        nome_cliente = input("Digite o nome do cliente: ")
        nro_agencia = int(input("Digite o numero da agencia do cliente: "))
        nro_conta_corrente = int(input("Digite o numero da conta corrente do cliente: "))
        saldo_cliente = float(input("Digite o saldo do cliente: "))
    except ValueError:
        print("Digite dados númericos para o código, o nro da agência, o nro da conta corrente e o saldo.")
    else:
        dados_cliente = {
            'Codigo_cliente': cod_cliente,
            'Nome_cliente': nome_cliente,
            'Nro_agencia_cliente': nro_agencia,
            'Nro_conta_corrente': nro_conta_corrente,
            'Saldo_conta_cliente': saldo_cliente
        }
        lista_clientes.append(dados_cliente)
        print("Cliente inserido com sucesso.")

def alterar_cliente(lista_clientes,indice):
    try:
        print(f"Nome do cliente: {lista_clientes[indice]['Nome_cliente']}")
        novo_nome_cliente = input("Digite o novo nome do cliente: ")
        print(f"Numero da agencia do cliente: {lista_clientes[indice]['Nro_agencia_cliente']}")
        novo_nro_agencia = int(input("Digite o novo numero da agencia do cliente: "))
        print(f"Numero da conta corrente do cliente: {lista_clientes[indice]['Nro_conta_corrente']}")
        novo_conta_corrente = int(input("Digite o novo numero da conta corrente do cliente: "))
        print(f"Saldo do cliente: {lista_clientes[indice]['Saldo_conta_cliente']}")
        novo_saldo = float(input("Digite o saldo do cliente: "))
    except ValueError:
        print("Digite dados númericos para o código, o nro da agência, o nro da conta corrente e o saldo.")
    else:
        # Captura alterações para o dicionario/lista   
        lista_clientes[indice]['Nome_cliente'] = novo_nome_cliente
        lista_clientes[indice]['Nro_agencia_cliente'] = novo_nro_agencia
        lista_clientes[indice]['Nro_conta_corrente'] = novo_conta_corrente
        lista_clientes[indice]['Saldo_conta_cliente'] = novo_saldo
        print("Dados alterados com sucesso.")

def excluir_cliente(lista_clientes,indice):
    lista_clientes.pop(indice)

def exibir_dados_cliente(lista_clientes,indice):
    for chave,valor in lista_clientes[indice].items():
        print(f"{chave}: {valor}")

def exibir_clientes_acima_10k(lista_clientes):
    for i in range(len(lista_clientes)):
        if (lista_clientes[i]['Saldo_conta_cliente'] > 10000):
            for chave, valor in lista_clientes[i].items():
                print(f"{chave}: {valor}")
        print("------------------------------------")

if (__name__ == "__main__"):
    main()

