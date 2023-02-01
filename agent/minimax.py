
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
    best_score = -math.inf
    best_move = None
    
    valid_move = clone.valid_move()
    
    if len(valid_move) != 0:
        for idx in valid_move:
            score = _minimax(clone)
            if score > best_score:
                best_score = score
                best_move = idx
                
    if best_move is not None:
        return best_move
        
    
def _minimax(game, depth:int = 8, alpha = -math.inf, beta = math.inf):

    clone = game.clone()

    maximizer = clone.playerone()
    
    if depth == 0 or clone.valid_move() == []: # or game end
        score = clone.score()
        # print("---------- End Leaf Node ----------\n")
        return score[0] - score[1] # return diff score (p1 - p2)
    
    if maximizer:
        max_score = -math.inf
        # find the best move for player one
        for idx in clone.valid_move():
            # print("--P1 Turn--")
            
            clone.move(idx)
            
            # print("Chosen Idx: ", idx)
            # print(clone.moves())
            # print(clone.board_render())
            
            score = _minimax(clone.clone(), depth - 1)
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
            
            score = _minimax(clone.clone(), depth - 1)
            min_score = min(score, min_score)
            beta = min(beta, score)
            
            # print("State Score : ", min_score)
            # print("Player Score : ", clone.score())
            
            if beta <= alpha:
                return min_score
            
        return min_score