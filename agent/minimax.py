
"""
    step to build an minimax ai
    - get board position
    - decide whos turn it is
        -- if player turn, pick a maximum score
        -- if ai turn, pick a minimum score
    - repeat for the search
"""

import math
from random import choice
from agent.heuristic import heuristic_fn
    
##########################################################

def bestmove(game, weight_h = [1,1,1,1,1]):
    clone = game.clone()
    best_score = -math.inf
    best_move = None
    
    valid_move = clone.valid_move()
    
    if len(valid_move) != 0:
        for idx in valid_move:
            score = _minimax(clone, weight_h = weight_h)
            
            # print("Investigating : ", idx)
            # print("Score : ", score)
            
            
            if score > best_score:
                best_score = score
                best_move = []
                best_move.append(idx)
            
            if score == best_score:
                best_move.append(idx)
            
            # if score > best_score:
            #     best_score = score
            #     best_move = idx
                
    # print("best move idx : ", best_move)
    if best_move is not None:
        return choice(best_move), best_score
        
    
def _minimax(game, ai = None, depth:int = 8, alpha = -math.inf, beta = math.inf, scoretrack = None, weight_h:list = [1,1,1,1,1]):

    clone = game.clone()
    init_score = clone.score() if scoretrack is None else list(scoretrack)

    is_ai = True if ai is None else ai
    
    if depth == 0 or clone.valid_move() == []: # or game end
        score = heuristic_fn(clone, init_score, list(weight_h))
        # print("---------- End Leaf Node ----------\n")
        return score # return diff score (p1 - p2)
    
    if is_ai:
        max_score = -math.inf
        # find the best move for AI
        for idx in clone.valid_move():
            clone.move(idx)
            
            score = _minimax(game = clone.clone(), ai = False, depth = depth - 1, alpha = alpha, beta = beta, scoretrack = init_score)
            max_score = max(max_score, score)
            alpha = max(alpha, score)
            
            if beta <= alpha:
                return alpha
            
        return max_score
    else:
        min_score = math.inf
        # find the best move for opponent
        for idx in clone.valid_move():            
            clone.move(idx)

            score = _minimax(game = clone.clone(), ai = True, depth = depth - 1, alpha = alpha, beta = beta, scoretrack = init_score)
            min_score = min(score, min_score)
            beta = min(beta, score)
            
            if beta <= alpha:
                return beta
            
        return min_score