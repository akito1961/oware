"""
Heuristic Ideas
- Most seeds in a pit /
- Right-most pit
- Max Gain By AI /
- Min Gain By a player /
- Sum seeds in the owner side /
- Move Diversity /
"""

def _h1(board): # most seed in the right most pit for AI
    
    max = board[-1]
            
    return max

def _h2(board): # seed for Ai side
    
    ai_sum = sum(board[6:12])
    
    return ai_sum

def _h3(board): # possible move diversity and maintaining options
    count = 0
    ai_board = list(board[6:12])
    
    for seeds in ai_board:
        if seeds != 0:
            count += 1
            
    return count
    
def _h4(init_score, final_score): # max score gain for AI
    return final_score - init_score

def _h5(init_score, final_score): # min score gain for player
    return final_score - init_score

########################################

def heuristic_fn(game, init_score, weight):
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
    
    ### reading each heuristic ###
    H1 = _h1(board)
    H2 = _h2(board)
    H3 = _h3(board)
    H4 = _h4(ai_init_score, ai_final_score)
    H5 = _h5(p_init_score, p_final_score)
    
    ### reading each weight ###
    w1 = weight[0]
    w2 = weight[1]
    w3 = weight[2]
    w4 = weight[3]
    w5 = weight[4]
    
    score = (w1 * H1) + (w2 * H2) + (w3 * H3) + (w4 * H4) - (w5 * H5)
    
    # print("h score : ", score, H1, H2, H3, H4, H6)
    
    return score