class Solution(object):
    def bestCoordinate(self, towers, radius):
        """
        :type towers: List[List[int]]
        :type radius: int
        :rtype: List[int]
        """


        import  math

        def judge(x, y):
            x = x
            y = y

            def calDis(a, b):
                return math.sqrt( math.pow(x- a, 2)+ math.pow(y- b, 2) )

            total =0
            for tower in towers:
                dis = calDis(tower[0], tower[1])
                if dis <= radius:
                    tmp = tower[2] / (1 +dis)
                    tmp = math.floor(tmp)  # 向下取整
                    total += tmp

            # print(total)
            return total

        X= []
        Y =[]
        for i in towers:
            X.append(i[0])
            Y.append(i[1])

        Xmi = min(X)
        Xma = max(X)

        Ymi = min(Y)
        Yma = max(Y)
        ans = 0
        result=None

        for i in range(Xmi, Xma+1):
            for j in range(Ymi, Yma+1):

                tmp = judge(i, j)

                if tmp > ans:
                    ans = tmp
                    result = [i, j]
                    print(tmp)
                    print(i, j)



        print(result)

        return result


Solution.bestCoordinate(None,[[10,8,27],[18,10,18],[18,8,41],[13,37,26],[49,24,27],[2,33,33],[31,42,41],[12,50,13],[20,41,12],[2,35,1],[0,0,28],[29,43,26],[16,3,1]],
8)