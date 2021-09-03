stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3


def solution(stones, k):
    answer = 0
    left, right = 0, 200000000
    
    while left <= right:
        gap = 0
        mid = (left+right) // 2

        for stone in stones:
            if stone - mid <= 0:
                gap +=1
                if gap ==k:
                    gap = k+len(stones)
                    break
            else:
                gap =0
        
        if gap == k+len(stones):
            right = mid-1
        else:
            left = mid+1
            answer = left

    print(answer)
    return answer

solution(stones, k)