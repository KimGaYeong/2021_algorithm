#무지의_먹방_라이브.py

food_times0=[3, 1, 2]
k0=5
food_times=[4,2,3,6,7,1,5,8]
k=16
food_times1=[4,2,3,6,7,1,5,8]
k1=27
food_times2=[3,1,1,1,2,4,3]
k2=12
food_times3=[4, 3, 5, 6, 2]
k3=7
food_times4=[4, 1, 1, 5]
k4=4
food_times5 = [1, 1, 1, 1]
k5 =4

a1 = [4, 1, 1, 5]
a2 = [4, 1, 1, 5]
a3 = [4, 1, 1, 5]
b1 = 5
b2 = 6
b7 = 7 # 4, 1, 4


def solution(food_times, k):
    lfood = len(food_times)
    idx = 1
    count =0
    while(True):
        #print(count, "~", count+1, "초 동안 ", idx, "번 음식 섭취")
        if count==k+1:
            if idx == 1:
                idx = lfood
            else:
                idx = idx-1
            #print(idx)
            break

        if sum(food_times) ==0:
                print(-1)
                return -1
            
        if food_times[idx-1] != 0 :
            food_times[idx-1] -=1
            if idx == lfood:
                idx =1
            else :
                idx +=1
            count +=1
            
            #print("남은 food는 ", food_times, '\n')
        else :
            if idx == lfood:
                idx =1
            else :
                idx +=1
            #print("남은 food는", food_times, '\n')

    print(idx)
    return idx
    

solution(food_times0, k0) #1

solution(food_times, k) #3

solution(food_times1, k1) #5

solution(food_times2, k2) #6

solution(food_times3, k3) #3

solution(food_times4, k4) #1

solution(food_times5, k5) #-1


solution(a1, b1) #4
solution(a2, b2) #1
solution(a3, b7) #4
solution([1, 5, 5, 5, 5, 6, 7], 31)



"""
import heapq
def solution(food_times, k):
    answer = -1
    h = []
    for i in range(len(food_times)):
        heapq.heappush(h, (food_times[i], i + 1))
    food_num = len(food_times) # 남은 음식 개수 
    previous = 0 # 이전에 제거한 음식의 food_time
        
    while h:
        # 먹는데 걸리는 시간: (남은 양) * (남은 음식 개수) 
        t = (h[0][0] - previous) * food_num
        # 시간이 남을 경우 현재 음식 빼기
        if k >= t:
            k -= t
            previous, _ = heapq.heappop(h)
            food_num -= 1
            # 시간이 부족할 경우(음식을 다 못먹을 경우) 남은 음식 중에 먹어야 할 음식 찾기 
        else:
            idx = k % food_num
            h.sort(key=lambda x: x[1])
            answer = h[idx][1]
            break
    return answer


"""