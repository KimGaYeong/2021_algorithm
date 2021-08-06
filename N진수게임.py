import re


n1, t1, m1, p1 = 2, 4, 2, 1
n2, t2, m2, p2 = 16, 16, 2, 1
n3, t3, m3, p3 = 16, 16, 2, 2
#n진법, t개 구하기, 인원m명, 순서p번째

def solution(n, t, m, p):
    answer = []
    result = []
    final = []
    i=0
    while i < m*t:
        answer.append(change(i, n))
        i+=1
    #print(answer)

    result = "".join(answer)
    print(result)
    #print(len(result))
    for i in range(0, len(result)):
        if (i+1)% p ==0:
            print("result", result[i])
            final.append(result[i])
            p += m
            if len(final) ==t:
                break
        else:
            continue
    print(final)
    return result

def change(n, N):
    result = ""
    ABC = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    if n!=0:
        while n != 0:
            result += ABC[n % N]
            n = n // N

        return(result[::-1])
    else:
        result+="0"
        return(result)


solution(n1, t1, m1, p1)
solution(n2, t2, m2, p2)
solution(n3, t3, m3, p3)