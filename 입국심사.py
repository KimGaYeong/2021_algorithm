def solution(n, times):
    answer = 0

    # 시간을 보고 몇명이 통과할 수 있는지를 체크하여 n값과 비교
    left = 1 # min time
    right = max(times) * n # max time
    l_times = len(times)

    while left <= right :
        tmp =0
        mid = (left + right) //2
        for i in range(l_times):
            tmp += mid//times[i]
        if(tmp < n):
            left = mid+1
        else:
            answer = mid
            right = mid-1
    return answer


# 실행시간 초과
# def solution(n, times):
#     answer = 0

#     # 시간을 보고 몇명이 통과할 수 있는지를 체크하여 n값과 비교
#     left = 1 # min time
#     right = max(times) * n # max time
#     l_times = len(times)

#     while left < right :
#         tmp =0
#         mid = (left + right) //2
#         for i in range(l_times):
#             tmp += mid//times[i]
#         if(tmp < n):
#             left = mid+1
#         elif(tmp > n):
#             right = mid-1
#         else :
#             answer = mid
#     return answer
