#JOGO DA VELHA
#EXPLICAÇÃO DE ORIGINALIDADE
#OS NUMEROS NA COMPUTAÇÃO COMEÇAM COM 0
#POR ISSO UTILIZEI O 'player' PARA JOGADOR 1
#E 'player1' PARA JOGADOR 2.
#PARA EVITAR MUITA REPETICAO FIZ TUDO
#UTILIZANDO A ESTRUTURA 'for'
#USEI A BIBLIOTECA NUMPY PARA CRIAR AS MATRIZES
#ELA PODE SER INSTALADA COM O SEGUINTE COMANDO
#'pip install numpy' NO CONSOLE DO SEU SO
#SÓ FALTA FAZER O SISTEMA DE VITORIA
#QUE TAMBÉM PRETENDO FAZER UTILIZANDO O 'for'
#BY: FELIPE TENÓRIO DO NASCIMENTO
import numpy as np

moves = 0
table = np.array([['1', '2', '3'],
                  ['4', '5', '6'],
                  ['7', '8', '9']])

print(table)

while moves < 9: #AQUI É ONDE O JOGO ACONTECE!

    #JOGADOR 1
    player = int(input('JOGADOR 1 JOGADA: ')) - 1
    if (player < 3):
        for x in range(3):
            if (player == x):
                table[0, x] = 'X'
                moves = moves + 1
    if (player > 2 and player < 6):
        for x in range(3):
            if (player == x + 3):
                table[1, x] = 'X'
                moves = moves + 1
    if (player > 5 and player < 9):
        for x in range(3):
            if (player == x + 6):
                table[2, x] = 'X'
                moves = moves + 1

    print(table)

    if (moves >= 9): #VERIFICA SE DEU VELHA
        break
    
    #JOGADOR 2
    player1 = int(input('JOGADOR 2 JOGADA: ')) - 1
    if (player1 < 3):
        for x in range(3):
            if (player1 == x):
                table[0, x] = 'O'
                moves = moves + 1    
    if (player1 > 2 and player1 < 6):
        for x in range(3):
            if (player1 == x + 3):
                table[1, x] = 'O'
                moves = moves + 1
    if (player1 > 5 and player1 < 9):
        for x in range(3):
            if (player1 == x + 6):
                table[2, x] = 'O'
                moves = moves + 1    
    print(table)

    #VERIFICAÇÂO DE FIM DE JOGO
            
    #PARAMOS NESSA VERIFICAÇÃO (INCOMPLETA)