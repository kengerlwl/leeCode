while True:
    s  = input()
    if s =="":
        break
    s = int(s)

    l = input().split(' ')
    list = [int(i) for i in l]

    def judge(nums):
        for i in nums:
            if i > 0:
                return False


        return True

    ans = 0
    while not judge(list):
        ans+=1
        flag = True
        while flag:
            flag = False
            for i in range(s):
                if list[i] >0:
                    list[i]-=2
                    if list[i]<=0:
                        flag =True

        # print(list)
    print(ans)