from re import I
import numpy as np
import matplotlib.pyplot as plt
import time

from board_logic import *
from ai_logic import *

'''
Program to draw a graph for performance tests
'''
def loopminimax(testboard, turn):
    times = []
    depths = [i for i in range(11)]

    for i in range(11):
        startTime = time.time()
        maximizing(testboard, turn, BIG_NEGATIVE, BIG_POSITIVE, i)
        endTime = time.time()

        times.append(endTime-startTime) 

    return times

empty_board = [[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]]

times_empty = loopminimax(np.array(empty_board), 2)
depths = [i for i in range(11)]

testboard = [[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0],
            [1,1,0,0,2,2,2]]

times_losing = loopminimax(np.array(testboard), 1)

testboard = [[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0],
            [1,1,0,0,2,2,2]]

times_winning = loopminimax(np.array(testboard), 2)


plt.plot(depths, times_empty, '-b', label='Empty board')
plt.plot(depths, times_losing, '-r', label='Losing board')
plt.plot(depths, times_winning, '-g', label='Winning board')
plt.legend(loc = 'upper left')
plt.ylim(-0.5,25)
plt.xlabel('Depth')
plt.ylabel('Time taken in seconds')
plt.title('Minimax with alpha-beta pruning performance test')
plt.show()

