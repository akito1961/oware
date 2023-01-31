
"""
    step to build an minimax ai
    - get board position
    - decide whos turn it is
        -- if player turn, pick a maximum score
        -- if ai turn, pick a minimum score
    - repeat for the search
"""

import math
    
##########################################################

def bestmove(game):
    clone = game.clone()
    bestscore = -math.inf
    
    valid_move = clone.valid_move()
    
    if len(valid_move) != 0:
        for idx in valid_move:
            score = _minimax(clone)
            if score > bestscore:
                bestscore = score
                move = idx
                
        print(bestscore)
        return move
    else:
        return clone.score()
        
    
def _minimax(game, depth:int = 8):

    p1_validmove = [True, True, True, True, True, True,
                    False, False, False, False, False, False]
    p2_validmove = [False, False, False, False, False, False,
                    True, True, True, True, True, True]

    clone = game.clone()

    maximizer = clone.playerone()
    
    if depth == 0 or clone.valid_move() == []: # or game end
        score = clone.score()
        return score[0] - score[1] # return diff score (p1 - p2)
    
    if maximizer:
        max_score = -math.inf
        # find the best move for player one
        for idx in clone.valid_move():
            clone.move(idx)
            score = _minimax(clone.clone(), depth - 1)
            max_score = max(max_score, score)
            
        return max_score
    else:
        min_score = math.inf
        # find the best move player two (AI)
        for idx in clone.valid_move():
            clone.move(idx)
            score = _minimax(clone.clone(), depth - 1)
            min_score = min(score, min_score)
            
        return min_score