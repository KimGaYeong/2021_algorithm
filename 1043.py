# 거짓말

from sys import stdin

N, M = map(int, stdin.readline().split())
T = list(map(int, stdin.readline().split()))

if T[0] ==0:
    truth, truth_1 = T[0], []
else:
    truth, truth_1 = T[0], T[1:]

truth_2 = []
li = []
count = M
for i in range(M):
    sub = list(map(int, stdin.readline().split()))
    li.append(sub[1:])
print("li", li)
print("truth_1", truth_1)

while(truth_1):
    truthman = truth_1.pop()
    truth_2.append(truthman)
    for i in range(M):
        if truthman in li[i]:
            for j in range(len(li[i])):
                if not li[i][j] in truth_1 and not li[i][j] in truth_2:
                    truth_1.append(li[i][j])
    
print("truth_2", truth_2)

for i in range(M):
    for j in range(len(truth_2)):
        if truth_2[j] in li[i]:
            count -=1
            break

print(count)
