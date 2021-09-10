from sys import stdin
from bisect import bisect_left

N = int(stdin.readline())
jbd = list(map(int, stdin.readline().split()))

#print(jbd)

DP = []
sub = []
for i in range(N):
    if not DP or jbd[i] > DP[-1]:
        DP.append(jbd[i])
        sub.append((len(DP)-1, jbd[i]))
    else:
        idx = bisect_left(DP, jbd[i])
        # idx = DP에 들어갔을 때 몇 뻔째 위치에 놓여 있는지
        DP[idx] = jbd[i]
        sub.append((idx, jbd[i]))
    #print(sub)

L_idx = len(DP)-1 
answer = []

for i in range(N-1, -1, -1):
    if sub[i][0] == L_idx:
        answer.append(sub[i][1])
        L_idx -=1

print(N - len(answer))