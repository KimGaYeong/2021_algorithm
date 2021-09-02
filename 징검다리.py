stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3


def solution(stones, k):
    answer = 1

    now, gap = 0, 1
    while (True):

        if gap == k:
            break
        
        if now == len(stones):
            now =0
            answer +=1

        if stones[now] == 0:
            now +=1
            gap +=1
        elif stones[now] != 0:
            stones[now] -=1
            now +=1
    return answer

solution(stones, k)