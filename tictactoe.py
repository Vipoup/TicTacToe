# Vipoup Shaipitisiri
# Ken Nguyen
# CSCI 4307
# AI TicTacToe
import re;
import copy;

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

# checkNextMove
def checkNextMove(space, storeMoves):
    tempStoreMoves = copy.deepcopy(storeMoves);
    tempStoreMoves.append(space);
    if checkWin(tempStoreMoves):
        return 1;
    return 0;

def move(board, coords, storeMoves, letter):
    storeMoves.append(coords); # add coords to array

    board[coords[0]][coords[1]] = letter; # place on board
    return board, storeMoves;

#AI moves
def moveAI(board, storeMovesAI, storeMovesPlayer, letter):

    emptySpaces = findEmptySpaces(board);
    winningMove = [];
    losingMove = [];
    neutralMove = [];

    for space in emptySpaces:
        checkNextAI = checkNextMove(space, storeMovesAI);
        checkNextPlayer = checkNextMove(space, storeMovesPlayer);
        if checkNextAI == 1:
            winningMove.append(space);
        elif checkNextPlayer == 1:
            losingMove.append(space);
        elif checkNextAI == 0 or checkNextPlayer == 0:
            neutralMove.append(space);
    
    if len(winningMove) != 0:
        board, storeMovesAI = move(board, winningMove.pop(0), storeMovesAI, letter);
    elif len(losingMove) != 0:
        board, storeMovesAI = move(board, losingMove.pop(0), storeMovesAI, letter);
    elif len(neutralMove) != 0 and len(storeMovesAI) != 0:
        prevMove = storeMovesAI.pop(-1);
        storeMovesAI.append(prevMove);
        #if diagnal placement
        if [prevMove[0]-1, prevMove[1]-1] in storeMovesPlayer \
        and [prevMove[0]+1, prevMove[1]+1] in storeMovesPlayer:
            #move in cardinal direction
            if [prevMove[0]-1, prevMove[1]] in neutralMove:
                board, storeMovesAI = move(board, [prevMove[0]-1, prevMove[1]], storeMovesAI, letter);
            elif [prevMove[0]+1, prevMove[1]] in neutralMove:
                board, storeMovesAI = move(board, [prevMove[0]+1, prevMove[1]], storeMovesAI, letter);
            elif [prevMove[0], prevMove[1]-1] in neutralMove:
                board, storeMovesAI = move(board, [prevMove[0], prevMove[1]-1], storeMovesAI, letter);
            elif [prevMove[0], prevMove[1]+1] in neutralMove:
                board, storeMovesAI = move(board, [prevMove[0]-1, prevMove[1]+1], storeMovesAI, letter);
        elif [prevMove[0]-1, prevMove[1]+1] in storeMovesPlayer \
        and [prevMove[0]+1, prevMove[1]-1] in storeMovesPlayer:
            #move in cardinal direction
            if [prevMove[0]-1, prevMove[1]] in neutralMove:
                board, storeMovesAI = move(board, [prevMove[0]-1, prevMove[1]], storeMovesAI, letter);
            elif [prevMove[0]+1, prevMove[1]] in neutralMove:
                board, storeMovesAI = move(board, [prevMove[0]+1, prevMove[1]], storeMovesAI, letter);
            elif [prevMove[0], prevMove[1]-1] in neutralMove:
                board, storeMovesAI = move(board, [prevMove[0], prevMove[1]-1], storeMovesAI, letter);
            elif [prevMove[0], prevMove[1]+1] in neutralMove:
                board, storeMovesAI = move(board, [prevMove[0], prevMove[1]+1], storeMovesAI, letter);
        #corners are more powerful otherwise
        elif [prevMove[0]-1, prevMove[1]-1] in neutralMove:
            board, storeMovesAI = move(board, [prevMove[0]-1, prevMove[1]-1], storeMovesAI, letter);
        elif [prevMove[0]-1, prevMove[1]+1] in neutralMove:
            board, storeMovesAI = move(board, [prevMove[0]-1, prevMove[1]+1], storeMovesAI, letter);
        elif [prevMove[0]+1, prevMove[1]-1] in neutralMove:
            board, storeMovesAI = move(board, [prevMove[0]+1, prevMove[1]-1], storeMovesAI, letter);
        elif [prevMove[0]+1, prevMove[1]+1] in neutralMove:
            board, storeMovesAI = move(board, [prevMove[0]+1, prevMove[1]+1], storeMovesAI, letter);
        else:
            board, storeMovesAI = move(board, neutralMove.pop(0), storeMovesAI, letter);
    elif len(neutralMove) != 0 and len(storeMovesPlayer) != 0:
        prevMove = storeMovesPlayer.pop(-1);
        storeMovesPlayer.append(prevMove);

        #corners are more powerful
        if [prevMove[0]-1, prevMove[1]-1] in neutralMove:
            board, storeMovesAI = move(board, [prevMove[0]-1, prevMove[1]-1], storeMovesAI, letter);
        elif [prevMove[0]-1, prevMove[1]+1] in neutralMove:
            board, storeMovesAI = move(board, [prevMove[0]-1, prevMove[1]+1], storeMovesAI, letter);
        elif [prevMove[0]+1, prevMove[1]-1] in neutralMove:
            board, storeMovesAI = move(board, [prevMove[0]+1, prevMove[1]-1], storeMovesAI, letter);
        elif [prevMove[0]+1, prevMove[1]+1] in neutralMove:
            board, storeMovesAI = move(board, [prevMove[0]+1, prevMove[1]+1], storeMovesAI, letter);
        else:
            board, storeMovesAI = move(board, neutralMove.pop(0), storeMovesAI, letter);
    else:
        board, storeMovesAI = move(board, neutralMove.pop(len(neutralMove)//2), storeMovesAI, letter);

    printBoard(board);
    # make AI output easier to understand for humans
    # take the last move AI made
    lastMoved = storeMovesAI[len(storeMovesAI)-1];
    # add 1 for readability
    output = [lastMoved[0]+1, lastMoved[1]+1];
    #turn to str to concat
    movedAI = str(output);
    print("AI moved "+ movedAI + ".\n");

    win = checkWin(storeMovesAI);
    if win:
        print("Computer has won.");

    return board, storeMovesAI, win;

def findEmptySpaces(board):
    rows = len(board);
    columns = len(board[0]);
    emptySpaces = [];
    coords = [];

    # check if there are any empty spots
    for row in range(rows):
        for col in range(columns):
            if board[row][col] == " ":
                coords = [row, col];
                emptySpaces.append(coords);
    return emptySpaces;

#Player moves
def movePlayer(board, storeMovesPlayer, exitGame, letter):
    rows = len(board);
    columns = len(board[0]);
    check = True;
    coords = [];

    #quality checking input
    while check:
        print("If you would like to exit game, enter 'exit'.");
        move = input("Enter coordinates to place '" + letter +
        "' (row,coulmn e.g. 1,1 for the top left spot): ");

        # if user wants to exit
        if re.search("[Ee]xit", move):
            exitGame = True;
            return board, storeMovesPlayer, False, exitGame;

        # if input is in num,num format
        if re.search("^[0-9]*,[0-9]*$", move):
            coords = move.split(",");
            # if input is not in the board range
            if int(coords[0]) > rows or int(coords[1]) > columns \
            or int(coords[0]) == 0 or int(coords[1]) == 0:
                print("The input was not the board range. Please try again.\n");
            else:
                # if spot is not taken
                if board[int(coords[0])-1][int(coords[1])-1] == " ":
                    check = False;
                else:
                    print("This spot is not empty. Please try again.\n");
        else:
            print("The input was not in the right format. Please try again.\n");
        
    # convert str to int
    coords[0] = int(coords[0]);
    coords[1] = int(coords[1]);

    # convert human readable text to array standard
    coords[0] = coords[0]-1;
    coords[1] = coords[1]-1;

    # board, storeMovesPlayer = move(board, coords, storeMovesPlayer, "o"); # crashes for some reason
    storeMovesPlayer.append(coords); # add coords to array

    board[coords[0]][coords[1]] = letter; # place on board

    printBoard(board);
    print();

    win = checkWin(storeMovesPlayer);
    if win:
        print("Player has won!");

    return board, storeMovesPlayer, win, exitGame;

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

        # board, storeMovesAI, win = moveAI(board, storeMovesAI, storeMovesPlayer, "x");
        #if win=true, break loop (unless we're doing the 5 in a row version)
        board, storeMovesAI, win, exitGame = movePlayer(board, storeMovesAI, exitGame, "x");
        if win or isBoardFull(board) or exitGame:
            break;
        # board, storeMovesPlayer, win, exitGame = movePlayer(board, storeMovesPlayer, exitGame, "o");
        #if win=true, break loop (unless we're doing the 5 in a row version)
        board, storeMovesPlayer, win = moveAI(board, storeMovesPlayer, storeMovesAI, "o");

    if win == False and not exitGame:
        print("Draw.");

    #out of loop
    # ask player if they want to play again; yes continue, no break

#issue: if player moves middle, ai moves [1,1], human moves [3,3], ai moves [1,2], humans moves [1,3] and have a 2 way win
#       ai sees no space in diagonals of last ai move, so it moves the first avaliable space thats neutral, WIP