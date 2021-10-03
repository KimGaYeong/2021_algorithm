b1 = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
s1 = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

b2=[[1,2,3],[4,5,6],[7,8,9]]
s2=[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]

from sys import setrecursionlimit
setrecursionlimit(10**9)
def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    for val in skill:
        s = [[0 for _ in range(M)] for _ in range(N)]
        for i in range(val[1], val[3]+1):
            if val[0] ==1:
                k = val[4]-val[2]+1
                s[i] = [0] *(val[2]-0)  + [-1 * val[5]] * (k) + [0] * (M-1-val[4])
            elif val[0] ==2:
                k = val[4]-val[2]+1
                s[i] = [0] *(val[2]-0)  + [val[5]] * (k) + [0] * (M-1-val[4])
        
        board = [[x+y for x, y in zip(a, b)]for a, b in zip(board, s)]

    for i in board:
        for j in i:
            if j <=0 :
                answer +=1

    return (M*N)-answer
solution(b1, s1)
solution(b2, s2)