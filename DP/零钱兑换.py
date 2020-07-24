# 伪码框架
def coinChange(coins, amount):

        l = len(coins)

        #备忘录 记住，别用数组，效率低下
        note =dict()
        def dp(n):
            if n == 0:
                return 0
            if n < 0:
                return -1


            if n in note:
                return note[n]

            res = 1000000

            # 做选择，选择需要***最少的那个结果



            for coin in coins:

                subMin = dp(n - coin)
                if subMin == -1:
                    continue
                res = min(res, 1 + subMin)

            if res ==1000000:
                note[n] = -1
                return -1
            else:
                note[n] = res
                return res


        return dp(amount)

coinChange( coins = [1, 2, 5], amount = 11)