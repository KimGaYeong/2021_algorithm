dartResult1 = "1S2D*3T"
dartResult2 = "1D2S#10S"
dartResult3 = "1D2S0T"
dartResult4 = "1S*2T*3S"
dartResult5 = "1D#2S*3S"
dartResult6 = "1T2D3D#"
dartResult7 = "1D2S3T*"

def solution(dartResult):

    dartlist = list(dartResult)
    print("predartlist", dartlist)
    dartlen = len(dartlist)
    i=0
    while True:
        if i+1 == dartlen:
            break
        if dartlist[i]=="1" and dartlist[i+1]=="0" :
            dartlist.pop(i)
            dartlist.pop(i)
            dartlist.insert(i, "10")
        i+=1
    
    print("dartlist", dartlist)
    answer = []
    num =""
    for j in range(len(dartlist)):
        if dartlist[j].isdigit() == True:
            num = dartlist[j]
        elif dartlist[j] == "S":
            num = int(num)
            answer.append(num)
            num = ''
        elif dartlist[j] == "D":
            num = int(num) **2
            answer.append(num)
            num = ''
        elif dartlist[j] == "T":
            num = int(num) **3
            answer.append(num)
            num = ''
        elif dartlist[j] == "*":
            if len(answer) == 1:
                answer[0] *= 2
            else :
                answer[-1] *= 2
                answer[-2] *= 2
        elif dartlist[j] == "#":
            if len(answer) == 1:
                answer[0] *= (-1)
            else :
                answer[-1] *= (-1)

    print(sum(answer))
    return sum(answer)

solution(dartResult1)
solution(dartResult2)
solution(dartResult3)
solution(dartResult4)
solution(dartResult5)
solution(dartResult6)
solution(dartResult7)

