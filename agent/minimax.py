
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

def bestmove(game):
    clone = game.clone()
    best_score = -math.inf
    best_move = None
    
    valid_move = clone.valid_move()
    
    if len(valid_move) != 0:
        for idx in valid_move:
            score = _minimax(clone)
            
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
        
    
def _minimax(game, depth:int = 8, alpha = -math.inf, beta = math.inf, scoretrack = None):

    clone = game.clone()
    
    init_score = clone.score() if scoretrack is None else list(scoretrack)

    maximizer = clone.playerone()
    
    if depth == 0 or clone.valid_move() == []: # or game end
        score = heuristic_fn(clone, init_score)
        # print("---------- End Leaf Node ----------\n")
        return score # return diff score (p1 - p2)
    
    if maximizer:
        max_score = -math.inf
        # find the best move for player one
        for idx in clone.valid_move():
            # print("--P1 Turn--")
            
            clone.move(idx)
            
            # print("Chosen Idx: ", idx)
            # print(clone.moves())
            # print(clone.board_render())
            
            score = _minimax(game = clone.clone(), depth = depth - 1, scoretrack = init_score)
            max_score = max(max_score, score)
            alpha = max(alpha, score)
            
            # print("State Score : ", max_score)
            # print("Player Score : ", clone.score())
            
            if beta <= alpha:
                return max_score
            
        return max_score
    else:
        min_score = math.inf
        # find the best move player two (AI)
        for idx in clone.valid_move():
            # print("--AI Turn--")
            
            clone.move(idx)
            
            # print("Chosen Idx: ", idx)
            # print(clone.moves())
            # print(clone.board_render())
            
            score = _minimax(game = clone.clone(), depth = depth - 1, scoretrack = init_score)
            min_score = min(score, min_score)
            beta = min(beta, score)
            
            # print("State Score : ", min_score)
            # print("Player Score : ", clone.score())
            
            if beta <= alpha:
                return min_score
            
        return min_score