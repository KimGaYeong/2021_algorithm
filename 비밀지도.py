
n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

n1 = 6
arr11 = [46, 33, 33 ,22, 31, 50]
arr12 = [27 ,56, 19, 14, 14, 10]

def binary(num):
    save = []

    while True:
        a = int(num/2)
        b = int(num%2)
        save.insert(0, b)

        if a!=0:
            num =a
        else:
            break
    
    final = ''.join(map(str, save))
    return final

def solution(n, arr1, arr2):
    arr3 = [0] * n
    bin1, bin2 = [], []
    for i in arr1:
        bin1.append(binary(i))
    for j in arr2:
        bin2.append(binary(j))

    for i in range(n):
        if len(bin1[i])<n:
            while True:
                if len(bin1[i])==n:
                    break
                bin1[i] = "0" + bin1[i]
    for i in range(n):
        if len(bin2[i])<n:
            while True:
                if len(bin2[i])==n:
                    break
                bin2[i] = "0" + bin2[i]
    
    print("bin1", bin1)
    print("bin2", bin2)
    bin3 = []

    for i in range(n):
        for j in range(n):
            if bin1[i][j] == bin2[i][j] and bin1[i][j] == "1":
                bin3.append("#")
            elif bin1[i][j] == bin2[i][j] and bin1[i][j] =="0":
                bin3.append(" ")
            else :
                bin3.append("#")

    bin4 = []
    for i in range(n):
        jstr = "".join(bin3[n*i:n*(i+1)])
        bin4.append(jstr)
        
    return bin4

solution(n, arr1, arr2)

solution(n1, arr11, arr12)