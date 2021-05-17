def solution(s):
    a = s.split(' ')
    
    for i in range(len(a)):
        a[i]= a[i][:1].upper() + a[i][1:].lower()
    
    return ' '.join(a)


    # upper, lower, join 사용