
class Puzzle8:

    def __init__(self, estado_inicial, estado_final, metodo_utilizado):
        self.estado_final = estado_final
        self.estado_inicial = estado_inicial
        self.nodos_abertos = []
        self.nodos_fechados = []
        self.proximo_nodo = []
        self.nodo_da_vez = []
        self.metodo_utilizado = metodo_utilizado
        # método 0: custo uniforme (sem heurística)
        # método 1: A* com heurística simples
        # método 2: A* com heurística mais precisa que conseguirem

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
        # if len(self.nodos_abertos) > 0:
        #   return True
        #return False
        return len(self.get_nodos_abertos()) > 0

    def get_total_nodos_abertos(self):
        return len(self.get_nodos_abertos())

    def get_total_nodos_fechados(self):
        return len(self.get_nodos_fechados())

    def menor_custo_abertos(self):
        # nodos_abertos_em_ordem = self.ordena_nodos_abertos() # Teoricamente já está ordenado.
        # self.set_nodos_abertos(nodos_abertos_em_ordem)
        # return nodos_abertos_em_ordem[0]
        self.nodo_da_vez = self.get_nodos_abertos()[0][len(self.nodos_abertos[0] - 1)]
        return self.nodo_da_vez

    def ordena_nodos_abertos(self):
        nodos_abertos_em_ordem = self.get_nodos_abertos()
        nodos_abertos_em_ordem.sort()
        return nodos_abertos_em_ordem

    def eh_nodo_objetivo(self, nodo_da_vez):
        # nodo_objetivo = self.get_estado_final()
        # if nodo_da_vez == nodo_objetivo:
        #    return True
        # return False
        return nodo_da_vez == self.get_estado_final() # Existe comparação de listas, assim?

    def resultado(self):
        return self.get_nodos_abertos()[0]
    
    def tamanho_do_caminho_final(self):
        return self.get_nodos_abertos()[1] # Criei este método.

    def esta_em_nodos_abertos(self, nodo_filho): # reescrevendo o método acima
        if len(self.get_nodos_abertos()) == 0:
            return False
        for i in range(len(self.get_nodos_abertos())):
            if nodo_filho in self.get_nodos_abertos()[i][len(self.get_nodos_abertos()[i]) -1]: # "in" funciona?
                return True
        return False

    def esta_em_nodos_fechados(self, nodo_filho): # reescrevendo o método acima
        if len(self.nodos_fechados) == 0:
            return False
        for i in range(len(self.get_nodos_fechados())):
            if nodo_filho in self.get_nodos_fechados()[i][len(self.get_nodos_fechados()[i]) -1]: # "in" funciona?
                return True
        return False
    
    def atribui_custos_ao_nodo(nodo_filho):
        pass

    def gera_nodos_filhos(self, nodo_da_vez):
        pai = nodo_da_vez
        for i in range(9):
            if pai[i] == 9:
                ordem = i
        nodos_filhos = [
            [
                [
                    pai[1], pai[0], pai[2], pai[3], pai[4], pai[5], pai[6], pai[7], pai[8]
                ],
                [
                    pai[3], pai[1], pai[2], pai[0], pai[4], pai[5], pai[6], pai[7], pai[8]
                ]
            ],
            [
                [
                    pai[1], pai[0], pai[2], pai[3], pai[4], pai[5],
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

