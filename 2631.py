from sys import stdin

N = int(stdin.readline())
line = [0] * N
DP = [1] * N

for i in range(N):
    line[i] = int(stdin.readline())

for i in range(1, N):
    for j in range(i):
        if line[i] > line[j]:
            DP[i] = max(DP[i], DP[j]+1)

print(N-max(DP))