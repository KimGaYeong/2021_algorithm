import sys

def fibo(num):
    zero = [1, 0]
    one = [0, 1]
    if num>=2:
        for i in range(2, num+1):
            zero.append(zero[i-2] + zero[i-1])
            one.append(one[i-2] + one[i-1])
    print(zero[num], one[num])

T = int(input())
for j in range(T):
    n = int(sys.stdin.readline())
    fibo(n)