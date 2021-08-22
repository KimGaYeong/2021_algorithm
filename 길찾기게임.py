
nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]

import sys
sys.setrecursionlimit(1000000)

def preorder(ysort, answer):
    node = ysort[0]
    left = []
    right = []
    
    for i in range(1, len(ysort)):
        if node[0] > ysort[i][0]:
            left.append(ysort[i])
        else:
            right.append(ysort[i])
    
    answer.append(node[2])
    if len(left) > 0:
        preorder(left, answer)
    if len(right) > 0:
        preorder(right, answer)
    return answer

def postorder(ysort, answer):
    node = ysort[0]
    left = []
    right = []
    
    for i in range(1, len(ysort)):
        if node[0] > ysort[i][0]:
            left.append(ysort[i])
        else:
            right.append(ysort[i])
    
    if len(left) > 0:
        postorder(left, answer)
    if len(right) > 0:
        postorder(right, answer)
    answer.append(node[2])
    return answer

def solution(nodeinfo):
    pre = []
    post = []
    
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    
    ysort = sorted(nodeinfo, key = lambda x : (-x[1], x[0]))
    

    return [preorder(ysort, pre), postorder(ysort, post)]

solution(nodeinfo)

# 일단 tree를 만드는 것이 우선.
# 문제를 보면 노드의 좌표값이 2차원 안에 있으므로 root노드와 좌 우 자식노드를 파악하기 위해서
# 정렬을 먼저 해주는게 중요해 보였는데 nodeinfo같은 경우 x좌표, y좌표 순으로 위치해 있으니까
# 우선 node 번호를 3번째 원소로 각각 삽입. 그다음 y좌표를 기준으로 내림차순 정렬을 해준 뒤 
# x좌표를 기준으로 오름차순 정렬.
# 전위 순회같은 경우 root노드를 기준으로 left 자식과 right 자식을 저장함.
# 