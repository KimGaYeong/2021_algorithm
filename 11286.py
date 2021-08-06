import heapq
from sys import stdin

N = int(stdin.readline())
maxheap = []

for i in range(N):
    x = int(stdin.readline())
    if len(maxheap) ==0:
        if x ==0:
            print(0)
        else:
            heapq.heappush(maxheap, -x)
    else:
        if x==0:
            print(-heapq.heappop(maxheap))
        else:
             heapq.heappush(maxheap, -x)
    
    