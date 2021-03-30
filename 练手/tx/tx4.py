t = int(input())

for j in range(t):
    n, k = input().split(' ')

    n = int(n)
    k = int(k)
    nums = input().split(' ')
    for i in range(len(nums)):
        nums[i] = int(nums[i])


    points = input().split(' ')
    for i in range(len(points)):
        try:
            points[i] = int(points[i])
        except:
            pass

    if False:
        print('NO')
    else:


        def judge(nums, points):
            # print(nums, points)
            if  len(nums) <= 1:
                return True
            if len(points) == 0:
                return True

            mid = points[0]
            midV = nums[mid]
            left  = nums[0: mid]
            right = nums[mid+1: len(nums)]

            if len(left) >0:
                lmin = min(left)
            else:
                lmin = float('INF')

            if len(right) >0:
                rmax = max(right)
            else:
                rmax = -float('INF')

            if lmin >= midV and midV  >= rmax:
                return judge(right, points[1: len(points)])

            else:
                return False
        f = judge(nums, points)
        if f:
            print('YES')
        else:
            print('NO')
