def solution(n, money):
    answer = 0
    money.sort()
    
    dp = [0 for _ in range(n+1)]
    dp[0] =1
    
    for i in money:
        for j in range(i, n+1):
            dp[j] += dp[j-i] 
    
    answer = dp[n]
    
    return answer % 1000000007