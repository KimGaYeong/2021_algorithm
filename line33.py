n1 = ["imhero111", "moneyman", "hero111", "imher1111", "hro111", "mmoneyman", "moneymannnn"]
e1 = ["superman5@abcd.com", "batman432@korea.co.kr", "superman@abcd.com", "supertman5@abcd.com", "superman@erty.net", "batman42@korea.co.kr", "batman432@usa.com"]

from sys import setrecursionlimit
setrecursionlimit(10**9)
import itertools

def lcs(a, b):
    max = 0
    index = 0

    l = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                l[i+1][j+1] = l[i][j] +1
            if max < l[i+1][j+1]:
                max = l[i+1][j+1]
                index = i+1
    return len(a[index-max:index])

def solution(nicks, emails):
    answer = []
    ne= []
    for i in range(len(nicks)):
        ne.append([nicks[i], emails[i]])

    nic = list(itertools.combinations(list(ne[i][0] for i in range(len(ne))), 2))
    
    same = []
    for a in nic:
        fi = a[0]
        se = a[1]
        
        l = lcs(fi, se)
        if l >= len(fi)-2 and l >= len(se)-2:
            h = [nicks.index(a[0]), nicks.index(a[1])]
            h = sorted(h)
            answer.append(h)
            same.append(a)

#----------------------------
    same2 = []
    ema = list(itertools.combinations(list(ne[i][1] for i in range(len(ne))), 2))
    answer2 = []
    for i in ema:
        g1 = i[0].index("@")
        g2 = i[1].index("@")
        if i[0][g1:] == i[1][g2:]:
            fi = i[0][:g1]
            se = i[1][:g2]
            l = lcs(fi, se)
            if l >= len(fi)-1 and l >= len(se)-1:
                h = [emails.index(i[0]), emails.index(i[1])]
                h = sorted(h)
                answer2.append(h)
                same2.append(i)

    print(answer, "닉네임이 동일한 원소들")
    print(answer2, "이메일이 동일한 원소들")

    return len(same)

solution(n1, e1)
