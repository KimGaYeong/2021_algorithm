import math 

def solution(progresses, speeds):
    lefted = []
    answer = []

    for i, j in zip(progresses, speeds):
        # lefted.append((100-i)/j) -> 소수점 고려 안하면 2번 tc 오류
        # lefted.append(int((100 - i)/j)) -> 몫으로 구하면 11번 tc 오류
        lefted.append(math.ceil((100-i)/j))
    l = len(lefted)
    top, count = 0, 0
    for i in range(l):
        if(lefted[top] < lefted[i]):
            answer.append(count)
            top = i
            count =1
        else :
            count +=1
    answer.append(count)
    return answer