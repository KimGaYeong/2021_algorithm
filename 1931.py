from sys import stdin
N = int(stdin.readline())
time = [[0] * 2 for i in range(N)]
for i in range(N):
    time[i][1], time[i][0] = map(int, stdin.readline().split())

time.sort()
count = 0
cmp = 0
for i in range(N):
    end, start = time[i][0], time[i][1]

    if cmp <= start:
        cmp = end
        count+=1

print(count)