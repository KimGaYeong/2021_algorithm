from sys import stdin
import heapq

N = int(stdin.readline())
classnet = [[0]*2 for i in range(N)]
room = []

for i in range(N):
    classnet[i][0], classnet[i][1] = map(int, stdin.readline().split())

classnet = sorted(classnet, key = lambda x : x[0])

print(classnet)
print("first push", classnet[0][1])
heapq.heappush(room, classnet[0][1])
for i in range(1, N):
    print("present room", room)
    if classnet[i][0] >= room[0]:
        
        heapq.heappop(room)
        print("after pop", room)
    
    heapq.heappush(room, classnet[i][1])
    print("after push", room)

print(len(room))

