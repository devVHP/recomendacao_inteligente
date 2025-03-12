from datetime import datetime
from typing import Disc, List, Optional, Set
import numpy as np
from collections import defaultdict
from collections import deque

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

        def buscar_produtos_relacionados(catalogo,produto_inicial,max_produtos=5):
            # Inicialização
            fila = deque([produto_inicial])
            visitados = {produto_inicial}
            relacionados = []

            # Busca
            while fila and len(relacionados) < max_produtos:
                atual = fila.popleft()

                if atual != produto_inicial:
                    relacionados.append(atual)

                produto = catalogo[atual]
                for similiar_id in produto.produtos_similares:
                    if similiar_id not in visitados:
                        fila.append(similiar_id)
                        visitados.add(similiar_id)
            return relacionados