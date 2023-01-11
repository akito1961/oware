"""
Structure Design
- caculatable board
- valid move checker
- score counter
- rules validation
"""

# import os

class Oware():
    """inital setup"""
    _default_board = [4, 4, 4, 4, 4, 4,
                      4, 4, 4, 4, 4, 4]
    
    def __init__(self):
        self._board = Oware._default_board
        self._playerOne = True
        self.playerOne_score = 0
        self.playerTwo_score = 0
        
        # move records
        self._moves = []
    
    ## accessory functions
    def score(self):
        return "Player one : {0: >2} || Player two : {1: >2}".format(self.playerOne_score, self.playerTwo_score)
    
    def playerone_turn(self):
        return self._playerOne
    
    def moves(self):
        return self._moves
    
    def clone(self):
        return
    
    
    """rendering pretty board"""
    def board_render(self):
        result = "+----+----+----+----+----+----+\n"
        result += "| {0: >2} | {1: >2} | {2: >2} | {3: >2} | {4: >2} | {5: >2} |\n".format(
            self._board[11], self._board[10], self._board[9], self._board[8], self._board[7], self._board[6])
        result += "+----+----+----+----+----+----+\n"
        result += "| {0: >2} | {1: >2} | {2: >2} | {3: >2} | {4: >2} | {5: >2} |\n".format(
            self._board[0], self._board[1], self._board[2], self._board[3], self._board[4], self._board[5])
        result += "+----+----+----+----+----+----+\n"
        
        return result
    
    
    """check if the game is over"""
    def side_empty(self):
        playerone_stones_left = sum(self._board[0:6])
        playertwo_stone_left = sum(self._board[6:12])
        return playerone_stones_left == 0 or playertwo_stone_left == 0
    
    def over(self):
        if self.side_empty():
            pass
        
    
    """check for zone owner"""
    @staticmethod
    def playerOne_idx(idx):
        return idx <= 5 and idx >= 0
    
    @staticmethod
    def playerTwo_idx(idx):
        return idx <= 11 and idx >= 6
    
    @staticmethod
    def own_zone(idx, playerOne):
        if playerOne:
            return Oware.playerOne_idx(idx)
        else:
            return Oware.playerTwo_idx(idx)
    
    
    """moving stone + rule checker"""
    def move(self, idx):
        # move stones
        giveaway = self._board[idx]
        self._board[idx] = 0
        current_idx = idx
        
        # initializing the giveaway
        while giveaway > 0:
            current_idx = (current_idx + 1) % len(self._board)
            
            # skip the chosen idx
            if current_idx == idx:
                current_idx = (current_idx + 1) % len(self._board)
                
            self._board[current_idx] += 1
            giveaway -= 1
            
        # capture rule
        
    