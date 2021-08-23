# 소수의 연속합
from sys import stdin

N = int(stdin.readline())

a = [False, False] + [True]*(N-1)
sosulist = []

for i in range(2, N+1):
    if a[i]:
        sosulist.append(i)
        for j in range(2*i, N+1, i):
            a[j] = False


sum =0
start, end = 0, 0
count = 0

while(True):
    if sum > N:
        sum -= sosulist[start]
        start +=1
    elif sum ==N :
        count +=1
        sum -= sosulist[start]
        start +=1
    elif end == len(sosulist):
        break
    else:
        sum += sosulist[end]
        end +=1
print(count)



"""
num = len(sosulist)
count =0
for i in range(num):
    answer = 0
    k = i
    while(k < num):
        answer += sosulist[k]
        if answer == N:
            count +=1
            break
        else:
            k+=1
print(count)
"""
