from sys import stdin
import sys
sys.setrecursionlimit(1000000)

N, M = map(int, stdin.readline().split())
print(N, M)

paper = [list(map(int, stdin.readline().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]

def DFS(x, y):
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
    visit[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M  and visit[nx][ny] != 1:
            if paper[nx][ny] >= 1:
                paper[nx][ny] += 1
            elif paper[nx][ny] == 0:
                visit[nx][ny] =1
                DFS(nx, ny)
    return paper

def erase_n_count(paper):
    global N, M
    count =0
    for h in range(N):
        for k in range(M):
            if paper[h][k] !=0:
                count +=1
            if paper[h][k] >= 3:
                paper[h][k] = 0
            elif paper[h][k] ==2:
                paper[h][k] -= 1
            
    if count ==0:
        return False
    else:
        return True

answer =0
while (True):
    DFS(0,0)
    
    if not erase_n_count(paper):
        break
    answer +=1


    visit = [[0]*M for _ in range(N)]

print(answer)

"""
8 9
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 1 1 0
0 1 0 1 1 1 0 1 0
0 1 0 0 1 0 0 1 0
0 1 0 1 1 1 0 1 0
0 1 1 0 0 0 1 1 0
0 0 0 0 0 0 0 0 0    

"""