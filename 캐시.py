a0 = 3
a1 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
b0 = 3
b1 = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
c0 = 2
c1 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
d0 = 5
d1 =["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
e0 = 2
e1 =["Jeju", "Pangyo", "NewYork", "newyork"]
f0 = 0
f1 =["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

from collections import deque

# 이미존재 hit 캐시에 없음 miss

def solution(cacheSize, cities):
    citeq = []
    for i in range(len(cities)):
        citeq.append(cities[i].upper())
    print(citeq)

    cache = deque()
    time = 0

    for i in citeq:
        if i in cache:
            time +=1
            cache.remove(i)
            cache.append(i)
        else:
            time +=5
            cache.append(i)
            if len(cache) == cacheSize+1:
                cache.popleft()
    print(time)
    return time


solution(a0, a1)
solution(b0,b1)
solution(c0,c1)
solution(d0, d1)
solution(e0, e1)
solution(f0,f1)