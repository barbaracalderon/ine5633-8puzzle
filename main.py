import gc
from puzzle import Puzzle8

# Trabalho Prático 1 - de Sistemas de Informações
# Jogo 8-puzzle com heurística
# Barbara Calderon e Edmilson Domingues

# configuracao_inicial = [6, 7, 5, 1, 2, 3, 9, 4, 8] # benchmark professor (18 passos)
configuracao_inicial = [1, 2, 3, 9, 5, 6, 4, 7, 8] # 3 passos. Deu certo.
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
    puzzle.extrai_nodo_da_vez()
    nodo_da_vez = puzzle.get_nodo_da_vez()
    estado = nodo_da_vez[0][len(nodo_da_vez[0]) -1]
    print("Estado: ", estado)
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
        print(f'Nodos fechados: {puzzle.get_nodos_fechados()}')
        continua = False
    else:
        filhos = puzzle.gera_nodos_filhos(estado)
        for i in range(len(filhos)):
            if not puzzle.esta_em_nodos_abertos(filhos[i]) and not puzzle.esta_em_nodos_fechados(filhos[i]):
                print()
                print('1')
                print("contador i: ", i)
                print("Nodos abertos 1: ", puzzle.get_nodos_abertos()) # certo
                caminho = puzzle.atribui_custos_ao_nodo(filhos[i])
                print("Nodos abertos 2: ", puzzle.get_nodos_abertos()) #errado
                print("Caminho novo: ", caminho)
                puzzle.coloca_em_abertos(caminho) #
                print("Nodos abertos : ", puzzle.get_nodos_abertos())
            else:
                
                if puzzle.esta_em_nodos_abertos(filhos[i]):
                    print()
                    print('2')
                    puzzle.avalia_substituicao_em_abertos(filhos[i])
                else:
                    print('3')
                    puzzle.avalia_substituicao_fechados(filhos[i])
        print(f'Nodo da vez: {nodo_da_vez}')
        puzzle.retira_de_nodo_da_vez_coloca_em_fechados(nodo_da_vez)

if continua is True:
    print("Falha")
del puzzle
gc.collect()

