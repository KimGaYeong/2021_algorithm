k = 10
room_number = [1,3,4,1,3,1]

from sys import setrecursionlimit
setrecursionlimit(10**9)

def solution(k, room_number):
    answer = []

    room = [0] * (2*k)

    for i, item in enumerate(room_number):
        if room[item] ==0:
            room[item] = chr(65+i)
        else:
            for j in range(item, 2*k):
                if room[j] ==0 and j > item:
                    room[j] = chr(65+i)
                    break
                
    #print(room)

    for i in range(1, 2*k):
        if room[i] != 0:
            answer.append(room.index(chr(64+i)))
    
    print(answer)
    return answer

solution(k, room_number)

"""
def solution(k, room_number):
    answer = []

    room = [0] * k
    
    for i, item in enumerate(room_number):
        if room[item-1] ==0:
            room[item-1] = i+1
        else:
            
    return answer
"""