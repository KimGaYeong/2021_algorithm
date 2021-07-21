m1 = 4
n1 = 5
board1 = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

def solution(m, n, board):
    board1 = []
    answer =0
    for i in range(n):
        line = ""
        for j in range(m):
            line += board[j][i]
        board1.append(line[::-1])
    print(board1)

    while True:
        
        for i in range(1, n):
            for j in range(1, m):
                if board1[i][j] != "*":
                    if board1[i][j] == board1[i][j-1]:
                        if board1[i][j] == board[i-1][j] and board1[i][j] == board[i-1][j-1] :
                            pass

    return answer
    
solution(m1, n1, board1)