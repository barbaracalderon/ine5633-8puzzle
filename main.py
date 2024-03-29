import gc
from puzzle import Puzzle8

configuracao_final = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('============== [ JOGO PUZZLE 8 ] =============')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Bem-vindo(a)s ao jogo Puzzle8!')
print()
print('Objetivo do jogo: \n'
      '  1  |  2  |  3   \n'
      '----- ----- ----- \n'
      '  4  |  5  |  6   \n'
      '----- ----- ----- \n'
      '  7  |  8  |      \n')
print('.')
print('.')
print('.')
print()
print('OBS.: Objetivo no formato lista: [1, 2, 3, 4, 5, 6, 7, 8, 9]')
print()
print('Obs.: Para fins de jogo, entenda número "9" como \n'
      'sendo o espaço vazio do tabuleiro.\n'
      '\n')
print('.')
print('.')
print('.')
print()
print('Informe a sua configuração de entrada a seguir...\n\n'
      'Exemplo: 1, 2, 3, 4, 5, 6, 7, 8, 9\n'
      'Obs.2: São 9 caracteres separados por vírgula.')
print('.')
print('.')
print('.')
print()

tem_nove_digitos_errados = True
digitos_aceitos = [1, 2, 3, 4, 5, 6, 7, 8, 9]

configuracao_inicial = []
while tem_nove_digitos_errados:
    configuracao_inicial_string = input('Digite a configuração inicial do jogo: ')
    configuracao_inicial_split = configuracao_inicial_string.split(',')
    for digito in configuracao_inicial_split:
        digito = digito.strip()
        if digito.isnumeric():
            digito_int = int(digito)
            if digito_int not in configuracao_inicial and digito_int in digitos_aceitos:
                configuracao_inicial.append(digito_int)
    if len(configuracao_inicial) == 9:
        print()
        print('Considerando apenas os 9 primeiros caracteres numéricos válidos digitados...')
        print('.')
        print('.')
        print('.')
        print('... CHECK!')
        tem_nove_digitos_errados = False
    else:
        print('\n... Dados inválidos. Digite números inteiros de 1 a 9, sem repetição.')
        del configuracao_inicial_string, configuracao_inicial_split, configuracao_inicial
        configuracao_inicial = []

print()
print('CONFIGURAÇÃO INICIAL: \n'
      f'{configuracao_inicial}\n'
      f'Status: OK')
print()
print('São 3 métodos de jogo:')
print(f'0 - custo uniforme\n'
      f'1 - A* com uma heurística simples\n'
      f'2 - A* com a heurística mais precisa alcançada')

escolha_do_metodo_esta_errada = True
metodos_aceitos_string = ['0', '1', '2']
metodo_utilizado = -1

while escolha_do_metodo_esta_errada:
    metodo_escolhido = input('\nDigite o método desejado: ').strip()

    if metodo_escolhido.isnumeric() and metodo_escolhido in metodos_aceitos_string:
        metodo_utilizado = int(metodo_escolhido)
        escolha_do_metodo_esta_errada = False
    else:
        print('\n... Dado inválido.\n')
        print('São 3 métodos de jogo:')
        print(f'0 - custo uniforme\n'
              f'1 - A* com uma heurística simples\n'
              f'2 - A* com a heurística mais precisa alcançada')

print()
print(f'MÉTODO UTILIZADO: {metodo_utilizado} \n'
      f'Status: OK\n')

print()
print()
print('============= [ INÍCIO DO JOGO ] ============')
print('Criando o tabuleiro com as peças de entrada...')
print('Inicializando os cálculos...')
print()

puzzle = Puzzle8(configuracao_inicial, configuracao_final, metodo_utilizado)

if metodo_utilizado == 0:
    heuristica = 0
elif metodo_utilizado == 1:
    heuristica = puzzle.calcula_heuristica_simples(configuracao_inicial)
else:
    heuristica = puzzle.calcula_heuristica_precisa(configuracao_inicial)

caminho_inicial = [[[configuracao_inicial], 0, heuristica, heuristica]]
puzzle.set_nodos_abertos(caminho_inicial)
puzzle.set_nodos_fechados([])
continua = True
iteracao = 0

while continua and puzzle.tem_abertos():
    iteracao += 1
    resto = iteracao % 500
    if resto == 0:
        print('*')
        print('*')
        print('*')
        print()
        print(f'Iteração...')
        print(iteracao)
        print()

    puzzle.extrai_nodo_da_vez()
    nodo_da_vez = puzzle.get_nodo_da_vez()
    estado = nodo_da_vez[0][len(nodo_da_vez[0]) - 1]

    if puzzle.eh_nodo_objetivo(estado):
        print()
        print('.')
        print('.')
        print('.')
        print('.')
        print('.')
        print()
        print("... RESULTADOS ..............................")
        print()
        print(f'1) CAMINHO FINAL: {puzzle.resultado()}')
        print()
        # print()
        print(f'2) TAMANHO DO CAMINHO: {puzzle.tamanho_do_caminho_final()}')
        print()
        # print()
        print(f'3) TOTAL DE NODOS ABERTOS: {puzzle.get_total_nodos_abertos()}')
        print()
        # print()
        # nodos_abertos = puzzle.get_nodos_abertos()
        # for i in range(len(nodos_abertos)):
        #     print(nodos_abertos[i])
        # print()
        # print()
        print(f'4) TOTAL DE NODOS FECHADOS: {puzzle.get_total_nodos_fechados()}')
        print()
        continua = False
    else:
        filhos = puzzle.gera_nodos_filhos(estado)
        for i in range(len(filhos)):
            if filhos[i] not in nodo_da_vez[0]:
                if not puzzle.esta_em_nodos_abertos(filhos[i]) and not puzzle.esta_em_nodos_fechados(filhos[i]):
                    caminho = puzzle.atribui_custos_ao_nodo(filhos[i])
                    puzzle.coloca_em_abertos(caminho)
                else:
                    if puzzle.esta_em_nodos_abertos(filhos[i]):
                        puzzle.avalia_substituicao_em_abertos(filhos[i])
                    else:
                        puzzle.avalia_substituicao_fechados(filhos[i])
        puzzle.retira_de_nodo_da_vez_coloca_em_fechados(nodo_da_vez)
print()
print('================== [ FIM ] ===================')

del puzzle
gc.collect()
