# Vipoup Shaipitisiri
# Ken Nguyen
# CSCI 4307
# AI TicTacToe
import re;

#create board based on given dimensions, return board
def makeBoard():
    # will get user input on this later
    cols = 3;
    rows = 3;
    #make a blank 2D board based on given rows,columns
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
def movePlayer(board, storeMovesPlayer, exitGame):
    rows = len(board);
    columns = len(board[0]);
    check = True;
    coords = [];

    #quality checking input
    while check:
        print("If you would like to exit game, enter 'exit'.");
        move = input("Enter coordinates to place 'o' " + 
        "(row,coulmn e.g. 1,0 for the top left spot): ");

        # if user wants to exit
        if re.search("[Ee]xit", move):
            exitGame = True;
            return board, storeMovesPlayer, exitGame, False;

        # if input is in num,num format
        if re.search("^[0-9]*,[0-9]*$", move):
            coords = move.split(",");
            # if input is not in the board range
            if int(coords[0]) > rows-1 or int(coords[1]) > columns-1:
                print("The input was not the board range. Please try again.\n");
            else:
                # if spot is not taken
                if board[int(coords[0])][int(coords[1])] == " ":
                    check = False;
                else:
                    print("This spot is not empty. Please try again.\n");
        else:
            print("The input was not in the right format. Please try again.\n");
        
    # convert str to int
    coords[0] = int(coords[0]);
    coords[1] = int(coords[1]);

    storeMovesPlayer.append(coords); # add coords to array

    board[coords[0]][coords[1]] = "o"; # place on board

    printBoard(board);
    print();

    win = checkWin(storeMovesPlayer);
    if win:
        print("Player has won!");

    return board, storeMovesPlayer, exitGame, win;

#Check if board is full
# if board is full, return true. 
# if board finds an empty space, return false 
def isBoardFull(board):
    rows = len(board);
    columns = len(board[0]);

    # check if there are any empty spots
    for row in range(rows):
        for col in range(columns):
            if board[row][col] == " ":
                return False;
    return True;

#check if a given array has a win
def checkWin(storeMoves):
    #check win by looking at all the moves 
    # (stored as an array of an array of moves e.g. [[1,1],[0,0],[2,2]])
    #if they do win, return something to break the loop
    for move in storeMoves:
        if [move[0]-1, move[1]-1] in storeMoves and [move[0]+1, move[1]+1] in storeMoves:
            # left to right diagnal
            return True;
        elif [move[0]-1, move[1]] in storeMoves and [move[0]+1, move[1]] in storeMoves:
            # up and down; vertical
            return True;
        elif [move[0], move[1]-1] in storeMoves and [move[0], move[1]+1] in storeMoves:
            # left and right; horizontal
            return True;
        elif [move[0]-1, move[1]+1] in storeMoves and [move[0]+1, move[1]-1] in storeMoves:
            # right to left diagnal 
            return True;
    return False;

#main
if __name__ == "__main__":
    #eventually, while true(or until user ends)
    #ask play vs AI, or pvp, or AIvAI; focus on PvsAI for now
    #could ask for who goes first; AI goes first for now
    #   could make class for AI/Player, have a func called move,
    #   then be able to make it more dynamic for if they want
    #   pvp, aivai, pvai, and who goes first. Do later
    #Ask user for board size, hardcoded for now for 3x3

    board = makeBoard();
    printBoard(board);
    print();
    exitGame = False;
    win = False;
    storeMovesAI = [];
    storeMovesPlayer = [];

    #while board is not empty or player chooses to end game; focus on full board for now
    while not isBoardFull(board) and not exitGame and not win:

        # board, storeMovesAI = moveAI(board, storeMovesAI, storeMovesPlayer);
        #if win=true, break loop (unless we're doing the 5 in a row version)

        board, storeMovesPlayer, exitGame, win = movePlayer(board, storeMovesPlayer, exitGame);
        #if win=true, break loop (unless we're doing the 5 in a row version)

        

    #out of loop
    # ask player if they want to play again; yes continue, no break