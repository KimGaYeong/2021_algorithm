from sys import stdin

N = int(stdin.readline())
M = int(stdin.readline())

str = stdin.readline().rstrip()

i, count, answer = 0,0,0
while i<M-1:
    if str[i-1] =="I" and str[i] =="O" and str[i+1] =="I":
        count +=1
        if count ==N:
            answer +=1
            count -=1
        i+=1
    else:
        count =0
    i +=1

print(answer)