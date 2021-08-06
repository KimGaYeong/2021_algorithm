f1 = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
f2 = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
f3 = ["foo9.txt", "foo010bar020.zip", "F-15"]

import re

def solution(files):

    #print(files)
    file_len = len(files)
    
    Head = []
    Number = []
    Tail = []

    for i in range(file_len):
        SubHead = []
        SubNum =[]
        SubTail = []
        #files[i] = files[i].upper()

        for j in files[i]:
            if len(SubNum)==0:
                if not re.findall(r"\d", j):
                    SubHead.append(j)
                elif re.findall(r"\d", j):
                    SubNum.append(j)
                    #print("SUbnum", SubNum)
            elif len(SubNum)>0:
                if len(SubTail)==0:
                    if re.findall(r"\d", j):
                        SubNum.append(j)
                        #print("SUbnum", SubNum)
                    else:
                        SubTail.append(j)
                elif len(SubTail)>0:
                    SubTail.append(j)
        
        Head.append(''.join(SubHead))
        Number.append(''.join(SubNum))
        Tail.append(''.join(SubTail))
    
    beforesort = []
    
    for i in range(file_len):
        beforesort.append([Head[i], Number[i], Tail[i], Head[i].upper()])
        
        print(beforesort[i])

    for i in range(file_len):
    

        aftersort = sorted(beforesort, key = lambda x : (x[3], int(x[1])))

    #print(first_sorted)
    answer = []
    for i in range(file_len):
        answer.append(''.join(aftersort[i][0:3]))

    print(answer)
    """
        print("Head[", i, "] : ", Head[i])
        print("Num[", i, "] : ", Number[i])
        print("Tail[", i, "] : ", Tail[i])
        print("\n")
    """       

    return answer

solution(f2)
