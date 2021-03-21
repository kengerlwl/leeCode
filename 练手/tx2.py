class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        Sum =sum(nums)

        if Sum % 2 != 0:
            return False
        target = Sum /2
        length = len(nums)


        # 枚举子集
        init = (1 << length )-1
        # i =init
        # while i >0:
        #     print(bin(i))
        #
        #     i = (i-1) & init

        self.ans = False
        note = {}
        def getAns(state, now):
            if state in note:
                return False

            print(bin(state), now)
            if now == target:
                self.ans = True
                return True
            note[state] = True
            for i in range(length):
                j = 1 << (i)
                a = state & j  # 取与判断是否ok
                if a == 0:  # 还没有取到过
                    next = state | j
                    nextSum = now + nums[i]
                    f = getAns(next, nextSum)
        getAns(0, 0)
        print(self.ans)
        return self.ans




a= Solution()
a.canPartition(nums= [1, 5, 11, 5])