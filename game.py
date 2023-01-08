"""
Structure Design
- caculatable board
- valid move checker
- score counter
- rules validation
"""

# import os

def int_to_text(num:int) -> str:
    if num < 10:
        return " " + str(num)
    else:
        return str(num)


class Oware():
    ## game inital setup
    _default_board = [4, 4, 4, 4, 4, 4,
                      4, 4, 4, 4, 4, 4]
    
    def __init__(self):
        self.bin = Oware._default_board
        self.playerOne = True
        self.playerOne_score = 0
        self.playerTwo_score = 0
        
    # show current board command
    def board_render(self):
        # os.system("cls")
        if not(self.playerOne):
            print("   f    e    d    c    b    a")
        
        print("+----+----+----+----+----+----+")
        print("| "+ int_to_text(self.bin[11]) +" | "+ int_to_text(self.bin[10]) +" | "+ int_to_text(self.bin[9]) +
              " | "+ int_to_text(self.bin[8]) +" | "+ int_to_text(self.bin[7]) +" | "+ int_to_text(self.bin[6]) +" |")
        print("+----+----+----+----+----+----+")
        print("| "+ int_to_text(self.bin[0]) +" | "+ int_to_text(self.bin[1]) +" | "+ int_to_text(self.bin[2]) +
              " | "+ int_to_text(self.bin[3]) +" | "+ int_to_text(self.bin[4]) +" | "+ int_to_text(self.bin[5]) +" |")
        print("+----+----+----+----+----+----+")
        
        if self.playerOne:
            print("   a    b    c    d    e    f")
            
        print
        
    # game reset
    def reset(self):
        self.bin = [4,4,4,4,4,4,
                    4,4,4,4,4,4]
        self.playerOne = True
        self.board()