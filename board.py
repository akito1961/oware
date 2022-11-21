import os

def int_to_text(num:int) -> str:
    if num < 10:
        return " " + str(num)
    else:
        return str(num)


class Oware():
    # game inital setup
    def __init__(self):
        self.bin = [4,4,4,4,4,4,
                    4,4,4,4,4,4]
        self.playerOne = True
        
    # show current board command
    def board(self):
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
        
    # game reset
    def reset(self):
        self.bin = [4,4,4,4,4,4,
                    4,4,4,4,4,4]
        self.playerOne = True
        self.board()