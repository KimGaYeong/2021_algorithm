from sys import stdin
from bisect import bisect_left

N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))

DP = [A[0]]

for i in range(N):
    if A[i] > DP[-1]: # 현재 수열의 마지막 수보다 더 큰 값을 찾았어!
        DP.append(A[i])
    else:
        idx = bisect_left(DP, A[i]) # 
        DP[idx] = A[i]

print(len(DP))