import gc
from puzzle import Puzzle8

estado_inicial = [1, 4, 5, 8, 9, 2, 3, 7, 6]
estado_final = [1, 2, 3, 4, 5, 6, 7, 8, 9]
metodo_utilizado = 1

puzzle = Puzzle8(estado_inicial, estado_final, metodo_utilizado)

puzzle.set_nodos_abertos(estado_inicial)
puzzle.set_nodos_fechados([])

continuar = True
while continuar and puzzle.tem_abertos():
    nodo_da_vez = puzzle.menor_custo_abertos()
    if puzzle.eh_nodo_objetivo(nodo_da_vez):
        caminho_final = puzzle.resultado()
        print(f'Caminho final: {caminho_final}')
        print(f'Total de "Nodos Abertos": {puzzle.get_total_nodos_abertos()}')
        print(f'Nodos Abertos: {puzzle.get_nodos_abertos()}')
        print(f'Total de "Nodos Fechados": {puzzle.get_total_nodos_fechados()}')
        print(f'Nodos Fechados: {puzzle.get_nodos_fechados()}')
        continuar = False
    else:
        nodos_filhos = puzzle.gera_filhos(nodo_da_vez)
        for i in len(nodos_filhos):
            if not puzzle.esta_em_abertos(nodos_filhos[i]) and not puzzle.esta_em_fechados(nodos_filhos[i]):
                puzzle.atribui_custos_ao_nodo(nodo_da_vez)
            else:
                if puzzle.esta_em_abertos(nodos_filhos[i]):
                    puzzle.avalia_substituicao_nodos_abertos(nodo_da_vez)
                else:
                    puzzle.avalia_substituicao_nodos_fechados(nodo_da_vez)
                    puzzle.coloca_em_fechados(nodo_da_vez)
                    puzzle.ordena_nodos_abertos()

del puzzle
gc.collect()



