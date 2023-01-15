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
    
    def __init__(self,
                 board = None,
                 playerOne = None):
        
        self._board = list(Oware._default_board) if board is None else board
        self._playerOne = True if playerOne is None else (playerOne == True)
        self.playerOne_score = 0
        self.playerTwo_score = 0
        
        # move records
        self._moves = []
        self._history = []
        
    
    ## accessory functions
    def score(self):
        return (self.playerOne_score, self.playerTwo_score)
    
    def playerone_turn(self):
        return self._playerOne
    
    def moves(self):
        return self._moves
    
    def history(self):
        return self._history
    
    # def clone(self):
    #     return 0
    
    # def score_board(self):
    #     text_score = "Player one : {0: >2} || Player two : {1: >2}".format(self.score())
    #     return text_score
    
    
    """rendering pretty board"""
    def board_render(self) -> str:
        result = "+----+----+----+----+----+----+\n"
        result += "| {0: >2} | {1: >2} | {2: >2} | {3: >2} | {4: >2} | {5: >2} |\n".format(
            self._board[11], self._board[10], self._board[9], self._board[8], self._board[7], self._board[6])
        result += "+----+----+----+----+----+----+\n"
        result += "| {0: >2} | {1: >2} | {2: >2} | {3: >2} | {4: >2} | {5: >2} |\n".format(
            self._board[0], self._board[1], self._board[2], self._board[3], self._board[4], self._board[5])
        result += "+----+----+----+----+----+----+\n"
        
        return result
    
    
    """check if the game is over"""
    def isside_empty(self):
        playerone_stones_left = sum(self._board[0:6])
        playertwo_stone_left = sum(self._board[6:12])
        return playerone_stones_left == 0 or playertwo_stone_left == 0
    
    def over(self):
        return self.playerOne_score >= 25 or self.playerTwo_score >= 25
    # give chance rule is moved to move()
    
    
    """giving opponent moves if possible"""
    def giveop_chance(self, idx: int):
        if self._playerOne:
            return self.isside_empty() and idx + self._board[idx] >= 6
        else:
            return self.isside_empty() and idx + self._board[idx] >= 12
        
    
    """check for zone owner"""
    @staticmethod
    def playerOne_idx(idx: int):
        return idx <= 5 and idx >= 0
    
    @staticmethod
    def playerTwo_idx(idx: int):
        return idx <= 11 and idx >= 6
    
    @staticmethod
    def own_zone(idx: int, playerOne):
        if playerOne:
            return Oware.playerOne_idx(idx)
        else:
            return Oware.playerTwo_idx(idx)
    
    
    """moving stone + rule checker"""
    def move(self, idx):
        ## Illegal move
        
        # empty idx
        if self._board[idx] == 0:
            return self.score()
        
        # choose opposing idx
        if not Oware.own_zone(idx, self._playerOne):
            return self.score()
        
        # give chance
        if self.giveop_chance(idx):
            return self.score()
        
        self._moves.append(idx)
        
        # move stones
        giveaway = self._board[idx]
        self._board[idx] = 0
        current_idx = idx
        
        
        ## Initializing the giveaway
        while giveaway > 0:
            current_idx = (current_idx + 1) % len(self._board)
            
            # skip the chosen idx
            if current_idx == idx:
                continue
                
            self._board[current_idx] += 1
            giveaway -= 1
            
        ## Capture rule
        while self._board[current_idx] in [2,3]:
            # distribute stones to the corresponding player
            if self._playerOne and not Oware.own_zone(current_idx, self._playerOne):
                self.playerOne_score += self._board[current_idx]
                self._board[current_idx] = 0
                
            if not self._playerOne and not Oware.own_zone(current_idx, self._playerOne):
                self.playerTwo_score += self._board[current_idx]
                self._board[current_idx] = 0
            
            current_idx = (current_idx - 1) % len(self._board)
            
        ## End game detection
        if self.over():
            self.playerOne_score += sum(self._board[0:6])
            self.playerTwo_score += sum(self._board[6:12])
            self._board[0:6] = [0, 0, 0, 0, 0, 0]
            self._board[6:12] = [0, 0, 0, 0, 0, 0]
            
        
        self._playerOne = not self._playerOne