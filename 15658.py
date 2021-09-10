from sys import getprofile, stdin

N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
s = list(map(int, stdin.readline().split()))
minval = 1000000000
maxval = -1000000000

def minmax(s, idx, answer):
    global maxval, minval
    # for문을 사용하지 않는 대신, index를 이용하여 함수의 재귀 횟수를 지정한다.
    if idx == N:
        maxval = max(maxval, answer)
        minval = min(minval, answer)
        return 
    for i in range(4):
            
        if i==0 and s[i] > 0:
            sub = answer + A[idx]
            s[i] -=1
            minmax(s, idx+1, answer + A[idx])
            s[i] +=1
        if i==1 and s[i] > 0:
            s[i] -=1
            minmax(s, idx+1, answer - A[idx])
            s[i] +=1
        if i==2 and s[i] > 0:
            s[i] -=1
            minmax(s, idx+1, answer * A[idx])
            s[i] +=1
        if i==3 and s[i] > 0:
            s[i] -=1
            minmax(s, idx+1, int(answer/A[idx]))
            s[i] +=1
                
            
answer = A[0]
minmax(s, 1, answer)

print(maxval)
print(minval)