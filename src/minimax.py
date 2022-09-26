import random
from src.connectfour import ConnectFour
import numpy as np

AI_TURN = 2
PLAYER_TURN = 1
BIG_NEGATIVE = -99999999
BIG_POSITIVE = 99999999

'''
AI that implements ConnectFour methods for keeping track of the game and additionally had methods for evaluating
the game with alpha-beta pruning algorithm
param board: N*M matrix with 0,1 and 2's. 0's indicate empty tile, 1 for player 1 and 2 for player 2
param turn: Whose turn it is currently
'''
class AIConnectFour(ConnectFour):

    def __init__(self, board, turn):
        super().__init__(board, turn)
    
    def make_children(self):
        '''
        Generates all valid children for the current board
        return: list of tuples of AIConnectFour instances and the position which defines the new child
        '''
        children = []
        rows, columns = self.get_dimensions()
        for col in range(columns):
            if (self.check_valid(col)):

                #Copy the current board for the child
                child = AIConnectFour(self.get_board().copy(), self.get_turn())

                #Place the disc and change turn before adding to dictionary
                child.place_disc(col)
                child.change_turn()
                children.append((child, col))

        return children

    def evaluate_position(self, window):
        """
        Function to evaluate given 4*1 window from the board
        """
        turn = self.turn
        value = 0

        #If four own discs in a row
        if window.count(turn) == 4:
            value += 50
        #If there are 3 own discs and one empty
        if window.count(turn) == 3 and window.count(0) == 1:
            value += 10
        if window.count(turn) == 2 and window.count(0) == 2:
            value += 5
        

        opponent = turn%2+1
        if window.count(opponent) == 4:
            value -= 50
        #If there are 3 own discs and one empty
        if window.count(opponent) == 3 and window.count(0) == 1:
            value -= 10
        if window.count(opponent) == 2 and window.count(0) == 2:
            value -= 5

        return value

    def scores(self):
        """
        Traverses the board in a similar way as check_win function, but instead slices arrays of length 4 for the evaluation function
        Higher score means better chance of winning
        return: value that determines the current score for the player, the higher the better
        """
        board = self.get_board().tolist()
        rows, columns = self.get_dimensions()
        turn = self.get_turn()
        value = 0

        #Center positions are most valuable at the start of the game
        center = [row[int(columns/2)] for row in board]
        value += center.count(turn)*3

        #Horizontal score
        for row in range(rows):
            for col in range(columns-3):
                value += self.evaluate_position(board[row][col:col+4])
        
        #Vertical score
        for col in range(columns):
            colarrays = [board[i][col] for i in range(4)]
            for row in range(rows-3):
                array = colarrays[row:row+4]
                value += self.evaluate_position(array)
        
        #Diagonal score
        for row in range(rows-3):
            for col in range(columns-3):
                window = [board[row+i][col+i] for i in range(4)]
                value += self.evaluate_position(window)

        #Negative slope diagonal
        board = board[:][::-1]
        for row in range(rows-3):
            for col in range(columns-3):
                window = [board[row+i][col+i] for i in range(4)]
                value += self.evaluate_position(window)

        return value

    def maximizing(self, alpha, beta, depth):
        """
        Minimax maximizing function with alpha-beta pruning, AI is the maximizer
        Returns: Best score and corresponding column number where the disc will be dropped
        """
        if (depth == 0):
            return (self.scores(), None)
        if (self.check_win()):
            return (BIG_POSITIVE, None)
        if (self.check_draw()):
            return (0, None)

        value = BIG_NEGATIVE
        children = self.make_children()

        #Choose initially a random position from all the valid positions
        chosen_position = random.choice([i[1] for i in children])

        random.shuffle(children)

        for child, position in children:
            new_score, new_position = child.minimizing(alpha, beta, depth-1)
            if new_score > value:
                value = new_score
                chosen_position = position
            if value >= beta:
                break
            alpha = max(alpha, value)
        return (value, chosen_position)

    def minimizing(self, alpha, beta, depth):
        """
        Minimax minimizing function with alpha-beta pruning, human is the minimizer
        Returns: Best score and corresponding column number where the disc will be dropped
        """
        if (depth == 0):
            return (self.scores()*(-1), None)
        if (self.check_win()):
            return (BIG_NEGATIVE, None)
        if (self.check_draw()):
            return (0, None)

        value = BIG_POSITIVE
        children = self.make_children()

        #Choose initially a random position from all the valid positions
        chosen_position = random.choice([i[1] for i in children])

        for child, position in children:
            new_score, new_position = child.maximizing(alpha, beta, depth-1)
            if new_score < value:
                value = new_score
                chosen_position = position
            if value <= alpha:
                break
            beta = min(beta, value)

        return (value, chosen_position)

    
