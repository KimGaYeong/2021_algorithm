from sys import stdin

N = int(stdin.readline())
line = [0] * N

for i in range(N):
    line[i] = int(stdin.readline())

answer = []
for i in range(N):
    answer.append(line[i])
    for j in range(i, N):
        if answer[len(answer)-1] < line[j]:
                answer.append(line[j])
    print("answer", answer)
    answer = []