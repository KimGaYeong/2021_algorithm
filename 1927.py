import heapq
from sys import stdin

N = int(stdin.readline())
heap = []
list = [0] * N

for i in range(0,N):
    list[i] = int(stdin.readline())

i=0
while i<N:
    if list[i] ==0 and len(heap) ==0:
        print(0)
    elif list[i]>0:
        heapq.heappush(heap, list[i])
    elif list[i]==0 and len(heap)>0 :
        print(heapq.heappop(heap))
    i+=1
