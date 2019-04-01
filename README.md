## Trabalho 1
Disciplina de Inteligência Artificial - PUCRS 2019/1
### Definição
O trabalho 1 da disciplina de IA visa fixar e exercitar conceitos relativos a agentes e a algoritmos de busca. 
O trabalho consiste na simulação de um jogo, no qual o agente deve encontrar a saída de um labirinto.
### Ambiente: Labirinto
O ambiente consiste em uma matriz n × n (Figura1 ). A entrada E e a
saída S do labirinto podem ser em qualquer lugar. No entanto, a entrada
é sempre conhecida pelo agente, é a sua célula inicial. Já a saída, ele tem
que descobrir. Serão fornecidos arquivos contendo os labirintos. Comece
sua implementação com o labirinto da figura.
### Movimentação do Agente
O agente pode se mover no ambiente, uma célula de cada vez nas direções:  
← → ↑ ↓, uma célula de cada vez. Agentes não caminham sobre paredes e
nem as transpassam.  
![image](https://user-images.githubusercontent.com/32601286/55297920-f180e400-5400-11e9-95b4-16f00beef12d.png)
### Solução
O agente deve encontrar a saída por meio de um algoritmo de busca
com informação por refinamentos sucessivos. Você pode usar Algoritmos Genéticos ou Simulated Annealing para encontrar a saída. Faz parte
do seu trabalho definir a forma de representação do problema e a função
heurística de avaliação que permitirão a execução desses algoritmos. O
caminho definido pelo algoritmo de busca que leva o agente da entrada
até a saída pode não ser o mais curto. Portanto, ao encontrar a saída,
execute um A* para encontrar a melhor rota entre a entrada e a saída do
labirinto.
### Simulação
A simulação deve exibir informações referentes às iterações dos algoritmos
de busca que objetivam encontrar a saida do labirinto. Se o algoritmo
encontrar a saída, exiba o caminho que leva da entrada à saida definido
pelo algoritmo. Uma vez encontrada a saída, sua simulação deve exibir o
caminho encontrado pelo A* e o agente percorrendo esse caminho.
