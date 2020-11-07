class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """

        i =0

        flag =[True for i in range(len(pieces))]
        while i < len(arr):
            prei = i
            # print(i)
            for j in range(len(pieces)):
                if i == len(arr):
                    return True
                if arr[i] == pieces[j][0] and flag[j]:
                    flag[j] = False
                    i+=1
                    if i == len(arr):
                        return True
                    for n in range(1, len(pieces[j])):
                        if arr[i] != pieces[j][n]:
                            # print(1,i)
                            return False
                        else:
                            i+=1
            # print(flag)
            if i == prei and i != len(arr):
                # print(2,i)
                return False
        return True





print(Solution.canFormArray(None,[91,4,64,78],
[[78],[4,64],[91]]
                            ))