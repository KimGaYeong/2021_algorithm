from sys import stdin

N = int(stdin.readline())
times = [0] * (N+1)
dic = {}

print("\n")
for i in range(1, N+1):
    li = list(map(int, stdin.readline().split()))
    print("list is", li)

    times[i] = li[0]
    print("times are ", times)
    if li[1] == 0:
        continue
    for j in li[2:]:
        if i in dic:
            dic[i].append(j)
        else:
            dic[i] = [j]

    print(dic)

for i in range(1, N+1):
    if i in dic:
        time =0
        for j in dic[i]:
            time = max(time, times[j])
        times[i] += time

print(times)
"""
7
5 0
1 1 1
3 1 2
6 1 1
1 2 2 4
8 2 2 4
4 3 3 5 6

 1번 작업 : 0~5  2번 작업 : 5~6
 3번 작업 : 6~9  4번 작업 : 5~11
 5번 작업 : 11~12 6번 작업 : 11~19
 7번 작업 : 19~23
"""