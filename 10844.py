from sys import stdin
import sys
sys.setrecursionlimit(1000000)

N = int(stdin.readline())
DP = [[0]*10 for _ in range(101)]
# DP[i][j] = 길이가 i고 마지막 숫자가 j인 애들의 개수?

for i in range(1, 10):
    DP[1][i] =1

for i in range(2, N+1):
    for j in range(10):
        if j==0:
            DP[i][j] = DP[i-1][1]
        elif 1 <= j <= 8:
            DP[i][j] = (DP[i-1][j-1] + DP[i-1][j+1])
        else: #9
            DP[i][j] = DP[i-1][8]

print(sum(DP[N]) % 1000000000)