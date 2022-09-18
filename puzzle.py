
class Puzzle8:

    def __init__(self, estado_inicial, estado_final, metodo_utilizado=1):
        self.estado_final = estado_final
        self.estado_inicial = estado_inicial
        self.nodos_abertos = []
        self.nodos_fechados = []
        self.proximo_nodo = []
        self.metodo_utilizado = metodo_utilizado

    def get_estado_final(self):
        return self.estado_final

    def set_estado_final(self, estado_final):
        self.estado_final = estado_final

    def get_estado_inicial(self):
        return self.estado_inicial

    def set_estado_inicial(self, estado_inicial):
        self.estado_inicial = estado_inicial

    def get_nodos_abertos(self):
        return self.nodos_abertos

    def set_nodos_abertos(self, nodos_abertos):
        self.nodos_abertos = nodos_abertos

    def get_nodos_fechados(self):
        return self.nodos_fechados

    def set_nodos_fechados(self, nodos_fechados):
        self.nodos_fechados = nodos_fechados

    def tem_abertos(self):
        if len(self.nodos_abertos) > 0:
            return True
        return False

    def menor_custo_abertos(self):
        nodos_abertos_em_ordem = self.ordena_nodos_abertos()
        self.set_nodos_abertos(nodos_abertos_em_ordem)
        return nodos_abertos_em_ordem[0]

    def ordena_nodos_abertos(self):
        nodos_abertos_em_ordem = self.get_nodos_abertos()
        nodos_abertos_em_ordem.sort()
        return nodos_abertos_em_ordem

    def eh_nodo_objetivo(self, nodo_da_vez):
        nodo_objetivo = self.get_estado_final()
        if nodo_da_vez == nodo_objetivo:
            return True
        return False

    def resultado(self):
        pass

    def gera_nodos_filhos(self, nodo_da_vez):
        pai = nodo_da_vez
        for i in range(9):
            if pai[i] == '8':
                ordem = i
        nodos_filhos = [
            [
                [
                    pai[1],
                    pai[0],
                    pai[2],
                    pai[3],
                    pai[4],
                    pai[5],
                    pai[6],
                    pai[7],
                    pai[8]
                ],
                [
                    pai[3],
                    pai[1],
                    pai[2],
                    pai[0],
                    pai[4],
                    pai[5],
                    pai[6],
                    pai[7],
                    pai[8]
                ]
            ],
            [
                [
                    pai[1],
                    pai[0],
                    pai[2],
                    pai[3],
                    pai[4],
                    pai[5],
                    pai[6],
                    pai[7],
                    pai[8]
                ],
                [
                    pai[0],
                    pai[2],
                    pai[1],
                    pai[3],
                    pai[4],
                    pai[5],
                    pai[6],
                    pai[7],
                    pai[8],
                ],
                [
                    pai[0],
                    pai[4],
                    pai[2],
                    pai[3],
                    pai[1],
                    pai[5],
                    pai[6],
                    pai[7],
                    pai[8]
                ]
            ],
            [
                [
                    pai[0],
                    pai[2],
                    pai[1],
                    pai[3],
                    pai[4],
                    pai[5],
                    pai[6],
                    pai[7],
                    pai[8],
                ],
                [
                    pai[0],
                    pai[1],
                    pai[5],
                    pai[3],
                    pai[4],
                    pai[2],
                    pai[6],
                    pai[7],
                    pai[8],
                ]
            ],
            [
                [
                    pai[3],
                    pai[1],
                    pai[2],
                    pai[0],
                    pai[4],
                    pai[5],
                    pai[6],
                    pai[7],
                    pai[8],
                ],
                [
                    pai[0],
                    pai[1],
                    pai[2],
                    pai[3],
                    pai[4],
                    pai[5],
                    pai[6],
                    pai[7],
                    pai[8],
                ],
                [
                    pai[0],
                    pai[1],
                    pai[2],
                    pai[6],
                    pai[4],
                    pai[5],
                    pai[3],
                    pai[7],
                    pai[8],
                ]
            ],
            [
                [
                    pai[0],
                    pai[4],
                    pai[2],
                    pai[3],
                    pai[1],
                    pai[5],
                    pai[6],
                    pai[7],
                    pai[8],
                ],
                [
                    pai[0],
                    pai[1],
                    pai[2],
                    pai[4],
                    pai[3],
                    pai[5],
                    pai[6],
                    pai[7],
                    pai[8],
                ],
                [
                    pai[0],
                    pai[1],
                    pai[2],
                    pai[3],
                    pai[5],
                    pai[4],
                    pai[6],
                    pai[7],
                    pai[8],
                ],
                [
                    pai[0],
                    pai[1],
                    pai[2],
                    pai[3],
                    pai[7],
                    pai[5],
                    pai[6],
                    pai[4],
                    pai[8],
                ]
            ],
            [
                [
                    pai[0],
                    pai[1],
                    pai[5],
                    pai[3],
                    pai[4],
                    pai[2],
                    pai[6],
                    pai[7],
                    pai[8],
                ],
                [
                    pai[0],
                    pai[1],
                    pai[2],
                    pai[3],
                    pai[5],
                    pai[4],
                    pai[6],
                    pai[7],
                    pai[8],
                ],
                [
                    pai[0],
                    pai[1],
                    pai[2],
                    pai[3],
                    pai[4],
                    pai[8],
                    pai[6],
                    pai[7],
                    pai[5],
                ]
            ],
            [
                [
                    pai[0],
                    pai[1],
                    pai[2],
                    pai[3],
                    pai[7],
                    pai[5],
                    pai[6],
                    pai[4],
                    pai[8],
                ],
                [
                    pai[0],
                    pai[1],
                    pai[2],
                    pai[3],
                    pai[4],
                    pai[5],
                    pai[7],
                    pai[6],
                    pai[8],
                ],
                [
                    pai[0],
                    pai[1],
                    pai[2],
                    pai[3],
                    pai[4],
                    pai[5],
                    pai[6],
                    pai[8],
                    pai[7],
                ]
            ],
            [
                [
                    pai[0],
                    pai[1],
                    pai[2],
                    pai[3],
                    pai[4],
                    pai[8],
                    pai[6],
                    pai[7],
                    pai[5],
                ],
                [
                    pai[0],
                    pai[1],
                    pai[2],
                    pai[3],
                    pai[4],
                    pai[5],
                    pai[6],
                    pai[8],
                    pai[7],
                ]
            ]
        ]
        return nodos_filhos[ordem]
