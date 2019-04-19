import random


def ler_arquivo(caminho):
    """
    Le o arquivo que contem o labirinto
    :param caminho:
    :return: matriz com o labirinto
    """
    arq = open(caminho, 'r')
    tamanho = int(arq.readline())
    labirinto = []
    for i in range(0, tamanho):
        linha = arq.readline()
        linha = linha.split()
        labirinto.append(linha)
    arq.close()
    return labirinto


def print_matriz(matriz):
    """
    Prita a matriz recebida para facil visualizacao.
    :param matriz:
    :return:
    """
    for arr in matriz:
        for s in arr:
            print(s, end="  ")
        print()


def get_direcao_aleatoria():
    return direcoes[random.randint(0, 3)]


def get_caminho_aleatorio():
    return [get_direcao_aleatoria() for _ in range(0, espacos_livre)]


def calcular_caminho(caminho, print_caminho=False):
    """
    Calcula o valor do caminho recebido.
    :param caminho:
    :param print_caminho: se for True, printa a visualizacao do caminho percorrido.
    :return:
    """
    caminho_andado = [[0 for _ in range(0, tamanho_labirinto)] for _ in range(0, tamanho_labirinto)]
    pos_vert_atual = posicao_inicial[0]
    pos_hor_atual = posicao_inicial[1]
    step = '#'
    caminho_andado[pos_vert_atual][pos_hor_atual] = step
    pontos = 0
    corretos = 0
    repet = 0
    for dir in caminho:
        if dir == 'C':
            pos_vert_atual -= 1
        elif dir == 'B':
            pos_vert_atual += 1
        elif dir == 'D':
            pos_hor_atual += 1
        elif dir == 'E':
            pos_hor_atual -= 1

        # TODO Ajustar valores de pontuacao
        if 0 <= pos_hor_atual < tamanho_labirinto and 0 <= pos_vert_atual < tamanho_labirinto:
            pos_lab = labirinto[pos_vert_atual][pos_hor_atual]

            if caminho_andado[pos_vert_atual][pos_hor_atual] == step:
                repet += 1
                pontos -= 2
            else:
                caminho_andado[pos_vert_atual][pos_hor_atual] = step
            if pos_lab == '0' or pos_lab == 'E':
                corretos += 1
                pontos += 1
            elif pos_lab == '1':
                pontos -= 2
                # break

            elif pos_lab == 'S':
                pontos += 100
                caminho_andado[pos_vert_atual][pos_hor_atual] = 'S'
                break

        else:
            pontos -= 2
            # break

    _ = (print_matriz(caminho_andado), print((pos_vert_atual, pos_hor_atual))) if print_caminho else False
    # print(pontos)
    return pontos


def mudar_caminho(caminho):
    """
    Muda uma direcao no caminho recebido.
    Pode mudar para a mesma.
    :param caminho:
    :return:
    """
    caminho[random.randint(0, espacos_livre - 1)] = get_direcao_aleatoria()
    return caminho


def esta_correto(caminho):
    """
    Verifica se o caminho recebido chega na saida sem bater ou sair do labirinto.
    :param caminho:
    :return: True se o caminho for correto, caso contrario, False
    """
    pos_vert_atual = posicao_inicial[0]
    pos_hor_atual = posicao_inicial[1]

    for dir in caminho:
        if dir == 'C':
            pos_vert_atual -= 1
        elif dir == 'B':
            pos_vert_atual += 1
        elif dir == 'D':
            pos_hor_atual += 1
        elif dir == 'E':
            pos_hor_atual -= 1

        if 0 <= pos_hor_atual < tamanho_labirinto and 0 <= pos_vert_atual < tamanho_labirinto:
            pos_lab = labirinto[pos_vert_atual][pos_hor_atual]

            if pos_lab == '1':
                return False
            elif pos_lab == 'S':
                return True
        else:
            return False
    return False


def gerar_populacao(tamanho):
    """
    Gera uma populacao aleatoriamente.
    :param tamanho:
    :return:
    """
    populacao = []
    for i in range(0, tamanho):
        populacao.append(get_caminho_aleatorio())
    return populacao


# TODO Arrumar o que acontece quando encontra o caminho errado e remover o Exit(somente depois do algoritmo funcionar)
def avaliar_populacao(populacao):
    """
    Calcula a pontuacao de cada caminho na populacao.
    :param populacao:
    :return:
    """
    out = []
    for caminho in populacao:
        if esta_correto(caminho):
            print(caminho)
            print("Correto")
            exit(2)
        out.append(calcular_caminho(caminho))
    return out


