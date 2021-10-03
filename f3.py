f1 = [180, 5000, 10, 600]
r1 = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

f2 = [120, 0, 60, 591]
r2 = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]

f3 = [1, 461, 1, 10]
r3 = ["00:00 1234 IN"]



import math
def solution(fees, records):
    answer = []
    li = []
    for i in records:
        li.append(i.split(' '))
    li = sorted(li, key= lambda x : (x[1], x[0]))
    car = []
    for i in range(0, len(records)-1):
        print(li[i])
        if li[i][2] == "IN" and li[i][1] == li[i+1][1]:
            after = int(li[i+1][0][0:2])*60 + int(li[i+1][0][3:])
            before = int(li[i][0][0:2])*60 + int(li[i][0][3:])
            time = after- before
            car.append([li[i][1], time])
        elif li[i][2] == "IN" and li[i][1] != li[i+1][1]:
            after = 23*60 + 59
            before = int(li[i][0][0:2])*60 + int(li[i][0][3:])
            time = after- before
            car.append([li[i][1], time])
        else:
            pass
    
    if li[-1][2] == "IN":
        after = 23*60 + 59
        before = int(li[-1][0][0:2])*60 + int(li[-1][0][3:])
        time = after- before
        car.append([li[-1][1], time])
    
    print(car)
    ans = {}
    for i in car:
        if i[0] in ans:
            ans[i[0]] += i[1]
        else:
            ans[i[0]] = i[1]

    for key in ans.keys():
        if ans[key] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((ans[key]-fees[0]) /fees[2])*fees[3])

    print(answer)
    return answer

solution(f2, r2)