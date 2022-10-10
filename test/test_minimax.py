import unittest
import io
import sys
from utils.ai_logic import *
from utils.board_logic import *
import numpy as np

BIG_NEGATIVE = -99999999
BIG_POSITIVE = 99999999

class MinimaxTest(unittest.TestCase):

    def test_winning(self):
        diagonal_top_left = [[1,0,0,0,0,0,0],
                            [0,1,0,0,0,0,0],
                            [0,0,1,0,0,0,0],
                            [0,0,0,1,0,0,0],
                            [0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0]]
        board = np.array(diagonal_top_left)
        self.assertEqual(1, check_win(board, 1), msg = f'Wrong deduction of winning condition for the board \n{board}')

        diagonal_bottom_right = [[0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0],
                                [0,0,0,1,0,0,0],
                                [0,0,0,0,1,0,0],
                                [0,0,0,0,0,1,0],
                                [0,0,0,0,0,0,1]]
        board = np.array(diagonal_bottom_right)
        self.assertEqual(1, check_win(board, 1), msg = f'Wrong deduction on winning condition for the board \n{board}')

        diagonal_top_right = [[0,0,0,0,0,0,1],
                              [0,0,0,0,0,1,0],
                              [0,0,0,0,1,0,0],
                              [0,0,0,1,0,0,0],
                              [0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0]]
        board =np.array(diagonal_top_right)
        self.assertEqual(1, check_win(board, 1), msg = f'Wrong deduction on winning condition for the board \n{board}')

        diagonal_bottom_left = [[0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0],
                                [0,0,0,1,0,0,0],
                                [0,0,1,0,0,0,0],
                                [0,1,0,0,0,0,0],
                                [1,0,0,0,0,0,0]]
        board = np.array(diagonal_bottom_left)
        self.assertEqual(1, check_win(board, 1), msg = f'Wrong deduction on winning condition for the board \n{board}')
        
        
        
        horizontal_bottom = [[0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0],
                            [1,1,1,1,0,0,0]]
        board = np.array(horizontal_bottom)
        self.assertEqual(1, check_win(board, 1), msg = f'Wrong deduction on winning condition for the board \n{board}')

        horizontal_bottom = [[0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0],
                            [0,0,0,1,1,1,1]]
        board = np.array(horizontal_bottom)
        self.assertEqual(1, check_win(board, 1), msg = f'Wrong deduction on winning condition for the board \n{board}')
        
        horizontal_top = [[0,0,0,1,1,1,1],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0]]
        board = np.array(horizontal_top)
        self.assertEqual(1, check_win(board, 1), msg = f'Wrong deduction on winning condition for the board \n{board}')

        vertical_left = [[1,0,0,0,0,0,0],
                         [1,0,0,0,0,0,0],
                         [1,0,0,0,0,0,0],
                         [1,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0]]
        board = np.array(vertical_left)
        self.assertEqual(1, check_win(board, 1), msg = f'Wrong deduction on winning condition for the board \n{board}')

        vertical_right = [[0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,1],
                          [0,0,0,0,0,0,1],
                          [0,0,0,0,0,0,1],
                          [0,0,0,0,0,0,1]]
        board = np.array(vertical_right)
        self.assertEqual(1, check_win(board, 1), msg = f'Wrong deduction on winning condition for the board \n{board}')

    def test_change_turn(self):
        board = np.zeros((6,7), int)
        self.assertEqual(2, change_turn(1))

    def test_draw(self):
        draw_board = [[1,2,1,2,1,2,1],
                [2,1,2,1,2,1,2],
                [1,2,1,2,1,2,1],
                [2,1,2,1,2,1,2],
                [1,2,1,2,1,2,1],
                [2,1,2,1,2,1,2]]
        board = np.array(draw_board)
        self.assertEqual(1, check_draw(board))

        not_draw = [[1,0,1,2,1,2,1],
                [2,1,2,1,2,1,2],
                [1,2,1,2,1,2,1],
                [2,1,2,1,2,1,2],
                [1,2,1,2,1,2,1],
                [2,1,2,1,2,1,2]]
        game = np.array(not_draw)
        self.assertEqual(1, check_draw(board))

    def test_children(self):
        board = [[1,0,1,0,1,0,1],
                [2,1,2,1,2,1,2],
                [1,2,1,2,1,2,1],
                [2,1,2,1,2,1,2],
                [1,2,1,2,1,2,1],
                [2,1,2,1,2,1,2]]

        game = np.array(board)
        children = make_children(game)
      
        self.assertEqual(True, all(x in [3,5,1] for x in children))

        testboard = [[1,2,1,2,1,2,1],
                [2,1,2,1,2,1,2],
                [1,2,1,2,1,2,1],
                [2,1,2,1,2,1,2],
                [1,2,1,2,1,2,1],
                [2,1,2,1,2,1,2]]
        
        children = make_children(np.array(testboard))
        self.assertEqual(children, [])

    def test_ai(self):

        testboard = [[0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [1,2,1,1,1,0,0],]

        winning_pos = iterative_deepening(np.array(testboard), 1, 2, True)

        self.assertEqual(winning_pos, 5)

        testboard = [[0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,1,0,0,0,0],
                     [0,1,0,0,0,0,0],
                     [1,2,2,1,1,1,0]]

        winning_pos = iterative_deepening(np.array(testboard), 1, 2, True)

        self.assertEqual(winning_pos, 6)

    def test_detect_winning(self):
        #Checks if AI fis able to detect guaranteed win in two turns
        win2turns = np.array([[0,1,2,0,0,0,0],
                                [0,0,2,1,0,0,0],
                                [0,0,2,2,0,0,0],
                                [0,0,2,1,0,2,1],
                                [1,2,1,2,2,1,2],
                                [1,1,2,1,1,1,2]])

        position = iterative_deepening(win2turns, 2, 6, True)
        win2turns, row = place_disc(win2turns, 6, position, 2)

        position = iterative_deepening(win2turns, 1, 6, True)
        win2turns, row = place_disc(win2turns, 6, position, 1)

        position = iterative_deepening(win2turns, 2, 6, True)
        win2turns, row = place_disc(win2turns, 6, position, 2)

        self.assertEqual(check_win(win2turns, 2), True)

    def test_detect_losing(self):
        #Detect losing situations

        avoidlosing = np.array([[0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0],
                                [0,0,0,2,0,0,0],
                                [0,0,1,1,0,0,0]])

        position = iterative_deepening(avoidlosing, 2 ,6, True)
        
        moves = [1,4]

        self.assertEqual((position in moves), True)

        #In this situation, player 2 must place their disc to the 3th column or else they will lose in the next round
        avoidlosing = np.array([[0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0],
                                [1,1,0,0,0,0,0],
                                [2,1,2,0,0,1,0],
                                [1,2,1,1,2,1,2]])

        position = iterative_deepening(avoidlosing, 2, 6, True)

        self.assertEqual(position, 2)



    def test_evaluation(self):
        
        self.assertEqual(50, evaluate_position(1, [1,1,1,1]))
        self.assertEqual(-50, evaluate_position(2, [1,1,1,1]))
        self.assertEqual(5, evaluate_position(1, [1,0,1,0]))
        self.assertEqual(-5, evaluate_position(2, [1,0,1,0]))
        self.assertEqual(10, evaluate_position(1, [1,0,1,1]))
        self.assertEqual(-10, evaluate_position(2, [1,1,0,1]))

    def test_score(self):

        testboard = [[0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [2,1,2,0,1,2,1],
                     [2,1,2,0,1,2,1],
                     [1,1,1,0,2,2,2]]

        self.assertEqual(scores(np.array(testboard), 1), 0)

        testboard = [[0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0],
                     [2,1,2,0,1,2,1],
                     [2,1,2,1,1,2,1],
                     [1,1,1,1,2,2,2]]

        self.assertEqual(scores(np.array(testboard), 1), 50+10+5+6)
        
