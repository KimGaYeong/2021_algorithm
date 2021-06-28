from collections import deque

def solution(n, edge):
    answer = 0
    edge.sort()
    elen = len(edge)
    nlen = [ 0 for _ in range(n+1)]
    elist = [[] for i in range(n+1)]
    queue = deque()
    
    for i in edge:
        elist[i[0]].append(i[1])
        elist[i[1]].append(i[0])
        
    queue.append(1) # 1번 노드부터 시작하기 때문
    nlen[1] =1
    
    while queue :
        i = queue.popleft()
        for j in elist[i]:
            if nlen[j]==0:
                queue.append(j)
                nlen[j] = nlen[i]+1
    
    maxlen = max(elist)
    for i in nlen:
        if i == maxlen:
            answer +=1
            
    return answer