
class state:
    def __init__(self):
        self.minD = 0
        self.state = {
            'a':0,
            'b':0
        }


class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        initState = state()
        initState.minD=0
        initState.state[s[0]] = 1

        dp =[initState]

        preSum =[]
        curb =0
        for i in s:
            if i =='b':
                curb +=1
            preSum.append(curb)


        def getAs(i):
            count =0
            while s[i] == 'a':

                count+=1
                i-=1
                if i <0:
                    break

            # print(count)
            return count

        for i in range(1, len(s)):
            lastState = dp[i-1]
            if s[i] == 'b':
                newState = state()
                newState.minD = lastState.minD
                newState.state['b'] = lastState.state['b'] +1
                newState.state['a'] = lastState.state['a']

                dp.append(newState)

            elif s[i] =='a':

                # 删a
                newState = state()

                delA = lastState.minD+1



                # 保留a

                delb = preSum[i-1]


                if delb <= delA:
                    newState.minD = delb
                    newState.state['a'] = True
                else:
                    newState.minD = delA
                    newState.state = lastState.state
                dp.append(newState)


                # newState = state()
                #
                # Alength = getAs(i)
                # delNum = i - Alength +1
                # # print('need del ',delNum)
                #
                # keepNum = None
                # if lastState.state['b'] == True:  # 需要删除当前的a
                #     keepNum = lastState.minD +1
                # else:
                #     keepNum = lastState.minD
                # # print('keepNum', keepNum)
                # if delNum > keepNum: # 应该保留last
                #     newState.minD = keepNum
                #     newState.state = lastState.state
                # elif delNum <= keepNum:  # 应该使用当前a的子串
                #     newState.minD = delNum
                #     newState.state ={
                #                 'a':True,
                #                 'b':False
                #             }
                # dp.append(newState)
        #
        # for i in dp:
        #     print(i.minD)
        #     print(i.state)
        #     print('\n')



        return dp[len(s) -1].minD

Solution.minimumDeletions(None,"baababbaabbaaabaabbabbbabaaaaaabaabababaaababbb")






