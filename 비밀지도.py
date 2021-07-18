
n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

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
    answer = []
    return answer

solution(n, arr1, arr2)