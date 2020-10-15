class Solution(object):
    def kthSmallest(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: int
        """
        last_row = [0]
        for i in range(len(mat)):
            new_row = []
            for j in range(len(mat[0])):
                for p in last_row:
                    new_row.append(p + mat[i][j])
            new_row.sort()
            if len(new_row) > k:
                last_row = new_row[:k]
            else:
                last_row = new_row

        print(last_row)
        return last_row[k - 1]




Solution.kthSmallest(None, mat = [[1,3,11],[2,4,6]], k = 5)