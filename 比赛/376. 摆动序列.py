class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <=1:
            return len(nums)
        elif len(nums) ==2:
            if nums[0] == nums[1]:
                return 1
        newList  = []
        for i in range(1,len(nums)):
            newList.append(nums[i] - nums[i-1])
        print(newList)
        count = 1
        if newList[0] ==0:
            count =0

        ans  = -float("INF")
        last = newList[0]
        for i in range(1,len(newList)):
            now = newList[i]
            if last * now <0:
                count +=1
                last = now
            else:
                if last==0 and now !=0:
                    last = now
                    count =1


        print(count+1)
        return count+1



Solution.wiggleMaxLength(None,[0,0,0])


