#SET BOARD LENGTH
N = 9

#PRINT BOARD
def printBoard(board):
    for row in range(N):
        for col in range(N):
            print(board[row][col], end=" ")
        print()

def isValid(board, row, col, num):
    #Check Row
    for x in range(N):
        if board[row][x] == num:
            return False
    
    #Check Column
    for x in range(N):
        if board[x][col] == num:
            return False

    #Check 3x3
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False

    #Valid Position
    return True

def solveSudoku(board):
    #Set Initial Varaibles
    row = -1
    col = -1
    empty = False

    #Found First 0 in Board
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                row, col = i, j
                empty = True
                break
        if empty:
            break
    #IF NOT FOUND A 0 RETURN TRUE, SUDOKU RESOLVED
    if not empty:
        return True

    #TRY EVERY CONVINATION FROM 1 TO 9
    for num in range(1, 10):
        #CHECK IF ITS VALID NUMEBER AND SET IT IN THE BOARD
        if isValid(board, row, col, num):
            board[row][col] = num

            #TRY TO SOLVE SUDOKU WITH THAT NUMBER AND JUMP TO THE NEXT EMPTY PLACE
            if solveSudoku(board):
                #SUDOKU SOLVED
                return True
            #BACKTRACKED SUDOKU WASNT SOLVED WITH THE NUMBER SET PREVIOUSLY GO BACK AND TRY AGAIN
            board[row][col] = 0
    #UNABLE TO SET ANY NUMBER FROM 1 TO 9 IN THAT CELL. IMPOSSIBLE TO SOLVE SUDOKU
    return False

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solveSudoku(board):
    printBoard(board)
else:
    print("No solution exists for this Sudoku")
