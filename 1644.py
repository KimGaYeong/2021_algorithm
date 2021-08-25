# 소수의 연속합
from sys import stdin

N = int(stdin.readline())
"""
[ 에라토스테네스의 체 ]
어떤 수 N를 확인 한 후, N**2를 첫항으로 하고 3을 공차로 하는 수를 소수가 아닌 수로 제외시키는 것.
ex) N = 3 이라면 3**2 = 9가 첫항, 9, 12, 15, ... 등을 소수가 아닌 수로 제외시키기

"""
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
