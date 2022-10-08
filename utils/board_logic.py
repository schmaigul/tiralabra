import numpy as np
import pygame

OFF_WHITE = (248, 240, 227)
BLACK = (24,25,28)
SQUARE_SIZE = 100
RED = (212, 57, 91)
BLUE = (67, 57, 212)

def draw_board(board, window):
    """
    params: game board, pygame window
    Draws the game state to the given pygame window
    """
    rows, columns = board.shape
    window.fill(BLACK)
    for row in range(rows):
        for col in range(columns):
            pygame.draw.rect(window, OFF_WHITE, (col*SQUARE_SIZE+2, row*SQUARE_SIZE+2+SQUARE_SIZE, SQUARE_SIZE-2, SQUARE_SIZE-2))
            if (board[row][col] == 1):
                pygame.draw.circle(window, RED, (int(col*SQUARE_SIZE+SQUARE_SIZE/2+1), int(row*SQUARE_SIZE+SQUARE_SIZE/2+1 + SQUARE_SIZE)), int(SQUARE_SIZE/2-2))
            if (board[row][col] == 2):
                pygame.draw.circle(window, BLUE, (int(col*SQUARE_SIZE+SQUARE_SIZE/2+1), int(row*SQUARE_SIZE+SQUARE_SIZE/2+1 + SQUARE_SIZE)), int(SQUARE_SIZE/2-2))

def check_valid(board, col):
    """
    params: current board, chosen column
    returns: if top row is occupied in selected column, if true, it is an invalid move
    """
    return board[0][col] == 0


def place_disc(board, rows, pos, turn):
    """
    Places disc on the board, updating the game state
    params: game board, number of rows in the board, position (column), player turn
    returns: new board and the row position where it was placed
    """
    for row in range(rows-1, -1, -1):
        if (board[row][pos] == 0):
            board[row][pos] = turn
            return (board, row)
    print(board)
    print('Cannot place anything to pos', pos)
    return False

def change_turn(turn):
    turn %= 2
    turn += 1
    return turn

def check_draw(board):
    return 0 not in board

def check_win(board, turn):
    """
    Method for checking if there is a winning condition on the current board
    """
    rows, columns = board.shape
    #Horizontal
    for row in range(rows-1, -1, -1):
        for col in range(columns-3):
            if board[row][col] == turn and board[row][col+1] == turn and board[row][col+2] == turn and board[row][col+3] == turn:
                return True

    #Vertical
    for row in range(rows-1, 2, -1):
        for col in range(columns):
            if board[row][col] == turn and board[row-1][col] == turn and board[row-2][col] == turn and board[row-3][col] == turn:
                return True
    
    #Check diagonals
    #Positive slope
    for row in range(rows-3):
        for col in range(columns-3):
            if board[row][col] == turn  and board[row+1][col+1] == turn and board[row+2][col+2] == turn and board[row+3][col+3] == turn:
                return True

    #Negative slope
    reverseboard = board[:,::-1]
    for row in range(rows-3):
        for col in range(columns-3):
            if reverseboard[row][col] == turn and reverseboard[row+1][col+1] == turn and reverseboard[row+2][col+2] == turn and reverseboard[row+3][col+3] == turn:
                return True

    return False
