import sys
sys.setrecursionlimit(1000000)

def solution(N, stages):
    loserate, answer = [], []
    for i in range(1, N+1):
        ooox = 0
        ox = stages.count(i)
        for j in range(len(stages)):
            if stages[j] >= i:
                ooox +=1
        
        if not ooox ==0:
            loserate.append([i, ox/ooox])
        else:
            loserate.append([i, 0])
    loserate = sorted(loserate, key = lambda x : x[1], reverse = True)
    
    for i in loserate:
        answer.append(i[0])

    return answer

N1, stages1 = 5, [2, 1, 2, 6, 2, 4, 3, 3]
N2, stages2 = 4, [4, 4, 4, 4, 4]

solution(N1, stages1)
solution(N2, stages2)