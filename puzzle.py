
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

    def get_metodo_utilizado(self):
        return self.metodo_utilizado

    def get_nodos_abertos(self):
        return self.nodos_abertos

    def set_nodos_abertos(self, nodos_abertos):
        self.nodos_abertos = nodos_abertos

    def get_nodos_fechados(self):
        return self.nodos_fechados

    def set_nodos_fechados(self, nodos_fechados):
        self.nodos_fechados = nodos_fechados
        
    def get_nodo_da_vez(self):
        return self.nodo_da_vez
        
    def set_nodo_da_vez(self, nodo):
        self.nodo_da_vez = nodo

    def tem_abertos(self):
        return len(self.get_nodos_abertos()) > 0

    def get_total_nodos_abertos(self):
        return len(self.get_nodos_abertos())

    def get_total_nodos_fechados(self):
        return len(self.get_nodos_fechados())

    def menor_custo_abertos(self):
        self.nodo_da_vez = self.get_nodos_abertos()[0][len(self.nodos_abertos[0]) - 1]
        return self.nodo_da_vez

    def ordena_nodos_abertos(self):
        nodos_abertos_em_ordem = self.get_nodos_abertos()
        nodos_abertos_em_ordem.sort()
        return nodos_abertos_em_ordem

    def eh_nodo_objetivo(self, nodo_da_vez):
        return nodo_da_vez == self.get_estado_final()

    def resultado(self):
        return self.get_nodos_abertos()[0]
    
    def tamanho_do_caminho_final(self):
        return self.get_nodos_abertos()[0][1]

    def esta_em_nodos_abertos(self, nodo_filho):
        if len(self.get_nodos_abertos()) == 0:
            return False
        for i in range(len(self.get_nodos_abertos())):
            if nodo_filho in self.get_nodos_abertos()[i][0][len(self.get_nodos_abertos()[i][0]) - 1]:
                return True
        return False

    def esta_em_nodos_fechados(self, nodo_filho):
        if len(self.nodos_fechados) == 0:
            return False
        for i in range(len(self.get_nodos_fechados())):
            if nodo_filho in self.get_nodos_fechados()[i][len(self.get_nodos_fechados()[i]) - 1]:
                return True
        return False
    
    def extrai_nodo_da_vez(self):
        nodos_abertos = self.get_nodos_abertos()
        nodo_da_vez = nodos_abertos[0]
        nodos_abertos.pop(0)
        self.set_nodos_abertos(nodos_abertos)
        self.set_nodo_da_vez(nodo_da_vez)
        
    def atribui_custos_ao_nodo(self, nodo_filho):
        metodo = self.get_metodo_utilizado()
        caminho = self.get_nodo_da_vez()
        print("Caminho antes: ", caminho)
        caminho[0].append(nodo_filho)
        caminho[1] += 1
        caminho[3] += 1
        if metodo == 0:
            heuristica = 0
        else:
            if metodo == 1:
                heuristica = self.calcula_heuristica_simples(nodo_filho)
                caminho[2] = heuristica
                caminho[3] = caminho[1] + heuristica
            else:
                heuristica = self.calcula_heuristica_precisa(nodo_filho)
                caminho[2] = heuristica
                caminho[3] = caminho[1] + heuristica
        print("Caminho depois: ", caminho)
        return caminho
                
    def calcula_heuristica_simples(self, nodo_filho):
        final = self.get_estado_final()
        heuristica = 0
        for i in range(9):
            if final[i] != 9 and final[i] != nodo_filho[i]:
                heuristica += 1
        return heuristica
    
    def calcula_heuristica_precisa(self, nodo_filho):
        matriz_diferenca = [
            [0, 1, 2, 1, 2, 3, 2, 3, 4],
            [1, 0, 1, 2, 1, 2, 3, 2, 3],
            [2, 1, 0, 3, 2, 1, 4, 3, 2],
            [1, 2, 3, 0, 1, 2, 1, 2, 3],
            [2, 1, 2, 1, 0, 1, 2, 1, 2],
            [3, 2, 1, 2, 1, 0, 3, 2, 1],
            [2, 3, 4, 1, 2, 3, 0, 1, 2],
            [3, 2, 3, 2, 1, 2, 1, 0, 1],
            [4, 3, 2, 3, 2, 1, 2, 1, 0]
            ]
        final = self.get_estado_final()
        heuristica = 0
        for i in range(9):
            if final[i] != 9:
                for j in range(9):
                    if nodo_filho[j] == final[i]:
                        diferenca = matriz_diferenca[i][j]
                        heuristica += diferenca
                        break
        return heuristica

    def gera_nodos_filhos(self, estado):
        pai = estado
        print("Pai: ", pai)
        for i in range(9):
            if pai[i] == 9:
                ordem = i
        nodos_filhos = [
            [
                [pai[1], pai[0], pai[2], pai[3], pai[4], pai[5], pai[6], pai[7], pai[8]],
                [pai[3], pai[1], pai[2], pai[0], pai[4], pai[5], pai[6], pai[7], pai[8]]
            ],
            [
                [pai[1], pai[0], pai[2], pai[3], pai[4], pai[5], pai[6], pai[7], pai[8]],
                [pai[0], pai[2], pai[1], pai[3], pai[4], pai[5], pai[6], pai[7], pai[8]],
                [pai[0], pai[4], pai[2], pai[3], pai[1], pai[5], pai[6], pai[7], pai[8]]
            ],
            [
                [pai[0], pai[2], pai[1], pai[3], pai[4], pai[5], pai[6], pai[7], pai[8]],
                [pai[0], pai[1], pai[5], pai[3], pai[4], pai[2], pai[6], pai[7], pai[8]]
            ],
            [
                [pai[3], pai[1], pai[2], pai[0], pai[4], pai[5], pai[6], pai[7], pai[8]],
                [pai[0], pai[1], pai[2], pai[4], pai[3], pai[5], pai[6], pai[7], pai[8]],
                [pai[0], pai[1], pai[2], pai[6], pai[4], pai[5], pai[3], pai[7], pai[8]]
            ],
            [
                [pai[0], pai[4], pai[2], pai[3], pai[1], pai[5], pai[6], pai[7], pai[8]],
                [pai[0], pai[1], pai[2], pai[4], pai[3], pai[5], pai[6], pai[7], pai[8]],
                [pai[0], pai[1], pai[2], pai[3], pai[5], pai[4], pai[6], pai[7], pai[8]],
                [pai[0], pai[1], pai[2], pai[3], pai[7], pai[5], pai[6], pai[4], pai[8]]
            ],
            [
                [pai[0], pai[1], pai[5], pai[3], pai[4], pai[2], pai[6], pai[7], pai[8]],
                [pai[0], pai[1], pai[2], pai[3], pai[5], pai[4], pai[6], pai[7], pai[8]],
                [pai[0], pai[1], pai[2], pai[3], pai[4], pai[8], pai[6], pai[7], pai[5]]
            ],
            [
                [pai[0], pai[1], pai[2], pai[6], pai[7], pai[5], pai[3], pai[7], pai[8]],
                [pai[0], pai[1], pai[2], pai[3], pai[4], pai[5], pai[7], pai[6], pai[8]]            ],
            [
                [pai[0], pai[1], pai[2], pai[3], pai[7], pai[5], pai[6], pai[4], pai[8]],
                [pai[0], pai[1], pai[2], pai[3], pai[4], pai[5], pai[7], pai[6], pai[8]],
                [pai[0], pai[1], pai[2], pai[3], pai[4], pai[5], pai[6], pai[8], pai[7]]
            ],
            [
                [pai[0], pai[1], pai[2], pai[3], pai[4], pai[8], pai[6], pai[7], pai[5]],
                [pai[0], pai[1], pai[2], pai[3], pai[4], pai[5], pai[6], pai[8], pai[7]]
            ]
        ]
        print("Nodos Filhos: ", nodos_filhos[ordem])
        return nodos_filhos[ordem]

    def coloca_em_abertos(self, caminho):
        nodos_abertos = self.get_nodos_abertos()
        nodos_abertos.append(caminho)
        self.set_nodos_abertos(nodos_abertos)
        
    def aaa_busca_nodo_menor_custo(self):
        # Ordenação de acordo com o custo total
        nodos_abertos = self.get_nodos_abertos()
        menor_custo_total_ate_agora = nodos_abertos[0][-1]
        indice_nodo_menor_custo_total_ate_agora = 0
        nodo_aberto_com_menor_custo_total = nodos_abertos[0]
        for i, value in enumerate(nodos_abertos):
            # caminho = value[0]
            # custo = value[1]
            # heuristica = value[2]
            custo_total_nodo_atual = value[3]
            if custo_total_nodo_atual < menor_custo_total_ate_agora:
                menor_custo_total_ate_agora = custo_total_nodo_atual
                indice_nodo_menor_custo_total_ate_agora = i
                nodo_aberto_com_menor_custo_total = value
        nodos_abertos.pop(indice_nodo_menor_custo_total_ate_agora)
        nodos_abertos[0] = nodo_aberto_com_menor_custo_total
        self.set_nodos_abertos(nodos_abertos)

    def busca_nodo_menor_custo(self):
        # Ordenação de acordo com o custo total
        nodos_abertos = self.get_nodos_abertos()
        ## menor_custo_total_ate_agora = nodos_abertos[0][-1]
        menor_custo_total_ate_agora = nodos_abertos[0][3] ## Troquei.
        indice_nodo_menor_custo_total_ate_agora = 0
        nodo_aberto_com_menor_custo_total = nodos_abertos[0]
        #for i, value in enumerate(nodos_abertos):
        #    # caminho = value[0]
        #    # custo = value[1]
        #    # heuristica = value[2]
        #      custo_total_nodo_atual = value[3]
        indice = 0
        nodo_aberto_com_menor_custo_total = nodos_abertos[0]
        for i, value in enumerate(nodos_abertos):
            # caminho = value[0]
            # custo = value[1]
            # heuristica = value[2]
            custo_total_nodo_atual = value[3]
            if custo_total_nodo_atual < menor_custo_total_ate_agora:
                menor_custo_total_ate_agora = custo_total_nodo_atual
                indice_nodo_menor_custo_total_ate_agora = i
                nodo_aberto_com_menor_custo_total = value
        nodos_abertos.pop(indice_nodo_menor_custo_total_ate_agora)
        #nodos_abertos[0] = nodo_aberto_com_menor_custo_total
        nodos_abertos.insert(0, nodo_aberto_com_menor_custo_total)
        self.set_nodos_abertos(nodos_abertos)
        
    def avalia_substituicao_em_abertos(self, nodo_filho):
        for i in range(len(self.get_nodos_abertos())):
            if nodo_filho in self.get_nodos_abertos()[i][len(self.get_nodos_abertos()[i]) - 1] == nodo_filho:
                custo_total_nodo_em_abertos = self.get_nodos_abertos()[i][3]
                caminho = self.atribui_custos_ao_nodo(nodo_filho)
                custo_total_nodo_filho = self.atribui_custos_ao_nodo(nodo_filho)[3]
                if custo_total_nodo_em_abertos <= custo_total_nodo_filho:
                    break
                else:
                    caminho_custoso = self.nodos_abertos.pop(i)
                    self.nodos_fechados.append(caminho_custoso) # retira abertos e coloca em fechados
                    self.nodos_abertos.append(caminho) # coloca o de menor custo em abertos
                    break

    def avalia_substituicao_fechados(self, nodo_filho):
        for i in range(len(self.get_nodos_fechados())):
            if nodo_filho in self.get_nodos_fechados()[i][len(self.get_nodos_fechados()[i]) - 1] == nodo_filho:
                custo_total_nodo_em_fechados = self.get_nodos_fechados()[i][3]
                caminho = self.atribui_custos_ao_nodo(nodo_filho)
                custo_total_nodo_filho = self.atribui_custos_ao_nodo(nodo_filho)[3]
                if custo_total_nodo_em_fechados <= custo_total_nodo_filho:
                    break
                else:
                    self.nodos_fechados.pop(i)
                    self.nodos_abertos.append(caminho) # retira fechados e coloca em abertos
                    break

    def retira_de_abertos_coloca_em_fechados(self, nodo_da_vez):
        nodos_abertos = self.get_nodos_abertos()
        if nodo_da_vez in nodos_abertos:
            nodo_removido_de_abertos = nodos_abertos.pop(0)
            self.set_nodos_abertos(nodos_abertos)
            self.set_nodos_fechados(nodo_removido_de_abertos)
