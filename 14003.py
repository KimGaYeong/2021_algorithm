from sys import stdin
from bisect import bisect_left

N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))

DP = []
sub = []
for i in range(N):
    if not DP or A[i] > DP[-1]:
        DP.append(A[i])
        sub.append((len(DP)-1, A[i]))
    else:
        idx = bisect_left(DP, A[i])
        # idx = DP에 들어갔을 때 몇 뻔째 위치에 놓여 있는지
        DP[idx] = A[i]
        sub.append((idx, A[i]))
    print(sub)

L_idx = len(DP)-1 
answer = []

for i in range(N-1, -1, -1):
    if sub[i][0] == L_idx:
        answer.append(sub[i][1])
        L_idx -=1

print("answer", answer)
# [50, 30, 20, 10]
print("len answer", len(answer))
# 4
print("reversed answer", answer[::-1])
# [10, 20, 30, 50]
print("*reversed answer", *reversed(answer))
# 10 20 30 50

