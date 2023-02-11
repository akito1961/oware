from Game import Oware
from agent.minimax import bestmove
from random import choice

# clear console stuff
from IPython.display import display, clear_output
import sys

P1 = 0
agent = 0
tie = 0

result = ""


for round in range(10):
    playing = True
    oware = Oware()

    while playing:
        
        clear_output(wait=True)
        
        print(f"[Epoch {round + 1: >2} / 10]")

        print(oware.board_render())
        print("P1 Score : ", oware.score()[0], ", AI score : ", oware.score()[1])
        print("Move History : ", oware.moves())

        if len(oware.valid_move()) != 0:
            if oware.playerone():
                valid_idx = oware.valid_move()
                move = choice(valid_idx)
            else:
                clone = oware.clone()
                move = bestmove(clone)
            
            oware.move(move)
            print("Chosen move : ", move)
            print("Move History : ", oware.moves())
        
        else:
            playing = False
        
        sys.stdout.flush()
    
    result += "[Epoch {0: >2} /10]\n".format(round + 1)
    result += "P1 Score : {0: >2}, AI score : {1: >2}\n".format(oware.score()[0], oware.score()[1])
    result += "Move History : {}\n\n".format(oware.moves())
    score = oware.score()
    
    if score[0] > score[1]:
        P1 += 1
    
    if score[0] == score[1]:
        tie += 1
    
    if score[0] < score[1]:
        agent += 1
    
    print(result)


result += "P1 wins: {0: >2}, Tie : {1: >2}, Agent wins : {2: >2}".format(P1, tie, agent)
print(result)
# print(oware.score())
# print("P1 Score : ", oware.score()[0], ", AI score : ", oware.score()[1])
# print("Move History : ", oware.moves())

with open("result.txt", "w") as f:
    f.write(result)