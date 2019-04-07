import random

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


def calcular_caminho(caminho):
    # Cria matriz NxN preenchida com zeros, onde N é o tamanho do labirinto
    caminho_andado = [[0 for _ in range(0, tamanho_labirinto)] for _ in range(0, tamanho_labirinto)]
    pos_vert_atual = posicao_inicial[0]
    pos_hor_atual = posicao_inicial[1]
    caminho_andado[pos_vert_atual][pos_hor_atual] = 1
    pontos = 0
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

            if caminho_andado[pos_vert_atual][pos_hor_atual] == 1:
                pontos -= 5
            else:
                caminho_andado[pos_vert_atual][pos_hor_atual] = 1

            if pos_lab == '0' or pos_lab == 'E':
                pontos += 1
            elif pos_lab == '1':
                pontos -= 3
            elif pos_lab == 'S':
                pontos += 10

    return pontos
