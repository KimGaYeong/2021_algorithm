u0 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
b0 = ["fr*d*", "abc1**"] #2

u1 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
b1 = ["*rodo", "*rodo", "******"] #2

u2 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
b2= ["fr*d*", "*rodo", "******", "******"] #3


import sys
sys.setrecursionlimit(10**9)

def solution(user_id, banned_id):
    answer = 0

    banimp = []
    for ban in banned_id:
        print(ban)
        sub = []
        lenb = len(ban)
        other = list(i for i in range(lenb))
        num =0
        for i in range(lenb):
            if ban[i] == "*":
                sub.insert(0, i)
                other.remove(i)
                num +=1
        ban = ban.replace("*", "")
        banimp.append([ban, lenb, sub, other, num])
    
    print(banimp)



    return answer

solution(u0, b0)