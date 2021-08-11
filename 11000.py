from sys import stdin
import sys
sys.setrecursionlimit(1000000)

N = int(stdin.readline())
classnet = [[0]*2 for i in range(N)]
DP = [1] * N

for i in range(N):
    classnet[i][0], classnet[i][1] = map(int, stdin.readline().split())

classnet = sorted(classnet, key = lambda x : x[0:N][0])

print(classnet)
for i in range(1, N):
    for j in range(i):
        if classnet[i][0] >= classnet[j][1]:
            DP[i] = max(DP[i-1], DP[j]+1)


print(max(DP))

