def main(n):
    if n  == 2:
        return 2
    if n ==1:
        return 0
    if n==0:
        return 0

    dp = [0] * (n+1)
    for i in range(1,n+1):
        dp[i] = i


    #初始化dp
    dp[1] =0
    dp[2] =2


    for ix in dp:
        if ix <= 2:
            continue
        for j in range(2,ix):
            if ix % j ==0:
                dp[ix] = min(dp[j] + ix /j, dp[ix])



    # print(dp)
    return int(dp[n])

main(12)