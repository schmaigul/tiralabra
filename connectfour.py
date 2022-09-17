import numpy as np
import pygame

OFF_WHITE = (248, 240, 227)
BLACK = (24,25,28)
SQUARE_SIZE = 100
RED = (212, 57, 91)
BLUE = (67, 57, 212)

class ConnectFour:
    """
    Class that contains current state of the game, game logic and drawing the board on graphical interface
    :attr rows: number of rows in the board
    :attr columns: number of columns in the board
    :attr board: initializing rows * columns connect four board
    """
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = np.zeros((rows, columns), int)

    def __str__(self) -> str:
        return f'{self.board}'

    def get_board(self):
        return self.board

    def get_dimensions(self):
        return (self.rows, self.columns)

    def draw(self, window):
        """
        Draws the game state to the given pygame window
        """
        window.fill(BLACK)
        for row in range(self.rows):
            for col in range(self.columns):
                pygame.draw.rect(window, OFF_WHITE, (col*SQUARE_SIZE+2, row*SQUARE_SIZE+2+SQUARE_SIZE, SQUARE_SIZE-2, SQUARE_SIZE-2))
                if (self.board[row][col] == 1):
                    pygame.draw.circle(window, RED, (int(col*SQUARE_SIZE+SQUARE_SIZE/2+1), int(row*SQUARE_SIZE+SQUARE_SIZE/2+1 + SQUARE_SIZE)), SQUARE_SIZE/2-2)
                if (self.board[row][col] == 2):
                    pygame.draw.circle(window, BLUE, (int(col*SQUARE_SIZE+SQUARE_SIZE/2+1), int(row*SQUARE_SIZE+SQUARE_SIZE/2+1 + SQUARE_SIZE)), SQUARE_SIZE/2-2)

    def check_valid(self, col):
        """
        Checks if top row is occupied in selected column
        """

        return self.board[0][col] == 0


    def place_disc(self, pos, turn):
        """
        Places disc on the board, updating the game state
        """

        for row in range(self.rows-1, -1, -1):
            if (self.board[row][pos] == 0):
                self.board[row][pos] = turn
                return True
        return False

    
    def check_draw(self):
        return 0 not in self.board
    
    def check_win(self, turn):
        """
        Method for checking if there is a winning condition on the current board
        """

        #Horizontal
        for row in range(self.rows-1, 0, -1):
            for col in range(self.columns-3):
                if self.board[row][col] == turn and self.board[row][col+1] == turn and self.board[row][col+2] == turn and self.board[row][col+3] == turn:
                    return True

        #Vertical
        for row in range(self.rows-1, 2, -1):
            for col in range(self.columns-1):
                if self.board[row][col] == turn and self.board[row-1][col] == turn and self.board[row-2][col] == turn and self.board[row-3][col] == turn:
                    return True
        
        #Check diagonals
        #Positive slope
        for row in range(self.rows-3):
            for col in range(self.columns-3):
                if self.board[row][col] == turn  and self.board[row+1][col+1] == turn and self.board[row+2][col+2] == turn and self.board[row+3][col+3] == turn:
                    return True

        #Negative slope
        reverseboard = self.board[:,::-1]
        for row in range(self.rows-3):
            for col in range(self.columns-3):
                if reverseboard[row][col] == turn and reverseboard[row+1][col+1] == turn and reverseboard[row+2][col+2] == turn and reverseboard[row+3][col+3] == turn:
                    return True

        return False
