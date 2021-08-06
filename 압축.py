msg1 = "KAKAO"
msg2 = "TOBEORNOTTOBEORTOBEORNOT"
msg3 = "ABABABABABABABAB"


def solution(msg):

    answer = []
    dictionary = []
    now = 0
    while now < len(msg):
        if msg[now:now+2] in dictionary: # 연속 문자가 존재하면
            for i in range(now+2, len(msg)): # 그 다음 애도 존재하는지 확인
                if msg[now:i+1] not in dictionary:
                    dictionary.append(msg[now:i + 1])
                    print("dictionary : ", dictionary)
                    print("answer : ", answer)
                    answer.append(dictionary.index(msg[now:i]) + 27)
                    now += i-now
                    break
            else:
                    answer.append(dictionary.index(msg[now:len(msg)]) + 27)
                    break
        else: # 연속 문자가 존재하지 않으면
            answer.append(ord(msg[now]) - 64)
            dictionary.append(msg[now:now+2])
            now += 1
    print(answer)
    return answer

    
solution(msg1)


'''
cd ..
cd Desktop
cd programmers_ga
python3 -m 압축 
'''