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
puzzle.set_Abertos(configuracao_inicial)
puzzle.set_Fechados([])
continua = True
while (continua and puzzle.tem_Abertos()):
    nodo_da_vez = puzzle.get_nodo_da_vez()
    if (puzzle.eh_nodo_objetivo(nodo_da_vez)):
        print("Caminho Final: ", puzzle.resultado())
        print("Tamanho do caminho: ", tamanho_do_caminho_final())
        print("Total de Nodos Abertos: ", puzzle.get_total_nodos_Abertos())
        print("Nodos Abertos: ", puzzle.get_Abertos())
        print("Total de Nodos Fechados: ", puzzle.get_total_nodos_Fechados())
        print("Nodos Fechados: ", puzzle.get_Fechados())
        continua = False
    else:
        filhos = puzzle.gera_filhos(nodo_da_vez)
        for i in length(filhos):
            if (not puzzle.esta_em_Abertos(filhos[i]) and not puzzle.esta_em_Fechados(filhos[i])):
                puzzle.atribui_custos_ao_nodo(filhos[i])
                puzzle.coloca_em_Abertos(filhos[i])
            else:
                if (puzzle.esta_em_Abertos(filhos[i])):
                    puzzle.avalia_substituicao_Abertos(filhos[i])
                else:
                    # puzzle.avalia_substituicao_Fechados(filhos[i]) # Falar com professor.
                    pass
        puzzle.retira_de_Abertos_coloca_em_Fechados(nodo_da_vez)
        # puzzle.ordena_Abertos()
if continua == True:
    print("Falha")
del puzzle
gc.collect()


                  


