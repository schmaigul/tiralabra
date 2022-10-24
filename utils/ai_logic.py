import numpy as np
from sympy import Ne
from utils.board_logic import *
import random


BIG_NEGATIVE = -99999999
BIG_POSITIVE = 99999999

HUMAN = 1
AI = 2

ROWS = 6
COLUMNS = 7


'''
All classes that are used by the AI.
'''

def evaluate_position(turn, window):
        """
        Function to evaluate given 4*1 window from the board
        """
        value = 0

        #If four own discs in a row
        if window.count(turn) == 4:
            value += 50
        #3 own discs and 1 empty
        if window.count(turn) == 3 and window.count(0) == 1:
            value += 10
        #2 own discs and 1 empty
        if window.count(turn) == 2 and window.count(0) == 2:
            value += 5
        
        #Check for opponent score
        opponent = turn%2+1
        if window.count(opponent) == 4:
            value -= 50
        if window.count(opponent) == 3 and window.count(0) == 1:
            value -= 10
        if window.count(opponent) == 2 and window.count(0) == 2:
            value -= 5

        return value

def scores(board, turn):
    """
    Traverses the board in a similar way as check_win function, but instead slices arrays of length 4 for the evaluation function
    Higher score means better chance of winning
    params: evaluated board, and turn
    return: value that determines the current score for the player, the higher the better
    """
    rows, columns = board.shape
    board = board.tolist()
    value = 0

    #Center positions are most valuable at the start of the game
    center = [row[int(columns/2)] for row in board]
    value += center.count(turn)*3

    #Horizontal score
    for row in range(rows):
        for col in range(columns-3):
            value += evaluate_position(turn, board[row][col:col+4])
    
    #Vertical score
    for col in range(columns):
        colarrays = [board[i][col] for i in range(4)]
        for row in range(rows-3):
            array = colarrays[row:row+4]
            value += evaluate_position(turn, array)
    
    #Diagonal score
    for row in range(rows-3):
        for col in range(columns-3):
            window = [board[row+i][col+i] for i in range(4)]
            value += evaluate_position(turn, window)

    #Negative slope diagonal
    board = board[:][::-1]
    for row in range(rows-3):
        for col in range(columns-3):
            window = [board[row+i][col+i] for i in range(4)]
            value += evaluate_position(turn, window)

    return value


def make_children(board):
    '''
    Generates all the possible moves for the current board
    '''
    children = []
    columns = board.shape[1]
    middle = columns//2

    #Choose randomly from which side from the middle the children will be generated
    choice = random.choice([1,2])

    #Check if middle is a valid position
    if (check_valid(board, middle)):
            children.append(middle)

    #Start iterating from the middle alternating to both sides
    if (choice == 1):
        #Check first left side, then right
        for i in range(1, middle+1, 1):
            if (check_valid(board, middle+i)):
                children.append(middle+i)

            if (check_valid(board, middle-i)):
                children.append(middle-i)
    
    if (choice == 2):
        #Check first right side, then left
        for i in range(1, middle+1, 1):
            if (check_valid(board, middle-i)):
                children.append(middle-i)
            if (check_valid(board, middle+i)):
                children.append(middle+i)

    return children


def maximizing(board, turn, alpha, beta, depth):
        """
        Minimax maximizing function with alpha-beta pruning, AI is the maximizer
        Returns: Best score and corresponding column number where the disc will be dropped
        """
        if (check_win(board, turn)):
            return (BIG_POSITIVE, None)

        if (check_draw(board)):
            return (0, None)

        #Call evaluation at bottom depth
        if (depth == 0):
            return (scores(board, turn) , None)

        #Initialize children and start minimax with the worst score
        value = BIG_NEGATIVE
        children = make_children(board)
        chosen_position = children[0]

        for position in children:

            #Place a disc on the board, and change turn
            board, row = place_disc(board, board.shape[0], position, turn)
            turn = change_turn(turn)

            #Pass the new board to the minimizing function
            new_score, new_position = minimizing(board, turn, alpha, beta, depth-1)
            
            #Invert changes to the board
            turn = change_turn(turn)
            board[row][position] = 0

            #Choose max score and the corresponding position in the board
            if new_score > value:
                value = new_score
                chosen_position = position

            #Alpha beta-pruning
            if value >= beta:
                break
            alpha = max(alpha, value)

        return (value, chosen_position)

