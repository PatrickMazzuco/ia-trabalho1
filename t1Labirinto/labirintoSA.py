from math import exp
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
    return [get_direcao_aleatoria() for x in range(0, espacos_livre)]


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
                corretos = 1
                pontos -= 2
                break

            elif pos_lab == 'S':
                pontos += 100
                caminho_andado[pos_vert_atual][pos_hor_atual] = 'S'
                break

        else:
            pontos -= 2
            break

    _ = (print_matriz(caminho_andado), print((pos_vert_atual, pos_hor_atual))) if print_caminho else False
    # print(pontos)
    return pontos


def mudar_caminho(caminho, index):
    """
    Randomiza o caminho a partir do index recebido.
    Para ser usado no simulated_annealing_ref
    :param caminho:
    :param index:
    :return:
    """
    for i in range(index, len(caminho)):
        caminho[i] = get_direcao_aleatoria()
    return caminho


def simulated_annealing():
    """
    Executa o algoritmo de SA comparando caminhos aleatorios.
    :return: o melhor caminho encontrado
    """
    temp_incial = 100
    temp = temp_incial
    escal = 0.90
    caminho = get_caminho_aleatorio()
    valor_atual = calcular_caminho(caminho)

    for _ in range(0, 10000):
        # print(valor_atual)
        temp = temp * escal
        prox_caminho = get_caminho_aleatorio()
        valor_prox = calcular_caminho(prox_caminho)
        dif_valores = valor_prox - valor_atual
        if dif_valores > 0:
            caminho = prox_caminho
            valor_atual = valor_prox
        elif random.random() < exp(dif_valores / temp):
            caminho = prox_caminho
            valor_atual = valor_prox
        if esta_correto(caminho):
            return caminho
    print(valor_atual)
    return caminho


def simulated_annealing_ref(caminho):
    """
    Executa o algoritmo de SA sobre o caminho recebido.
    Altera o caminho(refina) a partir de onde ocorre uma batida.
        Se estiver indo para o caminho errado, nao saira dele.
        This is not a feature
    :param caminho:
    :return:
    """
    temp_incial = 100
    temp = temp_incial
    escal = 0.90
    valor_atual = calcular_caminho(caminho)

    for _ in range(0, 10000):
        # print(valor_atual)
        temp = temp * escal
        prox_caminho = mudar_caminho(caminho, avaliar_caminho(caminho))
        valor_prox = calcular_caminho(prox_caminho)
        dif_valores = valor_prox - valor_atual
        if dif_valores > 0:
            caminho = prox_caminho
            valor_atual = valor_prox
        elif random.random() < exp(dif_valores / temp):
            caminho = prox_caminho
            valor_atual = valor_prox
        if esta_correto(caminho):
            return caminho
    print(valor_atual)
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
            pos_lab = labirinto_exemplo[pos_vert_atual][pos_hor_atual]

            if pos_lab == '1':
                return False
            elif pos_lab == 'S':
                return True
        else:
            return False
    return False


def avaliar_caminho(caminho):
    """
    Verifica ate onde o algoritmo vai sem bater.
    :param caminho:
    :return: o index no caminho onde bate.
    """
    pos_vert_atual = posicao_inicial[0]
    pos_hor_atual = posicao_inicial[1]

    for i in range(0, len(caminho)):
        if caminho[i] == 'C':
            pos_vert_atual -= 1
        elif caminho[i] == 'B':
            pos_vert_atual += 1
        elif caminho[i] == 'D':
            pos_hor_atual += 1
        elif caminho[i] == 'E':
            pos_hor_atual -= 1

        if 0 <= pos_hor_atual < tamanho_labirinto and 0 <= pos_vert_atual < tamanho_labirinto:
            pos_lab = labirinto_exemplo[pos_vert_atual][pos_hor_atual]

            if pos_lab == '1':
                return i
            elif pos_lab == 'S':
                return -1
        else:
            return i
    return i


# labirinto de exemplo

labirinto_exemplo_ = [['E', '0', '0', 'S'],
                      ['0', '0', '1', '0'],
                      ['0', '0', '1', '0'],
                      ['0', '0', '0', '0']]

labirinto_exemplo = [['E', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
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
        if labirinto_exemplo[i][j] == '0':
            espacos_livre += 1
        elif labirinto_exemplo[i][j] == 'E':
            posicao_inicial = (i, j)
direcoes = ('C', 'B', 'E', 'D')


resultado = simulated_annealing()
print("Exemplo correto:\n", a)
print("Resultado encontrado:\n", resultado)
print("Esta correto? ", esta_correto(resultado), "\nCaminho percorrido:")
calcular_caminho(resultado, True)
resultado = simulated_annealing_ref(resultado)
resultado = simulated_annealing_ref(resultado)
print("Resultado encontrado:\n", resultado)
print("Esta correto? ", esta_correto(resultado), "\nCaminho percorrido:")
calcular_caminho(resultado, True)
