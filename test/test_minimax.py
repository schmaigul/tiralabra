import unittest
import io
import sys
from utils.ai_logic import *
from utils.board_logic import *
import numpy as np

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
      
        self.assertEqual(children, [3,5,1])

        testboard = [[1,2,1,2,1,2,1],
                [2,1,2,1,2,1,2],
                [1,2,1,2,1,2,1],
                [2,1,2,1,2,1,2],
                [1,2,1,2,1,2,1],
                [2,1,2,1,2,1,2]]
        
        children = make_children(np.array(testboard))
        self.assertEqual(children, [])

    def test_minimax(self):
        testboard = [[0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,1],
                          [0,0,0,0,0,0,1],
                          [0,0,0,0,0,0,1],
                          [0,0,0,0,0,0,1]]

        value, pos = minimizing(testboard, 2, -9999999, 9999999, 1)