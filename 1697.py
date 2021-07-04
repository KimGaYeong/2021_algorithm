from collections import deque
N, K = map(int, input().split())
visit = [0] * 100001
queue = deque()
queue.append([N, 0])
while queue:
    now, count = queue[0][0], queue[0][1]
    if now == K :
        print(count)
        break
    queue.popleft()
    visit[now] =1
    if now-1 >= 0 and visit[now-1] ==0 :
        queue.append([now - 1, count + 1])
    if now + 1 < 100001 and visit[now + 1] == 0 :
        queue.append([now + 1, count + 1])
    if now * 2 < 100001 and visit[now * 2] == 0 :
        queue.append([now * 2, count + 1])

"""
조건문의 순서에 따라 Index Error, Runtime error가 발생할 수 있다는 사실을 깨달았음.
조건문의 경우     if now-1 >= 0 and visit[now-1] ==0 : -> 정답
순서를 바꾸었을 때는 계속해서 런타임 오류가 생성. 재밋넹ㅎ
"""