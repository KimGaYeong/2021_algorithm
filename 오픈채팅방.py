
R1 = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    name, answer, result = [], {}, []

    l_record = len(record)
    for i in range(l_record):
        name.append(record[i].split())
        
    
    answer = {name[i][1] : name[i][2]}
    for i in range(l_record):
        if name[i][0] == "Enter":
            answer[name[i][1]] = name[i][2]
            userid = name[i][1]
            result.append([userid, "님이 들어왔습니다."])
        elif name[i][0] == "Leave":
            userid = name[i][1]
            result.append([userid, "님이 나갔습니다."])        
        elif name[i][0] == "Change":
            answer[name[i][1]] = name[i][2]
            

    for i in range(len(result)):
        print(result[i][0])
        username = result[i][0]
        result[i][0] = answer[username]
        print(result)
        result[i] = "".join(result[i])
    
    print(result)
    return result

solution(R1)
