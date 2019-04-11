from math import exp
import random

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
espacos_livre = 1
tamanho_labirinto = 10
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


def print_matriz(matriz):
    for arr in matriz:
        for s in arr:
            print(s, end="  ")
        print()


def get_direcao_aleatoria():
    return direcoes[random.randint(0, 3)]


def get_caminho_aleatorio():
    return [get_direcao_aleatoria() for x in range(0, espacos_livre)]


def calcular_caminho(caminho, print_caminho=False):
    # Cria matriz NxN preenchida com zeros, onde N é o tamanho do labirinto
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
            pos_lab = labirinto_exemplo[pos_vert_atual][pos_hor_atual]

            if caminho_andado[pos_vert_atual][pos_hor_atual] == step:
                repet += 1
                pontos -= (1 + repet * 2)
            else:
                caminho_andado[pos_vert_atual][pos_hor_atual] = step
            if pos_lab == '0' or pos_lab == 'E':
                corretos += 1
                pontos += 1 + corretos * 2
            elif pos_lab == '1':
                pontos -= 20
                break
            elif pos_lab == 'S':
                pontos += espacos_livre * 2
                caminho_andado[pos_vert_atual][pos_hor_atual] = 'S'
                break
        else:
            return 0
    _ = print_matriz(caminho_andado) if print_caminho else False
    return pontos


def mudar_caminho(caminho):
    caminho[random.randint(0, espacos_livre - 1)] = get_direcao_aleatoria()
    return caminho


def simulated_annealing():
    temp_incial = 1000
    temp = temp_incial
    escal = 0.95
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


def esta_correto(caminho):
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


resultado = simulated_annealing()
print(resultado)
print(esta_correto(resultado))
print(a)
calcular_caminho(resultado, True)
