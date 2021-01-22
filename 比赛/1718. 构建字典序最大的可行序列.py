
def Mymax(a, b):
    if a> b:
        return a
    else:
        return b


import copy
class Solution(object):
    def __init__(self):

        self.ans  =[]
    def judge(self, list):
        flag = True
        for index, i in enumerate(list):
            if i ==1: #还没分配
                break
            else:
                if i < self.ans[index]:  #同位更小
                    flag = False
                    break
                else:
                    break

        return flag


    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        num = [1 for i in range(2*n -1)]
        self.ans = copy.deepcopy(num)
        def dfs(choice, road):
            if self.judge(road):
                pass
            else:
                return -1
            # print(choice, road)
            if choice == 1:
                self.ans = Mymax(self.ans, road)

            # 遍历可能做出的选择
            for i in range(len(road)):
                newRoad =copy.deepcopy(road)
                try:
                    if road[i] == 1 and road[i + choice] == 1: # 没有数字
                        newRoad[i] = choice
                        newRoad[i + choice] = choice

                        dfs(choice-1, newRoad)
                except:
                    pass





        dfs(n,num)
        print(self.ans)
        return self.ans
        # a = sorted(self.ans, reverse=True)
        # print(a)
        # return a[0]

s =Solution()
s.constructDistancedSequence(18)