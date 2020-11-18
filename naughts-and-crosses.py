import random


"""
Board format:

board[0][0] 0, 0 | board[0][1] 1, 0 | board[0][2] 2, 0
-----------------|------------------|-----------------
board[1][0] 0, 1 | board[1][1] 1, 1 | board[1][2] 2, 1
-----------------|------------------|-----------------
board[2][0] 0, 2 | board[2][1] 1, 2 | board[2][2] 2, 2
"""


def naughtsStrategy(board):
    MY_PIECE = "O"
    OTHER_PIECE = "X"  # Refer to marks on the board using these constants
    EMPTY = " "

    if board[0][1] == EMPTY:
        return 1, 0     # Notice the result is in format `x, y` whereas to access squares on the board you use
    else:               # `board[y][x]` (where x and y increase downwards and to the right). See above for more detail
        return 2, 2


def crossesStrategy(board):
    MY_PIECE = "X"
    OTHER_PIECE = "O"
    EMPTY = " "

    x = random.randint(0, 2)
    y = random.randint(0, 2)
    if board[y][x] == EMPTY:
        return x, y
    
    elif board[y][0] == MY_PIECE:
        return 1, y

    return 0, 0  # The code must always return a value in all code paths; if it doesn't return a value or if the value is an illegal move, you lose!


# This code can be found on https://github.com/Rolodophone/naughts-and-crosses. If you want to test your strategy,
# replace one of the above strategies with yours and the other with the one in userStrategy.py

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
    for y, row in enumerate(gameBoard):

        print(" {} | {} | {}".format(row[0], row[1], row[2]))

        if y != 2:
            print("---|---|---")


gameBoard = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

currentStrategy = naughtsStrategy

while True:
    nextMove = currentStrategy(gameBoard)

    if nextMove is None:
        if currentStrategy == naughtsStrategy:
            result = "Naughts did not return a move so crosses wins by default"
        else:
            result = "Crosses did not return a move so naughts wins by default"
        break

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
