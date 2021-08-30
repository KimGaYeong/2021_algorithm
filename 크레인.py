board= [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves= [1, 5, 3, 5, 1, 2, 5, 1, 4, 3]
result: 8

import sys
sys.setrecursionlimit(10**9)

def solution(board, moves):
    answer = 0
    box, baguni = [], []
    for i in range(len(board)):
        sub = []
        for line in board:
            if line[i] != 0:
                sub.append(line[i])
        box.append(sub)
    
    exsub, sub = 0, 0
    for i in range(len(moves)):

        position = moves[i]-1
        if box[position]:
            sub = box[position].pop(0)
            print(baguni)
            if exsub == sub:
                baguni.pop(-1)
                if baguni:
                    exsub = baguni[-1]
                else:
                    exsub =0
                answer +=1
                #print(baguni)
            else:
                baguni.append(sub)
                if baguni:
                    exsub = baguni[-1]
                else:
                    exsub =0
            #print("sub, ex", sub, exsub)
        else:
            pass
    
    print(answer*2)
    return answer*2

solution(board, moves)