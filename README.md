# 🏦 CRUD de Clientes — Aula 03

Projeto desenvolvido durante a **Aula 03** do curso de Python, com o objetivo de praticar a criação de um **CRUD (Create, Read, Update, Delete)** utilizando estruturas básicas da linguagem.

Nesta etapa, o sistema permite cadastrar, alterar, excluir e consultar clientes, armazenando os dados em uma lista de dicionários.

> 🚧 **Projeto em desenvolvimento:** esta é uma implementação inicial para fins de aprendizado. Novas funcionalidades e melhorias serão adicionadas nas próximas aulas.

---

## 📚 Objetivos da aula

Nesta aula foram praticados conceitos importantes de Python, como:

* Funções
* Listas
* Dicionários
* Estruturas condicionais
* Estrutura `match/case`
* Laços de repetição
* Entrada de dados com `input()`
* Conversão de tipos (`int` e `float`)
* Manipulação de listas
* Busca de informações
* Organização do código em funções

---

## ⚙️ Funcionalidades

O sistema possui um menu com as seguintes opções:

```text
1 - Inserir cliente
2 - Alterar cliente
3 - Excluir cliente
4 - Exibir dados de um cliente
5 - Exibir os clientes com saldo acima de 10k
6 - Sair
```

### ➕ Inserir cliente

Permite cadastrar um novo cliente informando:

* Código do cliente
* Nome
* Número da agência
* Número da conta corrente
* Saldo

Os dados são armazenados em um dicionário e adicionados à lista de clientes.

### 🔎 Buscar cliente

A função `buscar_cliente()` procura um cliente pelo seu código.

Caso o cliente seja encontrado, a função retorna o índice correspondente na lista.

Caso contrário, retorna:

```python
-1
```

### ✏️ Alterar cliente

Permite alterar os dados de um cliente já cadastrado.

O sistema busca o cliente pelo código e, caso ele exista, solicita os novos dados.

### 🗑️ Excluir cliente

Permite remover um cliente da lista utilizando o código informado.

A exclusão é realizada através do método:

```python
pop()
```

### 👤 Exibir dados de um cliente

Exibe todas as informações cadastradas para um cliente específico.

A função percorre o dicionário utilizando:

```python
for chave, valor in lista_clientes[indice].items():
```

### 💰 Clientes com saldo acima de 10 mil

A opção 5 percorre todos os clientes cadastrados e exibe aqueles que possuem saldo superior a:

```text
R$ 10.000,00
```

---

## 🗂️ Estrutura dos dados

Cada cliente é armazenado como um **dicionário**:

```python
dados_cliente = {
    'Codigo_cliente': cod_cliente,
    'Nome_cliente': nome_cliente,
    'Nro_agencia_cliente': nro_agencia,
    'Nro_conta_corrente': nro_conta_corrente,
    'Saldo_conta_cliente': saldo_cliente
}
```

Todos os clientes são armazenados dentro de uma lista:

```python
lista_clientes = []
```

A estrutura final fica semelhante a:

```text
lista_clientes
│
├── Cliente 1
│   ├── Código
│   ├── Nome
│   ├── Agência
│   ├── Conta
│   └── Saldo
│
├── Cliente 2
│   ├── Código
│   ├── Nome
│   ├── Agência
│   ├── Conta
│   └── Saldo
│
└── ...
```

---

## 🧩 Funções principais

| Função                        | Responsabilidade                              |
| ----------------------------- | --------------------------------------------- |
| `main()`                      | Controla o menu principal do sistema          |
| `inserir_cliente()`           | Cadastra um novo cliente                      |
| `buscar_cliente()`            | Procura um cliente pelo código                |
| `alterar_cliente()`           | Atualiza os dados de um cliente               |
| `excluir_cliente()`           | Remove um cliente                             |
| `exibir_dados_cliente()`      | Exibe os dados de um cliente                  |
| `exibir_clientes_acima_10k()` | Exibe clientes com saldo superior a R$ 10.000 |

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

### 2. Entre na pasta do projeto

```bash
cd nome-do-projeto
```

### 3. Execute o programa

```bash
python nome_do_arquivo.py
```

> É necessário ter o **Python 3.10 ou superior**, pois o projeto utiliza a estrutura `match/case`.

---

## 💻 Exemplo de utilização

Ao executar o programa, será apresentado o menu:

```text
1 - Inserir cliente
2 - Alterar cliente
3 - Excluir cliente
4 - Exibir dados de um cliente
5 - Exibir os clientes com saldo acima de 10k
6 - Sair

Digite a opcao desejada (1 a 6):
```

Ao escolher a opção `1`, por exemplo:

```text
Digite o codigo do cliente: 1
Digite o nome do cliente: João
Digite o numero da agencia do cliente: 123
Digite o numero da conta corrente do cliente: 45678
Digite o saldo do cliente: 15000
```

O cliente será adicionado à lista.

---

## 🚀 Próximos passos

Como este projeto faz parte do processo de aprendizado, algumas melhorias podem ser implementadas nas próximas aulas:

* [ ] Validar códigos de clientes duplicados
* [ ] Melhorar o tratamento de entradas inválidas
* [ ] Criar mensagens de confirmação para as operações
* [ ] Separar o projeto em diferentes arquivos
* [ ] Utilizar banco de dados
* [ ] Criar uma interface gráfica ou API
* [ ] Implementar persistência dos dados
* [ ] Melhorar a organização e padronização do código
* [ ] Adicionar testes automatizados

---

## 🧠 Conceito de CRUD

CRUD é uma sigla utilizada para representar as quatro operações básicas de manipulação de dados:

| Operação | Significado | Neste projeto            |
| -------- | ----------- | ------------------------ |
| **C**    | Create      | Inserir cliente          |
| **R**    | Read        | Consultar/exibir cliente |
| **U**    | Update      | Alterar cliente          |
| **D**    | Delete      | Excluir cliente          |

Este projeto representa uma primeira implementação desses conceitos utilizando apenas recursos básicos do Python.

---

## 📌 Status do projeto

🟡 **Em desenvolvimento — Aula 03**

O projeto será evoluído conforme o avanço das aulas e a introdução de novos conceitos de programação.

---

## 👨‍💻 Aprendizado

Este projeto faz parte da minha jornada de aprendizado em **Python e desenvolvimento de sistemas**, servindo como prática para entender na prática como funciona a construção de um CRUD.

**Aula 03 — CRUD de Clientes em Python 🐍**
