# ♟️ Board & Play

> Um sistema de gerenciamento de estoque e contratos de serviços para um negócio de aluguel de jogos de tabuleiro.

## 🎲 Sobre 

- A Board & Play é um projeto da disciplina de Programação Orientada a Objetos da Universidade Federal do Cariri (UFCA), a qual é ministrada pelo professor Jayr Pereira.
- O objetivo é desenvolver um sistema de linha de comando (CLI) para gerenciar um negócio fictício de aluguel de jogos de tabuleiro.
- Nele são necessárias as funcionalidades de cadastro de jogos e clientes no sistema, controle de contratos ativos e de clientes com pagamentos pendentes, multas por violação de contrato por tempo ou avaria do produto, registro de pagamentos, cálculo de custos de risco e previsiblidade de receita.


## 🖊️ Pré-requisitos

- Python 3

## 📦 Estrutura do projeto

```
Board_and_Play/
├── src/ 
|   ├── board_and_play_poo /                        # Diretório do sistema
|   |   ├── app/                                    # Diretório da aplicação
|   |   |    ├── menus/                             # Diretório dos menus
|   |   |    |   ├── __init__.py                    # Transforma o diretório em um pacote
|   |   |    |   ├── menu_acessorio.py              # Menu de acessorio
|   |   |    |   ├── menu_colaborador.py            # Menu de colaborador
|   |   |    |   ├── menu_consumivel.py             # Menu de jogo consumivel
|   |   |    |   ├── menu_contrato.py               # Menu de contrato
|   |   |    |   ├── menu_cliente.py                # Menu de cliente
|   |   |    |   ├── menu_jogo_aluguel.py           # Menu de jogo aluguel
|   |   |    |   ├── menu_jogo_venda.py             # Menu de jogo venda
|   |   |    |   ├── menu_registrar_contrato.py     # Menu de registrar contrato
|   |   |    |   ├── menu_registrar_venda.py        # Menu de registrar venda
|   |   |    |   └── menu_venda.py                  # Menu de venda
|   |   |    |
|   |   |    ├── __init__.py                        # Transforma o diretório em um pacote
|   |   |    └── app.py                             # Aplicação, onde o usuário interaje com o sistema
|   |   |
|   |   ├── data/                         #  Diretório do banco de dados
|   |   |     └── dados.db                #  Banco de dados SQLite
|   |   |
|   |   ├── data_test/                    #  Diretório do banco de dados de testes
|   |   |     └── dados.db                #  Banco de dados de testes SQLite
|   |   |
|   |   ├── database/                     #  Diretório das classes do banco de dados
|   |   |       ├── __init__.py           # Transforma o diretório em um pacote
|   |   |       ├── database.py           # Classe responsável pela conexão com o banco de dados
|   |   |       └── tabelas.py            # Classe responsável pelas tabelas do banco de dadoo
|   |   |
|   |   ├── modules/                      # Módulos do projeto
|   |   |    ├── domain/                  # Classes de domínio
|   |   |    |   ├── __init__.py          # Transforma o diretório em um pacote
|   |   |    |   ├── acessorios.py        # Classe que cuida de todos os produtos do tipo acessorio
|   |   |    |   ├── alugueis.py          # Classe responsável pelas transações de aluguel
|   |   |    |   ├── clientes.py          # Classe utilizada para para cadastro e gerenciamento de clientes
|   |   |    |   ├── colaboradores.py     # Classe utilizada para para cadastro e gerenciamento de colaboradores
|   |   |    |   ├── consumiveis.py       # Classe que cuida de todos os produtos do tipo consumível
|   |   |    |   ├── jogos_aluguel.py     # Classe que cuida de todos os produtos do tipo jogo aluguel
|   |   |    |   ├── jogos_venda.py       # Classe que cuida de todos os produtos do tipo jogo venda
|   |   |    |   ├── jogos.py             # Classe pai que descreve os atributos que existem em todas as especificações de jogos
|   |   |    |   ├── produtos.py          # Classe pai que integra atributos em comum de suas subclasses, servindo como generalização
|   |   |    |   ├── transacoes.p         # Classe abstrata que entrega atributos e métodos para Venda e Aluguel
|   |   |    |   └── venda.py             # Classe que representa uma venda, com métodos de calculo de valor e desconto
|   |   |    |
|   |   |    └── infrastructure/
|   |   |        ├── __init__.py          # Transforma o diretório em um pacote
|   |   |        ├── config_database.py   # Classe utilizada para configurar o banco de dados
|   |   |        └── descontos.py         # Classe utilizada para os descontos
|   |   |
|   |   ├── repositories/                         # Diretório de repositórios que interagem com o banco de dados
|   |   |     ├── __init__.py                     # Transforma o diretório em um pacote
|   |   |     ├── repository_acessorios.py        # Repositório de acessórios
|   |   |     ├── repository_alugueis.py          # Repositório de aluguéis
|   |   |     ├── repository_clientes.py          # Repositório de clientes
|   |   |     ├── repository_colaboradores.py     # Repositório de colaboradores
|   |   |     ├── repository_consumiveis.py       # Repositório de consumíveis
|   |   |     ├── repository_jogos_aluguel.py     # Repositório de jogos aluguel
|   |   |     ├── repository_jogos_venda.py       # Repositório de jogos venda
|   |   |     ├── repository_jogos.py             # Repositório de jogos
|   |   |     ├── repository_produtos.py          # Repositório de produtos
|   |   |     ├── repository_transacoes.py        # Repositório de transações
|   |   |     └── repository_venda.py             # Repositório de venda
|   |   |
|   |   ├── __init__.py                      # Transforma o diretório em um pacote
|   |   └── main.py                          # Arquivo principal do sistema
|   |   
|   └── tests/                               # Diretório de testes unitários
|         ├── __init__.py                    # Transforma o diretório em um pacote
|         ├── test_acessorios.py             # Testes unitários de acessório e seu repositório
|         ├── test_alugueis.py               # Testes unitários de alugúeis e seu repositório
|         ├── test_clientes.py               # Testes unitários de clientes e seu repositório
|         ├── test_colaboradores.py          # Testes unitários de colaboradores e seu repositório
|         ├── test_consumiveis.py            # Testes unitários de consumíveis e seu repositório
|         ├── test_jogos_aluguel.py          # Testes unitários de jogos aluguel e seu repositório
|         ├── test_jogos_venda.py            # Testes unitários de jogos venda e seu repositório
|         ├── test_jogos.py                  # Testes unitários de jogos e seu repositório
|         ├── test_produtos.py               # Testes unitários de produtos e seu repositório
|         ├── test_transacoes.py             # Testes unitários de transações e seu repositório
|         └── test_venda.py                  # Testes unitários de venda e seu repositório
|  
├── README.md                                # Este arquivo
└── requirements.txt                         # Bibliotecas externas
```

