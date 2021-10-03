s1 = [0,1,0,0]
k1 = 1

s2 = [0, 1, 0, 0, 1, 1, 0]
k2 = 2

s3 = [0, 1, 0]
k3 = 2

from itertools import permutations

def solution(student, k):
    answer = 0
    li = []
    for i in range(1, len(student)+1):
        sub = list(student[j:j+i] for j in range(0, len(student)))
        for s in sub:
            if len(s) == i:
                li.append(s)

    print(li)

    for i in li:
        if i.count(1) == k:
            answer+=1
    
    print(answer)
    return answer

solution(s2, k2)


"""def powerset(s):
    masks = [1 << i for i in range(len(s))]
    for i in range(1 << len(s)):
        yield [ss for ss, mask in zip(s, masks) if mask & i]


def solution(student, k):
    answer = -1

    for power in powerset(student):
        print(power)
    return answer
"""
