

while True:


    # print(s)
    try:
        k = input()
        if k =='':
            break
    except EOFError:
        break
    s = input()


    k = int(k)
    s = s.split(' ')
    num =[]
    preSum =[]
    curSum =0
    flag = False #是不是全部都是负数
    for i in s:

        tmp = int(i)
        if tmp >=0:
            flag = True
        num.append(tmp)
        curSum +=tmp
        preSum.append(curSum)

    if not flag:
        print("0 0 0")
        continue


    dp = [0 for i in range(k)]


    maxV = dp[0] = preSum[0]
    maxI = 0


    for i in range(1, k):
        if num[i] + dp[i-1] > num[i]:
            dp[i] = num[i] + dp[i-1]
        else:
            dp[i] = num[i]

        if dp[i] > maxV:
            maxV =  dp[i]
            maxI = i
    j = maxI
    while maxV != 0:
        maxV -= num[j]
        j -=1

    print(dp[maxI], end=' ')

    print(num[j+1],  end=' ')
    print(num[maxI],end= '\n')


# 4
# -1 -2 -4 -3
# 8
# 6 -2 11 -4 13 -5 -2 10
# 20
# -10 1 2 3 4 -5 -23 3 7 -21 6 5 -8 3 2 5 0 1 10 3
# 8
# -1 -5 -2 3 -1 0 -2 0
#
#



def solution(num_list):
    s, max_s = 0, 0
    i_start, i_end, i_temp = 0, 0, 0
    for i, num in enumerate(num_list):
        s += num
        if s > max_s:
            i_end = i
            i_start = i_temp
            max_s = s
        if s < 0:
            s = 0
            i_temp = i + 1
    if i_start == i_end and i_start == 0:
        print(max_s, num_list[0], num_list[-1])
    else:
        print(max_s, num_list[i_start], num_list[i_end])

def main():
    K = int(input())
    inputs = list(map(int, input().split()[:K]))
    solution(inputs)

if __name__ == '__main__':
    main()
