import random


# strategies return a tuple (x, y) of the x and y coordinates they want to place their mark in


def naughtsStrategy(board):
    MY_PIECE = "O"
    OTHER_PIECE = "X"
    EMPTY = " "

    if board[0][1] == OTHER_PIECE:
        return 0, 2


def crossesStrategy(board):
    MY_PIECE = "X"
    OTHER_PIECE = "O"
    EMPTY = " "

    return 2, 0


def moveIsLegal(move):
    return \
        move[0] in range(3) and move[1] in range(3) and \
        gameBoard[move[1]][move[0]] == " "


def thereIsWinner():
    # check rows
    for row in gameBoard:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True

    # check columns
    for x in range(3):
        if gameBoard[0][x] == gameBoard[1][x] == gameBoard[2][x] and gameBoard[0][x] != " ":
            return True

    # check diagonals
    if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2] and gameBoard[0][0] != " ":
        return True
    if gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0] and gameBoard[0][2] != " ":
        return True

    return False


def thereIsTie():
    for row in gameBoard:
        for square in row:
            if square == " ":
                return False

    return True


def printBoard():
    for row in gameBoard:
        for square in row:
            print("[{}]".format(square), end="")
        print()


gameBoard = [
    [" ", " ", " "],
    [" ", " ", " "], # gameBoard[2][0]
    [" ", " ", " "]
]

currentStrategy = naughtsStrategy

while True:
    nextMove = currentStrategy(gameBoard)

    if moveIsLegal(nextMove):
        # perform move
        if currentStrategy == naughtsStrategy:
            gameBoard[nextMove[1]][nextMove[0]] = "O"
        else:
            gameBoard[nextMove[1]][nextMove[0]] = "X"

        if currentStrategy == naughtsStrategy:
            print("Naughts: " + str(nextMove))
        else:
            print("Crosses: " + str(nextMove))

        print("\n")
        printBoard()

        # check for winner
        if thereIsWinner():
            if currentStrategy == naughtsStrategy:
                result = "Naughts got 3 in a row!"
            else:
                result = "Crosses got 3 in a row!"
            break

        # check for tie
        if thereIsTie():
            result = "It's a tie!"
            break

        # switch turns
        if currentStrategy == naughtsStrategy:
            currentStrategy = crossesStrategy
        else:
            currentStrategy = naughtsStrategy

    else:
        # win by default
        if currentStrategy == naughtsStrategy:
            result = "Naughts did an illegal move {} so crosses wins by default".format(nextMove)
        else:
            result = "Crosses did an illegal move {} so naughts wins by default".format(nextMove)
        break

    # require enter to continue
    input("\n---------------------------\n")

print("Game over!")
print(result)
