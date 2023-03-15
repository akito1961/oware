"""
Heuristic Ideas
- Most seeds in a pit /
- Right-most pit
- Max Gain By AI /
- Min Gain By a player /
- Sum seeds in the owner side /
- Move Diversity /
"""

import math

def _h1(valid_move, board): # most seed in the pit
    max = -math.inf
    
    if len(valid_move) != 0:
        for idx in valid_move:
            if board[idx] > max:
                max = board[idx]
    else:
        max = 0
            
    return max

def _h2(board, playerone): # seed dif between both sides
    
    p_sum = sum(board[0:6])
    ai_sum = sum(board[6:12])
    
    
    return ai_sum - p_sum

def _h3(valid_move): # possible move diversity and maintaining options
    return len(valid_move)
    
def _h4(init_score, final_score): # max score gain for AI
    return final_score - init_score

def _h5(init_score, final_score): # min score gain for player
    return final_score - init_score

########################################

def heuristic_fn(game, init_score):
    clone = game.clone()
    
    valid_move = clone.valid_move()
    board = clone.board()
    playerone = clone.playerone()
    final_score = clone.score()
    
    ### score set up ###
    p_init_score = init_score[0]
    ai_init_score = init_score[1]
    
    p_final_score = final_score[0]
    ai_final_score = final_score[1]
    
    H1 = _h1(valid_move, board)
    H2 = _h2(board, playerone)
    H3 = _h3(valid_move)
    H4 = _h4(ai_init_score, ai_final_score)
    H5 = _h5(p_init_score, p_final_score)
    
    score = (1 * H1) + (1 * H2) + (1 * H3) + H4 - (1 * H5)
    
    # print("h score : ", score, H1, H2, H3, H4, H6)
    
    return score