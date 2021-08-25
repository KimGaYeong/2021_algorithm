
# 2 15
# 3 2 1 2 1 2 1 2 1 3 3 3 3 3 3

from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10**9)

N, K = map(int, stdin.readline().split())
order = list(map(int, stdin.readline().split()))

tap = []
count =0
sub =0
max, maxcount = 0, 0
for i in range(K):

    #print(i, "st plug is", tap)
    if order[i] in tap : # 꽂아야 할 애가 이미 꽂혀있음
        pass

    elif len(tap) <N: # 멀티탭이 아직 다 안 찬 상태
        tap.append(order[i])
    
    elif len(tap) ==N: # 멀티탭이 다 찬 상태
        for j in range(N):
            if tap[j] not in order[i:]: # 꽂혀있는 애들 중 나중에 안쓰이는 애가 있음
                maxcount = j
                break
            elif order[i:].index(tap[j]) > sub: # 꽂혀있는 애들이 쓰이는 애들
                # 제일 나중에 쓰일 애들 지워야함!
                sub = order[i:].index(tap[j])
                maxcount = j
        tap.pop(maxcount)
        tap.append(order[i])
        sub, maxcount =0, 0
        count +=1
    
print(count)