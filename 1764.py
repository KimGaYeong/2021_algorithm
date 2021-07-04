from sys import stdin

N, M = map(int, stdin.readline().split())

d, b = set(), set()
count =0
for i in range(N):
    d.add(input())

for i in range(M):
    b.add(input())


lan = len(d&b)
answer = sorted(list(d&b))
print(lan)
for i in range(lan):
    print(answer[i])
