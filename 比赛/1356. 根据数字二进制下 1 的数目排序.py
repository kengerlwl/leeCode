class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(arr)):
            tmp = arr[i]
            arr[i] = str(bin(arr[i]))
            ans.append([arr[i].count('1'),tmp])

        ans = sorted(ans)
        a =[]
        for i in ans:
            a.append(i[1])

        print(a)
        return a


Solution.sortByBits(None,arr = [0,1,2,3,4,5,6,7,8])

