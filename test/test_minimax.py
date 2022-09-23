import unittest
import io
import sys
from src.minimax import AIConnectFour
import numpy as np

class MinimaxTest(unittest.TestCase):

    def test_winning(self):
        diagonal_top_left = [[1,0,0,0,0,0,0],
                            [0,1,0,0,0,0,0],
                            [0,0,1,0,0,0,0],
                            [0,0,0,1,0,0,0],
                            [0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0]]
        board = AIConnectFour(np.array(diagonal_top_left), 1)
        self.assertEqual(1, board.check_win(), msg = f'Wrong deduction of winning condition for the board \n{board}')

        diagonal_bottom_right = [[0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0],
                                [0,0,0,1,0,0,0],
                                [0,0,0,0,1,0,0],
                                [0,0,0,0,0,1,0],
                                [0,0,0,0,0,0,1]]
        board =AIConnectFour(np.array(diagonal_bottom_right),1)
        self.assertEqual(1, board.check_win(), msg = f'Wrong deduction on winning condition for the board \n{board}')

        diagonal_top_right = [[0,0,0,0,0,0,1],
                              [0,0,0,0,0,1,0],
                              [0,0,0,0,1,0,0],
                              [0,0,0,1,0,0,0],
                              [0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0]]
        board = AIConnectFour(np.array(diagonal_top_right),1)
        self.assertEqual(1, board.check_win(), msg = f'Wrong deduction on winning condition for the board \n{board}')

        diagonal_bottom_left = [[0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0],
                                [0,0,0,1,0,0,0],
                                [0,0,1,0,0,0,0],
                                [0,1,0,0,0,0,0],
                                [1,0,0,0,0,0,0]]
        board = AIConnectFour(np.array(diagonal_bottom_left),1)
        self.assertEqual(1, board.check_win(), msg = f'Wrong deduction on winning condition for the board \n{board}')
        
        
        
        horizontal_bottom = [[0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0],
                            [1,1,1,1,0,0,0]]
        board = AIConnectFour(np.array(horizontal_bottom),1)
        self.assertEqual(1, board.check_win(), msg = f'Wrong deduction on winning condition for the board \n{board}')
        
        horizontal_top = [[0,0,0,1,1,1,1],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0]]
        board = AIConnectFour(np.array(horizontal_top),1)
        self.assertEqual(1, board.check_win(), msg = f'Wrong deduction on winning condition for the board \n{board}')

        vertical_left = [[1,0,0,0,0,0,0],
                         [1,0,0,0,0,0,0],
                         [1,0,0,0,0,0,0],
                         [1,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0]]
        board = AIConnectFour(np.array(vertical_left),1)
        self.assertEqual(1, board.check_win(), msg = f'Wrong deduction on winning condition for the board \n{board}')

        vertical_right = [[0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,1],
                          [0,0,0,0,0,0,1],
                          [0,0,0,0,0,0,1],
                          [0,0,0,0,0,0,1]]
        board = AIConnectFour(np.array(vertical_right),1)
        self.assertEqual(1, board.check_win(), msg = f'Wrong deduction on winning condition for the board \n{board}')

    def test_change_turn(self):
        board = AIConnectFour((np.zeros((6,7), int)), 1)
        self.assertEqual(2, board.change_turn())

    def test_draw(self):
        draw_board = [[1,2,1,2,1,2,1],
                [2,1,2,1,2,1,2],
                [1,2,1,2,1,2,1],
                [2,1,2,1,2,1,2],
                [1,2,1,2,1,2,1],
                [2,1,2,1,2,1,2]]
        game = AIConnectFour(np.array(draw_board), 2)
        self.assertEqual(1, game.check_draw())

        not_draw = [[1,0,1,2,1,2,1],
                [2,1,2,1,2,1,2],
                [1,2,1,2,1,2,1],
                [2,1,2,1,2,1,2],
                [1,2,1,2,1,2,1],
                [2,1,2,1,2,1,2]]
        game = AIConnectFour(np.array(not_draw),2)
        self.assertEqual(0, game.check_draw())

    def test_children(self):
        board = [[1,0,1,0,1,0,1],
                [2,1,2,1,2,1,2],
                [1,2,1,2,1,2,1],
                [2,1,2,1,2,1,2],
                [1,2,1,2,1,2,1],
                [2,1,2,1,2,1,2]]

        game = AIConnectFour(np.array(board), 2)
        children = game.make_children()
        for child in children:
            self.assertEqual(child[0].get_turn(),1)

        testboard = [[1,2,1,0,1,0,1],
                [2,1,2,1,2,1,2],
                [1,2,1,2,1,2,1],
                [2,1,2,1,2,1,2],
                [1,2,1,2,1,2,1],
                [2,1,2,1,2,1,2]]
                
        self.assertEqual((children[0][0].get_board() == np.array(testboard)).all(), 1)