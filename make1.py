# DP!!! 잼나게하자.

N = int(input())

DP = [0, 0, 1, 1] # DP[0], DP[1], DP[2], DP[3]

for i in range(4, N+1):
    DP.append(DP[i-1]+1)

    if i%2 == 0 :
        DP[i] = min(DP[i//2]+1, DP[i])
    if i%3 == 0:
        DP[i] = min(DP[i//3]+1, DP[i])

print(DP[-1])