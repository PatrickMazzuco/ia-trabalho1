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

direcoes = ('N', 'S', 'L', 'O')


def print_matriz(matriz):
    for arr in matriz:
        for s in arr:
            print(s, end="  ")
        print()


def get_direcao_aleatoria():
    return direcoes[random.randint(0, 3)]


def get_caminho_aleatorio():
    return [get_direcao_aleatoria() for x in range(0, espacos_livre)]


print(posicao_inicial)
print(espacos_livre)
