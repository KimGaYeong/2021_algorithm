
relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

import itertools


def solution(relation):
    answer =0
    clen = len(relation)
    rlen = len(relation[0])
    count =0
    idx = list( i for i in range(rlen))
    check = []
    
    for j in range(rlen):
        sub = []
        for i in range(clen):
            if relation[i][j] not in sub:
                sub.append(relation[i][j])
        check.append(sub)
        print(check)

    for i in range(rlen):
        if len(check[i]) == clen:
            idx.pop(i)
    
    print(idx)
    permu = []

    for i in range(1, len(idx)+1):
        permu.append(list(itertools.permutations(check, i)))

    print(permu)
    """
    import itertools를 이용해서 조합을 추출해 저장한 뒤 조합들이 유일한지 위 for문을 반복해 찾고
    유일한 조합들 중 최소성을 만족하지 못한 애들이 존재하는지 any를 이용해 찾는다.
    any를 이용.

    """

    print("idx", idx)
    print(count)
    return answer

solution(relation)