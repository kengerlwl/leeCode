class Solution(object):
    def maxNonOverlapping(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # sum= [0 for  i in range(len(nums))]
        #
        # sum[0] = nums[0]
        # hashSum ={}
        # hashSum[sum[0]] =0
        # for i in range(1, len(nums)):
        #     sum[i] = sum[i-1] + nums[i]
        #     hashSum[sum[i]] = i
        #
        # sum.insert(0, 0)
        # print(sum)
        sum =[0]
        ans = []
        hashSum ={}
        # hashSum[sum[0]] =0
        for i in range(1, len(nums) +1):
            # if sum[i] < target:
            #     continue
            hashSum[sum[i-1]] = i-1
            sum.append(sum[i-1] +nums[i-1])
            # print(sum)
            tmpT = sum[i] - target
            # print(tmpT)
            # print(hashSum)
            if tmpT in hashSum:
                ans.append([hashSum[tmpT], i])

            # for j in range(0, i):
                # print(sum[i-1-j], 'bianli')



                # if sum[i-1-j] == tmpT:
                #     ans.append([i-1-j, i])
                #     break
        intervals = ans
        print(intervals)
        if intervals == []: return 0
        ## 根据区间右端点排序
        intervals = sorted(intervals, key = lambda x: x[1])
        num = 0
        new_interval = intervals[0]     # 被选的最新区间
        for interval in intervals[1:]:
            if interval[0] < new_interval[1]:   # 如果重叠删除区间，删除数量+1
                num += 1
            else:   # 如果不重叠更新new_interval
                new_interval = interval
        num = len(intervals) - num
        print(num)
        return num

Solution.maxNonOverlapping(None,
[-1,3,5,1,4,2,-9],
6)