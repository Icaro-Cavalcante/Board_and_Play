from pathlib import Path
from datetime import datetime
from src.board_and_play_poo.config_database import Config_database
from sqlalchemy import (
    Table, String, Column, MetaData, # para estrutura das tabelas
    Integer, Date, DateTime, Numeric, # para definir formato dos atributos
    ForeignKey) # para especializar relacionamentos
config = Config_database()

class Tabela():
    '''
    Classe responsável por gerenciar todas as tabelas do banco de dados.
    '''
    def __init__(self):
        self.metadata = MetaData()

# -------------------------------------------------- CADASTRO PESSOAS --------------------------------------------------

        self.clientes = Table('clientes', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('cpf', String(11), unique=True, nullable=False),
            Column('nome', String(40), nullable=False),
            Column('email', String(20), unique=True),
            Column('contato', String(11), unique=True, nullable=False),
            Column('status', String(20), nullable=False) # 'ATIVO', 'INATIVO', 'MULTADO'
        )

        self.colaboradores = Table('colaboradores', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('cpf', String(11), unique=True, nullable=False),
            Column('nome', String(40), nullable=False),
            Column('email', String(20), unique=True),
            Column('contato', String(11), unique=True, nullable=False),
            Column('contato_emergencia', String(11), unique=True, nullable=False),
            Column('salario', Numeric(10,2), nullable=False),
            Column('cargo', String(25), nullable=False),
            Column('status', String(10), nullable=False, default='ATIVO') # 'ATIVO', 'INATIVO', 'FERIAS', 'ATESTADO'
        )

# ------------------------------------------- TABELAS DA HIERARQUIA CONCEITUAL -------------------------------------------

        self.produtos = Table('produtos', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('nome', String(50), nullable=False),
            Column('codigo_barras', String(13), unique=True, nullable=False),
            Column('categoria', String(20), nullable=False)   # 'JOGO', 'ACESSORIO', 'CONSUMIVEL'
          )

        self.jogos = Table('jogos', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('produto_id', Integer, ForeignKey('produtos.id'), nullable=False, unique=True),
            Column('genero', String(15)),
            Column('descricao', String(200)),
            Column('idade_min', Integer, default=0),
            Column('num_jogadores', String(5), default=1)
        )
        
        self.jogos_aluguel = Table('jogos_aluguel', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('jogo_id', Integer, ForeignKey('jogos.id'), nullable=False, unique=True),
            Column('etiqueta', String(50), unique=True, nullable=False),
            Column('status', String(20), nullable=False)  # 'DISPONIVEL', 'INDISPONIVEL'
        )
        
        self.jogos_venda = Table('jogos_venda', self.metadata,
            Column('id', Integer, primary_key = True),
            Column('jogo_id', Integer, ForeignKey('jogos.id'), nullable=False, unique=True),
            Column('quantidade', Integer, nullable=False, default=1)
        )

        self.acessorios = Table('acessorios', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('produto_id', Integer, ForeignKey('produtos.id'), nullable=False, unique=True),
            Column('tipo_acessorio', String(20), nullable=False) # 'ROUPA', 'CHAVEIRO', 'CANECA'
        )

        self.consumiveis = Table('consumiveis', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('produto_id', Integer, ForeignKey('produtos.id'), nullable=False, unique=True),
            Column('data_validade', Date, nullable=False), #  default=datetime.date
            Column('lote', String(50)),
            Column('restricoes', String, nullable=False, default='Nenhum') # 'ALERGENICOS', 'LACTOSE', 'GLUTEN'
        )

# ------------------------------------------- TABELAS DA HIERARQUIA COMPORTAMENTAL -------------------------------------------
  
        self.transacoes = Table('transacoes', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('comprovante', String(10), unique = True),
            Column('data_hora', DateTime, nullable=False, default=datetime.now),
            Column('valor_total', Numeric(10,2), nullable=False),
            Column('forma_pagamento', String(30)),  # 'DINHEIRO', 'DEBITO', 'CREDITO', 'PIX'
            Column('tipo_transacao', String(10), nullable=False)  # 'VENDA' ou 'ALUGUEL'
        )

        self.vendas = Table('vendas', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('transacao_id', Integer, ForeignKey('transacoes.id'), nullable=False, unique=True),
            Column('cliente_id', Integer, ForeignKey('clientes.id'), nullable=False),
            Column('colaborador_id', Integer, ForeignKey('colaboradores.id')),
            Column('nota_fiscal', String(50), unique=True)
        )

        self.alugueis = Table('alugueis', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('transacao_id', Integer, ForeignKey('transacoes.id'), nullable=False, unique=True),
            Column('cliente_id', Integer, ForeignKey('clientes.id'), nullable=False),
            Column('colaborador_id', Integer, ForeignKey('colaboradores.id'), nullable=False),
            Column('numero_contrato', String(50), unique=True),
            Column('data_inicio', Date, nullable=False),
            Column('data_prevista_devolucao', Date, nullable=False),
            Column('data_devolucao_real', Date),
            Column('status', String, default='ABERTO') # 'ABERTO', 'ALTERADO' e 'FECHADO'
        )

# --------------------------------------------------- TABELAS RELACIONAIS ---------------------------------------------------

        self.itens_venda = Table('itens_venda', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('venda_id', Integer, ForeignKey('vendas.id'), nullable=False),
            Column('produto_id', Integer, ForeignKey('produtos.id'), nullable=False),
            Column('quantidade_venda', Integer, default=1),
            Column('preco_unitario', Numeric(10,2))
        )
        
        self.itens_aluguel = Table('itens_aluguel', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('aluguel_id', Integer, ForeignKey('alugueis.id'), nullable=False),
            Column('jogo_id', Integer, ForeignKey('jogos.id'), nullable=False),
            Column('valor_diaria', Numeric(10,2)),
            Column('valor_sessao', Numeric(10,2))
        )

        self.multas = Table('multas', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('item_aluguel_id', ForeignKey('itens_aluguel.id'), nullable=False,),
            Column('multa_diaria', Numeric(10,2), default=0),
            Column('multa_avaria', Numeric(10,2), default=0)
        )

# --------------------------------------------------------- MÉTODO ----------------------------------------------------------

    def create_table(self, database):
            '''Cria as tabelas no banco de dados'''
            if database.ambiente == "real":
                config.DATABASE_DIR.mkdir(exist_ok=True) # check se a tabela já existe
                self.metadata.create_all(database.session)
            elif database.ambiente == "teste":
                config.TESTS_DIR.mkdir(exist_ok=True) # check se a tabela já existe
                self.metadata.create_all(database.test_session)
