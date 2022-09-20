import gc
from puzzle import Puzzle8

# Trabalho Prático 1 - de Sistemas de Informações
# Jogo 8-puzzle com heurística
# Barbara Calderon e Edmilson Domingues

# configuracao_inicial = [1, 2, 3, 4, 9, 5, 7, 8, 6]
configuracao_inicial = [1, 2, 3, 4, 5, 6, 7, 9, 8]
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

while continua and puzzle.tem_abertos():
    puzzle.busca_nodo_menor_custo()
    abertos = puzzle.get_nodos_abertos()
    #nodo_da_vez = abertos[0][len(abertos[0]) -1]
    nodo_da_vez = abertos[0][0][len(abertos[0][0])-1]
    if puzzle.eh_nodo_objetivo(nodo_da_vez):
        print(f'Caminho final: {puzzle.resultado()}')
        print(f'Tamanho do caminho: {puzzle.tamanho_do_caminho_final()}')
        print(f'Total de nodos abertos: {puzzle.get_total_nodos_abertos()}')
        print(f'Nodos abertos: {puzzle.get_nodos_abertos()}')
        print(f'Total de nodos fechados: {puzzle.get_total_nodos_fechados()}')
        print(f'Nodos fechados: {puzzle.get_nodos_fechados()}')
        continua = False
    else:
        filhos = puzzle.gera_nodos_filhos(nodo_da_vez)
        for i in range(len(filhos)):
            if not puzzle.esta_em_nodos_abertos(filhos[i]) and not puzzle.esta_em_nodos_fechados(filhos[i]):
                caminho = puzzle.atribui_custos_ao_nodo(filhos[i])
                puzzle.coloca_em_abertos(caminho)
            else:
                if puzzle.esta_em_nodos_abertos(filhos[i]):
                    puzzle.avalia_substituicao_em_abertos(filhos[i])
                else:
                    puzzle.avalia_substituicao_fechados(filhos[i])
                    pass
        puzzle.retira_de_abertos_coloca_em_fechados(nodo_da_vez)

if continua is True:
    print("Falha")
del puzzle
gc.collect()
