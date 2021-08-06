from sys import stdin

N, K = map(int, stdin.readline().split())
coin = []
for i in range(N):
    coin.insert(0, int(stdin.readline()))

answer = 0

for i in range(N):
    answer += K // coin[i]
    K  = K % coin[i]


print(answer)