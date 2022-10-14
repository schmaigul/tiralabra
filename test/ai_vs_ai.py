import numpy as np
from utils.ai_logic import *
import matplotlib.pyplot as plt 

who_won = {0: 0, 1:0, 2:0}

for i in range(100):
    board = np.zeros((6,7), int)

    game_not_over = True

    turn = 1

    while (game_not_over):

        pos = iterative_deepening(board, turn, 6, True)
        board, row = place_disc(board, 6, pos, turn)
        
        if (check_draw(board)):
            
            who_won[0] += 1

            game_not_over = False

            print('draw')

        if (check_win(board, turn)):

            game_not_over = False

            if (turn == 1):
                print('The bot who started won')
                who_won[1] += 1

            if (turn == 2):
                print('The bot who did not start won')
                who_won[2] += 1

        turn = change_turn(turn)


end_state = ['Draw', 'Starting won', 'Second won']
values = list(who_won.values())
plt.bar(end_state, values)
plt.title('100 iterations AI vs AI')
plt.show()