from sys import stdin

from bisect import bisect_left

N = int(stdin.readline())
line = list(map(int, stdin.readline().split()))
DP = [line[0]]

for i in range(1, N):
    if line[i] > DP[-1]:
        DP.append(line[i])
    else:
        DP[bisect_left(DP, line[i])] = line[i]

print(len(DP))

"""
시간 초과 코드

for i in range(1, N):
    for j in range(i):
        if line[i] > line[j]:
            DP[i] = max(DP[i], DP[j]+1)

print(max(DP))
"""
# 선형이꺼의 줄세우기와 비슷하지만 for문 2개로 만드는 가장 긴 증가하는 부분 수열 코드로 돌리면
# 시간 초과가 남 ------------>> 이분 탐색을 이용해야 되구나...
# 이분 탐색을 직접 구현한다면 O(logN)

"""
-> c++의 lower_bound와 같음 (오름차순)
bisect_left(data, insert data, find start idx(0), len(data))
"""