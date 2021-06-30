import sys
sys.setrecursionlimit(10000)


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def dfs(x, y):
    visit[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and chu[nx][ny] ==1 and visit[nx][ny] != 1:
            visit[nx][ny] = 1
            dfs(nx, ny)


T = int(input())
for i in range(T):
    count =0
    M, N, K = map(int, input().split())
    chu = [[0]*M for _ in range(N)]
    visit = [[0]*M for _ in range(N)]

    for h in range(K):
        a, b = map(int, input().split())
        chu[b][a] = 1

    for j in range(N):
        for k in range(M):
            if chu[j][k] ==1 and visit[j][k] !=1:
                visit[j][k] =1
                dfs(j, k)
                count +=1

    print(count)