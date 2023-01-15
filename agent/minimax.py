
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
    def __init__(self, depth:int = 4):
        self._depth = depth
        
    def _minimax(self):
        pass
    
##########################################################
    
def Minimax(pos, depth:int = 4):
    if depth == 0: # or game end
        pass # return score
    
    # if playerOne:
    #     best_score = -math.inf