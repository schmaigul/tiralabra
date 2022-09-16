from re import S
import pygame
import numpy as np
import sys
from connectfour import ConnectFour

#Choose the number of columns and rows for the game
OFF_WHITE = (248, 240, 227)
BLACK = (24,25,28)
SQUARE_SIZE = 100
RED = (212, 57, 91)
BLUE = (67, 57, 212)


def play_connect_four(board):
    """Game loop for two player connect four. The loop exits when the game has ended"""
    
    #Setting up game variables
    turn = 1
    game_not_over = True
    turn_texts = ["Red's turn", "Blue's turn"]
    turn_colors = [RED, BLUE]
    rows, columns = board.get_dimensions()
    size = rows*columns
    play_counter = 0
    
    #Setting up the game window
    window = pygame.display.set_mode(size = (700, 700))
    pygame.display.set_caption('Connect Four')
    font = pygame.font.Font('freesansbold.ttf', 32)
    board.draw(window)
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
                playerPosition = int(event.pos[0]/SQUARE_SIZE)
                print(playerPosition)

                if (board.check_valid(playerPosition)):
                    board.place_disc(playerPosition, turn)  
                    play_counter += 1
                else:
                    print('Not a valid position, choose a new one')
                
                #Swithes turn of the player between 1 and 2
                if (board.check_win(turn)):
                    game_not_over = False

                    if (turn == 1):
                        text = font.render('Red wins!', True, turn_colors[turn-1])
                    if (turn == 2):
                        text =  font.render('Blue wins!', True, turn_colors[turn-1])
                #Game is draw if the play counter is columns*rows = size
                if (play_counter == size):
                    text = font.render('Draw!', True, (255,255,255))
                    game_not_over = False

                else: 
                    #Indexing is done such that it chooses the next one before the actual turn is changed
                    text = font.render(turn_texts[turn%2], True, turn_colors[turn%2])

                board.draw(window)
                window.blit(text, dest = (250, 40))
                pygame.display.update()

                #Delay the window if the game has ended
                if not game_not_over or play_counter == size:
                    pygame.time.delay(3000)

                turn %= 2
                turn += 1

if __name__ == '__main__':
    pygame.init()
    while (True):
        board = ConnectFour(6,7)
        play_connect_four(board)
       
