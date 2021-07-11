from sys import stdin
from collections import deque

N = int(stdin.readline())
num = int(stdin.readline())

com = [[0 for j in range(N)] for i in range(N)]
visit = [0] * N

for i in range(num):
    a, b = map(int, stdin.readline().split())
    com[a-1][b-1] = com[b-1][a-1] =1

queue = deque([0])
visit[0] =1
count = 0

while queue:
    a = queue.popleft()
    for i in range(N):
        if com[a][i] ==1 and visit[i] ==0:
            queue.append(i)
            visit[i] =1
            count +=1

print(count)
