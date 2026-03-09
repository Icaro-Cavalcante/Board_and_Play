from src.board_and_play_poo.repositories.repository_jogo_aluguel import RepositoryJogoAluguel
from src.board_and_play_poo.modules.domain.jogo_aluguel import JogoAluguel
from src.board_and_play_poo.modules.domain.transacoes import Transacao

class MenuRegistrarContrato:
    """Menu das classes Aluguel e ItemAluguel"""
    def menu_registrar_contrato():
        
        pass
        

"""
            self.itens_aluguel = Table('itens_aluguel', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('aluguel_id', Integer, ForeignKey('alugueis.id'), nullable=False),
            Column('jogo_id', Integer, ForeignKey('jogos.id'), nullable=False),
            Column('valor_diaria', Numeric(10,2)),
            Column('valor_sessao', Numeric(10,2))
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

        self.jogos_aluguel = Table('jogos_aluguel', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('jogo_id', Integer, ForeignKey('jogos.id'), nullable=False, unique=True),
            Column('etiqueta', String(50), unique=True, nullable=False),
            Column('status', String(20), nullable=False)  # 'DISPONIVEL', 'INDISPONIVEL', 'INATIVO'
        )
"""