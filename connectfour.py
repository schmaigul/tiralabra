from re import S
import pygame
import numpy as np
import sys

#Choose the number of columns and rows for the game
ROWS = 6
COLUMNS = 7
OFF_WHITE = (248, 240, 227)
BLACK = (24,25,28)
SQUARE_SIZE = 100
RED = (212, 57, 91)
BLUE = (67, 57, 212)

#Makes the initial board
def make_board():
    board = np.zeros((ROWS, COLUMNS), int)
    return board

#Draws board in Pygame
def draw_board(board, window):
    window.fill(BLACK)
    for row in range(ROWS):
        for col in range(COLUMNS):
            pygame.draw.rect(window, OFF_WHITE, (col*SQUARE_SIZE+2, row*SQUARE_SIZE+2, SQUARE_SIZE-2, SQUARE_SIZE-2))
            if (board[row][col] == 1):
                pygame.draw.circle(window, RED, (int(col*SQUARE_SIZE+SQUARE_SIZE/2+1), int(row*SQUARE_SIZE+SQUARE_SIZE/2+1)), SQUARE_SIZE/2-2)
            if (board[row][col] == 2):
                pygame.draw.circle(window, BLUE, (int(col*SQUARE_SIZE+SQUARE_SIZE/2+1), int(row*SQUARE_SIZE+SQUARE_SIZE/2+1)), SQUARE_SIZE/2-2)

#if top column is occupied, then position is not valid
def check_valid(board, col):
    return board[0][col] == 0

#Places a disc to the board according to whose turn it is
def place_disc(board, pos, turn):
    for row in range(ROWS-1, -1, -1):
        if (board[row][pos] == 0):
            board[row][pos] = turn
            return board
    return False

#Checks if there is a winning condition
def check_win(board, turn):

    #Horizontal
    for row in range(ROWS-1, 0, -1):
        for col in range(COLUMNS-3):
            if board[row][col] == turn and board[row][col+1] == turn and board[row][col+2] == turn and board[row][col+3] == turn:
                return True

    #Vertical
    for row in range(ROWS-1, 2, -1):
        for col in range(COLUMNS-1):
            if board[row][col] == turn and board[row-1][col] == turn and board[row-2][col] == turn and board[row-3][col] == turn:
                return True
    
    #Check diagonals
    #Positive slope
    for row in range(ROWS-3):
        for col in range(COLUMNS-3):
            if board[row][col] == turn  and board[row+1][col+1] == turn and board[row+2][col+2] == turn and board[row+3][col+3] == turn:
                return True

    #Negative slope
    reverseboard = board[:,::-1]
    for row in range(ROWS-3):
        for col in range(COLUMNS-3):
            if reverseboard[row][col] == turn and reverseboard[row+1][col+1] == turn and reverseboard[row+2][col+2] == turn and reverseboard[row+3][col+3] == turn:
                return True

    return False


def play_connect_four():
    #MAKE A BOARD OF SIZE ROWS * COLUMNS
    board = make_board()
    turn = 1
    game_not_over = True
    
    pygame.init()
    window = pygame.display.set_mode(size = (COLUMNS*SQUARE_SIZE, ROWS*SQUARE_SIZE))
    pygame.display.set_caption('Connect Four')
    draw_board(board, window)

    #Game loop, players are 1 and 2
    while(game_not_over):
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_not_over = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                #The chosen column is horizontal mouse int(position/SQUARE_SIZE)
                playerPosition = int(event.pos[0]/SQUARE_SIZE)
                print(playerPosition)

                if (check_valid(board, playerPosition)):
                    board = place_disc(board, playerPosition, turn)  
                    draw_board(board, window)
                    print(board[::-1])
                    if (check_win(board, turn)):
                        print(board)
                        print(f'Player {turn} wins')
                        game_not_over = False

                else:
                    print('Not a valid position, choose a new one')
                    
                turn %= 2
                turn += 1

    draw_board(board, window)
    pygame.quit()

if __name__ == '__main__':
    play_connect_four()