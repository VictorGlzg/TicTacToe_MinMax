board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]
isAWinner = False
ia = 'X'
player = 'O'
currentPlayer = player
scores = {'X': 1,
          'O': -1,
          'Ninguno - Empate': 0}
def bestMove():
    bestScore = -1000
    bMoveI = None
    bMoveJ = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = ia
                score = minimax(board,0,False)
                board[i][j] = '-'
                if score > bestScore:
                    bestScore = score
                    bMoveI = i
                    bMoveJ = j
    board[bMoveI][bMoveJ] = ia

def minimax(board,depth,isMaximizing):
    result = checkWinner()
    if(result!= None):
        return scores[result]
    if(isMaximizing):
        bestScore = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = ia
                    score = minimax(board, depth+1, False)
                    board[i][j] = '-'
                    if score > bestScore:
                        bestScore = score
        return bestScore
    else:
        bestScore = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = player
                    score = minimax(board, depth + 1, True)
                    board[i][j] = '-'
                    if score < bestScore:
                        bestScore = score
        return bestScore

def printBoard():
    abc = ['A','B','C']
    print("    1 2 3")
    for i in range(3):
        print(abc[i]+' [',end=' ')
        for j in range(3):
            print(board[i][j],end=' ')
        print(']')

def score(a,b,c):
    return a == b and b == c and a != '-'

def checkWinner():
    winner = None
    #Horizontal
    for i in range(3):
        if score(board[i][0],board[i][1],board[i][2]):
            winner = board[i][0]
    #Vertical
    for i in range(3):
        if score(board[0][i],board[1][i],board[2][i]):
            winner = board[0][i]
    #Diagonales
    if score(board[0][0],board[1][1],board[2][2]):
        winner = board[0][0]
    if score(board[2][0],board[1][1],board[0][2]):
        winner = board[2][0]

    espacios = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                espacios += 1

    if winner == None and espacios == 0:
        return 'Ninguno - Empate'
    else:
        return winner

def resetTablero():
    for i in range(3):
        for j in range(3):
            board[i][j] = '-'

def winCondition():
    w = checkWinner()
    if (w != None):
        isAWinner = True
        print("El juego ha terminado el ganador fue: " + w)
        return True
    return False

def moveAction(p,mov):
    letter = mov.split(',')[1]
    Y = int(mov.split(',')[0])-1
    decodeCoords={
        'A': 0,
        'B': 1,
        'C': 2
    }
    X = decodeCoords[letter]

    if(board[X][Y] == '-'):
        board[X][Y] = p
        #NextTurn
    else:
        move = input('Espacio ya esta ocupado, selecione otra coordenada')
        moveAction(p,move)


printBoard()
while(not isAWinner):
    move = input('Escoja una coordenada para mover ej. 1,A: ')
    moveAction(player,move)
    printBoard()
    if winCondition(): break
    print('El turno es de la IA:')
    bestMove()
    printBoard()
    if winCondition(): break

