from sys import stdin

N = int(stdin.readline())
li = list(map(str, stdin.readline().split()))
length = 0
for i in range(N):
    if len(li[i]) > length:
        length = len(li[i])

for i in range(N):
    sub = li[i]
    lenl = len(li[i])
    if lenl < length:
        for j in range(length-lenl):
            li[i] += li[i][0]
        
    li[i] = [li[i], i, sub]

print(li)

li = sorted(li, key = lambda x : x[0][0:length], reverse=True)
print(li)
answer = []
lsum = []
for i in range(N):
    lsum.append(int(li[i][2]))
    answer.append(li[i][2])

if (sum(lsum)) ==0:
    print(0)
else:
    print("".join(answer))