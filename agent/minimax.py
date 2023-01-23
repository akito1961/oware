
"""
    step to build an minimax ai
    - get board position
    - decide whos turn it is
        -- if player turn, pick a maximum score
        -- if ai turn, pick a minimum score
    - repeat for the search
"""

import math

class MiniMax():
    # def __init__(self, depth:int = 4):
    #     self._depth = depth
        
    def _minimax(self):
        pass
    
##########################################################
    
def Minimax(game, depth:int = 4):

    p1_validmove = [True, True, True, True, True, True,
                    False, False, False, False, False, False]
    p2_validmove = [False, False, False, False, False, False,
                    True, True, True, True, True, True]

    clone = game.clone()

    maximizer = clone.playerone()

    if maximizer:
        pass
    
    if depth == 0: # or game end
        pass # return score
    
    if maximizer:
        best_score = -math.inf
        # for move in