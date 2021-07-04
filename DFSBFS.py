
N, M= map(int, input().split())
nlist = [[0] * (N+1) for i in range(N+1)]
visit = [0] * (N+1)
count = [[0] * (N+1) for i in range(N+1)]

for i in range(M):
    a,b = map(int, input().split())
    nlist[a][b] =1
    nlist[b][a] =1


def BFS(a, b):
    queue = [a]
    visit[a] =1
    while queue:
        a = queue.pop(0)
        count[i] +=1
        for i in range(N+1):
            if(nlist[a][i] ==1 and visit[i] !=1):
                queue.append(i)
                visit[i]=1

for i in range(1, N+1):
    for j in range(1, N+1):
        BFS(a, b)


