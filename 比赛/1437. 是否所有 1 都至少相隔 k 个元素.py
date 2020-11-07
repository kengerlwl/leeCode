class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        ans = True
        curLen =0
        flag = False
        count =0
        for i in nums:
            print(count)
            count += 1
            if i ==0 and curLen == 0:
                curLen =1
            elif i ==0 and curLen !=0:
                curLen +=1

            elif i == 1:
                # print(i, '\n')
                print('curlen', curLen)
                print('\n\n')
                if curLen < k and flag:
                    return False
                curLen =0
                flag = True

        return True



print(Solution.kLengthApart(None, [1,0,0,0,1,0,0,1],
2))