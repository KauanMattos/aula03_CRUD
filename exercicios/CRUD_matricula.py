def main():
    lista_alunos = []

    opcao = 1

    while (opcao != 5):
        print("1 - Inserir matricula")
        print("2 - Alterar matricula")
        print("3 - Excluir matricula")
        print("4 - Exibir dados de um aluno")
        print("5 - Sair")

        opcao = int(input("Digite a opção desejada (1 a 5): "))
        if (opcao >= 1 and opcao <= 5):

            match opcao:
                case 1:
                    inserir_aluno(lista_alunos)
                case 2:
                    matricula_alterar = int(input("Digite a matricula que deseja alterar os dados: "))
                    indice = buscar_aluno(lista_alunos,matricula_alterar)
                    if (indice != -1):
                        alterar_aluno(lista_alunos, indice)
                    else:
                        print("Matricula inexistente")
                case 3:
                    matricula_excluir = int(input("Digite a matricula do aluno que deseja exibir os dados: "))
                    indice = buscar_aluno(lista_alunos, matricula_excluir)
                    if (indice != -1):
                        excluir_aluno(lista_alunos, indice)
                    else:
                        print("Matricula inexistente")
                case 4:
                    matricula_exibir = int(input("Digite a matricula do aluno que deseja exibir os dados: "))
                    indice = buscar_aluno(lista_alunos, matricula_exibir)
                    if (indice != -1):
                        exibir_dados_alunos(lista_alunos, indice)
                    else:
                        print("Matricula inexistente")
        else:
            print("Opção inválida")


# Funções do CRUD
def buscar_aluno(lista_alunos, matricula):
    indice = -1
    for i in range(len(lista_alunos)):
        if (matricula == lista_alunos[i]["Matricula_aluno"]):
            indice = i
    return indice

def inserir_aluno(lista_alunos):
    try:
        # Validação do código para simular uma CHAVE PRIMÁRIA
        matr_aluno = int(input("Digite a matricula do aluno: "))
        indice = buscar_aluno(lista_alunos,matr_aluno)
        while(indice != -1):
            print("Essa matricula já existe.")
            matr_aluno = int(input("Digite outra matricula para o aluno: "))
            indice = buscar_aluno(lista_alunos, matr_aluno)

        nome_aluno = input("Digite o nome do aluno: ")
        plano_tipo = input("Digite o tipo de plano do aluno: ")
        modalidade_aluno = input("Digite a modalidade do aluno: ")
        presencas_mes = int(input("Digite a quantidade de presencas no mês do aluno: "))
    except ValueError:
        print("Digite dados númericos para matricula e presenças no mês.")
    else:
        dados_alunos = {
            'Matricula_aluno': matr_aluno,
            'Nome_aluno': nome_aluno,
            'Plano_aluno': plano_tipo,
            'Modalidade_aluno': modalidade_aluno,
            'Presencas_mes_aluno': presencas_mes
        }
        lista_alunos.append(dados_alunos)
        print("Aluno inserido com sucesso.")

def alterar_aluno(lista_alunos, indice):
    try:
        print(f"Nome do aluno: {lista_alunos[indice]['Nome_aluno']}")
        novo_nome_aluno = input("Digite o novo nome do aluno: ")

        print(f"Plano do aluno: {lista_alunos[indice]['Plano_aluno']}")
        novo_plano_aluno = input("Digite o novo plano do aluno: ")

        print(f"Modalidade do aluno: {lista_alunos[indice]['Modalidade_aluno']}")
        novo_modalidade_aluno = input("Digite a nova modalidade do aluno: ")

        print(f"Presenças do aluno: {lista_alunos[indice]['Presencas_mes_aluno']}")
        novo_presencas_mes_aluno = int(input("Digite a nova quantidade de presenças no mês do aluno: "))
    except ValueError:
        print("Digite dados númericos para matricula e presenças no mês.")
    else:
        # Captura alterações para o dicionario/lista 
        lista_alunos[indice]['Nome_aluno'] = novo_nome_aluno
        lista_alunos[indice]['Plano_aluno'] = novo_plano_aluno
        lista_alunos[indice]['Modalidade_aluno'] = novo_modalidade_aluno
        lista_alunos[indice]['Presencas_mes_aluno'] = novo_presencas_mes_aluno
        print("Dados alterados com sucesso.")

def excluir_aluno(lista_alunos, indice):
    lista_alunos.pop(indice)

def exibir_dados_alunos(lista_alunos,indice):
    for chave, valor in lista_alunos[indice].items():
        print(f"{chave}: {valor}")

if (__name__ == "__main__"):
    main()

