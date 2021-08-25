from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)


N = int(stdin.readline())

numbers = list(map(int, stdin.readline().split()))

min = numbers.index(min(numbers))

DP1, DP2 = [0]* N, [0] * N # DP1 : 안뺀거, DP2 : 뺀거
DP1[0] = numbers[0]
DP2[0] = -999999999

for i in range(1, N):
    # 새로 시작하거나, 전단계에서 계속 더하거나
    DP1[i] = max(numbers[i], DP1[i-1]+numbers[i])
    DP2[i] = max(DP1[i-1], DP2[i-1]+numbers[i])
    # (새로 시작하거나, 전단계에서 계속 더한거거나), 전단계 그대로 가거나

answer = -999999999
for i in range(N):
    answer = max(answer ,DP1[i], DP2[i])

print(answer)

"""
연속합을 가장 빨리 풀 수 있는 방법은 DP    
"""