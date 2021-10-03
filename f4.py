i1 = [0,0,1,1,1,0,1,0,1,0,1,1]
e1 = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

i2 = [0,1,0,1,1,0,1,0,0,1,0]
e2 = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]

def solution(info, edges):
    answer = 0
    graph = [[] for _ in range(len(info)+1)]

    for i in range(len(edges)):
        a = edges[i][0]
        b = edges[i][1]
        print(a, b)
        if a in graph:
            graph[a].append(b)
        else:
            graph.append([a, b])
    
    print(graph)
    return answer

solution(i1, e1)