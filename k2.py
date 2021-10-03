n1 = 437674
k1 = 3

n2 = 110011
k2 = 10

def cn(n, base):
    T = "0123456789ABCDE"
    q, r = divmod(n, base)

    return cn(q, base) + T[r] if q else T[r]

def ip(n):
    s = [True] * (n+1)
    
    for i in range(2, int(n**0.5) +1):
        if s[i]:
            for j in range(i+i, n+1, i):
                s[j] =False
                
    print([i for i in range(2, (n+1)) if s[i]])
    return [i for i in range(2, (n+1)) if s[i]]

def solution(n, k):
    answer = 0

    ans = cn(n, k)
    print(ans)

    li = ans.split("0")

    for i in li:
        if len(i) ==0:
            pass
        else:
            if int(i) >= 2 and ip(int(i)) == True:
                answer +=1
    print(answer)
    return answer

solution(n2, k2)
ip(10)