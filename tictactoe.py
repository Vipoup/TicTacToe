# Vipoup Shaipitisiri
# Ken Nguyen
# CSCI 4307
# AI TicTacToe

#create board based on given dimensions, return board
def makeBoard():
    cols = 3;
    rows = 3;
    board = [["o"]*cols]*rows;
    return board;

#given a board (2D array), print board in a nice format 
def printBoard(board):
    rows = len(board);
    columns = len(board[0]);

    for row in range(rows):
        for col in range(columns):
            if(col != columns-1):
                print(board[row][col], "\b|", end="");
            else:
                print(board[row][col], "\b", end="");
        print();
        if(row != rows-1):
            print("--"*columns);

# calculate next move

#AI moves
def moveAI(board):

    printBoard(board);
    print("AI moved ", "here", "\n");
    return board, [];

#Player moves
def movePlayer(board):

    printBoard(board);
    print();
    return board, [];

#Check if board is full
def isBoardFull():
    return;

#check if a given array has a win
def checkWin():
    #check win by looking at all the moves (stored as an array of an array of moves e.g. [[1,1],[0,0],[2,2]])
    #if they do win, return something to break the loop
    return;

#main
if __name__ == "__main__":
    #eventually, while true(or until user ends)
    #ask play vs AI, or pvp, or AIvAI; focus on PvsAI for now
    #could ask for who goes first; AI goes first for now
    #Ask user for board size, hardcoded for now for 3x3
    board = makeBoard();
    printBoard(board);

    storeMovesAI = [];
    storeMovesPlayer = [];

    #while board is not empty or player chooses to end game
    board, storeMovesAI = moveAI(board, storeMovesAI);
    #win = checkWin(storeMovesAI)
    #if win=true, break loop (unless we're doing the 5 in a row version)
    board, storeMovesPlayer = movePlayer(board, storeMovesPlayer);
    #win = checkWin(storeMovesPlayer)

    #out of loop, announce who wins 
    # ask player if they want to play again; yes continue, no break



# ideas: push each move onto an array so its easier to keep track of if a win has been met