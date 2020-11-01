class Solution(object):
    def numWays(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        length = len(words[0])
        setList = [{} for i in range(length)]
        print(setList)
        for i in words:
            for j in range(length):
                char = i[j]
                if char in setList[j]:
                    setList[j][char] +=1
                else:
                    setList[j][char] =1
        print(setList)
        l2 = len(target)
        dp =[[0 for i in range(l2+1)] for j in range(length+1)]

        print(dp)

        # dp[1][1] = setList[0][target[0]]
        for i in range(length):
            dp[i][0] =1


        for i in range(1, length+1):
            tmpset = setList[i-1]
            for j in range(1, l2+1):
                print(target[j-1] in tmpset)
                print(i, j)
                print(dp[i-1][j-1])
                if j <= i:
                    if target[j-1] in tmpset:
                        if j < i:
                            dp[i][j] = dp[i-1][j-1] * tmpset[target[j-1]] + dp[i-1][j]
                        else:
                            dp[i][j] = dp[i - 1][j - 1] * tmpset[target[j-1]]
                    else:
                        dp[i][j] = dp[i-1][j]
                else:
                    break
        # print(dp)
        print(dp[length][l2])
        import math
        1000000007
        print(dp[length][l2] % (1000000007))
        return dp[length][l2] % (1000000007)


Solution.numWays(None,["ighdhd","hbakbh","ggidge","bcehgg","figjkg","fhedhk","cabdad"],
"gd")