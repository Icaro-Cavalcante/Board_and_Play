# Board & Play ♙

> Um sistema de gerenciamento de estoque e contratos de serviços para um negócio de aluguel de jogos de tabuleiro.

## ℹ️ Sobre 

- A Board & Play é um projeto da disciplina de Programação Orientada a Objetos da Universidade Federal do Cariri (UFCA), a qual é ministrada pelo professor Jayr Pereira.
- O objetivo é desenvolver um sistema de linha de comando (CLI) para gerenciar um negócio fictício de aluguel de jogos de tabuleiro.
- Nele são necessárias as funcionalidades de cadastro de jogos e clientes no sistema, controle de contratos ativos e de clientes com pagamentos pendentes, multas por violação de contrato por tempo ou avaria do produto, registro de pagamentos, cálculo de custos de risco e previsiblidade de receita.


## 📋 Pré-requisitos

- Python 3

## 📦 Estrutura do projeto

```
Board_and_Play/
├── src/boad_and_play_poo            
|   ├── modules
|   |   ├── domain
|   |   |    ├── __init__.py          # Transforma o diretório em um pacote
|   |   |    ├── alugaveis.py         # Classe utilizada para gerenciamento de jogos que atendem aos serviços de aluguel
|   |   |    ├── clientes.py          # Classe utilizada para cadastro e gerenciamento de clientes
|   |   |    ├── colaboradores.py     # Classe utilizada para para cadastro e gerenciamento de colaboradores
|   |   |    ├── compraveis.py        # Classe utilizada para gerenciamento de jogos que atendem aos serviços de compra
|   |   |    ├── jogos.py             # Classe pai que dá atributos comuns aos jogos alugáveis e compráveis
|   |   |    └── produtos.py          # Classe pai principal do negócio que dá atributos comuns a todos os itens do negócio
|   |   |
|   |   ├── infraestructure
|   |   |    ├── __init__.py          # Transforma o diretório em um pacote
|   |   |    └── configuracoes.py     # Arquivo de configurações
|   |   |
|   |   └── services
|   |       ├── __init__.py           # Transforma o diretório em um pacote
|   |       ├── aluguel.py            # Classe utilizada para CRUD das instânicas de contratos de aluguel
|   |       ├── negocios.py           # Classe utilizada para observar outras classes e manter registro de somatórios
|   |       ├── transacoes.py         # Classe utilizada para CRUD das instâncias de comprovantes de pagamento
|   |       └── venda.py              # Classe utilizada para CRUD das instâncias de vendas de produto
|   |  
|   ├── __init__.py                   # Transforma o diretório em um pacote
|   └── main.py                       # Arquivo principal do sistema
|              
├── testes
|   ├── __init__.py                   # Transforma o diretório em um pacote
|   ├── test_aluguel.py               # Testes para o aluguel
|   └── test_jogo_aluguel.py          # Testes para os jogos alugáveis
|
├── README.md                         # Este arquivo
|
└── __init__.py                       # Transforma o diretório em um pacote
```

## 🖳 Como usar 
- 1 - Clone o repositório
- 2 - Crie um ambiente virtual
  -  Abra o terminal
  -  Crie o venv: `python -m venv .venv`
  -  Ative o venv:
    - Linux/mac: `source .venv/bin/activate`
    - Windows powershell: `.venv\Scripts\Activate.ps1`
    - Windows bash: `source .venv/Scripts/activate`
  -  Atualize o pip: `python -m pip install --upgrade pip`
  -  Adicione o gitignore (opcional): `echo "*" > .vevn/.gitignore`
  -  Baixe a biblioteca necessária para os testes: `pip install pytest`
  
- 3 - Para rodar o arquivo principal, digite no Terminal: `python src/board_and_play_poo/main.py`



## 📖 UML textual


