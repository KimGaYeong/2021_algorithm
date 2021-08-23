from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10**9)

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
n = int(stdin.readline())
forest = [list(map(int, stdin.readline().split())) for _ in range(n)]
visit = [ [-1] * n for _ in range(n)]

print(visit)
def DFS(x, y):
    if visit[x][y] <0:
        visit[x][y] =0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(0 <= nx < n and 0 <= ny < n and forest[nx][ny]> forest[x][y]):
                visit[x][y] = max(visit[x][y], DFS(nx, ny))
        visit[x][y] +=1

    return visit[x][y]

sub = 0
for i in range(n):
    for j in range(n):
        sub = max(sub, DFS(i, j))

print(sub)