def minimizing(board, turn, alpha, beta, depth):
    """
    Minimax minimizing function with alpha-beta pruning
    Returns: Best score and corresponding column number where the disc will be dropped
    """

    #If win detected, return immidiately
    if (check_win(board, turn)):
        return (BIG_NEGATIVE, None)

    if (check_draw(board)):
        return (0, None)

    if (depth == 0):
        #Return negative score
        return (scores(board, turn)*(-1), None)

    #Initialize children and start minimax with the worst score
    value = BIG_POSITIVE
    children = make_children(board)
    chosen_position = children[0]

    for position in children:

        #Place a disc on the board, and change turn
        board, row = place_disc(board, board.shape[0], position, turn)
        turn = change_turn(turn)
        
        #Pass the new board to the maximizing function
        new_score, new_position = maximizing(board, turn, alpha, beta, depth-1)

        #Invert changes to the board
        turn = change_turn(turn)
        board[row][position] = 0

        #Choose min score and the corresponding position in the board
        if new_score < value:
            value = new_score
            chosen_position = position

        #Alpha beta-pruning
        if value <= alpha:
            break
        beta = min(beta, value)

    return (value, chosen_position)


def iterative_deepening(board, turn, depth, isMax):
    '''
    Iterative deepening used for move ordering based on the best move found at previous depth to make alpha-beta pruning faster
    '''

    #Initiation, scores is a dictionary with children as the key and corresponding score initated at 0
    children = make_children(board)
    chosen_position = children[0]
    scores = dict.fromkeys(children, BIG_NEGATIVE)

    #Detect if opponent has winning condition on the next move, and block it immidiately
    block = block_lose(board, children, turn)
    if (block != None):
        return block

    
    #iterate from 0 to depth
    if (isMax):
        for current_depth in range(depth):

            #Emulate max algorithm but sort children after each iteration

            alpha = BIG_NEGATIVE
            beta = BIG_POSITIVE

            best_score = BIG_NEGATIVE

            for pos in children:
                
                #Place a disc on the board and change current turn
                board, row = place_disc(board, board.shape[0], pos, turn)
                turn = change_turn(turn)
            
                new_score, new_position = minimizing(board, turn, alpha, beta, current_depth)

                #Pick max score for sorting later
                scores[pos] = max(scores[pos], new_score)

                #Revert previous board actions
                board[row][pos] =  0
                turn = change_turn(turn)

                if (new_score == BIG_POSITIVE):
                    return pos

                #Always pick best score to be max from all children
                if (new_score > best_score):
                    best_score = new_score
                    chosen_position = pos

                #Max pruning
                if best_score >= beta:
                    break
                
                alpha = max(alpha, best_score)

            #Sort children in descending order and use this order in the next iteration, to hopefully prune early on
            children = sorted(children, key=lambda x: scores[x], reverse = True)

    return chosen_position



def block_lose(board, children, turn):
    '''
    Heuristic that runs before iterative deepening. Detects whether current player needs to block a losing condition immidiately which otherwise would take a lot of time for the alpha-beta pruning.
    return: position if losing situation found, otherwise None.
    '''
    turn = change_turn(turn)

    for pos in children:

        board, row = place_disc(board, board.shape[0], pos, turn)
        
        if (check_win(board, turn)):

            board[row][pos] =  0
            turn = change_turn(turn)

            return pos

        board[row][pos] =  0
    
    turn = change_turn(turn)

    return None