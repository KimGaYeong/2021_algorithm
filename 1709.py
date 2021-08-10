from sys import stdin

N = int(stdin.readline())
HN = N//2

def distance(a, b): # 원소들의 거리를 유클리드 공식을 사용하여 계산하는 함수

    answer =0
    for i in range(2):
        answer += ((a[i] - b[i]) **2)

    return ((answer) ** 0.5)

answer =0

for i in range(1, N+1):
    for j in range(1, N+1):
        y = [HN, HN]
        if i <= HN and j <= HN: # 2사분면
            x1 = [i-1, j-1]
            x2 = [i, j]
            if distance(x1, y) > HN and distance(x2, y) <= HN:
                answer +=1
        elif i > HN and j <= HN: # 1사분면
            x1 = [i, j-1]
            x2 = [i-1, j]
            if distance(x1, y) <= HN and distance(x2, y) > HN:
                answer +=1
        elif i <= HN and j > HN: # 3사분면
            x1 = [i-1, j]
            x2 = [i, j-1]
            if distance(x1, y) <= HN and distance(x2, y) > HN:
                answer +=1
        elif i > HN and j > HN: # 4사분면
            x1 = [i-1, j-1]
            x2 = [i, j]
            if distance(x1, y) <= HN and distance(x2, y) > HN:
                answer +=1

print(answer)