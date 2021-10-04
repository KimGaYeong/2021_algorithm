from sys import stdin

N, K = map(int, stdin.readline().split())
yo = list(i for i in range(1, N+1))

result = []
now = 0 #now : 현재 위치를 나타냄

while len(yo) >1 :
    now += K
    if now > len(yo):
        now = now % len(yo)
        if now ==0:
            now = now + len(yo)
    
    now -= 1
    result.append(yo.pop(now))

print("<", end = "")
for i in range(len(result)):
    print(result[i], end = ", ")
print(yo.pop(), end = "")
print(">")