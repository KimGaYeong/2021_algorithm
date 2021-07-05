from sys import stdin

N = int(stdin.readline())

print(N//5 + N//(5**2) + N//(5**3))