## ✍️ Como usar 
- 1 - Clone o repositório
- 2 - Crie um ambiente virtual
  -  Abra o terminal
  -  Crie o venv: `python -m venv .venv`
- 3 -  Ative o venv:
    - 🐧 Linux/mac: `source .venv/bin/activate`
    - 🤖 Windows powershell: `.venv\Scripts\Activate.ps1`
    - 🖥️ Windows bash: `source .venv/Scripts/activate`
- 4 -  Atualize o pip: `python -m pip install --upgrade pip`
- 5 -  Adicione o gitignore (opcional): `echo "*" > .vevn/.gitignore`
- 6 -  Baixe as bibliotecas necessárias: `pip install -r requirements.txt`
  
- 7 - Para executar o arquivo principal, digite no Terminal: `python -m src.board_and_play_poo.main`
- 8 - Se quiser executar os testes use `python -m pytest`

## 🏛️ Arquitetura utilizada
> Domain Driven Development (DDD)

## 🎮 Principios SOLID
- S — `Princípio da responsabilidade única`
- O — `Princípio Aberto-Fechado`
- L — `Princípio da substituição de Liskov`
- I — `Princípio da Segregação da Interface`
- D — `Princípio da inversão da dependência`

## 🏗️ Padrões de projeto
- `Template Method` - Método AplicarDesconto presente em Aluguel e Venda
- `Decorator` - Chamar o método `create` de uma generalização toda vez que chama o método `create` de uma especificação (ex: toda criação de um `acessorio` leva à criação de um `produto` nas tabelas `acessorios` e `produtos`, respectivamente); Método para checar `status` de um contrato e aplicar multas, caso o contrato esteja `alterado`; Métodos que alterem status de um contrato de `'ABERTO'` ou `'ALTERADO'` para `'FECHADO'` ao término da interação de pagamento.

## 📚 Bibliotecas externas
- `sqlalchemy` - Para interagir com o banco de dados e facilitar migração
- `pytest` - Para testes unitários

## 👤 Membros
| Contribuidores 🧑‍🎓  | Funções 🚀 |
| ------------- | ------------- |
| [Icaro Cavalcante](https://github.com/Icaro-Cavalcante)  | Desenvolvedor  |
| [Elilúcio Teixeira](https://github.com/Elilucio7) | Desenvolvedor  |
| [Samuel Jackson](https://github.com/SJacksonML) | Desenvolvedor  |


| Professor Orientador  👨‍🏫 |
| ------------- |
| [Jayr Alencar Pereira](https://github.com/jayralencar)  |