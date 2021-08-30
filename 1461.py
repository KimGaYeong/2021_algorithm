# 도서관

from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

N, M = map(int, stdin.readline().split())
position = list(map(int, stdin.readline().split()))
minus, plus = [], []

for i in range(N):
    if position[i] > 0 :
        plus.append(position[i])
    else:
        minus.append(abs(position[i]))

minus = sorted(minus, reverse= True)
plus = sorted(plus)

print(minus, plus)

result = []
i=0
while i < len(minus):
    if i==0:
        for j in range(i, i+M-1):
            result.append(minus[j]-minus[j+1])
        result.append(minus[i+M-1])
    else:
        
    i += M
    print(result)
position = sorted(position, key = lambda x : x)
