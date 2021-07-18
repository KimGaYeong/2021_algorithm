from sys import stdin

T = int(stdin.readline())

for i in range(T):
    p = input()
    p = p.replace("RR", " ")
    n = int(stdin.readline())
    list = stdin.readline().rstrip()[1:-1].split(',')
    print("p is", p)
    print("n  ", n)
    print("list is ", list)

    r, front, back =0, 0, 0
    for j in p:
        if j=="R":
            r+=1
        elif j=="D":
            if r%2 ==0:
                front+=1
            else:
                back+=1

    if front+back <= n:
        list= list[front:n-back]
        if r%2 !=0:
            print(list[::-1]) # liststart:end:step]
        elif r%2 ==0:
            print(list)
    else:
        print("error")
