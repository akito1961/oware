import random
import math
from Game import Oware
from agent.minimax import bestmove

weight = [round(random.random(), 5) for _ in range(1000)]
weight.append(1)

def _rand_seq():
    seq = random.choices(weight, k = 5)
    
    return seq

def _fill_pool(pool, n):
    for i in range(n):
        pool[0].append(_rand_seq())
        pool[1].append(_eval(pool[0][i]))
        
    return pool

## evaluation func (win rates)
def _eval(seq):
    agent = 0
    test_round = 20

    for _ in range(test_round):
        playing = True
        oware = Oware()

        while playing:
        
            if len(oware.valid_move()) != 0:
                if oware.playerone(): # P1 makes a play. (random)
                    valid_idx = oware.valid_move()
                    move = random.choice(valid_idx)
                    
                else: # Agent makes a play. (Minimax)
                    clone = oware.clone()
                    move, score = bestmove(clone, weight_h = list(seq))
                
                oware.move(move)
            
            else:
                playing = False

        score = oware.score()

        if score[0] < score[1]:
            agent += 1
    
    return agent / test_round

def _prune_pool(pool, r):
    max = -math.inf
    min = math.inf
    
    for i in range(int(0.3 * len(pool[0]))):
        rate = pool[1][i]
        if rate > max:
            max = rate
        if rate < min:
            min = rate
    
    threshold = min + (r * (max - min))
    print(f"Min : {min}, Max : {max}, Threshold :{threshold}")
    
    new_pool = [[],
                []]
    
    for idx, seq in enumerate(pool[0]):
        eval_score = pool[1][idx]
        
        if eval_score >= threshold:
            new_pool[0].append(seq)
            new_pool[1].append(eval_score)
    
    return new_pool
    
def _mutate(seq):
    idx = random.randint(0, len(seq) - 1)
    seq[idx] = random.choice(weight)
    
    return seq

def _mutate_pool(pool, n):
    for _ in range(n):
        idx = random.randint(0, len(pool[0]) - 1)
        seq = pool[0][idx]
        m_seq = _mutate(seq)
        
        before = pool[1][idx]
        after = _eval(m_seq)
        
        if after > before:
            pool[0].append(m_seq)
            pool[1].append(after)
    
    return pool

def _crossover(seq1, seq2):
    p = random.randint(0, len(seq1) - 1)
    new_seq = []
    
    for i in range(len(seq1)):
        if i < p:
            new_seq.append(seq1[i])
        else:
            new_seq.append(seq2[i])
    
    return new_seq

def _crossover_pool(pool, n):
    for _ in range(n):
        idx1 = random.randint(0, len(pool[0]) - 1)
        idx2 = random.randint(0, len(pool[0]) - 1)
        seq1 = pool[0][idx1]
        seq2 = pool[0][idx2]
        new_seq = _crossover(seq1, seq2)
        
        before = max(pool[1][idx1], pool[1][idx2])
        after = _eval(new_seq)
        
        if after > before:
            pool[0].append(new_seq)
            pool[1].append(after)
    
    return pool


def GA(n:int):
    pool = [[],
            []]
    
    # [[],
    #         []]
    
    for round in range(n):
        
        pool = _fill_pool(pool, 20)
        print(f"After filling : {len(pool[0])}")
        
        pool = _mutate_pool(pool, 10)
        print(f"After mutation : {len(pool[0])}")
        
        pool = _crossover_pool(pool, 10)
        print(f"After Crossing over : {len(pool[0])}")
        
        pool = _prune_pool(pool, 0.8)
        print(f"After pruning : {len(pool[0])}")
    
        print(pool)
    
    text = []
    
    with open("result/weight_04182023.txt", "w") as file:
        for idx, line in enumerate(pool[0]):
            text.append(f"weight : {line} , score : {pool[1][idx]}\n")
        
        file.writelines(text)



GA(10)