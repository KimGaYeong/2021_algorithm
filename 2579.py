from sys import stdin

N = int(stdin.readline())
stair = [0 for _ in range(N+1)]
DP = [0 for _ in range(N+1)]

for i in range(N):
    stair[i] = int(stdin.readline())

if N==1:
    print(stair[0])
else:
    DP[0] = stair[0]
    DP[1] = stair[0] + stair[1]
    DP[2] = max(stair[1] + stair[2], stair[0] + stair[2])
    if N>=3:
        for i in range(3, N):
            DP[i] = max(DP[i-2]+stair[i], DP[i-3]+stair[i-1]+stair[i])

    print(DP[N-1])

    """
    * 계단이 1개인 것을 생각하는 것이 중요!

    """