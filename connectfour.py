import pygame
import numpy as np
import sys

#Choose the number of columns and rows for the game
COLUMNS = 7
ROWS = 6

#Makes the initial board
def make_board():
    board = np.zeros((ROWS, COLUMNS), int)
    return board

#if top column is occupied, then position is not valid
def check_valid(board, col):
    return board[0][col] == 0

#Places a disc to the board according to whose turn it is
def place_disc(board, pos, turn):
    for row in range(ROWS-1, 0, -1):
        if (board[row][pos] == 0):
            board[row][pos] = turn
            return board
    return False

#Checks if there is a winning condition
def check_win(board, turn):
    return True

board = make_board()
turn = 1

while(True):
    print(board)
    playerPosition = int(input(f'Player {turn} turn: choose a column between 1 and {COLUMNS}')) - 1
    if (check_valid(board, playerPosition)):
        board = place_disc(board, playerPosition, turn)  
        if (check_win(board, turn)):
            print(f'Player {turn} wins')
    else:
        print('Not a valid position, choose a new one')
    turn %= 2
    turn += 1