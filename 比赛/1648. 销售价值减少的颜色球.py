class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        def cal(n):
            return n * (n +1) /2
        def calSum(n, m):
            return cal(n) - cal(m)


        count={}
        count[0]=0
        for i in inventory:
            if i in count:
                count[i] +=1
            else:
                count[i] =1
        ans = 0
        index = sorted(count, reverse=True)
        for i in range(0, len(index)-1):
            curValue = index[i]
            nextValue = index[i+1]

            if orders >= count[curValue]* (curValue - nextValue):
                ans += count[curValue] * calSum(curValue, nextValue)
                count[index[i+1]] += count[index[i]]
                # count[index[i]] =0
                orders -= count[curValue]* (curValue - nextValue)
            else:
                big = orders // count[curValue]
                small = orders % count[curValue]
                print(big, small)
                ans += calSum(curValue, curValue - big) * count[curValue]
                smallValue = curValue - big
                print(smallValue)
                ans += smallValue * small
                orders =0
            if orders ==0:
                print(ans % (10**9 + 7))

                return ans % (10**9 + 7)


            print(ans % (10**9 + 7), index[i],count[curValue]* (curValue - nextValue))

        return int(ans % (10**9 + 7))



Solution.maxProfit(None,[497978859,167261111,483575207,591815159],
836556809)