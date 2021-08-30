
s0 = "{{2},{2,1},{2,1,3},{2,1,3,4}}" #[2, 1, 3, 4]
s1 = "{{1,2,3},{2,1},{1,2,4,3},{2}}" #[2, 1, 3, 4]
s2 = "{{20,111},{111}}"	             #[111, 20]
s3 = "{{123}}"	                     #[123]
s4 = "{{4,2,3},{3},{2,3,4,1},{2,3}}" #[3, 2, 4, 1]

def solution(s):
    answer = []
    li, sub, ssub = [], [], []
    
    for i in range(len(s)-1):

        if s[i].isdigit():
            if s[i+1].isdigit():
                ssub.append(s[i])
            elif s[i+1] == ",":
                ssub.append(s[i])
                sub.append("".join(ssub))
                ssub = []
            elif s[i+1] == "}":
                ssub.append(s[i])
                sub.append("".join(ssub))
                ssub = []
                li.append(sub)
                sub = []
        
    li = sorted(li, key= lambda x : len(x))

    i =0
    while(True):
        sub2 = li[i][0]
        answer.append(int(sub2))
        if i == len(li)-1 :
            break
        for j in range(i+1, len(li)):
            li[j].remove(sub2)
        i +=1

    print(answer)
    return answer

solution(s0)
solution(s1)
solution(s2)
solution(s3)
solution(s4)