import gc
from puzzle import Puzzle8

# Trabalho Prático 1 - de Sistemas de Informações
# Jogo 8-puzzle com heurística
# Barbara Calderon e Edmilson Domingues

configuracao_inicial = [1, 4, 5, 8, 9, 2, 3, 7, 6]
configuracao_final = [1, 2, 3, 4, 5, 6, 7, 8, 9]
metodo_utilizado = 1

# método 0: custo uniforme (sem heurística)
# método 1: A* com heurística simples
# método 2: A* com heurística mais precisa que conseguirem

puzzle = Puzzle8(configuracao_inicial, configuracao_final, metodo_utilizado)
puzzle.set_nodos_abertos(configuracao_inicial)
puzzle.set_nodos_fechados([])
continua = True

while continua and puzzle.tem_abertos():
    puzzle.busca_nodo_menor_custo()  ####
    nodo_da_vez = puzzle.menor_custo_abertos()
    if puzzle.eh_nodo_objetivo(nodo_da_vez):
        print(f'Caminho final: {puzzle.resultado()}')
        print(f'Tamanho do caminho: {puzzle.tamanho_do_caminho_final()}')
        print(f'Total de nodos abertos: {puzzle.get_nodos_abertos()}')
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
                    puzzle.avalia_substituicao_em_abertos(filhos[i]) ### fiz
                else:
                    puzzle.avalia_substituicao_fechados(filhos[i]) ###
                    pass
        puzzle.retira_de_abertos_coloca_em_fechados(nodo_da_vez) ###

if continua is True:
    print("Falha")
del puzzle
gc.collect()
