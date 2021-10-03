
n1 = ["imhero111", "moneyman", "hero111", "imher1111", "hro111", "mmoneyman", "moneymannnn"]
e1 = ["superman5@abcd.com", "batman432@korea.co.kr", "superman@abcd.com", "supertman5@abcd.com", "superman@erty.net", "batman42@korea.co.kr", "batman432@usa.com"]

from sys import setrecursionlimit
setrecursionlimit(10**9)
import itertools
def solution(nicks, emails):
    answer = -1

    nic = list(itertools.combinations(nicks, 2))
    
    same = []
    print(nic)
    for a in nic:
        fi = a[0]
        se = a[1]
        sub1, sub2 = [], []
        for i, v in enumerate(fi):
            sub1.append([i, v])
        for i, v in enumerate(se):
            sub2.append([i, v])
        
        sam = [i for i, j in zip(sub1, sub2) if i == j]
        if len(sam) >= len(sub1)-2 and len(sam) >= len(sub2)-2:
            same.append(a)

#----------------------------
    ans2 = []
    ema = list(itertools.combinations(emails, 2))
    for i in ema:
        g1 = i[0].index("@")
        g2 = i[1].index("@")
        if i[0][g1:] == i[1][g2:]:
            ans2.append(i)
    same2 = []
    print("ans2",ans2)
    for a in ans2:
        g1 = a[0].index("@")
        fi = a[0][:g1]
        g2 = a[1].index("@")
        se = a[1][:g2]

        sub1, sub2 = [], []
        for i, v in enumerate(fi):
            sub1.append([i, v])
        for i, v in enumerate(se):
            sub2.append([i, v])
    
        sam = [i for i, j in zip(sub1, sub2) if i == j]
        if len(sam) >= len(sub1)-2 and len(sam) >= len(sub2)-2:
            same2.append(a)
    
    print(same)
    print(same2)
    return answer


solution(n1, e1)