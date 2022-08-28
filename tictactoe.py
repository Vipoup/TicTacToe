# Vipoup Shaipitisiri
# Ken Nguyen
# CSCI 4307
# AI TicTacToe
import re;

#create board based on given dimensions, return board
def makeBoard():
    cols = 3;
    rows = 3;
    board = [[" " for i in range(cols)] for j in range(rows)]
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
def moveAI(board, storeMovesAI, storeMovesPlayer):

    printBoard(board);
    print("AI moved ", "here", "\n");
    return board, storeMovesAI;

#Player moves
def movePlayer(board, storeMovesPlayer):
    rows = len(board);
    columns = len(board[0]);
    check = True;
    coords = [];

    while check:
        move = input("Enter coordinates to place 'o' " + 
        "(row,coulmn e.g. 1,0 for the top left spot): ");

        if re.search("^[0-9]*,[0-9]*$", move):
            coords = move.split(",");
            if int(coords[0]) > rows or int(coords[1]) > columns:
                print("The input was not the board range. Please try again.");
            else:
                check = False;
        else:
            print("The input was not in the right format. Please try again.");
        

    coords[0] = int(coords[0]);
    coords[1] = int(coords[1]);

    storeMovesPlayer.append(coords);

    board[coords[0]][coords[1]] = "o";

    printBoard(board);
    print();
    return board, storeMovesPlayer;

#Check if board is full
# if board is full, return true. 
# if board finds an empty space, return false 
def isBoardFull(board):
    rows = len(board);
    columns = len(board[0]);

    for row in range(rows):
        for col in range(columns):
            if board[row][col] == " ":
                return False;
    return True;

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
    print();

    storeMovesAI = [];
    storeMovesPlayer = [];

    #while board is not empty or player chooses to end game
    board, storeMovesAI = moveAI(board, storeMovesAI, storeMovesPlayer);
    #win = checkWin(storeMovesAI)
    #if win=true, break loop (unless we're doing the 5 in a row version)
    board, storeMovesPlayer = movePlayer(board, storeMovesPlayer);
    #win = checkWin(storeMovesPlayer)
    #if win=true, break loop (unless we're doing the 5 in a row version)

    # testing -----------------------
    # print(isBoardFull(board));
    # -------------------------------

    #out of loop, announce who wins 
    # ask player if they want to play again; yes continue, no break



# ideas: push each move onto an array so its easier to keep track of if a win has been met