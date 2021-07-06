N, M = map(int, input().split())
friend = [[0]*(N+1) for i in range(N+1)]
num = []
for i in range(M):
    a, b = map(int, input().split())
    friend[a][b] = friend[b][a] =1

def Find(a):

    visit = [0] * (N + 1)
    queue = [a]
    visit[a] =1
    while queue:
        a = queue.pop(0)
        for i in range(1, N+1):
            if friend[a][i] ==1 and visit[i] ==0 :
                visit[i] = visit[a]+1
                queue.append(i)
    for i in range(1, N+1):
        visit[i] -=1
    return sum(visit)


for i in range(1, N+1):
    num.append(Find(i))

print(num.index(min(num))+1)