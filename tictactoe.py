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

def minimax(board, depth, maximizer, alpha, beta, letterAI, letterPlayer):
    emptySpaces = findEmptySpaces(board);
    if checkWin(board, letterPlayer):
        return -1;
    elif checkWin(board, letterAI):
        return 1;
    elif len(emptySpaces) == 0:
        return 0;

    if maximizer:
        best = MIN;
        for i in range(len(emptySpaces)):   
            space = emptySpaces[i];
            board[space[0]][space[1]] = letterAI;
            best = max(best, minimax(board, depth+1, not maximizer, alpha, beta, letterAI, letterPlayer));
            alpha = max(alpha, best);
            board[space[0]][space[1]] = " ";

            if beta <= alpha:
                break;

        return best;
    else:
        best = MAX;
        for i in range(len(emptySpaces)):        
            space = emptySpaces[i];
            board[space[0]][space[1]] = letterPlayer;
            best = min(best, minimax(board, depth+1, not maximizer, alpha, beta, letterAI, letterPlayer));
            beta = min(beta, best);
            board[space[0]][space[1]]= " ";

            if beta <= alpha:
                break;

        return best;

def nextBestMove(board, letterAI, letterPlayer):
    bestVal = -10;
    bestMove = [];
    emptySpaces = findEmptySpaces(board);

    for i in range(len(emptySpaces)): 
        space = emptySpaces[i];

        board[space[0]][space[1]] = letterAI;

        moveVal = minimax(board, 0, False, MIN, MAX, letterAI, letterPlayer);

        board[space[0]][space[1]] = " ";

        # If the value of the current move is
        # more than the best value, then update
        # best/
        if (moveVal > bestVal):			
            bestMove = emptySpaces[i];
            bestVal = moveVal;
    
    return bestMove;

#AI moves
def moveAI(board, letterAI, letterPlayer):
    bestPlay = nextBestMove(board, letterAI, letterPlayer);

    board[bestPlay[0]][bestPlay[1]] = letterAI;

    printBoard(board);
    # make AI output easier to understand for humans
    # take the last move AI made
    # lastMoved = storeMovesAI[bestPlaySpace];

    # add 1 for readability
    output = [bestPlay[0]+1, bestPlay[1]+1];
    #turn to str to concat
    movedAI = str(output);
    print("AI moved "+ movedAI + ".\n");

    win = checkWin(board, letterAI);
    if win:
        print("Computer has won.");

    return board, win;

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
def movePlayer(board, exitGame, letter):
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
            return board, False, exitGame;

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

    board[coords[0]][coords[1]] = letter; # place on board

    printBoard(board);
    print();

    win = checkWin(board, letter);
    if win:
        print("Player has won!");

    return board, win, exitGame;

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
def checkWin(board, letter):
    #check win by looking at all the moves 
    # get all moves done by the letter, then check if there are any 3 in a rows
    storeMoves = [];
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == letter:
                storeMoves.append([i, j]);

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
    MIN, MAX = -10, 10;

    #while board is not empty or player chooses to end game; focus on full board for now
    while not isBoardFull(board) and not exitGame and not win:

        board, win = moveAI(board, "x", "o");
        #if win=true, break loop (unless we're doing the 5 in a row version)
        # board, win, exitGame = movePlayer(board, exitGame, "x");
        if win or isBoardFull(board) or exitGame:
            break;
        # board, win, exitGame = movePlayer(board, exitGame, "o");
        #if win=true, break loop (unless we're doing the 5 in a row version)
        board, win = moveAI(board, "o", "x");

    if win == False and not exitGame:
        print("Draw.");

    #out of loop
    # ask player if they want to play again; yes continue, no break

#issue: if player moves middle, ai moves [1,1], human moves [3,3], ai moves [1,2], humans moves [1,3] and have a 2 way win
#       ai sees no space in diagonals of last ai move, so it moves the first avaliable space thats neutral, WIP