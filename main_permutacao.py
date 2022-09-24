import gc
from puzzle import Puzzle8
import numpy as np

# Trabalho Prático 1 - de Sistemas de Informações
# Jogo 8-puzzle com heurística
# Barbara Calderon e Edmilson Domingues

configuracao_inicial = [1, 2, 3, 4, 5, 6, 7, 9, 8] # 1 passo
#configuracao_inicial = [1, 2, 3, 4, 5, 6, 9, 7, 8] # 2 passo
#configuracao_inicial = [1, 2, 3, 9, 5, 6, 4, 7, 8] # 3 passos. 
#configuracao_inicial = [9, 2, 3, 1, 5, 6, 4, 7, 8] # 4 passos.
#configuracao_inicial = [2, 9, 3, 1, 5, 6, 4, 7, 8] # 5 passos.
#configuracao_inicial = [2, 3, 9, 1, 5, 6, 4, 7, 8] # 6 passos.
#configuracao_inicial = [2, 3, 9, 1, 4, 6, 7, 5, 8] # 6 passos.
#configuracao_inicial = [2, 3, 6, 1, 5, 9, 4, 7, 8] # 7 passos.
#configuracao_inicial = [2, 3, 6, 1, 9, 5, 4, 7, 8] # 8 passos.
#configuracao_inicial = [9, 1, 2, 5, 6, 3, 4, 7, 8] # 8 passos.
configuracao_inicial = [6, 7, 5, 1, 2, 3, 9, 4, 8] # benchmark professor (18 passos previstos)
lista_origem = [1, 2, 3, 4, 5, 6, 7, 8, 9]
configuracao_inicial = np.random.permutation(lista_origem)
print("Configuração inicial: ", configuracao_inicial)
configuracao_final = [1, 2, 3, 4, 5, 6, 7, 8, 9]
metodo_utilizado = 2

# método 0: custo uniforme (sem heurística)
# método 1: A* com heurística simples
# método 2: A* com heurística mais precisa que conseguirem

puzzle = Puzzle8(configuracao_inicial, configuracao_final, metodo_utilizado)
metodo = puzzle.get_metodo_utilizado()
if metodo == 0:
    heuristica = 0
else:
    if metodo == 1:
        heuristica = puzzle.calcula_heuristica_simples(configuracao_inicial)
    else:
        heuristica = puzzle.calcula_heuristica_precisa(configuracao_inicial)
caminho_inicial = [[[configuracao_inicial], 0, heuristica, heuristica]]
puzzle.set_nodos_abertos(caminho_inicial) ## correção
puzzle.set_nodos_fechados([])
continua = True
iteracao = 0
while continua and puzzle.tem_abertos():
    iteracao += 1
    print("Iteração: ", iteracao)
    '''
    print()
    print("Nova iteração")
    print(f'Total de nodos abertos: {puzzle.get_total_nodos_abertos()}')
    nodos_abertos = puzzle.get_nodos_abertos()
    for i in range(len(nodos_abertos)):
        print(nodos_abertos[i])
    print(f'Total de nodos fechados: {puzzle.get_total_nodos_fechados()}')
    nodos_fechados = puzzle.get_nodos_fechados()
    for i in range (len(nodos_fechados)):
        print(nodos_fechados[i])
    print(f'Nodos fechados: {puzzle.get_nodos_fechados()}')
    '''
    #puzzle.busca_nodo_menor_custo()
    puzzle.extrai_nodo_da_vez()
    nodo_da_vez = puzzle.get_nodo_da_vez()
    estado = nodo_da_vez[0][len(nodo_da_vez[0]) -1]
    #print("Estado antes: ", estado)
    if puzzle.eh_nodo_objetivo(estado):
        print("---------------------------------------------")
        print(f'Caminho final: {puzzle.resultado()}')
        print(f'Tamanho do caminho: {puzzle.tamanho_do_caminho_final()}')
        print(f'Total de nodos abertos: {puzzle.get_total_nodos_abertos()}')
        nodos_abertos = puzzle.get_nodos_abertos()
        for i in range(len(nodos_abertos)):
            print(nodos_abertos[i])
        print(f'Total de nodos fechados: {puzzle.get_total_nodos_fechados()}')
        nodos_fechados = puzzle.get_nodos_fechados()
        for i in range (len(nodos_fechados)):
            print(nodos_fechados[i])
        continua = False
    else:
        filhos = puzzle.gera_nodos_filhos(estado)
        #print("Filhos: ", filhos)
        for i in range(len(filhos)):
            if not puzzle.esta_em_nodos_abertos(filhos[i]) and not puzzle.esta_em_nodos_fechados(filhos[i]):
                '''
                print()
                print('Passou em 1')
                print("contador i: ", i)
                print("Nodos abertos 1: ", puzzle.get_nodos_abertos()) # certo
                '''
                caminho = puzzle.atribui_custos_ao_nodo(filhos[i])
                #print("Nodos abertos 2: ", puzzle.get_nodos_abertos()) #errado
                #print("Caminho novo: ", caminho)
                puzzle.coloca_em_abertos(caminho) #
                #print("Nodos abertos : ", puzzle.get_nodos_abertos())
            else:
                if puzzle.esta_em_nodos_abertos(filhos[i]):
                    print()
                    print('Passou em 2')
                    #puzzle.avalia_substituicao_em_abertos(filhos[i])
                else:
                    print('Passou em 3')
                    #puzzle.avalia_substituicao_fechados(filhos[i])
        #print(f'Nodo da vez: {nodo_da_vez}')
        puzzle.retira_de_nodo_da_vez_coloca_em_fechados(nodo_da_vez)
        #print("_*_*_*_*_*_*_*_*_*_")

if continua is True:
    print("Falha")
del puzzle
gc.collect()