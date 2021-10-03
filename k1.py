
i1 = ["muzi", "frodo", "apeach", "neo"]
r1 = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k1 = 2


i2 = ["con", "ryan"]
r2 = ["ryan con", "ryan con", "ryan con", "ryan con"]
k2 = 3

from sys import setrecursionlimit
setrecursionlimit(10**9)

def solution(id_list, report, k):
    answer = []
    rlist = []
    black = []

    sre = set(report)
    report = list(sre)
    ks = []

    for i in range(len(id_list)):
        rlist.append([id_list[i], [], 0])

    for r in range(len(report)):
        sub = report[r].split()
        ks.append(sub[1])

        for j in rlist:
            if sub[0] == j[0]:
                j[1].append(sub[1])

    for i in id_list:
        if ks.count(i) >= k:
            black.append(i)
    
    num = 0
    for r in rlist:
        for b in black:
            if num == len(report):
                break
            if b in r[1]:
                r[2]+=1
                num +=1
        answer.append(r[2])
    
    print(answer)
    return answer

solution(i1, r1, k1)



"""
from sys import setrecursionlimit
setrecursionlimit(10**9)

def solution(id_list, report, k):
    answer = []
    rlist = []
    black = []
    
    sre = set(report)
    report = list(sre)
    
    for i in range(len(id_list)):
        rlist.append([id_list[i], [], 0, 0])

    for r in range(len(report)):
        sub = report[r].split()
        for j in rlist:
            if sub[0] == j[0] and sub[1] not in j[1]:
                j[1].append(sub[1])
    
    
    for r in rlist:
        for j in rlist:
            if j[0] != r[0] and j[0] in r[1]:
                j[3]+=1

    for i in rlist:
        if i[3] >= k:
            black.append(i[0])
    
    for r in rlist:
        for b in black:
            if b in r[1]:
                r[2]+=1
        answer.append(r[2])
    
    return answer    

"""