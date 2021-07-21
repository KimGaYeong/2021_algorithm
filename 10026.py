from sys import stdin
import sys
sys.setrecursionlimit(10000)

"""
------------------------------------
import sys
sys.setrecursionlimit(10000)
------------------------------------
위 두 줄의 코드를 추가하지 않은면 Runtime error (recursion 오류)가 난다.

Python에서는 재귀 호출의 깊이가 1000 이상으로 늘어나는 것을 막고 있다.
따라서 default값으로 설정된 "1000"의 재귀 호출 깊이를 늘려주면 된다.

위 코드는 임의로 재귀 호출 횟수를 늘려주는 것이다.
"""


N = int(stdin.readline())
paint = [list(stdin.readline().rstrip()) for _ in range(N)]
visit = [[0]*N for _ in range(N)]

case1, case2 = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

def DFS(x, y):

    visit[x][y] = 1
    RGBcolor = paint[x][y] # 현재 color

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<N and 0<=ny<N:
            if paint[nx][ny] == RGBcolor and visit[nx][ny] != 1:
                DFS(nx, ny)

for i in range(N):
        for j in range(N):
            if visit[i][j] ==0:
                DFS(i, j)
                case1 +=1


for i in paint:
    for j in range(N):
        if i[j] == "R":
            i[j] = "G"

visit = [[0]*N for _ in range(N)]

for i in range(N):
        for j in range(N):
            if visit[i][j] ==0:
                DFS(i, j)
                case2 +=1

print(case1, case2)

