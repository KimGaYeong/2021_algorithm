import heapq

def solution(jobs):
    # jobs : [ 요청 시점, 소요 시간 ]
    answer =0
    start, now, count = -1, 0, 0
    jlen = len(jobs)
    pq =[]
    
    while count < jlen:
        for j in jobs:
            if start < j[0] <= now:
                answer += now-j[0]
                heapq.heappush(pq, j[1])
        if len(pq)>0:
            answer += pq[0] * len(pq)
            start = now
            now += heapq.heappop(pq)
            count +=1
        else :
            now +=1
            
    return answer// jlen