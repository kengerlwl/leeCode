class Solution:
    def restoreMatrix(self, rowSum, colSum):
        matrix = [[0] * len(colSum) for _ in rowSum]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                minVal = min(rowSum[i], colSum[j])
                matrix[i][j] = minVal
                rowSum[i] -= minVal
                colSum[j] -= minVal
                # 剪枝：当发现 rowSum[i] 和 colSum[i] 都是 0 的时候，就没必要再继续遍历下去了
                if rowSum[i] == 0 and colSum[i] == 0: break
        return matrix

