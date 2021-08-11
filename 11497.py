from sys import stdin

T = int(stdin.readline())

for i in range(T):
    N = int(stdin.readline())
    L = list(map(int, stdin.readline().split()))

    L = sorted(L, reverse = True)
    answer = []
    for i in range(len(L)):
        if i%2 ==1:
            answer.insert(0, L[i])
        else:
            answer.insert(len(L), L[i])
    
    print("answer", answer)
    result = 0
    for i in range(len(L)-1):
        if abs(answer[i+1] - answer[i]) > result:
            result = abs(answer[i+1] - answer[i])

    print("result is ", result)