

class Solution(object):
    def minimumJumps(self, forbidden, a, b, x):
        """
        :type forbidden: List[int]
        :type a: int
        :type b: int
        :type x: int
        :rtype: int
        """

        maxV =max(a, b)

        posInf= float('INF')

        note ={}



        def dg(i, flag):



            if i == 0:
                return 0
            if i < 0:
                return posInf

            if i > 200 *  maxV+x:
                return posInf

            if i in forbidden:
                return posInf # 到不了
            else:
                low = posInf
                up = posInf
                if not flag:

                    if  (i+b) not in note:
                        note[(i+b)] = True

                        low = dg(i+b, True)  # 退到当前点
                else:

                    low = posInf  #不能连续退

                if (i -a) not in note:
                    note[(i-a)] =True

                    up = dg(i -a, False)

                if up == low:
                    print('failure')
                elif up < low:
                    print('up')
                else:
                    print('low')

                return 1 + min(up, low)

        ans  = dg(x,False)
        print(ans)
        if ans == posInf:
            return -1
        else:
            return ans



Solution.minimumJumps(None,[128,178,147,165,63,11,150,20,158,144,136],
61,
170,
135)