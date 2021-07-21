import re

str1 = "FRANCE"
str2 = "french"

str11 = "handshake"
str12 = "shake hands"

str21 = "aa1+aa2"
str22 = "AAAA12"

str31 = "E=M*C^2"
str32 = "e=m*c^2"

def solution(stra, strb):

    #str1 = "".join(re.findall("[a-zA-Z]+", stra)).upper()
    #str2 = "".join(re.findall("[a-zA-Z]+", strb)).upper()
    str1 = stra.upper()
    str2 = strb.upper()

    list1, list2 = [], []
    for i in range(len(str1)-1):
        if str1[i].isalpha() == str1[i+1].isalpha() == True:
            list1.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i].isalpha() == str2[i+1].isalpha() == True:
            list2.append(str2[i:i+2])

    if len(list1) ==0 and len(list2)==0:
        print(65536)
    else:
        s1 = set(list1)
        s2 = set(list2)

        print("list1", list1)
        print("list2", list2)
        com = list(s1&s2)
        print("common", com)
        union = list(s1|s2)
        lcom = list(com)
        print("minus", s1^s2)
        print(lcom)
        for i in lcom:
            commin = (min(list1.count(i), list2.count(i)))
            commax = (max(list1.count(i), list2.count(i)))
            for j in range(commin-1):
                com.append(i)
            for j in range(commax-1):
                union.append(i)

        print("com",com)
        print("union", union)

        print(int(len(com) / len(union) * 65536))

solution(str1, str2)
print("\n")
print("\n")

solution(str11, str12)
print("\n")
print("\n")
solution(str21, str22)
print("\n")
print("\n")
solution(str31, str32)