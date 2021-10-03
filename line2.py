r1 = ["abaaaa","aaa","abaaaaaa","fzfffffffa"]
n1 = 2
k1 = 2

r2 = ["yxxy","xxyyy"]
n2 = 2
k2 = 1

r3 = ["yxxy","xxyyy","yz"]
n3 = 2
k3 = 1

r4 = ["xy","xy"]
n4 = 1
k4 = 1


def solution(research, n, k):
    answer = ''
    dic = []
    sub2 = []
    for re in research:
        sub = list(re)
        for i in sub:
            if not i in dic:
                dic.append(i)
    
    dic = sorted(dic)

    for re in research:
        sub = list(re)
        s = []
        
        for j in dic:
            s.append(sub.count(j))
        sub2.append(s)
        #if re.count()
    
    print(sub2)
    ans = []
    for j in range(len(dic)):
        n = 0
        max = 0
        add = 0
        maxadd = 0
        for i in range(len(research)):
            if sub2[i][j] >=k:
                add += sub2[i][j]
                n +=1
                if n>=2:
                    max = n
                    maxadd = add
            else:
                n =0
                add = 0
        if max>=k and maxadd >= (2 * n * k):
            ans.append([j, max])
    
    print(ans)
    if not ans:
        return 0
    else:

        ans = sorted(ans, key = lambda x : (-x[1], x[0]))

        answer = dic[ans[0][0]]
        print(answer)
        return answer

solution(r1, n1, k1)
solution(r2, n2, k2)
solution(r3, n3, k3)
solution(r4, n4, k4)