from sys import stdin

N = int(stdin.readline())

stick = []

for i in range(N):
    stick.append(int(stdin.readline()))

result = 0
small = 0


for s in range(N-1, -1, -1):
    if small < stick[s]:
        small = stick[s]
        result +=1
print(result)