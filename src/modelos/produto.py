from datetime import datetime
from typing import Disc, List, Optional, Set
import numpy as np
from collections import defaultdict

class Produto:
    def __init__(self,
                 identificador: int,
                 preco: float,
                 nome: str,
                 categoria: str,
                 caracteristicas: Disc[str, any]):
        self.identificador = identificador
        self.nome =  nome
        self.preco = preco
        self.categoria = categoria
        self.caracteristicas = caracteristicas


        # Histórico e métricas estabelecidas
        self.historico_visualizacoes: List[Disc]
        self.historico_compras: List[Disc] = []
        self.avaliacoes: List[Disc] = []
        self.produtos_similares: Set[int] = set()

        # Métricas dinâmicas
        self.popularidade = 0.0
        self.tendencia = 0.0
        self.ultima_atualizacao = datetime.now()

        #Vetores para aprendizado de máquina
        self.valor_caracteristicas = Optional[np.array()] = None
        self.gerar_vetor_caracteristicas()

        def adicionar_avalicao(self,
                                usuario.id: int,
                                nota: float,
                                comentario: str = "",
                                metadata: Dict = None) -> None: