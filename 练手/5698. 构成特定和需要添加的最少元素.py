class Solution(object):
    def minElements(self, nums, limit, goal):
        """
        :type nums: List[int]
        :type limit: int
        :type goal: int
        :rtype: int
        """
        Sum = sum(nums)

        dis = goal - Sum

        dis = abs(dis)
        print(dis)
        if dis == 0:
            return 0
        if limit >= dis:
            return 1
        if limit ==1:
            return dis

        def finA(s, up):



            left = s % up
            intMain = s // up
            print(left, intMain)
            if left >0:
                intMain+=1

            return intMain

        return finA(dis,limit)



a = Solution.minElements(None,[5,6,4,5,-1,-5,1,4],
6,
589268180)
print(a)