def selecao(populacao, avaliacao):
    """
    Encontra uma populacao intermediaria a partir da populacao recebida.
    :param populacao:
    :param avaliacao:
    :return:
    """
    chance_mutacao = 0.05
    pop_intermed = []
    melhor = False
    for i in range(0, len(avaliacao)):
        if melhor is False:
            melhor = avaliacao[i], i
        elif avaliacao[i] > melhor[0]:
            melhor = avaliacao[i], i
    melhor = populacao[melhor[1]]
    pop_intermed.append(melhor)
    pop_intermed.append(get_caminho_aleatorio())
    pai = populacao[rnd(avaliacao)]
    mae = populacao[rnd(avaliacao)]
    while len(pop_intermed) < len(populacao):
        filhos = cruzamento(pai, mae, chance_mutacao)
        pop_intermed.append(filhos[0])
        pop_intermed.append(filhos[1])
    return pop_intermed


def cruzamento(pai, mae, mutacao):
    """
    Faz o cruzamento de pai e mae utilizando dois pontos de crossover.
    :param pai:
    :param mae:
    :param mutacao: a chance de ocorrer uma mutação em um filho. 0.10 = 10%
    :return: uma tupla com os 2 filhos
    """

    filho1 = []
    filho2 = []
    rnd1 = random.randint(1, len(pai) - 2)
    rnd2 = random.randint(1, len(pai) - 2)
    crossover1 = min(rnd1, rnd2)
    crossover2 = max(rnd1, rnd2)

    filho1.extend(pai[0:crossover1])
    filho1.extend(mae[crossover1:crossover2])
    filho1.extend(pai[crossover2:len(mae)])

    filho2.extend(mae[0:crossover1])
    filho2.extend(pai[crossover1:crossover2])
    filho2.extend(mae[crossover2:len(mae)])

    if mutacao > random.random():
        filho1 = mudar_caminho(filho1)
    if mutacao > random.random():
        filho2 = mudar_caminho(filho2)
    return filho1, filho2


def rnd(avalicao):
    """
    Metodo que escolhe dois valores aleatorios da lista e retorna o index do maior.
    Utilizado para escolher pai ou mae em uma populacao.
    """
    rnd1 = random.randint(0, len(avalicao) - 1)
    rnd2 = random.randint(0, len(avalicao) - 1)
    if avalicao[rnd1] >= avalicao[rnd2]:
        return rnd1
    return rnd2


def alg_genetico(tam_pop, geracoes):
    """
    Executa o algoritmo genetico
    :param tam_pop: tamanho da populacao
    :param geracoes: numero de geracoes
    :return: melhor caminho encontrado
    """
    pop_inicial = gerar_populacao(tam_pop)
    new_pop = pop_inicial.copy()
    avaliacao = avaliar_populacao(pop_inicial)
    for geracao in range(0, geracoes):
        new_pop = selecao(new_pop, avaliacao)
        avaliacao = avaliar_populacao(new_pop)
        # print(new_pop[0])
    melhor = avaliacao[0], 0
    for i in range(1, len(avaliacao)):
        if avaliacao[i] > melhor[0]:
            melhor = avaliacao[i], i
    return new_pop[melhor[1]]


# Labirintos de exemplo

labirinto__ = [['E', '1', '1', 'S'],
               ['0', '1', '1', '0'],
               ['0', '1', '1', '0'],
               ['0', '0', '0', '0']]

labirinto_ = [['E', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
              ['0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
              ['1', '1', '1', '0', '1', '1', '1', '1', '1', '0'],
              ['0', '0', '1', '0', '1', '0', '0', '0', '0', '0'],
              ['0', '0', '1', '0', '1', '1', '0', '1', '1', '1'],
              ['0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
              ['0', '1', '1', '1', '1', '0', '0', '1', '0', 'S'],
              ['0', '1', '0', '0', '0', '0', '0', '0', '1', '1'],
              ['0', '1', '1', '1', '1', '1', '1', '0', '0', '1'],
              ['0', '0', '0', '0', '0', '0', '0', '0', '0', '1']]

# Main


labirinto = ler_arquivo('./labirintos/labirintoE.txt')
espacos_livre = 1
tamanho_labirinto = len(labirinto[0])
posicao_inicial = -1
a = ['B', 'D', 'D', 'D', 'B', 'B', 'B', 'B', 'E', 'E', 'E', 'B', 'B', 'B', 'B', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'C',
     'C', 'E', 'C', 'C', 'D', 'D', 'D', 'B']
for i in range(0, tamanho_labirinto):
    for j in range(0, tamanho_labirinto):
        if labirinto[i][j] == '0':
            espacos_livre += 1
        elif labirinto[i][j] == 'E':
            posicao_inicial = (i, j)
espacos_livre = tamanho_labirinto ** 2
direcoes = ('C', 'B', 'E', 'D')

resultado = alg_genetico(100, 1000)

print("Exemplo correto:\n", a)
print("Resultado encontrado:\n", resultado)
print("Esta correto? ", esta_correto(resultado), "\nCaminho percorrido:")
calcular_caminho(resultado, True)
print(posicao_inicial)
