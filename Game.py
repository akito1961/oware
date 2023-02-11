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
                 playerOne = None,
                 history = None,
                 moves = None,
                 scoretrack = None):
        
        self._board = list(Oware._default_board) if board is None else list(board)
        self._playerOne = True if playerOne is None else (playerOne == True)
        self._scoretrack = [0, 0] if scoretrack is None else list(scoretrack)
        self.playerOne_score = self._scoretrack[0]
        self.playerTwo_score = self._scoretrack[1]
        
        # move & board records
        self._moves = [] if moves is None else list(moves)
        self._history = [] if history is None else list(history)
        
    
    ## accessory functions
    def score(self):
        return self._scoretrack
    
    def playerone(self):
        return self._playerOne
    
    def moves(self):
        return self._moves
    
    def history(self):
        return self._history

    def board(self):
        return self._board

    def valid_move(self) -> list:
        _valid_idx = []
        for idx in range(len(self._board)):
            if self._board[idx] != 0 and Oware.own_zone(idx, self._playerOne) and not self.giveop_chance(idx):
                _valid_idx.append(idx)
        
        return _valid_idx
    
    def clone(self):
        return Oware(
            board = list(self.board()),
            playerOne = self.playerone(),
            history = list(self.history()),
            moves = list(self.moves()),
            scoretrack = list(self.score())
        )
    
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

    
    """giving opponent moves if possible"""
    def giveop_chance(self, idx: int):
        if self._playerOne:
            return self.isside_empty() and idx + self._board[idx] < 6
        else:
            return self.isside_empty() and idx + self._board[idx] < 12
    
    def over(self):
        return self._scoretrack[0] >= 25 or self._scoretrack[1] >= 25
    # give chance rule is moved to move()

    
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
        
        if self.over():
            return self.score()
        
        ## Illegal move
        
        # empty idx
        if self._board[idx] == 0:
            return self.score()
        
        # choose opposing idx
        if not Oware.own_zone(idx, self._playerOne):
            return self.score()
        
        # give chance [consider only if one side is empty and the other has a move that can distribute stones to]
        if self.giveop_chance(idx):
            return self.score()
        
        self._moves.append(idx)
        self._history.append(self.board())
        
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
                self._scoretrack[0] += self._board[current_idx]
                self._board[current_idx] = 0
                
            if not self._playerOne and not Oware.own_zone(current_idx, self._playerOne):
                self._scoretrack[1] += self._board[current_idx]
                self._board[current_idx] = 0
            
            current_idx = (current_idx - 1) % len(self._board)
            
        ## End game detection
        if self.over() or self.valid_move() == []:
            self._scoretrack[0] += sum(self._board[0:6])
            self._scoretrack[1] += sum(self._board[6:12])
            self._board[0:6] = [0, 0, 0, 0, 0, 0]
            self._board[6:12] = [0, 0, 0, 0, 0, 0]
            
        
        self._playerOne = not self._playerOne

        return 0