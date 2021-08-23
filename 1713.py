from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10**9)

N = int(stdin.readline())
num = int(stdin.readline())
s_num = list(map(int, stdin.readline().split()))

def find(list, letter): 
    for i in range(len(list)):
        if list[i][1] == letter:
            return i # letter가 list에 있으먄 그 index를 반환
    else:
        return -1

recommend = []
for i, letter in enumerate(s_num):
    if find(recommend, letter) != -1: # 먼저 letter가 list에 있는지 확인
        sub = find(recommend, letter) 
        recommend[sub][2] +=1 # index를 찾았으면 그 인덱스의 추천 횟수를 증가
    else: # [들어온 순서, 추천 번호, 추천 횟수]
        if len(recommend) <N: # N개 미만인 경우 그냥 추가
            recommend.append([i, letter, 1])
        elif len(recommend) ==N:
            # N개인 경우 sort를 통해 가장 추천수가 적은순, 먼저 온 순으로 정렬해서 첫번째인 원소 삭제
            sub = sorted(recommend, key = lambda x : (x[2], x[0]))
            recommend.remove(sub[0])
            recommend.append([i, letter, 1])
    
sort = sorted(recommend, key = lambda x : (x[1]))

for i in range(len(sort)):
    print(sort[i][1], end = " ")

"""
3
9
2 1 4 3 5 6 2 7 2
"""