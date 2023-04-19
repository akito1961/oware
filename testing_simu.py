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
score_dict = {}

test_round = 100


for round in range(test_round):
    playing = True
    oware = Oware()
    
    score_track = []

    while playing:
        
        clear_output(wait=True)
        
        print(f"[Epoch {round + 1: >2}/{test_round: >2}]")

        print(oware.board_render())
        print("P1 Score : ", oware.score()[0], ", AI score : ", oware.score()[1])
        print("Move History : ", oware.moves())
        print("P1 wins: {0: >2}, Tie : {1: >2}, Agent wins : {2: >2}".format(P1, tie, agent))

        if len(oware.valid_move()) != 0:
            if oware.playerone(): # P1 makes a play. (random)
                valid_idx = oware.valid_move()
                move = choice(valid_idx)
                
            else: # Agent makes a play. (Minimax)
                clone = oware.clone()
                move, score = bestmove(clone, weight_h= [0.21181, 0.28749, 0.1347, 0.27368, 0.39376])
                score_track.append(score)
            
            oware.move(move)
            print("Chosen move : ", move)
            print("Move History : ", oware.moves())
        
        else:
            playing = False
        
        sys.stdout.flush()
    
    result += "[Epoch {0: >2}/{1: >2}]\n".format(round + 1, test_round)
    result += "P1 Score : {0: >2}, AI score : {1: >2}\n".format(oware.score()[0], oware.score()[1])
    result += "Move History : {}\n".format(oware.moves())
    result += "Score Track : {}\n\n".format(score_track)
    score = oware.score()
    
    if score[0] > score[1]:
        P1 += 1
    
    if score[0] == score[1]:
        tie += 1
    
    if score[0] < score[1]:
        agent += 1
    
    score_dict[round] = list(score_track)


result += "P1 wins: {0: >2}, Tie : {1: >2}, Agent wins : {2: >2}".format(P1, tie, agent)
print(result)
# print(oware.score())
# print("P1 Score : ", oware.score()[0], ", AI score : ", oware.score()[1])
# print("Move History : ", oware.moves())

with open("result/weight_set5_r3_04192023.txt", "w") as f:
    f.write(result)
