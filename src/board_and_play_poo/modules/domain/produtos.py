from pathlib import Path
caminho_data_pasta = r"src/board_and_play_poo/data"

class Produto:
    '''Integra atributos em comum de suas subclasses, mantendo controle do atributo 'custo' para verificar valor de operação/despesa'''

    def __init__(self, id, nome, custo_aquisicao):
        self._nome = nome
        self._id = id
        self._custo_aquisicao = custo_aquisicao

    def pasta_database():
        '''Método que cria a pasta (data) de dados, caso ela não exista'''
        data_dir = Path(caminho_data_pasta)
        data_dir.mkdir(exist_ok=True)