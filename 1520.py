from  sys import stdin
import sys
sys.setrecursionlimit(10000)

"""
    python에서는 재귀 호출 횟수를 제한하고 있기 때문에
    default로 설정되어있는 1000번의 호출 횟수를 넘어서면 런타임 에러가 발생한다.
    
    기본 재귀 호출 횟수를 늘려주면 해결할 수 있다.

    import sys
    sys.setrecursionlimit(10000)
"""

M, N = map(int, stdin.readline().split())
lowmap = [list(map(int, stdin.readline().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

def solution(x, y):

    print("현재 장소는 (", x, ",", y, ")")

    if x==0 and y==0:
        return 1

    if dp[x][y] == -1:
        dp[x][y] =0
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if lowmap[x][y] < lowmap[nx][ny]:
                    dp[x][y] += solution(nx, ny)
    
    return dp[x][y]

print(solution(M-1, N-1))