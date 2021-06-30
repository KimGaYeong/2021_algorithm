
N, r, c = map(int, input().split())

answer =0
while N>1:
    line = 2 ** N
    half = 2 ** (N-1)

    if r < half and c >= half:
        answer += (half**2)
        c -= half

    elif r >= half and c < half:
        answer += ((half**2)*2)
        r -= half

    elif r >= half and c >= half:
        answer += ((half**2)*3)
        r -= half
        c -= half

    N -=1


if r==0 and c==0:
    print(answer)
elif r==0 and c==1:
    print(answer+1)
elif r==1 and c==0:
    print(answer+2)
elif r==1 and c==1:
    print(answer+3)