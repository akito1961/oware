import random
import math
from Game import Oware
from agent.minimax import bestmove

weight = [round(random.random(), 5) for _ in range(1000)]

def _rand_seq():
    seq = []
    for i in range(5):
        seq.append(random.choice(weight))
    
    return seq

def _fill_pool(pool, n):
    for i in range(n):
        pool.append(_rand_seq())
        
    return pool

def _eval(seq):
    P1 = 0
    agent = 0
    tie = 0

    test_round = 10


    for round in range(test_round):
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

        if score[0] > score[1]:
            P1 += 1

        if score[0] == score[1]:
            tie += 1

        if score[0] < score[1]:
            agent += 1
    
    return agent / test_round

def _prune_pool(pool, r):
    max = -math.inf
    min = math.inf
    
    for i in range(int(0.3 * len(pool))):
        rate = _eval(pool[i])
        if rate > max:
            max = rate
        if rate < min:
            min = rate
    
    threshold = min + (r * (max - min))
    
    new_pool = []
    
    for seq in pool:
        eval_string = _eval(seq)
        
        if eval_string >= threshold:
            new_pool.append(seq)
    
    return new_pool
    
def _mutate(seq):
    idx = random.randint(0, len(seq) - 1)
    seq[idx] = random.choice(weight)
    
    return seq

def _mutate_pool(pool, n):
    for i in range(n):
        seq = random.choice(pool)
        m_seq = _mutate(seq)
        
        before = _eval(seq)
        after = _eval(m_seq)
        
        if after > before:
            pool.append(m_seq)
    
    return pool

def _crossover(seq1, seq2):
    p = random.randint(0, len(seq1) - 1)
    new_seq = []
    
    for i in range(len(seq1)):
        if i < p:
            new_seq.append(seq1)
        else:
            new_seq.append(seq2)
    
    return new_seq

def _crossover_pool(pool, n):
    for i in range(n):
        seq1 = random.choice(pool)
        seq2 = random.choice(pool)
        new_seq = _crossover(seq1, seq2)
        
        before = max(_eval(seq1), _eval(seq2))
        after = _eval(new_seq)
        
        if after > before:
            pool.append(new_seq)
    
    return pool


def GA(n:int):
    pool = []
    for round in range(n):
        
        pool = _fill_pool(pool, 30)
        print(f"After filling : {len(pool)}")
        
        pool = _mutate_pool(pool, 10)
        print(f"After mutation : {len(pool)}")
        
        pool = _crossover_pool(pool, 10)
        print(f"After Crossing over : {len(pool)}")
        
        pool = _prune_pool(pool, 0.8)
        print(f"After pruning : {len(pool)}")
    
    with open("result/weight_03272023.txt", "w") as file:
        file.write(pool)



GA(10)