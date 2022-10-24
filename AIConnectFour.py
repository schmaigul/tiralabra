from re import I
import pygame
import numpy as np
from utils.board_logic import *
from utils.ai_logic import *

#Constants for drawing the game and player number.
OFF_WHITE = (248, 240, 227)
BLACK = (24,25,28)
SQUARE_SIZE = 100
RED = (212, 57, 91)
BLUE = (67, 57, 212)
HUMAN = 1
AI = 2

BIG_NEGATIVE = -99999999
BIG_POSITIVE = 99999999

def play_connect_four(board, turn):
    """Game loop for two player connect four. The loop exits when the game has ended"""

    #Setting up game variables 
    game_not_over = True
    turn_texts = ["Human's turn", "AI's turn"]
    turn_colors = [RED, BLUE]
    rows, columns = board.shape
    
    #Setting up the game window
    window = pygame.display.set_mode(size = (700, 700))
    pygame.display.set_caption('Connect Four')
    font = pygame.font.Font('freesansbold.ttf', 32)
    draw_board(board, window)

    text = font.render(turn_texts[turn-1], True, turn_colors[turn-1])
    window.blit(text, dest = (250, 40))
    
    pygame.display.update()

    #Game loop, players are 1 (red) and 2 (blue)
    while(game_not_over):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                #The chosen column is horizontal mouse int(position/SQUARE_SIZE)
                if (turn == HUMAN):
                    
                    playerPosition = int(event.pos[0]/SQUARE_SIZE)

                    if (check_valid(board, playerPosition)):
                        board, row = place_disc(board, rows, playerPosition, turn)

                    else:
                        print('Not a valid position, choose a new one')
                        break
                    
                    #Swithes turn of the player between 1 and 2
                    if check_draw(board):
                        game_not_over = False
                        text = font.render('Draw!', True, (255,255,255))

                    if check_win(board, turn):
                        game_not_over = False
                        text = font.render('Human wins!', True, turn_colors[HUMAN-1])

                    #Game is draw if there are no 0's in the array
                    if (not check_win(board, turn) and not check_draw(board)): 
                        
                        #If not end state, change turn
                        turn = change_turn(turn)
                        text = font.render(turn_texts[AI-1], True, turn_colors[AI-1])

                    draw_board(board, window)
                    window.blit(text, dest = (250, 40))
                    pygame.display.update()
    
        if (turn == AI):

            #AI is maximizing its score
            position = iterative_deepening(board, turn, 6, True)
            board, row = place_disc(board, rows, position, turn)

            if check_draw(board):
                    game_not_over = False
                    text = font.render('Draw!', True, (255,255,255))

            if check_win(board, turn):
                game_not_over = False
                text = font.render('AI wins!', True, turn_colors[AI-1])
                
            #Game is draw if there are no 0's in the array
            if (not check_win(board, turn) and not check_draw(board)): 
                #If not end state, change turn

                turn = change_turn(turn)
                text = font.render(turn_texts[HUMAN-1], True, turn_colors[HUMAN-1])

            draw_board(board, window)
            window.blit(text, dest = (250, 40))
            pygame.display.update()

        #Delay the window if the game has ended
        if not game_not_over:
            pygame.time.wait(4000)

if __name__ == '__main__':
    #Start the game
    pygame.init()
    while (True):
        board = np.zeros((6,7), int)
        play_connect_four(board, HUMAN)