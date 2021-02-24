# 5 3
# 1 2 3 4 5

while True:
    s  = input()
    if s == '':
        break

    n, k = s.split(' ')
    n = int(n)
    k = int(k)
    nums = input().split(' ')
    list  = [int(i) for i in nums]

    start = min(list)

    def judge(num, nums, k):
        count = 0
        for i in nums:
            if num % i ==0:
                count +=1

        if k <= count:
            return True
        else:
            return False

    while True:
        if judge(start, list, k):
            break
        else:
            start+=1

    print(start)
