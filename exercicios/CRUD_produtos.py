def main():
    lista_produtos = []

    opcao = 1

    while (opcao != 5):
        print("1 - Inserir produto")
        print("2 - Alterar produto")
        print("3 - Excluir produto")
        print("4 - Exibir dados de um produto")
        print("5 - Sair")
    
        opcao = int(input("Digite a opcao desejada (1 a 5): "))
        if (opcao >= 1 and opcao <= 5):
    
            match opcao:
                    case 1:
                        inserir_produto(lista_produtos)
                    case 2:
                        codigo_alterar = int(input("Digite o codigo do produto que deseja alterar os dados: "))
                        indice = buscar_produto(lista_produtos,codigo_alterar)
                        if (indice != -1):
                            alterar_produto(lista_produtos, indice)
                        else:
                            print("Codigo inexistente")
                    case 3:
                        codigo_excluir = int(input("Digite o codigo do produto que deseja excluir: "))
                        indice = buscar_produto(lista_produtos, codigo_excluir)
                        if (indice != -1):
                            excluir_produto(lista_produtos, indice)
                            print("Produto excluido com sucesso.")
                        else:
                            print("Codigo inexistente")
                    case 4:
                        codigo_exibir = int(input("Digite o codigo do produto que deseja exibir os dados: "))
                        indice = buscar_produto(lista_produtos, codigo_exibir)
                        if (indice != -1):
                            exibir_dados_produto(lista_produtos, indice)
                        else:
                            print("Codigo inexistente")
        else:
            print("Opcao invalida")
    
    
    # Funcoes do CRUD
def buscar_produto(lista_produtos,codigo):
        indice = -1
        for i in range(len(lista_produtos)):
            if (codigo == lista_produtos[i]['Codigo_produto']):
                indice = i
        return indice
    
def inserir_produto(lista_produtos):
        try:
            # Validacao do codigo para simular uma chave primaria
            cod_produto = int(input("Digite o codigo do produto: "))
            indice = buscar_produto(lista_produtos,cod_produto)
            while(indice != -1):
                print("Esse codigo já existe")
                cod_produto = int(input("Digite outro codigo de produto: "))
                indice = buscar_produto(lista_produtos, cod_produto)
            
            nome_produto = input("Digite o nome do produto: ")
            cat_produto = input("Digite a categoria do produto: ")
            qtd_produto = int(input("Digite a quantidade de produtos: "))
            forn_produto = input("Digite o fornecedor do produto: ")
            preco_unitario_produto = float(input("Digite o preco unitario do produto: "))
        except ValueError:
            print("Digite dados númericos para o código, a qtde e preco unitario do produto.")
        else:
            dados_produto = {
                'Codigo_produto': cod_produto,
                'Nome_produto': nome_produto,
                'Categoria_produto': cat_produto,
                'Quantidade_produto': qtd_produto,
                'Fornecedor_produto': forn_produto,
                'Preco_unitario': preco_unitario_produto
            }
            lista_produtos.append(dados_produto)
            print("Produto inserido com sucesso.")
    
def alterar_produto(lista_produtos,indice):
        try:
            print(f"Nome do produto: {lista_produtos[indice]['Nome_produto']}")
            novo_nome_produto = input("Digite o novo nome do produto: ")
            
            print(f"Categoria do produto: {lista_produtos[indice]['Categoria_produto']}")
            novo_categoria_produto = input("Digite a nova categoria do produto: ")

            print(f"Quantidade de produtos disponiveis: {lista_produtos[indice]['Quantidade_produto']}")
            novo_qtd_produto = int(input("Digite a nova quantidade de produtos: "))

            print(f"Fornecedor do produto: {lista_produtos[indice]['Fornecedor_produto']}")
            novo_forn_produto = input("Digite o novo fornecedor de produtos: ")

            print(f"Preco unitario do produto: {lista_produtos[indice]['Preco_unitario']}")
            novo_preco_produto = float(input("Digite o novo preco unitario do produto: "))

        except ValueError:
            print("Digite dados númericos para o código, a qtde e preco unitario do produto.")
        else:
            # Captura alterações para o dicionario/lista   
            lista_produtos[indice]['Nome_produto'] = novo_nome_produto
            lista_produtos[indice]['Categoria_produto'] = novo_categoria_produto
            lista_produtos[indice]['Quantidade_produto'] = novo_qtd_produto
            lista_produtos[indice]['Fornecedor_produto'] = novo_forn_produto
            lista_produtos[indice]['Preco_unitario'] = novo_preco_produto
            print("Dados alterados com sucesso.")
    
def excluir_produto(lista_produtos,indice):
            lista_produtos.pop(indice)

def exibir_dados_produto(lista_produto,indice):
            for chave,valor in lista_produto[indice].items():
                print(f"{chave}: {valor}")
        
if (__name__ == "__main__"):
    main()